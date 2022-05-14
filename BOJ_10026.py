n = int(input())
graph = []

# 그림 정보
for _ in range(n):
  graph.append(list(input()))


def DFS(graph, color, x, y, hasBlind):
  if x < 0 or x >= n or y < 0 or y >= n:
      return False
  
  if hasBlind:
      if (graph[x][y] == 'R' or graph[x][y] == 'G') and (color == 'R' or color == 'G'):
          color = graph[x][y] 
  
  if graph[x][y] == color:
      graph[x][y] = '#'  # 방문 처리
      DFS(graph, color, x - 1, y, hasBlind)
      DFS(graph, color, x + 1, y, hasBlind)
      DFS(graph, color, x, y - 1, hasBlind)
      DFS(graph, color, x, y + 1, hasBlind)
      return True
  return False


generalResult = 0
blindnessResult = 0
generalGraph = [_list.copy() for _list in graph]
blindGraph = [_list.copy() for _list in graph]


for i in range(n):
  for j in range(n):
    if generalGraph[i][j] != '#':
        if DFS(generalGraph, generalGraph[i][j], i, j, False):
          generalResult += 1
    
    if blindGraph[i][j] != '#':
        if DFS(blindGraph, blindGraph[i][j], i, j, True):
            blindnessResult += 1
    
print(generalResult, blindnessResult, end = ' ')
    