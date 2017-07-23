#!/bin/bash

# Archive the input file to a predetermined location.

# Check for exactly 1 argument
# translation: if number of arguments is not equal to 1
if [ $# -ne 1 ]
then
  echo "Usage: $0 FILE"
  echo "Error: must entire destination path"
  # exit the script
  # 1 indicates the error (exit anything other than 0 is error)
  exit 1
fi

# The archive location (absolute path):
# Remember, variable assignment has no spaces
archive=/home/pi/Desktop/archives

# Make the archive (if it doesn't exist)
# -p flag creates parent directories if doesn't exist, and handle previously existing
mkdir -p $archive

# copy the input file 
# cp (copy) FROM -  TO
# -r flag means recursive - i.e., copy everything, including subdirectories 
cp -r $1 $archives

exit 0