##---------------------------------------------------------------
## Given an array of sorted integers and find the closest value to
##  the given number. Array may contain duplicate values
##  and negative numbers.
##
## Example : Array : 2,5,6,7,8,8,9 
## Target number : 5
## Output : 5
##
## Target number : 11
## Output : 9
##
## Target Number : 4
## Output : 5
##
##-----------------------------------------------------------------


def closest (num,num_array):
    found = False
    for i in num_array:
        if i == num:
            return i
        elif i > num:
            return i
        else:
            continue
    return num_array[len(num_array)-1]



if __name__ == "__main__":
    num_array = [1,2,4,5,6,6,8,9]
    num = 11
    num = -2
    number = closest(num,num_array)
    print number
