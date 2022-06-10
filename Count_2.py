from operator import index
from random import randint


def counting_sort(numbers :list) -> list:
    len_numbers = len(numbers)
    max_num = max(numbers)

    nums = [0]*(max_num+1) #0 ~ max_num個の要素
    sum = [0]*(max_num+1)  #0 ~ max_num個の要素
    result = [0]*(len_numbers)  #結果用を分けておかないと、numbers[index] = numbers[i]でnumbers[index]が上書きされてしまう

    for i in range(max_num+1):
        for j in range(len_numbers):
            if numbers[j] == i:
                nums[i] = nums[i] + 1

    sum[0] = nums[0]

    for i in range(max_num):
        sum[i+1] = sum[i] + nums[i+1]

    for i in range(len_numbers):
        index = sum[numbers[i]]-1
        result[index] = numbers[i]
        sum[numbers[i]] = sum[numbers[i]] -1
    return result


if __name__ == '__main__':
    import random
    nums = [random.randint(0,100) for _ in range(10)]
    print(nums)
    print(counting_sort(nums))

        

