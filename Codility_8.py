def solution(X,A):
    
    len_A = len(A)
    list_X = []
    len_X = len(list_X)
    i = 0

    while len_X < X and i < len_A:
        if A[i] <= X and A[i] not in list_X:
            list_X.append(A[i])
            len_X = len(list_X)
        i +=1
    if len_X == X:
        return i-1
    if i == len_A :
        return -1


if __name__ == '__main__':
    nums = [1]
    print(solution(1,nums))


