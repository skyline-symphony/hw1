def task9(n: int) -> None:

    cnt = 0
    n_char = n-1
    x = 0
    y = n-1

    uzumaki = [[0] * n for i in range(n)]
    
    for _ in range(n):
        cnt += 1
        uzumaki[x][_] = cnt

    while cnt != n*n:
        
        for _ in range(n_char):
            cnt += 1
            x += 1
            uzumaki[x][y] = cnt
            
        for _ in range(n_char):
            cnt += 1
            y -= 1
            uzumaki[x][y] = cnt

        for _ in range(n_char-1):
            cnt += 1
            x -= 1
            uzumaki[x][y] = cnt

        for _ in range(n_char-1):
            cnt += 1
            y += 1
            uzumaki[x][y] = cnt

        n_char -= 2

    for i in range(len(uzumaki)):
        for j in range(len(uzumaki[i])):
            print(uzumaki[i][j], end=' ')
        print()


task9(int(input()))