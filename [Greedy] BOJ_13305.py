# Python3는 정수 범위가 무제한

N = int(input())           # 도시의 개수 (2 <= N <= 100000)
distances = list(map(int, input().split()))
oilCosts = list(map(int, input().split()))
totalDistance = sum(distances)
minOilCost = min(oilCosts)

#---------------------------------------------------------------------

def Solution(distances, totalDistance, oilCosts, minOilCost):
    i = 0
    totalOilCost = 0
    
    while i < N - 1:                           # 마지막 도시 전까지만 체크하면 됨
        currentOilCost = oilCosts[i]
        isNextLastCity = (i == N - 2)
        moveDistance = 0
    
        if isNextLastCity:                     # 마지막 전 도시까지 왔다면 그 도시에서 남은 거리만큼 기름 사면 끝
            totalOilCost += currentOilCost * totalDistance
            return totalOilCost
    
        while oilCosts[i+1] >= currentOilCost: # 다음 도시 기름값이 현재 내가 머무르는 도시 기름값보다 비쌀 경우
            betweenDistance = distances[i]     # 현재 도시 기름값보다 값 싼 도시가 나올 때까지 이동할만큼의 기름을 현재 도시에서 구매
            moveDistance += betweenDistance
            totalOilCost += currentOilCost * betweenDistance
            i += 1
        
            if i == N - 2:
                break
        
        # 기름값이 싼 도시와 그 이전 도시 사이의 거리만큼 기름 구매가 while문 조건에 의해 생략됐으므로 진행
        betweenDistance = distances[i]
        moveDistance += betweenDistance
        totalOilCost += currentOilCost * betweenDistance
        totalDistance -= moveDistance
        i += 1
    
        if oilCosts[i] == minOilCost:   # 제일 값 싼 주유소를 찾았다면 남은 거리만큼 사고 끝
            totalOilCost += minOilCost * totalDistance
            return totalOilCost
    


result = Solution(distances, totalDistance, oilCosts, minOilCost)
print(result)