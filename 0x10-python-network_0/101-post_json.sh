#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
