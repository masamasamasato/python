from itertools import count


def solution(A):
    len_A = len(A)
    i = 0
    j = 0
    count_box =1
    while A[i] != -1 and j < len_A:
        count_box +=1
        i = A[i]
        j +=1
    
    if j >= len_A:
        return -1
    return count_box