class MinStack:

    # Solution of using pair: value, current minimum or you can also do
    # the same thing by just using 2 stacks instead of one stack with pairs.
    def __init__(self):
        self.stackl = []

    def push(self, val: int) -> None:

        if not self.stackl or val<self.stackl[-1][1]:
            minv = val
        else: 
            minv = self.stackl[-1][1]

        self.stackl.append([val, minv])

    def pop(self) -> None:
        self.stackl.pop()

    def top(self) -> int:
        return self.stackl[-1][0]

    def getMin(self) -> int:
        if self.stackl:
            return self.stackl[-1][1]
        else: 
            return None
    # Time complexity of o(1) and space of o(n)

        

    # # Easiest, less optimal solution:
    # def __init__(self):
    #     self.stack_l = []
    #     # self.min = inf

    # def push(self, val: int) -> None:
    #     self.stack_l.append(val)

    # def pop(self) -> None:
    #     self.stack_l.pop()

    # def top(self) -> int:
    #     return self.stack_l[-1]

    # def getMin(self) -> int:
    #     min_n = inf
    #     for v in self.stack_l:
    #         if v<min_n:
    #             min_n=v
    #     return min_n
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()