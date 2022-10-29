def isValid(s):
    # Write your code 
    from collections import Counter
    chars = set(s)
    deletions = 0
    letters = {}
    
    for c in chars:
        letters[c] = s.count(c)
        
    val = list(letters.values())
    val_counter = Counter(val)
    common_value = val_counter.most_common(1)[0][0]
    
    for v in val:
        if common_value == v:
            continue
        elif v == 1:
            deletions += 1
        elif common_value - v not in [-1, 1]:
            deletions += 2
        else:
            deletions += 1
    
    return "YES" if deletions <= 1 else "NO"




def gamingArray(arr):
    # Write your code here
    totalRounds = 0
    max_ = 0
    for i in range(len(arr)): 
        if arr[i] > max_ :
            max_ = arr[i]
            totalRounds += 1
    if totalRounds % 2 == 0:
        return 'ANDY'
    return 'BOB'