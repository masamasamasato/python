def binary_search(numbers:list, N:int) -> int:
    len_numbers = len(numbers)
    left,right = 0,len_numbers  #インデックス番号
    while left < right:
        mid = (left+right)//2
        if numbers[mid] == N:
            return mid
        elif N < numbers[mid]:
            right = mid -1
        else:
            left = mid +1
    return -1



def binary_search(numbers:list, N:int) -> int:
    def _binary_search(numbers:list, left:int, right:int) -> int:
        if left > right:
            return -1
        mid = (left+right)//2
        if numbers[mid] == N:
            return mid
        elif numbers[mid] > N:
            _binary_search(numbers, mid+1,right)
        else:
            _binary_search(numbers, left, mid-1)
        