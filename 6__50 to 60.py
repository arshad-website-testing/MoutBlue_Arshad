def maximumPerimeterTriangle(sticks):
    # Write your code here
    from itertools import combinations
    ls=list(filter(lambda x:x[0]+x[1]>x[2] and x[0]+x[2]>x[1] and x[1]+x[2]>x[0],list(combinations(sorted(sticks), 3))))
    ls_s=tuple(map(lambda x:(x, sum(x)), ls))
    return [-1] if not ls_s else list(max(ls_s)[0])








def alternatingCharacters(s):
    # Write your code here
    r= r'(\w)(?=\1)'
    o = re.findall(r, s)
    
    return len(o)






def pangrams(s):
    # Write your code here
    s = s.lower()
    l = 'qwertyuiopasdfghjklzxcvbnm'
    l = [i for i in l]
    for i in s:
        if i in l:
            l.remove(i)
    if len(l) == 0:
        return 'pangram'
    return 'not pangram'







def beautifulBinaryString(b):
    # Write your code here
    pattern=r"010"
    l=re.findall(pattern,b)
    return len(l)





def utopianTree(n):
    # Write your code here
    res = 1
    for i in range(n):
        if i % 2 != 0:
            res += 1
        else:
            res *= 2
    return res





def beautifulTriplets(d, arr):
    # Write your code here
    c=0
    for i in arr:
        if(i+d in arr):
            if(i+d+d in arr):
                c+=1
    return c







def pickingNumbers(a):
    # Write your code here
    newA, length, lengthArr = sorted(a), 0, []
    for index in range(0, len(newA)):
        for index2 in range(index + 1, len(newA)):
            if abs(newA[index] - newA[index2]) <= 1:
                length += 1
            elif abs(newA[index] - newA[index2]) > 1:
                lengthArr.append(length + 1)
                length = 0
                break
            if index2 == len(newA) - 1 and len(lengthArr) == 0: 
                return length+1
    return max(lengthArr)







def repeatedString(ss, n):
    # Write your code here
    s = ss
    a = ss.count('a')
    l = n // len(ss)
    # print(a*l, s[:(n-(len(ss*l))])
    return (a * l + s[:(n-(len(s)*l))].count('a'))








def hackerrankInString(s):
    # Write your code here
    pattern = ".*".join(list("hackerrank"))
    if re.search(pattern,s):
        return "YES"
    else:
        return "NO"








def designerPdfViewer(h, word):
    # Write your code 
    import string
    alp = string.ascii_lowercase
    print(alp)
    tall = 0
    for i in word:
        ind = alp.index(i)
        if tall <= h[ind]:
            tall = h[ind]
    return tall * len(word)