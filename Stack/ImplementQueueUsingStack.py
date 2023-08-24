class MyQueue:
    '''46ms - '''

    def __init__(self):
        self.l = []

    def push(self, x: int) -> None:
        self.l.insert(0, x)

    def pop(self) -> int:
        return self.l.pop()

    def peek(self) -> int:
        return self.l[-1]

    def empty(self) -> bool:
        return bool(not self.l)
    # 32ms
    '''def __init__(self):
        self.storage = []

    def push(self, x: int) -> None:
        self.storage.append(x)

    def pop(self) -> int:
        return self.storage.pop(0)

    def peek(self) -> int:
        return self.storage[0]

    def empty(self) -> bool:
        return not self.storage'''

    # 18ms
    ''' 
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if not self.stack2:
            self.fill()
        return self.stack2.pop()
        

    def peek(self) -> int:
        if not self.stack2:
            self.fill()
        
        return self.stack2[-1]
        
            
            
    def fill(self):
        while(self.stack1):
                self.stack2.append(self.stack1.pop())

        

    def empty(self) -> bool:
        return not len(self.stack1) and not len(self.stack2)
    '''

'''
Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
'''