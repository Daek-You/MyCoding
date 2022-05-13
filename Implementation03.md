# [구현 시뮬레이션] 게임 개발
- N * M의 직사각형 맵
- 각 칸은 육지 또는 바다
- 캐릭터는 동서남북 중 한 곳을 바라봄
- 맵의 각 칸은 (A, B)
- A는 북쪽으로부터 떨어진 칸의 개수
- B는 서쪽으로부터 떨어진 칸의 개수
- 캐릭터는 상하좌우 움직임이 가능하고 바다는 못 감

다음의 메뉴얼을 따라야 한다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
   - 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
   - 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

### 입력 조건
1. 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력 (3 <= N, M <= 50)
2. 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.

방향 d의 값으로는 다음과 같이 4가지가 존재한다.

- 0 : 북쪽
- 1 : 동쪽
- 2 : 남쪽
- 3 : 서쪽

3. 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다.
   - 맵의 외곽은 항상 바다로 되어 있다.

- 0 : 육지
- 1 : 바다

4. 처음에 캐릭터가 위치한 칸의 상태는 항상 육지


### 출력 조건
- 첫째 줄에 이동을 마친 후, 캐릭터가 방문한 칸의 수를 출력


### 내가 작성한 코드
```python
n, m = map(int, input().split())
a, b, d = map(int, input().split())

lookDirections = [0, 1, 2, 3]
groundType = [0, 1, 2]     # 2는 이미 밟은 땅을 의미
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ground = []

for _ in range(n):
    ground.append(list(map(int, input().split())))


def LookAtLeft():
    length = len(lookDirections)
    
    if d == 0:
        return lookDirections[length - 1]
    else:
        return lookDirections[d - 1]

result = 0
count = 0
while True:
  nextDirection = LookAtLeft()
  dA = a + steps[nextDirection][0]
  dB = b + steps[nextDirection][1]

  if dA >= 0 and dA < n and dB >= 0 and dB < m:
    if ground[dA][dB] == 1 or ground[dA][dB] == 2:
      if count == 4:
        backStep = (a + (-steps[d][0]), b + (-steps[d][1]))
        if ground[backStep[0]][backStep[1]] == 1:
          break
        elif ground[backStep[0]][backStep[1]] == 2:
          a, b = backStep
          count = 0
          continue
        
      d = nextDirection
      count += 1
      continue

    elif ground[dA][dB] == 0:
      d = nextDirection
      ground[dA][dB] = 2
      a, b = dA, dB
      result += 1
    count = 0
  
print(result)
```


### 답지 풀이
```python
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력 받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
  # 왼쪽 회전
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]

  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if d[nx][ny] == 0 and array[nx][ny] == 0
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue

  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]

    # 뒤로 갈 수 있다면 이동
    if array[nx][ny] == 0:
      x = nx
      y = ny
    
    # 뒤가 바다로 막혀 있는 경우
    else:
      break
    turn_time = 0

print(count)
```


### 느낀 점
- 처음 풀어보는 시뮬레이션 문제라 요구 조건들을 전부 파악하는데 오래 걸림
- 빠른 시간 내에 요구 조건들을 파악하는 것이 핵심일 듯