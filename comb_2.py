def comb_sort(numbers: list) -> list:
    gap = int(len(numbers)/1.3)

    while gap > 1:
            for i in range(len(numbers) - gap):
                if numbers[i] > numbers[i + gap]:
                    numbers[i],numbers[i + gap] = numbers[i + gap],numbers[i]
            gap = int(gap/1.3)

    if gap <= 1:
        gap = 1
    swapped = True
    
    while swapped == True:
            swapped = False
            for i in range(len(numbers) - gap):
                if numbers[i] > numbers[i + gap]:
                    numbers[i],numbers[i + gap] = numbers[i + gap],numbers[i]
                    swapped = True

    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(comb_sort(nums))