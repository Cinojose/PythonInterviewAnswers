#! /bin/bash

## Given  lines of input, print the  character from each line as a new line
## of output. It is guaranteed that each of the
## lines of input will have a  character.
##
## sample Input
## Hello
## World
## how are you

## sample Output
## l
## r
## w

cut -c3 /dev/stdin

## To display 3 and 7th Char

cut -c2,7 /dev/stdin

## To dsiplay from 2nd to 7th Chat

cut -c2-8 /dev

## cut a tab delimited file and print 3 fields

cut -f1,2,3

## get the first 20 lines form a file using head

head -20

## read first 20 chars using head

head -c20

## read middle of a file from line#12 -22, using sed

sed -n "12,22p"

## print last 20 chars of a file

tail -c 20

## replace () with [] in text using tr

tr "()" "[]"

## Delete lowercase char from the text

tr -d [:"lower":]

## convert a txt file into tabdelimited text

paste -s /dev/stdin

## group text into file with 3 columns.

paste  - - -
