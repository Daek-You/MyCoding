# BOJ_1931 : [회의실 배정](https://www.acmicpc.net/problem/1931)
- Greedy Algorithm, Sorting


### 전략
- 가장 이른 시간대부터 써야, 회의를 많이 할 수 있으므로 ```회의 시작 시간```을 기준으로 정렬
- 회의 간 공백이 적어야 회의를 많이 할 수 있으므로, ```회의 종료 시간```을 기준으로 다시 한 번 정렬
- 정렬된 회의 스케쥴 리스트에서 하나씩 꺼내오기
    - 다음 회의 시간이 이전 회의 종료 시간보다 크다면, 회의 수 카운트를 1 증가 시키고 종료 시간을 다음 회의의 종료 시간으로 설정


### 소스 코드
```python
n = int(input())
meetingList = []

for _ in range(n):
    startTime, endTime = map(int, input().split())
    meetingList.append((startTime, endTime))

meetingList = sorted(meetingList, key = lambda element: element[0])
meetingList = sorted(meetingList, key = lambda element: element[1])

preEndTime = 0
count = 0

for startTime, endTime in meetingList:
    if startTime >= preEndTime:
        count += 1
        preEndTime = endTime
        
print(count)
```