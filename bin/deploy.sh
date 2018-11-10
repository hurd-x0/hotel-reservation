#!/usr/bin/env bash

set -eu

# echo "Starting Cassandra"
# cd ./data/cassandra
# ./deploy.sh
# cd -

# echo "Starting MariaDB"
# cd ./data/mariadb
# ./deploy.sh
# cd -

# echo "Migrating data"
python main.py
