def task5(str_5: str) -> bool:
    return str_5 == str_5[::-1]

print(task5(input().lower()))