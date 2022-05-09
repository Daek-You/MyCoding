# [실전문제] 큰 수의 법칙
#### 내 풀이

``` python
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

maxNum = secNum = numbers[0]
for num in numbers[1:]:
  if maxNum < num:
    secNum = maxNum
    maxNum = num
  elif secNum < num:
    secNum = num

count = 0
sum = 0

for _ in range(M):
  if maxNum == secNum:
    sum += maxNum
  else:
    if count == K:
      sum += secNum
      count = 0
      continue
    sum += maxNum
    count += 1

print(sum)
```


#### 답지 풀이
```python
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0:
        break
    result += second
    m -= 1

print(result)
```


## 느낀 점
- 정렬에 대해 걸리는 시간 계산을 고려하지 못했음
- 좀 더 나은 방법이 없는지 고민하다가 시간을 헛날림
- 이런 부분도 다음부터는 고려할 수 있도록 해보자.