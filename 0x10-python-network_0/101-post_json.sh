#!/bin/bash
# posts a json
curl -s -H "Content-Type: application/json" -d "(cat $2)" "$1"
