

n, k = map(int, input().split())
values = []

for _ in range(n):
    values.append(int(input()))
    
values.reverse()
count = 0


for value in values:
    cnt = k // value
    
    if cnt > 0:
        count += cnt
        k %= value
    
    if k == 0:
        break
        
        
print(count)