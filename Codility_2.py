def rotation(numbers: list, N:int) -> list:
    len_numbers = len(numbers)
    rotated_list = [0]*(len_numbers)

    for i in range(len_numbers):
        rotated_list[(i+N)%len_numbers] = numbers[i]

    return rotated_list

if __name__ == '__main__':
    import random
    nums = [random.randint(0,10) for _ in range(10)]
    print(nums)
    print(rotation(nums,3))