# SJF Scheduling 정책을 생각해보자.


n = int(input())  # 사람 수
Pi = list(map(int, input().split()))
result = 0
waitingTime = 0


while len(Pi) != 0:
    value = min(Pi)
    result += min(Pi) + waitingTime
    
    del Pi[Pi.index(value)]
    waitingTime += value

print(result)