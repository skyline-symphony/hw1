def task4(str_4: str) -> int:
    res_4 = []

    for i in set(str_4.lower()):
        if i in ['а','у','о','ы','э','я','ю','ё','и','е']:
            res_4.append(i)

    return len(res_4)

print(task4(input()))
