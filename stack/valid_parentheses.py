class Solution:
    def isValid(self, s: str) -> bool:
        # Use a stack to keep track of opening brackets
        stack = []
        # Map each closing bracket to its corresponding opening bracket
        mapping = {')': '(', '}': '{', ']': '['}
        
        for v in s:
            if v in mapping:  # If it's a closing bracket
                # Check if stack is empty or if the brackets don't match
                if len(stack) == 0 or mapping[v] != stack.pop():
                    return False
            else:  # If it's an opening bracket
                stack.append(v)
                
        # If stack is empty, all brackets were properly matched
        return len(stack) == 0

# Time complexity is O(n) where n is the length of the string
# Space complexity is O(n) in worst case (e.g., "((((")