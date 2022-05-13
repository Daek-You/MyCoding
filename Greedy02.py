n, m = map(int, input().split())

targetValue = 0
for _ in range(n):
    minValue = min(map(int, input().split()))
    targetValue = max(targetValue, minValue)

print(targetValue)