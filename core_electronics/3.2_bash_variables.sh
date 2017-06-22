#!/bin/bash

# Demo of decision making

# how to make variables
a=5
b=200
# $ symbol to access a variable

# math
# O.G. version
c=$(($a*$b))
# cleaner version
let c=a*b

# if statment
if [ $a -gt $b ]
then
  # Do something
  echo a greater than b
  let c=1
else
  echo a less than b
  let c=5
# end if statment with fi
fi

# loop 10 times
while [ $c -le 10 ]; do
  echo Number $c
  let c++
done