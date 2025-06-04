class Solution:
    def reverseBits(self, n: int) -> int:
        # >> Moves bit to the right
        # << Moves bit to the left
        # AND &. 'n & 1' extracts the least significan bit
        # OR | 'result | bit' to set bits in the result

        result = 0

        for i in range(32):
            lastbit = n & 1           # Extract least significant bit
            result = (result << 1) | lastbit  # Shift result left, then add bit
            n = n >> 1                # Remove processed bit from n
        
        return result


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res