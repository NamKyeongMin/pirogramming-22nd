height = int(input())

for i in range(height):
    for j in range(height):
        if j<(height-i-1):
            print(' ', end='')
        else:
            print('*', end='')
    for k in range(i):
        print('*', end='')
    print()