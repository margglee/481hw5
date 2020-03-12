#!/bin/bash

for file in $*; do
  ./pngtest imgs/$file.png > junk.txt 2> error
  OUTPUT=$(gcov *.c 2> error | tail -1)
done
rm *.gcda pngout.png

reg='[0-9]+\.[0-9]+'
[[ $OUTPUT =~ $reg ]]
echo ${BASH_REMATCH}

if [ ${BASH_REMATCH} == "37.97" ]; then
    exit 1
fi
exit 0
