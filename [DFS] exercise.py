'''
# 테스트 케이스 입력
2
2
1 2
2 1
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

# 출력
#1 2
#2 5
'''


import math
import sys
sys.setrecursionlimit(10**6)

def DFS(row, col, currentYear):
    if row >= N or row < 0 or col >= N or col < 0:
        return False
    
    if visited[row][col] == False and field[row][col] > currentYear:
        visited[row][col] = True
        DFS(row + 1, col, currentYear) # 상
        DFS(row - 1, col, currentYear) # 하
        DFS(row, col - 1, currentYear) # 좌
        DFS(row, col + 1, currentYear) # 우
        return True
    return False 

def GetMaxAreaCount(currentYear):
    count = 0
    for row in range(N):
        for col in range(N):
            if DFS(row, col, currentYear):
                count += 1
    return count       



T = int(input())
field = []

for testID in range(1, T + 1):
    N = int(input())
    maxHeight = -math.inf
    afterYear = 1
    visited = [[False for _ in range(N)] for _ in range(N) ]
    
    for i in range(N):  # N x N 맵 2차원 리스트로 형성
        field.append(list(map(int, input().split())))
        thisMaxHeight = max(field[i])
        
        if maxHeight < thisMaxHeight:   # 맵에서 최고 높이 값 찾기
            maxHeight = thisMaxHeight
    
    result = 1    # 모든 땅의 높이가 1인 경우가 있을 수 있으므로
    while afterYear < maxHeight:
        thisYearMaxAreaCount = GetMaxAreaCount(afterYear)
        if result < thisYearMaxAreaCount:
            result = thisYearMaxAreaCount
        
        # 방문했던 곳들 다시 False로 초기화
        for i in range(N):
            for j in range(N):
                visited[i][j] = False
        afterYear += 1
    
    print("#" + str(testID) + ' ' + str(result))
    field.clear()
    del visited