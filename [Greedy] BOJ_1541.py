'''
- 첫 번째 수는 무조건 양수
- +는 괄호를 해봐야 의미가 없으니 -가 나올 때가 비교 대상
- (-)가 나왔다면 선택을 해야 함.

ex1) 5 + 4 - 3 - 5 - 10)   : - - 일 경우 뒷 자리 수가 나보다 작을 경우 수행
ex2) 55 - 50 - 40 - 30   : - + 일 경우 -가 나오기 전까지 수행
'''

def ToNumber(stringFormular):
    result = []
    strInt = ""
    preOperator = '+'
    isFirstZero = True
    
    for element in stringFormular:
        if element.isdigit():   # 숫자일 경우
           if element == '0' and isFirstZero:  # 제일 큰 자리수가 0일 경우
               continue
           strInt += element

           if isFirstZero:                     # '40'처럼 이후의 0이 생략되지 않도록
               isFirstZero = False
        
        else:                   # 부호일 경우
            data = int(strInt)
            if preOperator == '-':
                data *= -1
            preOperator = element
            isFirstZero = True
            result.append(data)
            strInt = ""
    
    # for 문이 끝나면 맨 마지막 숫자가 list에 추가되지 않으므로 추가 작업 시행
    data = int(strInt)
    if preOperator == '-':
        data *= -1
    preOperator = element
    result.append(data)
    return result

def Solution(operands):
    N = len(operands)
    _sum = 0
    
    for i in range(N - 1):
        if operands[i] < 0:         # 음수일 경우 그 다음 수를 확인
            if operands[i+1] >= 0:  # (- +)의 경우 무조건 수행
                operands[i+1] *= -1
        _sum += operands[i]
    
    _sum += operands[-1]
    return _sum
        
        
expression = input()
operands = ToNumber(expression)
result = Solution(operands)
print(result)