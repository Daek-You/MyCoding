# 3의 배수 찾는 법
# 각 자리의 합이 3의 배수가 되면 그 수는 3의 배수
# ex) 1234567890은 1+2+3+4+5+6+7+8+9+0 = 45 가 3의 배수이므로 3의 배수
# 10의 배수는 두 자리 이상의 수의 일의 자리가 0이어야 함
# 이걸 이용하면 풀 수 있을 것 같다.

N = input()
numbers = []
sumNum = 0

for charNum in N:
    intNum = int(charNum)
    numbers.append(int(intNum))
    sumNum += intNum

if (0 not in numbers) or (sumNum % 3 != 0):
    print(-1)
    exit()
    
numbers.sort(reverse = True)       # 내림차순 정렬
result = "".join(map(str, numbers))
print(result)
