def solution(A):
    A = sorted(A)
    print(A)
    i = 0
    len_A = len(A)
    while  i+1 == A[i]:
        if i < len_A -1:
            i +=1
        elif i == len_A -1:
            i +=1
            break
    return i+1

if __name__ == '__main__':
    nums = [2,1,3,5] 
    nums_2 = [2,3,4,5]
    nums_3 = [1,2,3,4]
    print(nums)
    print(solution(nums))
    print(solution(nums_2))
    print(solution(nums_3))
