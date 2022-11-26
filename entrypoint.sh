#!/bin/bash

set -e

# set the postgres database host, port, user and password according to the environment
# and pass them as arguments to the tele process if not present in the config file
: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='tele'}}}
: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='telepwd'}}}

DB_ARGS=()
function check_config() {
    param="$1"
    value="$2"
    if grep -q -E "^\s*\b${param}\b\s*=" "$TELE_RC" ; then       
        value=$(grep -E "^\s*\b${param}\b\s*=" "$TELE_RC" |cut -d " " -f3|sed 's/["\n\r]//g')
    fi;
    DB_ARGS+=("--${param}")
    DB_ARGS+=("${value}")
}
check_config "db_host" "$HOST"
check_config "db_port" "$PORT"
check_config "db_user" "$USER"
check_config "db_password" "$PASSWORD"

case "$1" in
    -- | tele)
        shift
        if [[ "$1" == "scaffold" ]] ; then
            exec /opt/app/tele/tele-make "$@"
        else
            wait-for-psql.py ${DB_ARGS[@]} --timeout=30
            exec /opt/app/tele/tele-make "$@" "${DB_ARGS[@]}"
        fi
        ;;
    -*)
        wait-for-psql.py ${DB_ARGS[@]} --timeout=30
        exec /opt/app/tele/tele-make "$@" "${DB_ARGS[@]}"
        ;;
    *)
        exec "$@"
esac

exit 1
