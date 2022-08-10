#!/bin/bash

set -ue

CONTAINER_NAME={{ container_name }}

docker stop ${CONTAINER_NAME} || true

docker rm -f ${CONTAINER_NAME} || true
