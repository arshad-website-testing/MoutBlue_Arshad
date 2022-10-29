def maximumToys(prices, k):
    # Write your code here
    num_toys = 0
    total = 0
    prices.sort()
    for price in prices:
        if (total + price) < k:
            total += price
            num_toys += 1
    return num_toys






def closestNumbers(arr):
    # Write your code here
    ls = sorted(arr)    
    min = ls[1] - ls[0]

    for i in range(len(ls) - 1):
        if ls[i + 1] - ls[i] < min:
            min = ls[i + 1] - ls[i]
    
    result = [(ls[i], ls[i + 1]) for i in range(len(ls) - 1) 
              if ls[i + 1] - ls[i] == min]

    return [item for t in result for item in t]






def findMedian(arr):
    # Write your code here
    sorted_list=sorted(arr)
    median=sorted_list[int((n-1)/2)]
    return median




def balancedSums(arr):
    # Write your code here
    total = sum(arr)
    for element in arr:
        if total == element:
            return "YES"
        total -= element * 2
    return "NO"





def flippingBits(n):
    # Write your code here
    return n ^ 4294967295






def jimOrders(orders):
    # Write your code here
    return tuple(zip(*sorted(enumerate(map(sum, orders),1),key=lambda x:x[1])))[0]





def twoArrays(k, A, B):
    # Write your code here
    count = 0
    A = sorted(A)
    B = sorted(B,reverse=True)
    for i in range(len(A)):
        if A[i]+B[i]>=k:
            count +=1
    return 'YES' if count==len(A) else 'NO'







def missingNumbers(arr, brr):
    # Write your code here
    crr = [b for b in set(brr) if brr.count(b) > arr.count(b)]
    crr.sort()
    return  crr





def formingMagicSquare(s):
    # Write your code here
    c1 = [(8, 1, 6), (3, 5, 7), (4, 9, 2)]
    c2 = [[c1[2-c][f] for c in range(3)] for f in range(3)]
    c3 = [[c1[f][2-c] for c in range(3)] for f in range(3)]
    c4 = [[c1[c][f] for c in range(3)] for f in range(3)]
    all_squares = [c1, c1[::-1], c2, c2[::-1], c3, c3[::-1], c4, c4[::-1]]
    dif = min([sum([abs(s[f][c] - square[f][c]) for f in range(3) for c in range(3)]) for square in all_squares])
    return dif







def climbingLeaderboard(ranked, player):
    # Write your code here
    rank_list = []
    cur = ranked[0]
    rank_list.append(cur)
    for e in ranked[1:]:
        if e != cur :
            rank_list.append(e)
            cur = e
    print(rank_list)
    # build result list
    res =[]
    i = len(rank_list)-1
    j=0
    while(j < len(player) and i >=0):
        r = rank_list[i]
        if player[j] < r:
            res.append(i+2)
            j=j+1
        elif player[j] == r:
            res.append(i+1)
            j=j+1
        else:
            if i==0:
                while(j<len(player)):
                    res.append(1)
                    j=j+1
                return res
            i=i-1            
    return res









