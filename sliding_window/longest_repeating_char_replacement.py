class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        slow = 0
        freq = {}
        longest = 0
        max_freq = 0

        for fast in range(len(s)):
            freq[s[fast]] = freq.get(s[fast], 0) + 1

            # Replace neededs = substring size - most commom character
            # Most common character -> max frequency
            max_freq = max(freq.values()) if freq else 0
            replacements = fast-slow+1 - max_freq

            while replacements>k:
                freq[s[slow]] -= 1
                # Decrease the freq before moving the slow pointer!!
                slow += 1
                max_freq = max(freq.values()) if freq else 0
                replacements = fast-slow+1 - max_freq

            longest = max(longest, fast-slow+1)

        return longest

        # Time complexity O(n) and space O(n)
        # Space is O(1) because you store at most 26 uppercase letters in the frequency
        # map, regardless of input size.

# Others solutions. Neetcode:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                    
                res = max(res, r - l + 1)
        return res


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
