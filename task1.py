from typing import List

def task1(lst_1: List[int]) -> List[int]:
    mx_comb = []

    lst_1.sort()

    if lst_1[0] * lst_1[1] >= lst_1[-2] * lst_1[-1]:
        mx_comb.append(lst_1[0])
        mx_comb.append(lst_1[1])
    else:
        mx_comb.append(lst_1[-1])
        mx_comb.append(lst_1[-2])

    return mx_comb

print(task1([int(x) for x in input().split(' ')]))
