def solution(A,B,K):
    i = A
    count = 0
    while i <= B:
        if i % K == 0:
            count += 1
        i +=1
    return count


def solution_2(A,B,K):
    if A == B == 0:
        return 1
    else:
        if A % K == 0:
            return (B // K) - (A//K) + 1
        else:
            return (B // K) - (A//K)


if __name__ == '__main__':
    print(solution(0,0,11))
