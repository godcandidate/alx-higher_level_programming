#!/bin/bash

read -p "Enter your name : " filename
echo "#!/bin/bash" >> $filename

chmod u+x $filename
nano $filename
