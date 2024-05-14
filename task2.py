from typing import List

def task2(lst_2: List[int]) -> List[int]:
    mx = 0
    mx_comb = []
    mlt = 0

    for i in range(0, len(lst_2)):
        for j in range(0, len(lst_2)):
            for k in range(0, len(lst_2)):
                        if i == j or i==k or k==j:
                            continue
                        mlt = lst_2[i] * lst_2[j] * lst_2[k]
                        if mlt >  mx:
                           mx = mlt
                           mx_comb.clear()
                           mx_comb.append(lst_2[i])
                           mx_comb.append(lst_2[j])
                           mx_comb.append(lst_2[k])
                        else:
                           continue
                       
    return mx_comb

print(task2([int(x) for x in input().split(' ')]))