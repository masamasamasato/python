from random import random


def comb_sort(numbers: list) -> list:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped == True: #ずっとFalseの場合は終了
        gap = int(gap/1.3)
        if gap < 1:
            gap = 1
        
        swapped = False #初期化

        for i in range(0,len_numbers-gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i],numbers[i+gap] = numbers[i+gap],numbers[i]
                swapped = True
        
    return numbers

if __name__ == '__main__':
    import random
    num = [random.randint(0,1000) for i in range(10)]
    print(comb_sort(num))