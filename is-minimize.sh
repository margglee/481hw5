#!/bin/bash
#$current_dir/queue/
for file in $*
do
    ./pngtest $file.png > junk.txt
    OUTPUT=$(gcov *.c | tail -1)
    #$file $OUTPUT >> testResult.txt
    reg='[0-9]+\.[0-9]+'
    [[ $OUTPUT =~ $reg ]]
    echo ${BASH_REMATCH}
    #echo $file.png $OUTPUT
    #echo "--------------------------------"
done
rm *.gcda pngout.png
rm junk.txt
if [ ${BASH_REMATCH} == "23.02" ]; then 
    exit 1
fi
exit 0
#return coverage