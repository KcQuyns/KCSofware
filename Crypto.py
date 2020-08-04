Crypto = input("Crypto: ")
print("Input the key: ")
ltr1 = input("Letter 1: ")
ltr2 = input("Letter 2: ")
pos1 = ord(ltr1) - 64
pos2 = ord(ltr2) - 64
list1 = []

if pos1 > 1:
    list2 = []
    for i in range(pos1, 27):
        if pos2 <= 26:
            list1.insert(i, pos2)
        else:
            pos2 = pos2 - 26
            list1.insert(i, pos2)
        pos2 += 1

    for i in range(1, pos1):
        list2.insert(i, pos2)
        pos2 += 1

    list1 = list2 + list1

if pos1 == 1:
    for i in range(pos1, 26):
        list1.insert(i, pos2)
        pos2 += 1

for ltt in Crypto:
    if ltt == ' ':
        print('/', sep='', end=' ')
    else:
        print(chr((list1.index(ord(ltt) - 64) + 1)+64), sep='', end=' ')
