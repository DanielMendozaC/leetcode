class Solution:
    def hammingWeight(self, n: int) -> int:
        def bit(n):
            num = int(n/2)
            residual = n%2
            return num, residual

        num_bits=0
        num=n
        while num!=0:
            num, residual = bit(num)

            if residual==1:
                num_bits+=1
            
        return num_bits


# Simplified Version
def hammingWeight(self, n: int) -> int:
    count = 0
    while n != 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count

# Best Approach

def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += n & 1  # Bitwise AND to check last bit
        n >>= 1        # Right shift (faster than division)
    return count
