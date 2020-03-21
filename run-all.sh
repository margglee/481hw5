#!/bin/bash

# INSTRUCTIONS:
# Run ./run-all.sh from in libpng directory
# Put images inside of a directory inside of libpng
# Change folder to name of directory containing images
FOLDER=minres1639
# Notes:
# "2> error" puts stderr output into error file (not to shell/screen)

SUM=0
for file in $FOLDER/*.png; do
  SUM=$((SUM + 1))
  ./pngtest $file > junk.txt 2> error
  #OUTPUT=$(gcov *.c 2> error | tail -1)
  #echo $file: $OUTPUT
  #echo $file
  #echo "--------------------------------"
done
OUTPUT=$(gcov *.c 2> error | tail -1)
echo $OUTPUT
rm *.gcda pngout.png
rm junk.txt error
echo $SUM files
