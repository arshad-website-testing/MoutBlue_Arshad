def strangeCounter(t):
    # Write your code here
    p = 3 
    while t > p: 
        t -= p
        p *= 2
    return p - t + 1






def insertionSort1(n, arr):
    # Write your code here
    for i in range((n-1),0,-1):
        if arr[i] < arr[i-1]:
            tmp = arr[i]
            arr[i] = arr[i-1]
            print(*arr)
            arr[i-1] = tmp
    print(*arr)




def makingAnagrams(s1, s2):
    # Write your code here
    cl = set(s1) & set(s2)
    rl = 0
    for l in cl:
        rl += min(s1.count(l), s2.count(l))
    return len(s1) + len(s2)-rl * 2





def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key




def runningTime(arr):
    # Write your code here
    a = 0
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
           arr[j+1] = arr[j]
           j -= 1
           a += 1
        arr[j+1] = key
    return a






def insertionSort2(n, arr):
    # Write your code here
    for start in range(1,n):
        j=start
        while arr[j-1]>arr[j] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        print(*arr)






def introTutorial(V, arr):
    # Write your code here
    return [i for i,value in enumerate(arr) if value==V][0]






def countingSort(arr):
    # Write your code here
    arrCount = [0]*100
    for x in arr:
        arrCount[x] += 1
    returnArr = []
    for x in range(100):
        for y in range(arrCount[x]):
            returnArr.append(x)
    return returnArr






def stones(n, a, b):
    # Write your code here
    results=set([a*i+b*(n-i-1) for i in range(n)])
    return sorted(list(results))





def largestPermutation(k, arr):
    # Write your code here
    dict_ = {}
    for i, a in enumerate(arr):
        dict_[a] = i
    cnt = 0
    n = len(arr)
    for i in range(n):
        if cnt == k:
            break
        v = arr[i]
        if v < n - i:
            arr[i], arr[dict_[n-i]] = arr[dict_[n-i]], arr[i]
            dict_[v], dict_[n-i] = dict_[n-i], dict_[v]
            cnt += 1
    return arr