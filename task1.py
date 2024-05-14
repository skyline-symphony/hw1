from typing import List

def task1(lst_1: List[int]) -> List[int]:
    mx = 0
    mx_comb = []
    mlt = 0

    for i in range(0, len(lst_1)):
        for j in range(0, len(lst_1)):
            if i == j:
                continue
            mlt = lst_1[i] * lst_1[j]
            if mlt >  mx:
                mx = mlt
                mx_comb.clear()
                mx_comb.append(lst_1[i])
                mx_comb.append(lst_1[j])
            else:
                continue
            
    return mx_comb

print(task1([int(x) for x in input().split(' ')]))
