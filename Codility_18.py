def solution(A):
    len_A = len(A)
    count = 0

    for i in range(len_A-1):
        print(str(i)+"番目のカウント")
        for j in range(i+1,len_A):
            if (A[i] + A[j]) >= (j-i) and ((j-i) >= (A[j] - A[i]) or (j-i) >= (A[i] - A[j])):
                count +=1
                print(count)

    if count > 10000000:
        return -1
    return count

if __name__ == '__main__':
    nums = [1,5,2,1,4,0]
    print(solution(nums))


    
