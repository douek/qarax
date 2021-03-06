#!/bin/bash -e
DB_NAME=${1:-"qarax"}
DB_USER=${2:-"qarax"}
SU_PREFIX="sudo su - postgres -c "
COMMAND_PREFIX="psql -U postgres -d"
TEMPLATE_DB="template1"
existing_user=$(${SU_PREFIX} "${COMMAND_PREFIX} ${TEMPLATE_DB} -c \"SELECT usename FROM pg_catalog.pg_user WHERE usename = '${DB_USER}';\" --tuples-only")

if [ ! -z "$existing_user" ]
then
    echo "User already exists, not creating"
else
    echo "Creating user ${DB_USER}..."
    ${SU_PREFIX} "${COMMAND_PREFIX} ${TEMPLATE_DB} -c \"create user ${DB_USER} password 'qarax';\""
fi

existing_db=$(${SU_PREFIX} "${COMMAND_PREFIX} ${TEMPLATE_DB} -c \"SELECT datname FROM pg_database WHERE datname = '${DB_NAME}';\" --tuples-only")
if [ ! -z "$existing_db" ]
then
    echo "Database already exists, not creating"
else
    ${SU_PREFIX} "${COMMAND_PREFIX} ${TEMPLATE_DB} -c \"create database ${DB_NAME} owner ${DB_USER} template template0
    encoding 'UTF8' lc_collate 'en_US.UTF-8' lc_ctype 'en_US.UTF-8';\""
    ${SU_PREFIX} "${COMMAND_PREFIX} "${DB_NAME}" -c \"CREATE EXTENSION \"pgcrypto\";\""
fi

exit 0
