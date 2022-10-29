def countingValleys(steps, path):
    # Write your code here
    a,b = 0,0
    d = {"U":1, "D":-1}
    for i in path:
        if not a+d[i] and a<0:
            b+=1
        a+=d[i]
    return b






def libraryFine(d2, m2, y2, d1, m1, y1):
    # Write your code here
    if y2 > y1 :
        return 10000
    elif m2 > m1 and y1==y2:
        return 500 * (m2-m1)
    elif d2 > d1 and m1==m2 and y1==y2:
        return 15 * (d2-d1)
    else:
        return 0





def timeConversion(s):
    # Write your code here
    s = s.split(':')
    if s[0] == '12' and s[2][2] == 'A':
        s[0] = str(int(s[0]) - 12) + '0'
        return s[0] +':' + s[1] + ':' + s[2][:2]
    if s[0] == '12' and s[2][2] == 'P':
        return s[0] +':' + s[1] + ':' + s[2][:2]        
    if s[2][2] == 'P':
        s[0] = str(int(s[0]) + 12)
    
        
    print(s[0] +':' + s[1] + ':' + s[2][:2])
    return s[0] +':' + s[1] + ':' + s[2][:2]








def caesarCipher(s, k):
    # Write your code here
    def next_char(c):
        if c.islower() or c.isupper():
            return chr((ord('a') if c.islower() else ord('A')) + (((ord(c) + k) - (ord('a') if c.islower() else ord('A'))) % 26))
        return c

    return ''.join(list(map(next_char, s)))






def towerBreakers(n, m):
    # Write your code here
    if m ==1 : 
        return 2
    if n%2 ==0: 
        return 2 
    return 1








def dayOfProgrammer(year):
    # Write your code here
    if year < 1918:
        if year % 4 == 0:
            return f'12.09.{year}'
        return f'13.09.{year}'    
    if year == 1918:
        return f'26.09.{year}'
            
    if (year % 400 == 0) and (year % 100 == 0):
        return f'12.09.{year}'

    if (year % 4 ==0) and (year % 100 != 0):
        return f'12.09.{year}'

    return f'13.09.{year}'







def hurdleRace(k, height):
    # Write your code here
    return max(max(height)-k,0)






def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    res1 = max(0, 6 - n)
    res2 = 0
    if not any(c in password for c in lower_case):
        res2 += 1
    if not any(c in password for c in upper_case):
        res2 += 1
    if not any(c in password for c in numbers):
        res2 += 1
    if not any(c in password for c in special_characters):
        res2 += 1
    return max(res1, res2)







def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    min_diff = abs(arr[-1]-arr[0])
    
    for i in range(len(arr)-1):
        min_diff = min(abs(arr[i]-arr[i+1]),min_diff)
    return min_diff





def marsExploration(s):
    # Write your code here
    cnt = 0
    n = "SOS"*(len(s)//3)
    for i in range(len(s)):
        if s[i] != n[i]:
            cnt += 1
    return(cnt)











