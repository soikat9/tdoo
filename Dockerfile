FROM ubuntu/postgres

USER root

RUN  apt-get update && \
     DEBIAN_FRONTEND=noninteractive   apt-get install -y --no-install-recommends apt-utils  && \
     DEBIAN_FRONTEND=noninteractive apt-get install -y wkhtmltopdf

# ---- Install tool packages ----
RUN  apt install python3-pip wget python3-dev python3-venv python3-wheel libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev -y 

# -- Other packages (Only ubuntu >= 18.04) ---
RUN  apt install postgresql -y

# ---- Install python packages LDAP based on OpenLDAP ----
RUN  useradd -m -d /opt/tele -U -r -s /bin/bash tele

# --- Install other required packages (node, less) ----
RUN  su - tele

USER tele

RUN chmod 777 -R .

RUN python3 -m venv tele-venv

RUN source tele-venv/bin/activate

RUN pip3 install wheel

RUN pip3 install -r requirements.txt

RUN ./tele-make -w tele -r tele --applets-path=./applets,enterprise,verticals --db_host 127.0.0.1




