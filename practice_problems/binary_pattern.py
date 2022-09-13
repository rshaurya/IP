
for i in range(5):
    for j in range(5):
        if j % 2 == 0 and i % 2 == 0:
            print('1', end=" ")
        elif j % 2 != 0 and i % 2 != 0:
            print('0', end=" ")
    print('\n')
