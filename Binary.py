import numbers
from xml.dom.expatbuilder import ExpatBuilderNS


# def linear_search(numbers: list, value: int) -> int:
#     for i in range(len(numbers)):
#         if value == numbers[i]:
#             return i
#     return -1


# def binary_search(numbers: list, value: int) -> int:
#     left,right = 0,len(numbers)-1
#     mid = int((left + right)/2)

#     while left <= right:    #見つからなければいずれleftがrightを超えてしまう
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] > value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

def binary_search(numbers: list, value: int) -> int:
    def _bainary_search(numbers: list, value: int, right: int, left: int) -> int:
        if left > right:
            return  -1
        
        mid = int((left + right)/2)
        if numbers[mid] == value:
            return mid
        elif numbers[mid] > value:
            return _bainary_search(numbers, value, mid -1, left)
        else:
            return _bainary_search(numbers, value, right, mid + 1)
    return _bainary_search(numbers, value, len(numbers) - 1, 0)

if __name__ == '__main__':
    nums =[0,1,3,6]
    print(binary_search(nums,0))
        
