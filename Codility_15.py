def solution(A):
    len_A = len(A)
    A = sorted(A)
    i = 1
    count = 1

    if len_A == 0:
        return 0

    if len_A == 1:
        return 1
    
    while i < len_A:
        if A[i] > A[i-1]:
            count +=1
        i +=1
    
    return count
        
if __name__ == '__main__':
    nums = [1]
    print(solution(nums))
