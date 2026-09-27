#!/bin/bash
#
# Run the server for a service.

# Set some failure conditions
set -o errexit   # Fail on any error
set -o pipefail  # Trace ERR through pipes
set -o errtrace  # Trace ERR through sub-shell commands

export APPLICATION_ID="dev~project-id-stg" && dev_appserver.py \
    app_dev.yaml \
    --application=project-id-stg \
    --enable_console \
    --support_datastore_emulator=False $@
