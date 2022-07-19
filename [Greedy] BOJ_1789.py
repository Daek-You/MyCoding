S = int(input())

def Solution(S):
    cumulativeSum = 0
    N = 0
    num = 1
    
    while True:
        cumulativeSum += num
        remainedAMount = S - cumulativeSum
    
        if remainedAMount == 0:
            N += 1
            return N
    
        elif remainedAMount < num:
            while True:
                cumulativeSum -= num
                remainedAMount = S - cumulativeSum
                
                if remainedAMount > num:
                    cumulativeSum += remainedAMount
                    N += 1
                    return N
                
                N -= 1
                num -= 1
                
        N += 1
        num += 1

print(Solution(S))
