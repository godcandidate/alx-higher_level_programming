#!/bin/bash

read -p "Enter your name : " filename
echo "#!/usr/bin/python3" >> $filename

nano $filename
