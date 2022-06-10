def bubble_sort(numbers: list) -> list:
    max_index = len(numbers)

    while max_index > 0:
        for i in range(max_index - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i],numbers[i + 1] = numbers[i + 1],numbers[i]
        max_index = max_index -1
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(bubble_sort(nums))
    
        



