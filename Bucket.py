def insertion_sort(numbers: list) -> list:
    len_numbers = len(numbers)

    for i in range(1,len_numbers):  #[2,1,3,0]
        tmp = numbers[i]
        j = i -1

        while j >= 0 and numbers[j] > tmp:
            numbers[j+1] = numbers[j]
            j = j -1
        
        numbers[j+1] = tmp 
    return numbers







def bucket_sort(numbers: list) -> list:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num / len_numbers #分類されてできたグループの個数

    bucket = [[] for _ in range(size)]

    for num in numbers:
        i = num/size

        if i != size:
            bucket[i].append(num) #append 追加
        else:
            bucket[size-1].append(num)

    for i in range(size):
        insertion_sort(bucket[i])
    
    for i in range(size):
        result =[]
        result += bucket[i]
    
    return result

    


