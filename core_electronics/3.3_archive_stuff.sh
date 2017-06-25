#!/bin/bash

# Archive the input file to a predetermined location.

# The archive location (absolute path):
# Remember, variable assignment has no spaces
archive=/home/pi/Desktop/archives

# Make the archive (if it doesn't exist)
# -p flag creates parent directories if doesn't exist, and handle previously existing
mkdir -p $archive

# copy the input file
cp $1 $archive