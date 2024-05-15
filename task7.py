def task7(str_7: str) -> int:
    lst = []
    cnt = 0

    for i in set(str_7):
        lst.append(str_7.count(i))

    for i in reversed(sorted(lst)):
        if i % 2 == 0:
            cnt += i
        elif (cnt % 2) == 0:
            cnt += i
        elif (cnt % 2) == 1:
            cnt += i-1

    return cnt

print(task7(input().lower()))