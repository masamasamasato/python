def solution(A):
    len_A = len(A)
    sum_A = sum(A)
    min = abs(sum_A)
    sum_left = 0
    for i in range(len_A):
        sum_left = sum_left + A[i]
        sum_right = sum_A - sum_left

        if min > abs(sum_left - sum_right):
            min = abs(sum_left - sum_right)
    
    return min




if __name__ == '__main__':
    nums = [-1,-3]
    print(solution(nums))
