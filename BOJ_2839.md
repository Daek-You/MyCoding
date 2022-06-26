# [BOJ 2839] [설탕 배달](https://www.acmicpc.net/problem/2839)
---
  


### 내 풀이  

```python
n = int(input())  # 설탕 KG
anwserSums = []


loopCountPack3 = n // 3
loopCountPack5 = n // 5


for x in range(loopCountPack3 + 1):
    for y in range(loopCountPack5 + 1):
         result = 3 * x + 5 * y
         
         if result == n:
             anwserSums.append(x+y)
         

if len(anwserSums) == 0:
    print("-1")
else:
    print(min(anwserSums))
```


### 느낀 점
- 3과 5의 몫을 통해 루프 반복 수를 줄이고자 노력하였음
- 다른 사람의 코드를 보니, 굉장히 아름답길래 풀이를 요약해봄
    1. 5KG 팩으로 담을 수 있는 개수를 먼저 구한다.
    2. 5KG 팩으로 담고 남은 설탕 KG양을 저장한다.
    3. 남은 설탕 양을 3KG 팩으로 얼만큼 담을 수 있는지를 계산
        - 정확히 계산이 된다면, 해당 5KG 팩 개수와 3KG 팩 개수를 더한 것이 답
        - 계산이 안 된다면, 5KG 팩 개수 하나를 줄이고, 남은 설탕 양에 +5KG
        - 다시 3번 계산
        - 5KG 팩 개수가 음수가 된다면 해가 없다는 의미이므로 -1 리턴


- 이런 생각을 할 수 있도록 노력해봐야겠다.