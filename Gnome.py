from re import I


def gnome_sort(numbers: list) -> list:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:

        if index == 0:
            index = index + 1

        if numbers[index -1] <= numbers[index]:
            index = index + 1

        else:
            numbers[index],numbers[index -1] = numbers[index -1],numbers[index]
            index = index - 1

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(gnome_sort(nums))
#[2,1,0] -> [1,2,0] -> [1,0,2] -> [0,1,2]







#[2,1,0] -> [1,2.0] -> [1,0,2] -> [0,1,2]

#[1,3,5,2,4,0] -> [1,3,2,5,4,0] -> [1,2,3,5,4,0] -> [1,2,3,4,5,0] -> []

#numbers[i]とnumbers[i+1]の比較 numbers[i]>numbers[i+1]の時 numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
#でさらにnumbers[i-1]とnumbers[i]を比較してnumbers[i-1]>