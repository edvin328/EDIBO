#!/bin/bash

echo "Fibonacci rindas kārtas skaitlis:" $1
n=$1
a=0
b=1
while [ "$n" != 0 ]
do
  a=$(($a + $b))
  b=$(($a - $b))
  n=$(($n-1))
done
echo "Fibonacci skaitlis:" $a
