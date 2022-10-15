def listchecker(hand):
    result = 0
    i = 0
    print(hand[0][1])
    hand[0][0] += 1
    print(hand[0][0])
    while i<3:
        if (1<=hand[i][0]<=7):
            print("this criteria is met", hand[i])
            result += 1
        else:
            print("this is not met", hand[i])
        if (hand[i][1] == hand[0][1]):
            print("Hey the suit is the same!", hand[i][1], hand[0][1])
        i+=1
    #return 0



def main():
    #printy = listchecker([[1, 'obama'], [7, 'not obama'], [5, 'obama']])
    listy = [[1], [1], [2]]
    print(listy[1][0])
    i = 1
    j = 1
    print(listy[i + 1][0])
    if 1 == i == j:
        print("1", i, j)
    if listy[0] == listy[1] == listy [2]:
        print("they are all equal")
main()
