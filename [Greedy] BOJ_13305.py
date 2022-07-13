# Python3는 정수 범위가 무제한

N = int(input())           # 도시의 개수 (2 <= N <= 100000)
distances = None
oilCosts = None
minOilCost = None
totalDistance = 0

distances = list(map(int, input().split()))
totalDistance = sum(distances)

oilCosts = list(map(int, input().split()))
minOilCost = min(oilCosts)
    
i = 0
totalOilCost = 0

while i < N - 1:
    currentOilCost = oilCosts[i]
    moveDistance = 0
    
    if i == N - 2:  # 마지막 전 도시까지 왔다면 그 도시에서 남은 거리만큼 기름 사면 끝
        totalOilCost += currentOilCost * totalDistance
        break
    
    while oilCosts[i+1] >= currentOilCost:
        betweenDistance = distances[i]
        moveDistance += betweenDistance
        totalOilCost += currentOilCost * betweenDistance
        i += 1
        
    betweenDistance = distances[i]
    moveDistance += betweenDistance
    totalOilCost += currentOilCost * betweenDistance
    totalDistance -= moveDistance
    i += 1
    
    if oilCosts[i] == minOilCost:
        totalOilCost += minOilCost * totalDistance
        break
    
print(totalOilCost)

# 예제2에서 인덱스 오버플로우 남