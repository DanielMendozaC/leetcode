class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(node):
            r, c = node
            nodeval = grid[r][c]
            if nodeval == 0 or node in visited:
                return 0
            
            area = 1  # Count current cell
            visited.add(node)
            neighbors = ((r+1,c),(r-1,c),(r,c+1),(r,c-1))

            for neighbor in neighbors:
                r,c = neighbor
                in_range = r>-1 and c>-1 and r<num_rows and c<num_cols
                if in_range:
                    area = area + dfs(neighbor)  # Add areas from connected land
            return area

        # Main logic: find max area among all islands
        max_area = 0
        for i in range(num_rows):
            for j in range(num_cols):
                node = (i,j)
                nodeval = grid[i][j] 
                if node not in visited and nodeval == 1:  # Found new island
                    area = dfs(node)
                    max_area = max(max_area, area) 

        return max_area
        # Time: O(m*n), Space: O(m*n)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            # Return 0 for invalid cells (bounds, water, or visited)
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            
            visit.add((r, c))
            # Return 1 (current cell) + area of all connected neighbors
            return (1 + dfs(r + 1, c) + 
                        dfs(r - 1, c) + 
                        dfs(r, c + 1) + 
                        dfs(r, c - 1))
        
        area = 0
        # Try DFS from every cell, keep track of max area found
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
        
        # Time: O(m*n), Space: O(m*n)