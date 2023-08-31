#!/bin/bash
# bash script that sends a DELETE request to the URL passes as first arguement.
curl -sX DELETE "$1"
