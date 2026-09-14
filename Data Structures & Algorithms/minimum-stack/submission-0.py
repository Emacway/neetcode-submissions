class MinStack:

    def __init__(self):
        self.stack = [] #initialize empty stack
        self.min = float('inf') #initialize minimum as infinity

    def push(self, val: int) -> None:
        if self.stack == []:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val
                

    def pop(self) -> None:
        if self.stack == []:
            return
        
        pop = self.stack.pop()

        if pop < 0: #we just popped the min!
            self.min = self.min - pop #reset min to previous

    def top(self) -> int:
        top = self.stack[-1]
        
        if top > 0: # not the min
            return top + self.min
        else:
            return self.min 

    def getMin(self) -> int:
        return self.min
