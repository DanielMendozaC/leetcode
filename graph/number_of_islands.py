class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0]) 

        def dfs(node):
            row, col = node
            nodeval = grid[row][col]
            if nodeval=="0" or node in visited:
                return

            visited.add(node)
            # Explore 4 directions: down, right, left, up
            neighbors = ((row+1,col),(row,col+1),(row,col-1),(row-1,col))
            for neighbor in neighbors:
                r, c = neighbor
                if r>=0 and c>=0 and r<num_rows and c<num_cols:  # Check bounds
                    dfs((r,c))
        
        island = 0
        # Check every cell in grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                node = (i,j)
                if node not in visited and grid[i][j]=='1':  # Found new island
                    island+=1
                    dfs((i,j))  # Mark entire connected island as visited

        return island

        # Time: O(m*n), Space: O(m*n)

    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define 4 directions: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # Base case: out of bounds or water
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or grid[r][c] == "0"
            ):
                return
            
            # Mark current land as visited by "sinking" it (turn to water)
            grid[r][c] = "0"
            
            # Explore all 4 neighboring cells
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Check every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":  # Found unvisited land
                    dfs(r, c)  # Sink the entire connected island
                    islands += 1  # Count this island
                    
        return islands

# Time Complexity: O(m*n) - visit each cell once
# Space Complexity: O(m*n) - recursion stack in worst case
# Key insight: Use grid itself as visited tracker by modifying land to water

