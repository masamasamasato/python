def solution(N,A):
    len_A = len(A)
    ans = [0]*(N)
    ans_max = 0
    i = 0

    while i < len_A:
        if A[i] <= N:
            ans[A[i]-1] +=1
            if ans[A[i]-1] >= ans_max:
                ans_max = ans[A[i]-1]
        else:
            ans = list(map(lambda x: ans_max, ans))
        i +=1
    
    return ans

if __name__ == '__main__':
    nums = [3,4,4,6,1,4,4]
    print(solution(5,nums))




