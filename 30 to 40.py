def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    res = 0
    for i in keyboards:
        for j in drives:
            print(i, j)
            if i + j <= b and res < i + j :
                res = i + j
                
    if res == 0:
        return -1
    return res 








def camelcase(s):
    # Write your code here
    i = 1
    for a in s:
        if a.isupper():
            i = i + 1
    return i






def viralAdvertising(n):
    # Write your code here
    res = 0
    x = 5
    for i in range(n):
        res += x // 2
        x = x//2 * 3
    return res 








def jumpingOnClouds(c, k):
    e = 100
    x = 0
    while True:
        if c[x] == 0:
            e -= 1
        else:
            e -= 3
        x += k
        
        if x >= len(c):
            x -= len(c)
        if x == 0:
            break
    return e






def gameOfStones(n):
    # Write your code here
    return 'Second' if n%7<2 else 'First'







def marcsCakewalk(calories):
    # Write your code here
    calories.sort();
    calories=calories[::-1]
    su=0
    for i in range(n):
        su=su+(calories[i]*pow(2,i));
    return(su)







def catAndMouse(x, y, z):
    if max(x, z) - min(x, z) > max(y, z) - min(y, z):
        return "Cat B"
    elif max(x, z) - min(x, z) < max(y, z) - min(y, z):
        return "Cat A"
    else:
        return "Mouse C"







def saveThePrisoner(n, m, s):
    # Write your code here
    return (((S - 1 + M - 1) % N) + 1)






def saveThePrisoner(n, m, s):
    # Write your code 
    return (((s - 1 + m - 1) % n) + 1)





def beautifulDays(i, j, k):
    # Write your code here
    res = 0
    for x in range(i, j+1):
        rev = int(str(x)[::-1]) 
        div = ( x - rev ) / k 
        if div - int(div) == 0:
            res += 1
            print(div)
    return res






def permutationEquation(p):
    # Write your code here
    dic = {}
    l = []
    n = len(p)
    for i in range(len(p)):
        dic[p[i]] = i+1  
    for i in range(1,len(p)+1):
        a1 = dic.get(i)
        l.append(dic.get(a1))
        # resu.append(a2)
    return l

