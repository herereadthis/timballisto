#!/bin/bash
# This is the hash bang line, tells Raspberry Pi what interpreter to use: bash

# access some arguments
# remember to increment
echo The command entered was $0
echo My name is $1

# -e flag allows you to format the echo, but remember to wrap in quotes
# the $# can grab how many arguments were passed
echo -e "I am $2 years old\n\t$# arguments were passed in"

# after saving this and running ls -l in terminal, you will get this:
# -rw-r--r-- permissions are in sets of three: 
# file owner, owner's usergroups, and everyone else
# r-read, w-write, x-execute
# To add owner execute: chnmod u+x
# u = owner, + = add, x = execute

# to run this:
# ./3.1_shell_script.sh jimmy 14