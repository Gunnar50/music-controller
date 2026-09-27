#!/bin/bash
#
# Utils
#
# Set some failure conditions
set -o errexit   # Fail on any error
set -o pipefail  # Trace ERR through pipes
set -o errtrace  # Trace ERR through sub-shell commands


# Work out if we're running in Cloudbuild
if [[ -z "${PWD##*workspace*}" ]] ;then
    IS_CLOUDBUILD="1"
fi
