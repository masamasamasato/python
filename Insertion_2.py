def insertion_sort(numbers: list) -> list:
    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index = index + 1

        if numbers[index] <= numbers[index-1]:  
            tmp = numbers[index]
            tmp_index = index
            while tmp < numbers[tmp_index-1] and tmp_index > 0:
                numbers[tmp_index] = numbers[tmp_index-1]
                tmp_index = tmp_index - 1
            numbers[tmp_index] = tmp
        else:
            index = index +1

    return numbers

if __name__ == "__main__":
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(insertion_sort(nums))



            
