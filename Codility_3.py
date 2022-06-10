def num_count(numbers:list,N:int) -> int:
    len_numbers = len(numbers)
    count_num = 0
    for i in range(len_numbers):
        if numbers[i] == N:
            count_num += 1
    return count_num



def pairs(numbers:list) -> int:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        count = num_count(numbers,numbers[i])
        if count%2 == 1:
            return numbers[i]
        


def solution(A):
    A = sorted(A)
    len_A = len(A)
    i = 0
    if len_A > 1:
        while i < len_A and A[i+1] == A[i]:
            if i+2 < len_A-1:
                i +=2
        return A[i]
    else:
        return A[0]


[1,2,3,2,1] [1,1,2,3,3]


        






            
if __name__ == '__main__':
    import random
    nums = [random.randint(0,10) for _ in range(10)]
    nums =  [0,2,4,2,0]
    print(nums)
    print(pairs(nums))
