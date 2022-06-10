
from typing import List, Tuple, Optional
from warnings import catch_warnings


def get_pair(numbers: list, target: int) -> Optional[Tuple[int,int]]:   #Tuple 一つの情報が複数の要素から構成されているもの　(1,2)というタプルを返す。　オプショナル型の場合Noneを返してもいい。
    cache = set()   #set集合型　重複を考えない
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)  #[1,3,3,5,5] 8 => (3,5) 3に対して5がヒット 5はまだcacheにないのでif文を抜けて3が格納される


def get_pair_half_sum(numbers: list) -> Optional[Tuple[int,int]]:   #[1,2,3,4]  (1,4) = (2,3) ペアの和と残りの要素の和が同じ
    sum_numbers = sum(numbers)
    if sum_numbers%2 != 0:  #ペアなので必ず2で割り切れないといけない　(1,4) (2,3) 全部足すと10
        return 

    half_sum = sum_numbers/2
    cache = set()   #set集合型

    for num in numbers:
        val = half_sum - num
        if val in cache:
            return val, num
        cache.add(num)

if __name__ == '__main__':
    l = [1,2,3,4,4,5,6,7]   #(4,7)よりも先に(5,6)が見つかる
    t = 11
    print(get_pair(l,t))