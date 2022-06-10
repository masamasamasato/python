
def bubble_sort(numbers: list) -> list:
    for i in range(len(numbers)-1): #[2,1,3,4,0]| -> [1,2,3,4,0]| -> [1,2,3,0,4]|
        for j in range(len(numbers)-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

if __name__=='__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(bubble_sort(nums))


#forのループが二重にあるので計算速度はn^2に比例することがわかる。