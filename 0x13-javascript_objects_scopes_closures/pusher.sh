#!/bin/bash

echo "Enter file name"
read filename

git add $filename
git commit -m "create $filename"
git push
