#! bin/bash
##our task is to use for loops to display only odd natural numbers from  to .


for i in `seq 1 100`;
do
    if [[ `expr $i % 2` -ne 0 ]];
    then
        echo $i
    fi
done
    
