from tarfile import LENGTH_NAME


def solution(A):
    len_A = len(A)
    A = sorted(A)
    i = 0
    while i < len_A:
        if A[i]+A[i+1]>A[i+2]:
            break
        i +=1
    if i == len_A:
        return 0
    else:
        return 1
    
