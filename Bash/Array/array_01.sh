#! /bin/bash

## ----------------------------------
## Read a file line by line to array and
## print with space
## ---------------------------------------

a=[]
i=0
while read LINE
do
    a[i]=$LINE
    let "i+=1"
done
echo ${a[@]}
