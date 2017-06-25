#!/bin/bash

# Archive the input file to a predetermined location.

# Check for Sxactly 1 argument
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
# To understand the date format, run man date in terminal to get the date manual
# when assigning a value to a variable that involves running a command, wrap in backticks
DATE=`date +%Y-%m-%d`

# append date variable to end of path
archive=/home/pi/Desktop/archives/$DATE


# Make the archive (if it doesn't exist
mkdir -p $archive

# copy the input file
# rsync makes more sense - synchronizing - checks to see if a file needs to be copied
# if it hasn't already been created
# -v flag means verbose
# -a flag keeps permissions
rsync -avr $1 $archive

exit 0
