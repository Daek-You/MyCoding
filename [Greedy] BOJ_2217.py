# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 수 있음
# 이때 각 로프가 받는 가중치는 w/k
# 

n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(input()))

ropes.sort()
maxWeight = ropes[-1]
ropesNum = len(ropes)

for i in range(n):
    length = ropesNum - i
    weight = ropes[i] * length
    
    if maxWeight < weight:
        maxWeight = weight

print(maxWeight)