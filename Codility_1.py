from itertools import count


def binary(N:int) -> int:
    binary_n = format(N,'b')  #二進数変換
    print(binary_n)
    binary_n_str = str(binary_n)    #文字列変換
    binary_list = list(binary_n_str)    #リスト変換
    len_list = len(binary_list)
    max_zero = 0
    count_zero = 0
    for i in range(len_list):
        if binary_list[i] == '0':
            j = i
            while binary_list[j] == '0':
                tmp = max_zero
                if j < len_list-1:
                    count_zero += 1
                    j += 1
                else:
                    return tmp
            if max_zero < count_zero:
                max_zero = count_zero
            count_zero = 0
    
    return max_zero
if __name__ == '__main__':
    num = 9
    num_2 = 57
    print(binary(num))
    print(binary(num_2))
        



