from typing import List

def task3(lst_3: List[int]) -> bool:
    flg = True

    for i in range(1, len(lst_3)):
        if lst_3[i] > lst_3[i-1]:
            continue
        else:
            flg = False
            break
        
    return flg

print(task3([int(x) for x in input().split(' ')]))