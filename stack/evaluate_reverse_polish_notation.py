class Solution:
    def check_op(self, num1, num2, op):
        if op=='+':
            return num1+num2
        elif op=='-':
            return num1-num2
        elif op=='*':
            return num1*num2
        else:
            # return num1//num2
            # Truncate toward zero
            return int(num1 / num2)

    # Using a stack and pushing result to the stack
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])

        stack_op = []
        for v in tokens:
            stack_op.append(v)
           
            if v in '+-*/':
                ope = v
                stack_op.pop()
                num2 = int(stack_op.pop())
                num1 = int(stack_op.pop())
                result=self.check_op(num1,num2,ope)
                stack_op.append(result)

        return result
        # Time complexity is o(n) and space is o(n)
        


        
    # More "optimal"
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])

        stack_op = []
        for v in tokens:
            if v in '+-*/':
                # If operator, pop two values and compute
                num2 = int(stack_op.pop())
                num1 = int(stack_op.pop())
                result = self.check_op(num1, num2, v)
                stack_op.append(result)
            else:
                # If number, just push to stack
                stack_op.append(v)

        return stack_op[0]  # Return the final value on stack



    # # IMPORTANT TO READ!!!
    # # Good solution but too many edge cases and can be improved to avoid using 
    # # cum variable
    # def evalRPN(self, tokens: List[str]) -> int:
    #     if len(tokens)<=1:
    #         return tokens
    #     result = None
    #     op=0
    #     stack_op = []
    #     for v in tokens:
    #         stack_op.append(v)
    #         # First operator
    #         current = stack_op[-1]
    #         if op==0 and current in '+-*/':
    #             stack_op.pop()
    #             # Important to think that is a string and not a number
    #             num2 = int(stack_op.pop())
    #             num1 = int(stack_op.pop())

    #             result=self.check_op(num1,num2,current)
    #             op+=1

    #         # Next operations
    #         elif current in '+-*/': 
    #             stack_op.pop()
    #             num1 = int(stack_op.pop())
    #             result=self.check_op(num1,result,current)

    #     return result
    #     # Time complexity is o(n) and space is o(n)
        