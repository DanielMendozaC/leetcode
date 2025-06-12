class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(start, end):
            # BASE CASE: Reached end of string, found valid partition
            if start == end:
                result.append(path[:])  # Add copy of current path
                return
            
            # EXPLORE: Try all possible substrings starting from 'start'
            for i in range(start, end):
                substring = s[start:i+1]  # Current substring to check
                
                # Only proceed if current substring is palindrome
                if self.check_palindrome(substring):
                    # MAKE CHOICE: Add palindrome to current path
                    path.append(substring)
                    
                    # RECURSE: Continue partitioning from next position
                    backtrack(i+1, end)
                    
                    # BACKTRACK: Remove choice to try other options
                    path.pop()
        
        result = []  # Store all valid partitions
        path = []    # Current partition being built
        backtrack(0, len(s))
        
        return result
    
    def check_palindrome(self, word):
        """Check if a word is palindrome using two pointers"""
        left, right = 0, len(word) - 1
        
        # Only need to check first half of word
        for left in range(int((right + 1) / 2)):
            if word[left] != word[right]:
                return False
            left += 1    # Note: This line is redundant (for loop handles left)
            right -= 1
        return True

# TIME COMPLEXITY: O(N × 2^N)
# - 2^N: Number of possible ways to partition string (cut/no-cut at each position)
# - N: Each palindrome check takes O(N) time in worst case
# - Total: 2^N partitions × N time per check = O(N × 2^N)

# SPACE COMPLEXITY: O(N) 
# - Recursion stack: Maximum depth N (length of string)
# - Path array: Maximum N elements at any time
# - Note: If counting output space, it's O(N × 2^N) for storing all partitions

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True