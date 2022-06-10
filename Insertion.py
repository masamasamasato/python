def insertion_sort(numbers: list) -> list:
    len_numbers = len(numbers)
    for i in range(1,len_numbers):    #[1,2,3,0] [1,2,0]
        tmp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > tmp:
            numbers[j+1] = numbers[j]
            j = j -1
        
        numbers[j+1] = tmp
    
    return numbers
    
