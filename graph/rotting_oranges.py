class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # What's this?
        queue = deque()
        # visited = set()
        fresh_count = 0
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count+=1

        while queue and fresh_count>0:
            minutes+=1
            size = len(queue)
            for i in range(size): # Process current level
                r, c = queue.popleft()
                # Process current node

                for dr, dc in directions:
                    ri, ci = r + dr, c + dc
                    if -1<ri<rows and -1<ci<cols and grid[ri][ci]==1:
                        queue.append((ri,ci))
                        grid[ri][ci]=2
                        fresh_count-=1

        return minutes if fresh_count==0 else -1
        




# Neetcode sol:
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1