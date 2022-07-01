# # Data Structure Implementation | Stack
- ```Push()``` : 데이터 삽입
- ```Pop()``` : 데이터 삭제. 없으면 ```None```` 리턴


```python
class Stack:
    def __init__(self):
        self.stackList = list()
        self.size = 0

    def Push(self, data):
        self.stackList.append(data)
        self.size += 1

    def Pop(self):
        if self.size > 0:
            result = self.stackList[-1]
            self.size -= 1
            del self.stackList[-1]
            return result
        return None

```