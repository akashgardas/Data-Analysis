n1, n2, n3 = map(int, input().split())

if n1 > n2:
    if n1 > n3:
        print(f'Greatest: {n1}')
    else:
        print(f'Greatese: {n3}')
else:
    if n2 > n3:
        print(f'Greatest: {n2}')
    else:
        print(f'Greatest: {n3}')
        

