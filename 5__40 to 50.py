





def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
        
    # Check each column is sorted.
    for i in range(len(grid[0])):
        column_list = []
        for j in range(len(grid)): 
            column_list.append(grid[j][i])
        if (column_list != sorted(column_list)):
            return "NO"
            
    return "YES"






def angryProfessor(k, a):
    # Write your code here
    x = 0
    for i in a:
        if i <= 0:
            x += 1
    if x >= k:
        return 'NO'
    return 'YES'







def squares(a, b):
    # Write your code here
    c = int(math.sqrt(b))-int(math.sqrt(a))
    return c+1 if int(math.sqrt(a))**2==a else c




def circularArrayRotation(a, k, queries):
    # Write your code here
    from collections import deque
    b=[]
    a=deque(a)
    a.rotate(k)
    a=list(a)
    print(a)
    for i in queries:
        b.append(a[i])
    return b





def bigSorting(unsorted):
    # Write your code here
    unsorted.sort(key = lambda x: int(x))
    return unsorted





def equalizeArray(arr):
    # Write your code here
    s = set(arr)
    cnt = 0
    for i in s:
        if cnt < arr.count(i):
            elem = i 
            cnt = arr.count(i)
    l = [i for i in arr if i !=  elem]
    return len(l)





def minimumDistances(a):
    # Write your code here
    res = []
    for i in range(len(a)):
        fi = i 
        bi = i
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                bi = j
                break
        if fi == bi:
            continue
        # print(fi, bi)
        res.append(bi-fi)
        print(res)
    if len(res) == 0:
        return -1
    return min(res)






def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s) // 2 + 1):
        num = s[:i]
        valid_s = num
        count = 1
        while len(valid_s) < len(s):
            next_num = int(num) + count
            valid_s += str(next_num)
            count += 1
        if valid_s == s:
            print(f'YES {num}')
            return
    print('NO')









def theLoveLetterMystery(s):
    # Write your code here
    i, j = 0, len(s) - 1
    count = 0
    while i < j:
        if s[i] != s[j]:
            count += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j -= 1
    return count








def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    budget = s
    g = 0
    while p <=budget:
        budget -= p
        g+=1
        p = max(p-d,m)

    return g