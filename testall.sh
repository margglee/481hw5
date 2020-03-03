#!/bin/bash
current_dir=$(pwd)
FILES=$current_dir/*
SUM=0
#touch testResult.txt
for file in $FILES
do
  if [ ${file: -4} == ".png" ]
  then
    SUM=$((SUM + 1))
    ./pngtest $file > junk.txt
    OUTPUT=$(gcov *.c | tail -1)
    #$file $OUTPUT >> testResult.txt
    echo $file $OUTPUT
    echo "--------------------------------"
  fi
done
rm *.gcda pngout.png
rm junk.txt
echo $SUM
