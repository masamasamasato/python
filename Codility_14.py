from http.client import TEMPORARY_REDIRECT
from re import S


def solution(A):
    len_A = len(A)
    i = 0
    j = 0
    s = 0
    min_avg = sum(A)/len_A

    for i in range(len_A):
        s = 0
        for j in range(i,len_A):
            s += A[j]
            if j == i:
                continue
            avg = s/(j-i+1)

            if min_avg > avg:
                min_avg = avg
                tmp = i

    return tmp



if __name__ == '__main__':
    nums = [4,2,2,5,1,5,8]
    print(nums)
    print(solution(nums))




