# Data Structure Implementation | Queue, PriorityQueue
- ```Enqueue``` : 데이터를 삽입
- ```Dequeue``` : 첫 번째 데이터 가져오기. 없으면 ```None``` 리턴


## Queue
```python
class Queue:
    def __init__(self):
        self.queueList = list()
        self.size = 0
    
    def Enqueue(self, data):
        self.queueList.append(data)
        self.size += 1

    def Dequeue(self):
        if size > 0:
            result = self.queueList[0]
            del self.queueList[0]
            size -= 1
            return result
        return None
    
    def Print(self):
        for i in range(self.size):
            print(self.queueList[i], end = ' ')
        print()
```


## PriorityQueue
```python
class PriorityQueue:
    def __init__(self):
        self.QueueList = list()
        self.size = 0
        
    def Enqueue(self, priority, data):
        self.QueueList.append((priority, data))
        self.size += 1
        
    def Dequeue(self):
        
        if self.size > 0:
            self.QueueList.sort()
            result = self.QueueList[0][1]
            self.size -= 1
            del self.QueueList[0]
            return result
        return None
```