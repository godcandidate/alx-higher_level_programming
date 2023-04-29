#!/bin/bash

echo "Enter filename"
read filename

git add $filename
git commit -m "create $filename"
git push

