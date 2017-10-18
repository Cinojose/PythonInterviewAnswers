

"""
 Given an array of numbers, find any two number with the given sum
 Eg : array  [1,2,4,7,11,15]
      sum 15
      Answer 4,11
"""
def sum_of_no(list,sum_no):
    head = 0
    tail = len(list) - 1
    found = False
    while (not found):
        print list[head]
        print list[tail]
        sum_tmp = list[head] + list[tail]
        if (sum_tmp < sum_no):
            head = head +1
        elif(sum_tmp > sum_no):
            tail = tail -1
        elif (head == tail):
            found = True
        else:
            print("Numbers are {0},{1}".format(numbers[head],numbers[tail]))
            found = True


if __name__=="__main__":
        numbers =[1,2,4,7,11,15]
        sum_of_no(numbers,15)
