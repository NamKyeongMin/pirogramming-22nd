### 계단식 출력력
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()
    
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()
    
for i in range(5):
    for j in range(5):
        if j<=i:
            print('*', end='')
    print()

### 한줄 대각선 출력
for i in range(5):
    for j in range(5):
        if j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    
### 역삼각형 출력
for i in range(5):
    for j in range(5):
        if j>=i:
            print('*', end='')
        else:
            print(' ', end='')
    print()