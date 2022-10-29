def timeInWords(h, m):
    # Write your code here
    nums = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","forteen","quarter","sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","half"]
    num2word = dict(enumerate(nums, 1))
    
    if m == 0:
        word_time = num2word[h] + " o' clock"
    elif m == 1:
        word_time = num2word[m] + " minute past " + num2word[h]
    elif m == 15:
        word_time = "quarter past " + num2word[h]
    elif 2 <= m <= 29:
        word_time = num2word[m] + " minutes past " + num2word[h]
    elif m == 30:
        word_time = "half past " + num2word[h]
    elif m == 45:
        word_time = "quarter to " + num2word[h+1]
    elif 31 <= m <= 59:
        word_time = num2word[60-m] + " minutes to " + num2word[h+1]

    return word_time







def organizingContainers(container):
    # Write your code here
    total = [sum(x) for x in zip(*container)]
    capacity = [sum(x) for x in container]  
    
    capacity.sort()   
    total.sort()        
    
    if capacity == total:
        return 'Possible'
    return 'Impossible'







def encryption(s):
    # Write your code here
    split = math.ceil(math.sqrt(len(s)))
    weight = math.floor(math.sqrt(len(s)))
    ss = ''
    for g in range(split):
        ss += ''.join([c for i,c in enumerate(s) if i%split == g])+' '    
    return ss





def sansaXor(arr):
    # Write your code here
    return 0 if len(arr)%2 == 0 else eval("^".join(str(v) for i, v in enumerate(arr) if i%2==0))





def superDigit(n, k):
    # Write your code here
    m = int(n) * k % 9
    return m if m  !=0 else 9 






def gridSearch(G, P):
    # Write your code here
    for i in range(len(G)):
        indexes = [(m.start(0), m.start(0) + len(P[0])) for m in re.finditer(f"(?=({P[0]}))", G[i])]
        if len(indexes) == 0:
            continue
        for index in indexes:
            check = []
            if i + len(P) > len(G):
                continue
            for j in range(len(P)):
                check.append(G[i+j][index[0]:index[1]])
            if check == P:
                return 'YES'
    return 'NO'








def flippingMatrix(matrix):
    # Write your code here
    t = len(matrix) - 1
    n = len(matrix) // 2
    max_sum = 0
    for i in range(n):
        for j in range(n):
            max_value = max(matrix[i][j], matrix[i][t - j], matrix[t-i][j], matrix[t-i][t-j])
            max_sum += max_value
    return max_sum






def counterGame(n):
    # Write your code here
    s = bin(n)
    return 'Louise' if (s.count('1') + s[:1:-1].find('1')) % 2 == 0 else 'Richard'






def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min_unfairness = 2147483647
    for i in range(len(arr)- k + 1):
        current_unfairness = arr[i+(k-1)] - arr[i]
        if current_unfairness < min_unfairness:
            min_unfairness = current_unfairness
    return min_unfairness






def getMinimumCost(k, c):
    c.sort(reverse=True)
    total = 0
    for i in range(len(c)):
        total += int(i/k+1)*c[i]
    return total