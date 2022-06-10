def cooktail_sort(numbers: list) -> list:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1

    while swapped:
        #左から右にやってく
        swapped = False
        for i in range(start,end):#range(0 4) = [0 1 2 3]|
            if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped = True #ひっくり返したらTrueにする
        
        if not swapped:
            break

        #右から左へやってく
        swapped = False

        end = end - 1
        for i in range(end-1,start-1,-1): #range(2,-1) = [0 1 2 | 3] range(a b) bは含めない　 numbers[i]とnumbers[i+1]を比較しているのでrange(end-1 start-1)としてる
            if numbers[i] > numbers[i+1]:
                numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
                swapped = True #ひっくり返したらTrueにする
        
        start = start + 1

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(cooktail_sort(nums))
