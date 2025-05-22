class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # Optimal approach: Monotonic decreasing stack
        # Strategy: Stack stores indices of days waiting for warmer weather
        # When we find a warmer day, resolve all previous cooler days
        
        stack_t = []  # Store indices of days waiting for warmer temperature
        answer = [0] * len(temperatures)  # Pre-fill with 0 (no warmer day)
        
        for i, v in enumerate(temperatures):
            # Pop all previous days that current day can resolve
            while stack_t and v > temperatures[stack_t[-1]]:
                ini_day_index = stack_t.pop()
                answer[ini_day_index] = i - ini_day_index  # Days until warmer
            
            stack_t.append(i)  # Add current day to wait list
        
        # Days remaining in stack never get warmer (already 0 in answer)
        return answer
        
        # Time: O(n) - each element pushed/popped once
        # Space: O(n) - stack can hold up to n elements

        return answer



        

        answer = []
        for i in range(len(temperatures)):
            c = 1
            for j in range(i+1,len(temperatures)):
                ini_day = temperatures[i]
                current_day = temperatures[j]
                if current_day>ini_day:
                    answer.append(c)
                    break
                elif j==(len(temperatures)-1):
                    answer.append(0)
                c+=1
        answer.append(0)
        return answer

        # Time complexity of o(n^2) and space o(n)