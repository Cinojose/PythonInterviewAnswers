
"""
  Given an array of integers greater than zero, find if it is possible to split
  it in two (without reordering the elements), such that the sum of the two
  resulting arrays is the same. Print the resulting arrays.
  url : https://www.careercup.com/question?id=5716403849003008
"""

def checkSum(arr):
    idx= 0
    arr_sum = sum(arr)
    total = arr[idx]
    samesum = False
    while (idx<len(arr)):
        total = sum(arr[:idx+1])
        if(total == sum(arr[idx+1:])):
           samesum = True
           break
        else:
            idx+=1
    return samesum
if __name__=="__main__":
    arr = [[1,2,3,3,2,1],[5,6,7,4,32,1]]
    for l in arr:
        samesum = checkSum(l)
        if samesum:
            print ("l is possible{0}".format(l))
        else:
            print ("l is not possible{0}".format(l))
