
def gnone_sort(numbers: list) -> list:

    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index = 1
        
        if numbers[index] <= numbers[index-1]:
            numbers[index],numbers[index-1] = numbers[index-1],numbers[index]
            index = index - 1
        else:
            index = index + 1
    return numbers

if __name__ == "__main__":
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(gnone_sort(nums))