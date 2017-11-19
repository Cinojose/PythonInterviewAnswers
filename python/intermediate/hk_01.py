# script to left rotate array

def array_left_rotation(a, n, k):
    i = 0
    temp = a
    temp_1 = a
    len_a = len(a)
    while i < k:
        a = temp[0]
        for idx in range(0,len_a):
            if idx == (len_a - 1):
                temp_1[len_a-1] = a
            else:
                temp_1[idx] = temp[idx+1]
        temp = temp_1
        i += 1
    return temp

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

def array_left_rotation(a, n, k):
    i = 0
    temp = a
    len_a = len(a)
    old_idx =0
    for idx in range(0,len_a):
        old_idx = idx - 4
        print (old_idx)
        if old_idx < 0:
            new_idx = (len(a) - abs(old_idx) )
        else:
            new_idx = old_idx
        print (new_idx)
        temp[new_idx] = a[idx]
        print (temp)
    return temp

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
