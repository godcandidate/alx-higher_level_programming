#!/bin/bash

# stores all the files in the current directory as an array
files=(*)

# loops through the files and replaces the string
for filename in ${files[@]};
do
	sed -i 's/Edward Obeng/Edward Obeng/' $filename
done

echo "Change was successful"
