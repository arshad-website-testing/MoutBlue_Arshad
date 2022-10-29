def serviceLane(n, cases):
    # Write your code here
    lis=[]
    for list in cases:
        lis.append(min(width[list[0]:list[1]+1]))
    return lis





def lonelyinteger(a):
    # Write your code here
    return [x for x in a if a.count(x)==1][0]




def luckBalance(k, contests):
    # Write your code here
    imp, unimp = [], 0
    for i in range(len(contests)):
        if contests[i][1]:
            imp.append(contests[i][0])
        else:
            unimp += contests[i][0]
    imp.sort(reverse=True)
    return sum(imp[:k]) - sum(imp[k:]) + unimp







def appendAndDelete(s, t, k):
    # Write your code here
    if (k == 0): 
        if s == t:
            return "Yes"
        else:
            return "No"
        
    if len(s)+k > len(t):
         return appendAndDelete(s[:-1], t, k-1)
        
    if len(s)+k == len(t) and t.startswith(s):
        return "Yes"
    else:
        return "No"








def misereNim(s):
    # Write your code here
    from functools import reduce
    if (set(s)=={1}) and n%2==1:
        return 'Second'
    elif (set(s)=={1}) and n%2==0:
        return 'First'
    elif reduce((lambda x,y:x^y),s):
        return 'First'
    else:
        return 'Second'






def jumpingOnClouds(c):
    # Write your code here
    stp=0
    ind=0
    while(ind < len(c)-1):
        if ind+2 < len(c) and c[ind+2]==0:
            ind+=2    
        else:
            ind+=1
        stp+=1
    return stp 









def gemstones(arr):
    # Write your code here
    s=set(arr[0])
    for i in arr:
        s=s&set(i)
    return len(s)






def twoStrings(s1, s2):
    # Write your code here
    intersecting_letters = set(s1) & set(s2)
    if len(intersecting_letters) >= 1:
        return 'YES'
    return 'NO'






def chocolateFeast(n, c, m):
    # Write your code here
    wrappers=candies=int(n/c)
    while wrappers>=m:
        wrappers-=(m-1)
        candies+=1
    return candies





def acmTeam(topic):
    # Write your code 
    import itertools
    combi = itertools.combinations(topic,2)
    result = 0
    count = 0
    for c in combi:
        value = 0
        for i in range(len(c[0])):
            if c[0][i] == '1' or c[1][i] == '1':
                value += 1
        if value > result:
            result = value
            count = 1
            continue
        elif value < result:
            continue
        elif value == result:
            count+=1
        
    return [result,count] 

















