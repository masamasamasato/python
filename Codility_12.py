from itertools import count


def solution(A):
    len_A = len(A)
    i = 0
    count_list = []

    while A[i] != 0:
        if i < len_A:
            i +=1
        break
    
    while i < len_A:
        if A[i] == 0:
            count_list.append(0)
        else:
            count_list = list(map(lambda x: x+1,count_list))
        i +=1
    return sum(count_list)





def solution_2(A):
    len_A = len(A)
    i = 0
    j = len_A -1
    sum = 0
    count_zero = 0

    while A[i] != 0:
        if i < len_A -1:
            i +=1
        break

    while A[j] != 1:
        if j > 0:
            j -=1
        break

    if i <= j:
        while i <= j:
            if A[i] == 0:
                count_zero +=1
            else:
                sum += count_zero
            i +=1
        if sum > 1000000000:
            return -1
        else:
            return sum
    else:
        return 0



if __name__ == '__main__':
    nums = [0,1]
    print(solution_2(nums))
            
        
            


