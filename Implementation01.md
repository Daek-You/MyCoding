## [구현] 예제-1
- 내 풀이

```python
n = int(input())
plan = input().split()
currPosition = [1, 1]


def Move(char, curPosition):
  if char == 'L':
    if curPosition[1] != 1:
      curPosition[1] -= 1
      
  elif char == 'R':
    if curPosition[1] != n:
      curPosition[1] += 1
    
  elif char == 'U':
    if curPosition[0] != 1:
      curPosition[0] -= 1
  elif char == 'D':
    if curPosition[0] != n:
      curPosition[0] += 1



for char in plan:
  Move(char, currPosition)

print(currPosition)
```
  

- 답지 풀이
```python
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx < 1 or ny < or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
```