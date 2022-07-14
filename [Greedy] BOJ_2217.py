n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()
totalRopeCount = len(ropes)
maxWeight = ropes[0] * totalRopeCount

for i in range(1, n):
    usingRopeCount = totalRopeCount - i
    weight = ropes[i] * usingRopeCount
    
    if maxWeight < weight:
        maxWeight = weight

print(maxWeight)