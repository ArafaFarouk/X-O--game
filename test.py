examble = ['a','b','c','d','e','f']
for i in range(0,6,3):
    print('|'.join(examble[i:i+3]))
    if i < 6:
        print('-'*5)
