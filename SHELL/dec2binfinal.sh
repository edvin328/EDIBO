#!/bin/bash

echo Decimal number given: $1

# a ir dotais decimālais cipars
a=$1;
# array  ir  jauns tukšs massīvs
array=()

while [ "$a" != 0 ]
do
# array  ir atlikums no dalijuma un ir massīvs; + zīme nozīmē elementa pievienošanu
  array+=$(($a%2))
  a=$(($a/2))
done

# c ir gatavs binārais skaitlis (tas pats lasot massīvu array otrādāk)

c=$(echo "${array[*]}" | rev)
echo "Binary of $1 is:" $c

