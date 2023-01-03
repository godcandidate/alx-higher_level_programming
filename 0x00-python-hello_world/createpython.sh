#!/bin/bash

read -p "Enter your name : " filename
echo "#!/bin/bash" >> $filename
nano $filename
