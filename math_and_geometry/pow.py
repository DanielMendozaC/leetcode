class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = 1

        if n<0:
            exp_nums = -n
            nega = True
        else:
            nega = False
            exp_nums = n

        for i in range(exp_nums):
            exp *= x

        if nega:
            return 1/exp
        else:
            return exp

        # brute force sol. O(n) and O(1)
        # or

        # return x**n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        current_power = x
        
        # Binary exponentiation
        while n > 0:
            # If n is odd, multiply result by current power
            if n % 2 == 1:
                result *= current_power
            
            # Square the current power and halve n
            current_power *= current_power
            n //= 2
        
        return result

# How it works for x=2, n=10:
# n=10 (even): result=1, current_power=2
# n=5 (odd):   result=1*2=2, current_power=4, n=5//2=2  
# n=2 (even):  result=2, current_power=16, n=2//2=1
# n=1 (odd):   result=2*16=32, current_power=256, n=1//2=0
# n=0: stop, return 32

# Time: O(log n) - we halve n each iteration
# Space: O(1) - only using a few variables
