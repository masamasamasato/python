
def cooktail_sort(numbers: list) -> list:
    max_index = len(numbers)
    min_index = 0
    swapped = True

    while swapped == True:  #左から右に移る
        swapped = False
        for i in range(min_index,max_index-1):
            if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped = True
        max_index = max_index - 1



    while swapped == True:    #右から左に
        swapped == False
        for i in range(min_index,max_index -1):
            if numbers[max_index - 1 -i] > numbers[max_index -i]:
                numbers[max_index - 1 -i],numbers[max_index -i] = numbers[max_index -i],numbers[max_index - 1 -i]
                swapped = True
            min_index = min_index + 1
    
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(cooktail_sort(nums))

