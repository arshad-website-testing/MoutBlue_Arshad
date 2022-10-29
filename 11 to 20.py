def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)




def plusMinus(arr):
    # Write your code here
    p, n, z = 0, 0, 0
    for i in arr:
        if i < 0:
            n += 1
        elif i == 0:
            z += 1
        else:
            p += 1
    print(p / len(arr))
    print(n / len(arr))
    print(z / len(arr))







def birthday(s, d, m):
    # Write your code here
    cnt , res = 0, 0
    while cnt <= len(s):  
        # print(cnt, s[cnt:cnt+m])
        if sum(s[cnt:cnt+m]) == d and len(s[cnt:cnt+m]) == m:
            res += 1
        cnt += 1
        
    return res 









def migratoryBirds(arr):
    # Write your code here
    cnt, res = 0, 0
    for i in set(arr):
        if arr.count(i) > cnt :
            cnt = arr.count(i)
            res = i
    return res 








def diagonalDifference(arr):
    # Write your code here
    d1, d2 = 0 , 0
    print(type(arr))
    for i in range(1, len(arr)+1):
        d1 += (arr[i-1][i-1])
        d2 += (arr[-i][i-1])
        
    return abs(d1 - d2)









def birthdayCakeCandles(candles):
    # Write your code here
    m = max(candles)
    return candles.count(m)






def gradingStudents(grades):
    # Write your code here
    res = []
    for i in grades :
        cnt = 0
        x = i
        while(i % 5 != 0):
            i += 1
            cnt += 1
        if cnt < 3 and i >= 40:
            res.append(i)
        else:
            res.append(x)
    return res






def pageCount(n, p):
    # Write your code here
    if p == 1:
        return 0
    if n % 2 == 0:
        if p == n:
            return 0
        if p == n-1:
            return 1
    if n % 2 != 0:
        if p == n or p == n-1:
            return 0
    res1 = 1
    for i in range(2, n, 2):
        if i == p or i + 1 == p:
            break 
        res1 += 1

    res2 = 0
    for i in range(n, 1, -2):
        if i == p or i - 1 == p:
            break
        res2 += 1
    
    return min(res1, res2)







def divisibleSumPairs(n, k, ar):
    # Write your code here
    ans = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                ans += 1
    return ans







def miniMaxSum(arr):
    # Write your code here
    s = []
    for i in range(len(arr)):
        s.append(sum(arr) - arr[i])

    print(min(s), max(s))











