from typing import List

def task2(lst_2: List[int]) -> List[int]:
    mx_comb = []

    lst_2.sort()

    if lst_2[0] * lst_2[1] * lst_2[2] >= lst_2[-3] * lst_2[-2] * lst_2[-1]:
        mx_comb.append(lst_2[0])
        mx_comb.append(lst_2[1])
        mx_comb.append(lst_2[2])
    else:
        mx_comb.append(lst_2[-1])
        mx_comb.append(lst_2[-2])
        mx_comb.append(lst_2[-3])

    return mx_comb

print(task2([int(x) for x in input().split(' ')]))