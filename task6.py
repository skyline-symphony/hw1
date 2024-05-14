def task6(str_6: str) -> int:
    mx = 0

    if len(str_6) == 1:
        return 1
    
    for i in range(0, len(str_6)):
        l_edge = i
        r_edge = i
        while l_edge >= 0 and r_edge < len(str_6) and str_6[l_edge] == str_6[r_edge]:
            l_edge -= 1
            r_edge += 1
            if mx < len(str_6[l_edge+1:r_edge]):
                mx = len(str_6[l_edge+1:r_edge])

    for i in range(0, len(str_6)):
        l_edge = i
        r_edge = i+1
        while l_edge >= 0 and r_edge < len(str_6) and str_6[l_edge] == str_6[r_edge]:
            l_edge -= 1
            r_edge += 1
            if mx < len(str_6[l_edge+1:r_edge]):
                mx = len(str_6[l_edge+1:r_edge])

    return mx

print(task6(input().lower()))

