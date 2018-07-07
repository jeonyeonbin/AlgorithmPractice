first = ['t', 'o', 'p', 'c', 'o', 'd', 'e', 'r', 's', 'i', 'n', 'g', 'l', 'e', 'r', 'o', 'u', 'n', 'd', 'm', 'a', 't',
         'c', 'h', 'f', 'o', 'u', 'r', 'n', 'i']
second = ['n', 'e', 'f', 'o', 'u', 'r', 'j', 'a', 'n', 'u', 'a', 'r', 'y', 't', 'w', 'e', 'n', 't', 'y', 't', 'w', 'o',
          's', 'a', 't', 'u', 'r', 'd', 'a', 'y']
maxNumber = 0
# commit
for idx, firs in enumerate(first):
    turn = idx
    myfirstSum = 0
    mySecondSum = 0
    print(firs)
    while 1:
        turn = (turn + 1) % len(first)
        if turn == idx:
            print(myfirstSum)
            maxNumber = max([myfirstSum + 1, maxNumber, mySecondSum + 1])
            break
        elif firs == first[turn]:
            myfirstSum = myfirstSum + 1
            continue
        elif firs == second[turn]:
            myfirstSum = myfirstSum + 1
            continue
        elif second[idx] == second[turn]:
            mySecondSum += 1
            continue
        elif second[idx] == first[turn]:
            mySecondSum += 1
            continue

print(maxNumber)
