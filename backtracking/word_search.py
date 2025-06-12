class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        num_rows = len(board)
        num_cols = len(board[0])

        word_list = list(word)
        visited = set()
        word_check = []

        def backtrack(row, col):
            pos = (row,col)
            visited.add(pos)
            word_check.append(board[row][col])

            if word_check != word_list[:len(word_check)]:
                return False
            elif word_check == word_list:
                return True

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in directions:
                adj_row, adj_col = row + dr, col + dc

                if (adj_row, adj_col) not in visited and 0 <= adj_row < num_rows and 0 <= adj_col < num_cols:
                    result = backtrack(adj_row, adj_col)
                    visited.remove((adj_row, adj_col))
                    word_check.pop()

                    if result:
                        return result
                    
 
        for i in range(num_rows):
            for j in range(num_cols):
                result = backtrack(i, j)

                visited.remove((i,j))
                word_check.pop()

                if result:
                    return True
        return False

# Time: O(m × 4^n) where m = total cells, n = word length  
# Space: O(n) where n = word length



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()  # Track visited cells to avoid cycles
        
        def dfs(r, c, i):
            # BASE CASE: Successfully found entire word
            if i == len(word):
                return True
            
            # EARLY TERMINATION: Check all invalid conditions
            if (min(r, c) < 0 or           # Out of bounds (negative)
                r >= ROWS or c >= COLS or   # Out of bounds (too large)
                word[i] != board[r][c] or   # Character doesn't match
                (r, c) in path):            # Already visited this cell
                return False
            
            # MAKE CHOICE: Mark current cell as visited
            path.add((r, c))
            
            # EXPLORE: Try all 4 directions (DFS)
            # Use 'or' for short-circuit: if any path succeeds, return True
            res = (dfs(r + 1, c, i + 1) or  # Down
                   dfs(r - 1, c, i + 1) or  # Up  
                   dfs(r, c + 1, i + 1) or  # Right
                   dfs(r, c - 1, i + 1))    # Left
            
            # BACKTRACK: Remove current cell from visited (undo choice)
            path.remove((r, c))
            
            return res
        
        # Try starting from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):  # Start with index 0 of word
                    return True
        return False

# TIME COMPLEXITY: O(M * N * 4^L)
# - M * N: We try starting from each cell on the board
# - 4^L: For each starting position, in worst case we explore 4 directions 
#        for L levels deep (where L = length of word)
# - In practice, pruning makes it much faster than worst case

# SPACE COMPLEXITY: O(L) 
# - Recursion stack depth: at most L (length of word)
# - Path set: at most L elements (length of current path)
# - L = len(word)


# Time: O(m × 4^n) where m = total cells, n = word length  
# Space: O(n) where n = word length


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or visited[r][c]):
                return False

            visited[r][c] = True
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False