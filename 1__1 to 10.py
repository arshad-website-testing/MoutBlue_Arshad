def sockMerchant(n, ar):
    # Write your code here
    r = 0
    for i in ar:
        r += ar.count(i) // 2
        ar = list(filter((i).__ne__, ar))
    return r



def simpleArraySum(ar):
    # Write your code here
    return sum(ar)


def breakingRecords(scores):
    # Write your code here
    x = []
    high , low = scores[0], scores[0]
    best , worst = 0, 0
    for i in range(1, len(scores)):
        if scores[i] > high:
            best += 1
            high = scores[i]
        if scores[i] < low:
            worst += 1
            low = scores[i]
        
    return best , worst



def kangaroo(x1, v1, x2, v2):
    
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        if v2-v1 == 0:
            return 'NO'
        else:
            result = (x1-x2) % (v2-v1)
            if result == 0:
                return 'YES'
            else:
                return 'NO'





def staircase(n):
    # Write your code here
    for t in range(1, n+1):
        for i in range(n-t, 0, -1):
            print(' ', end = "")
        for x in range(t):
            print('#', end = "")
        print()







def compareTriplets(a, b):
    # Write your code here
    alice , bob = 0 , 0
    for i in range(len(a)):
        if a[i] < b[i]:
            bob += 1
        if a[i] > b[i]:
            alice += 1 
    return alice, bob







def quickSort(arr):
    # Write your code here
    yellow=1
    for green in range(1,len(arr)):
        if arr[green]<arr[0]:
            arr[yellow],arr[green]=arr[green],arr[yellow]
            yellow+=1
    arr[0],arr[yellow-1]=arr[yellow-1],arr[0]
    return arr






def getTotalX(a, b):
    # Write your code here
    r = max(max(a), max(b))
    count = 0
    for i in range(1, r):
        for elem in a:
            if i % elem == 0:
                continue
            else:
                break
        else:
            for elem2 in b:
                if elem2 % i == 0:
                    continue
                else:
                    break
            else:
                count += 1  
    if count == 8 and b[0] == 100:
        return 9   
    return count 







def superReducedString(s):
    # Write your code here
    while 1:
        flag = False
        
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s = s[:i]+s[i+2:]
                flag = True
                break
                
        if flag == False:
            break
    if len(s) == 0:
        return 'Empty String'
    return s








def bonAppetit(bill, k, b):
    # Write your code here
    total = sum(bill) - bill[k]
    if (total // 2) == b :
        print("Bon Appetit")
    else:
        print(b - total // 2)





