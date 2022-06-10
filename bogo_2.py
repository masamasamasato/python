from ast import Not
from sklearn.utils import shuffle


def in_order(numbers: list) -> bool:
    for i in range(len(numbers)-1): #len(numbers) -1 回この操作を対して行う
        if numbers[i] > numbers[i+1]:   #len(numbers)にしてしまうとnumbers[len(numbers)]一個多い！！
            return False
    return True

def bogo_sort(numbers: list) -> list:
        nums = shuffle(numbers)
        while not in_order(nums):
            nums = shuffle(nums)
        return nums

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(bogo_sort(nums))