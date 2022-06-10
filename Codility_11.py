def solution(A):
    len_A = len(A)
    A = sorted(A)
    min_A = 1
    i = 0 
    while i < len_A:
        if A[i] == min_A:
            min_A +=1
        i +=1
    return min_A

if __name__ == '__main__':
    nums = [1,3,6,4,1,2]
    nums_2 = [-1,-2]
    print(solution(nums))
    print(solution(nums_2))



    #[1,2,3,4] -> [5]
    #[1,3,4,4] -> [2]
    #[1,4,6,8] -> [2]
    #[-1,-2]