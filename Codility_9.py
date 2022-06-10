from bdb import Breakpoint


def solution(A):
    A = sorted(A)
    print(A)
    len_A = len(A)
    i = 0
    while i < len_A:
        if i+1 == A[i]:
            i += 1
        else:
            break
    
    if i == len_A:
        return 1
    else:
        return 0

if __name__ == '__main__':
    nums = [4,1,2,3]
    print(solution(nums))
    
