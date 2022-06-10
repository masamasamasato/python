from types import new_class


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

def bucket_sort(numbers :list) -> list:
    len_numbers = len(numbers)
    index = int(max(numbers)/len_numbers)
    new_numbers = [len_numbers]  

    for i in range(len_numbers):
        for j in range(index):
            if numbers[i] == j:
                new_numbers[j] = numbers[i]

    listed_numbers = [len_numbers]

    for k in range(index):
        listed_numbers.append(insertion_sort(new_numbers[k]))
    return listed_numbers

if __name__ == "__main__":
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(bucket_sort(nums))
    


