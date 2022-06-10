def solution(A):
    A = sorted(A)
    len_A = len(A)
    max_1 = A[len_A-3]*A[len_A-2]*A[len_A-1]
    max_2 = A[0]*A[1]*A[len_A-1]
    if max_1 > max_2:
        return max_1
    else:
        return max_2

if __name__ == '__main__':
    nums = [-3,1,2,-2,5,6]
    print(solution(nums))