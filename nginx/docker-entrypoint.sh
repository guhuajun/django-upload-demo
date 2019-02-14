#!/usr/bin/env sh
set -eu

envsubst '${BACKEND_CLUSTER_IP}' < /etc/nginx/conf.d/server.template > /etc/nginx/conf.d/server.conf

exec "$@"