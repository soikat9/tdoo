FROM ubuntu:20.04

LABEL maintainer="Tele"

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN set -x; \
        apt-get update \
        && apt-get install -y --no-install-recommends \
            ca-certificates \
            apt-utils \
            sudo \
            curl \
            dirmngr \
            node-less \
            python3-pip  \
            docker.io \
            nano \
	    python3-setuptools \
	    gnupg \
        && curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_amd64.deb \
        && apt install ./wkhtmltox.deb -y \
        && apt-get -y install -f --no-install-recommends \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false \
        && rm -rf /var/lib/apt/lists/* wkhtmltox.deb \
        && pip3 install psycogreen==1.0

# install latest postgresql-client
RUN set -x; \
        echo 'deb http://apt.postgresql.org/pub/repos/apt/ focal-pgdg main' > etc/apt/sources.list.d/pgdg.list \
        && export GNUPGHOME="$(mktemp -d)" \
        && repokey='B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8' \
        && gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "${repokey}" \
        && gpg --batch --armor --export "${repokey}" > /etc/apt/trusted.gpg.d/pgdg.gpg.asc \
        && gpgconf --kill all \
        && rm -rf "$GNUPGHOME" \
        && apt-get update  \
        && apt-get install -y postgresql-14 postgresql-client \
        && rm -rf /var/lib/apt/lists/* \
	&& apt update && apt-get install -y npm \
	&& npm install -g less less-plugin-clean-css \
	&& apt-get install -y node-less \
        && sudo service postgresql start

# Install Tele
ENV TELE_VERSION 1.0

# This binds to service file.So, take care
ARG TELE_USER=tele
ARG TELE_USER_UID=1000
ARG TELE_USER_GID=1000
# Set the default Tele port (you still have to use -c /etc/tele-server.conf for example to use this.)
# ARG TELE_PORT="8069"
# Set this to True if you want to install Nginx!
# ARG INSTALL_NGINX="False"
# Set the superadmin password - if GENERATE_RANDOM_PASSWORD is set to "True" we will automatically generate a random password, otherwise we use this one
# ARG TELE_SUPERADMIN="admin"
# Set to "True" to generate a random password, "False" to use the variable in ARG TELE_SUPERADMIN
# ARG GENERATE_RANDOM_PASSWORD="True"
# ARG TELE_CONFIG="${TELE_USER}-server"
# Set the website name
# ARG WEBSITE_NAME="_"
# Set the default Tele longpolling port (you still have to use -c /etc/tele-server.conf for example to use this.)
# ARG LONGPOLLING_PORT="8072"
# Set to "True" to install certbot and have ssl enabled, "False" to use http
# ARG ENABLE_SSL="True"
# Provide Email to register ssl certificate
# ARG ADMIN_EMAIL="tele@example.com"

RUN mkdir /opt/app

RUN set -x; \
        groupadd -r -g ${TELE_USER_GID} ${TELE_USER} \
        && adduser --system --home=/opt/app/${TELE_USER} ${TELE_USER} --uid ${TELE_USER_UID} --gid ${TELE_USER_GID} \
        && apt update && apt-get install -y git libpq-dev libxml2-dev libxslt-dev libffi-dev gcc python3-dev libsasl2-dev python-dev libldap2-dev libssl-dev libjpeg-dev \
        && mkdir /var/log/tele \
        && chown ${TELE_USER}:root /var/log/tele \
        && sudo su - postgres -c "createuser -s $TELE_USER" 2> /dev/null || true \
        && sudo adduser $TELE_USER sudo \
        && usermod -a -G docker ${TELE_USER}

# Install rtlcss (on Debian buster)
RUN npm install -g rtlcss

COPY --chown=tele:tele ./tele /opt/app/tele
RUN pip3 install -r /opt/app/tele/requirements.txt

RUN cp /opt/app/tele/setup/tele /opt/app/tele/tele-make && chmod +x /opt/app/tele/tele-make

# Copy entrypoint script and Tele configuration file
COPY --chown=tele:tele ./entrypoint.sh /
COPY --chown=tele:tele ./tele.conf /etc/tele/

# Set permissions and Mount /var/lib/tele to allow restoring filestore and /mnt/extra-applets for users applets
RUN chown tele /etc/tele/tele.conf \
    && mkdir -p /mnt/extra-applets \
    && chown -R tele /mnt/extra-applets \
    && mkdir -p /var/lib/tele \
    && chown -R tele /var/lib/tele 
VOLUME ["/var/lib/tele", "/mnt/extra-applets"]

# Expose Tele services
EXPOSE 8069 8071 8072 5432

# Set the default config file
ENV TELE_RC /etc/tele/tele.conf

COPY --chown=tele:tele wait-for-psql.py /usr/local/bin/wait-for-psql.py

# Set default user when running the container
USER tele

ENTRYPOINT ["/entrypoint.sh"]
CMD ["tele"]
