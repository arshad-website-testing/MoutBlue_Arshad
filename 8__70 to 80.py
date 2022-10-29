def taumBday(b, w, bc, wc, z):
    # Write your code here
    if wc + z < bc:
        return (wc*w)+(b*(wc+z))
    elif bc + z < wc:
        return (bc*b)+(w*(bc+z))
    else:
        return (bc*b) + (wc*w)






def funnyString(s):
    # Write your code here
    ordinals = [ord(i) for i in s]
    diffs = [abs(ordinals[i - 1] - ordinals[i]) for i in range(1, len(ordinals))]
    return 'Funny' if diffs == diffs[::-1] else 'Not Funny'





def sumXor(n):
    # Write your code here
    num_of_zero = 0
    while n != 0 :
        if n % 2 == 0 :
            num_of_zero += 1
        n = n // 2
    return pow(2,num_of_zero)








def stringConstruction(s):
    # Write your code here
    return len(set(s))





def findDigits(n):
    # Write your code here
    x = str(n)
    list1=[]
    list1[:1]=x
    
    count = 0
    for k in list1:
        if int(k)!=0 and n%int(k) ==0: 
            count +=1
    return count








def palindromeIndex(s):
    # Write your code here
    rev = s[::-1]
    lst = list(s)
    revlst = list(rev)
    if (rev == s):
        return -1
    else:
        for c,v in enumerate(s):
            if v != rev[c]:
                lst.pop(c)
                revlst.pop(c)
                if (lst != lst[::-1]):
                    return (len(s)-c-1)
                if (revlst != revlst[::-1]):
                    return (c)
        return -1





def workbook(n, k, arr):
    # Write your code here
    book_page = 0
    count = 0
    
    for i in range(n):
        page_per_ch = math.ceil(arr[i] / k)        
        for p in range(1, arr[i]+1):
            if p == math.ceil(p/k) + book_page:
                count += 1
        book_page += page_per_ch
                
    return count





def is_smart_number(num):
    val = int(math.sqrt(num))
    if num  == val*val:
        return True
    return False






def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res






def fairRations(B):
    # Write your code here
    count = 0
    n = len(B)
    for i in range(n-1):
        if B[i]%2 !=0:
            B[i] = B[i] + 1
            B[i+1] = B[i+1]+1
            count += 2
    flag = True
    for i in B: 
        if i%2 != 0:
            flag = False
    if flag:
        return str(count)
    else:
        return "NO"














