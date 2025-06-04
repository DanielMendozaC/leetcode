class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:
            return [strs]

        result_hash = {}
        # result = []

        for i, v in enumerate(strs):
            st = ''.join(sorted(v))
            if st in result_hash:
                # result_hash[st] = result_hash.get(st).append(v) # This return None, not the list
                # So I should just append to it
                result_hash[st].append(v)
            else:
                result_hash[st] = [v]
                # result.append(result_hash[st])

        # return result
        return list(result_hash.values())
        # Time complexity is O(m * nlog(n)) m: list length, n: longest string length and space is O(m * n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        # Time complexity is O(m * n) m: list length, n: longest string length and space is O(m * n)
        # Space complexity:
        # O(m) extra space.
        # O(m∗n) space for the output list.

        