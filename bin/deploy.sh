#!/usr/bin/env bash

set -eu

# echo "Stargin Cassandra"
# cd ./data/cassandra
# ./deploy.sh
# cd -

# echo "Stargin MariaDB"
# cd ./data/mariadb
# ./deploy.sh
# cd -

echo "Migrating data"
python main.py
