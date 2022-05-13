## [구현] 왕실의 나이트
- 내 풀이  


```python
inputStr = input()
row, col = int(inputStr[1]), inputStr[0]
count = 0

def CheckOneRowMove():
  result = 0
  if row + 1 <= 8:
    result += 1
  if row - 1 >= 1:
    result += 1

  return result

def CheckOneColMove():
  result = 0
  if ord(col) + 1 <= ord('h'):
    result += 1
  if ord(col) - 1 >= ord('a'):
    result += 1

  return result


if ord(col) + 2 <= ord('h'): # 오른쪽 두 칸 이동이 가능
  count += CheckOneRowMove()
      
if ord(col) - 2 >= ord('a'): # 왼쪽 두 칸 이동 가능
  count += CheckOneRowMove()

if row + 2 <= 8:  # 아래로 두 칸 이동 가능
  count += CheckOneColMove()
if row - 2 >= 1:  # 위로 두 칸 이동 가능
  count += CheckOneColMove()

print(count)
```

- 답지 풀이  
```python
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
    result += 1

print(result)

```


### 느낀 점
- 정보를 저장하여 활용하는 방법을 좀 더 연습해 봐야겠다.