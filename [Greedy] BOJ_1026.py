
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

for i in range(N - 1):
    if B[i+1] > B[i]:
        A[i], A[i+1] = A[i+1], A[i]
    

result = 0

for a, b in zip(A, B):
    result += a * b
    
print(result)

# 예제 입력2, 3에서 예외 케이스 발생