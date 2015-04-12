#!/bin/bash
chown -R postgres $PGDATA
chmod -R 700 $PGDATA
sudo -u postgres /usr/lib/postgresql/9.3/bin/initdb -D $PGDATA
sudo -u postgres /usr/lib/postgresql/9.3/bin/postgres -c config_file=/etc/postgresql/9.3/main/postgresql.conf >logfile 2>&1 &
sleep 1 # give postgres some time to start
sudo -u postgres psql --command "CREATE USER $DB_USER WITH SUPERUSER PASSWORD '$DB_USER';"
sudo -u postgres psql --command "ALTER USER $DB_USER CREATEDB;"
sudo -u postgres psql --command "CREATE DATABASE gtokendb OWNER=gtokendb"
#/bin/bash
kill $(ps aux | grep '/usr/lib/postgresql/9.3/bin/postgres' | awk '{print $2}')
sleep 1 # LOL calm down baby
sudo -u postgres /usr/lib/postgresql/9.3/bin/postgres -c config_file=/etc/postgresql/9.3/main/postgresql.conf

