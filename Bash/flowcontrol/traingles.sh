#! bin/bash
## Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is Scalene, Isosceles, or Equilateral.
##
## Input Format
##
## Three integers, each on a new line.
##
## Constraints
##
##
## Sum of any two sides will be greater than the third.
##
##
## Output Format
##
## One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

read a
read b
read c

if [[ $a -eq $b ]] && [[ $a -eq $c ]] && [[ $b -eq $c ]]
then
    echo "EQUILATERAL"
elif [[ $a -ne $b ]] && [[ $a -ne $c ]] && [[ $b -ne $c ]]
then
    echo "SCALENE"
else
    echo "ISOSCELES"
fi
