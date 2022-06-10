
from random import random


def count_sort(numbers: list) -> list:  #[2,3,3,4]
    max_num = max(numbers)
    counts = [0]*(max_num +1)
    result = [0]*(len(numbers)) #結果のリスト

    for num in numbers: #[0,0,1,2,1]
        counts[num] = counts[num]+1 #要素個数count

    for i in range(1,len(counts)):  #[0,0,1,3,4]
        counts[i] = counts[i-1] + counts[i]
    
    i = len(numbers) - 1    #インデックス番号

    while i >= 0:
        index = numbers[i]  #[2,1,3]
        result[counts[index] -1] = numbers[i]
        counts[index] = counts[index] -1
        i = i - 1

    return result


if __name__ == '__main__':
    import random
    nums = [random.randint(0.1000) for _ in range(10)]
        




