<<<<<<< HEAD
# 1<= N <= 50
# 0 < A, B <= 100
# 입력 받기
=======

>>>>>>> dac44361740f900da90481b54d93b67a89b4a648
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

<<<<<<< HEAD

# 전략
# 1. A를 내림차순 정렬한다.
# 2. B의 원소 중 가장 작은 원소의 인덱스를 알아낸다.
# 3. A를 복사한 새로운 리스트의 해당 인덱스 위치에 A 원소를 넣는다.
# 4. 처리한 B의 원소는 이후 탐색에서 제외되도록 무한대 처리한다.
# 5. for문을 돌며 2-4번 과정을 반복한다.
# 6. 가장 작은 S의 합계는 처리한 A와 B의 각 원소의 곱의 합 

A.sort(reverse = True)
tempB = B.copy()
resultA = A.copy()

for elementA in A:
    minElementB = min(tempB)
    idx = tempB.index(minElementB)
    resultA[idx] = elementA
    tempB[idx] = float("inf")
    
    
del tempB
minSum = 0
for a, b in zip(resultA, B):
    minSum += a * b

print(minSum)
=======
A.sort()

for i in range(N - 1):
    if B[i+1] > B[i]:
        A[i], A[i+1] = A[i+1], A[i]
    

result = 0

for a, b in zip(A, B):
    result += a * b
    
print(result)

# 예제 입력2, 3에서 예외 케이스 발생
>>>>>>> dac44361740f900da90481b54d93b67a89b4a648
