#!/bin/bash
# a bash script that  displays the size of the body of the response
curl -sI 0.0.0.0:5000 | awk '/Content-Length/ {print $2}'
