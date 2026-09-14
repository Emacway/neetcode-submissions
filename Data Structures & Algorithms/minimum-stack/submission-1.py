class MinStack:
# keep track of differences from minimum value

    def __init__(self):
        self.stack = [] #initialize empty stack
        self.min = float('inf') #initialize minimum as infinity

    def push(self, val: int) -> None:
        if self.stack == []:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min) #if val is new min we appended a negative number
            if val < self.min:
                self.min = val #reset the min
                

    def pop(self) -> None:
        if self.stack == []:
            return
        
        pop = self.stack.pop()

        if pop < 0: #we just popped the min!
            self.min = self.min - pop #reset min to previous min

    def top(self) -> int:
        top = self.stack[-1] #difference between a value and the min
        
        if top > 0: # not the min
            return top + self.min # value is difference plus min
        else:
            return self.min #else return min

    def getMin(self) -> int:
        return self.min #easy peasy to get the min now!
