def anagram(s):
    # Write your code here
    from collections import Counter
    if len(s) % 2 == 1:
        return -1    
    
    first, last = s[:len(s) // 2], s[len(s) // 2:]
    c = Counter(first) - Counter(last)
    return len(list(c.elements()))








def cutTheSticks(arr):
    # Write your code here
    sizes = []
    while len(arr) > 0:
        sizes.append(len(arr))
        smallest = min(arr)
        arr = [elem for elem in arr if elem != min(arr)]
    return sizes









def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar = []
    for i in range(p,q+1):
        b_str = str(i**2)
        
        if(int(b_str)<=9):
            if(int(b_str)==1):
                kaprekar.append(i)
        elif(int(b_str[0:(len(b_str)//2)])+int(b_str[len(b_str)//2:len(b_str)])==i):
            kaprekar.append(i)

    if (len(kaprekar)==0):
        print("INVALID RANGE")
    else:
        for i in kaprekar:
            print(i,end=' ')





def decentNumber(n):
    # Write your code here
    fives = threes = -1
    i = 0 # Loop Counter
    while (n - 5*i) >= 0:
        if (n - 5*i) % 3 == 0:
            fives = n - 5*i
            threes = 5*i
            break 
        i+=1
    print(int((fives*'5')+(threes*'3')) if fives > -1 else -1)





def gameOfThrones(s):
    # Write your code here
    l=set(s)
    c=0
    for i in l:
        if(s.count(i)%2==1):
            c+=1
        if(c>=2):
            return "NO"
    return "YES"








def maximizingXor(l, r):
    # Write your code here
    max_xor = 0
    for x, y in ((i, j) for i in range (l, r + 1) for j in range(i, r + 1)):
        max_xor = max(max_xor, x ^ y)
    return max_xor





def happyLadybugs(b):
    # Write your code here
    for i in set(b):
        if b.count(i) == 1 and i != "_":
            return  "NO"
    if b.count("_") == 0:
        s = 0
        i = 0
        while i < (len(b) - 1):
            if b[s] == b[i + 1]:
                i = i + 1
            else:
                if len(b[s:i + 1]) == 1:
                    return "NO"
                else:
                    s = i + 1  
    return "YES"





def countingSort(arr):
    # Write your code here
    res=[] 
    a=0 
    count=0 
    while(a<100): 
        for i in range(len(arr)):
            if(arr[i]==a):
                count+=1
        res.append(count)
        count=0
        a+=1
    return res




def toys(w):
    # Write your code here
    w.sort() 
    containers=0 
    minn=-5 
    for i in w: 
        if i>minn+4: 
            containers+=1 
            minn=i 
    return containers





def cavityMap(grid):
    # Write your code here
    modified=list(grid)
    for r in range(1,n-1):
        for c in range(1,n-1):
            if all([grid[r][c] > adj for adj in[grid[r+1][c],grid[r-1][c],grid[r][c+1],grid[r][c-1]]]):
                ss=list(modified[r])
                ss[c]="X"
                modified[r]="".join(ss)
    return modified





