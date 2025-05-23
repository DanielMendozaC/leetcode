# Backtracking Pattern Cheatsheet

## 1. Pattern Overview
**What it is:** A systematic method to explore all possible solutions by building candidates incrementally and abandoning ("backtracking") partial candidates that cannot lead to valid solutions.

**When to recognize/use this pattern:**
- Need to find ALL possible solutions or combinations
- Problem involves making a sequence of choices where each choice affects future options
- Need to explore a solution space systematically (like a decision tree)
- Asked to generate permutations, combinations, subsets, or valid arrangements
- Problem mentions constraints that require trying different paths
- **Keyword triggers:** "all possible", "generate", "find all", "permutations", "combinations", "subsets", "valid arrangements", "place N queens", "solve sudoku"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Define base case and constraints, initialize result collection
2. **Choice:** At each step, iterate through all possible choices
3. **Constraint Check:** Verify if current choice is valid given constraints
4. **Recurse:** Make the choice and recursively explore further
5. **Backtrack:** Undo the choice to try the next option
6. **Base Case:** When complete solution found, add to results

### Code Template:
```python
def backtrack_template(nums, target, path, result, start_index):
    # Base case - found complete solution
    if is_complete_solution(path, target):
        result.append(path[:])  # Make copy of current path
        return
    
    # Try all possible choices from current state
    for i in range(start_index, len(nums)):
        # Skip invalid choices (pruning)
        if not is_valid_choice(nums[i], path):
            continue
            
        # Make choice
        path.append(nums[i])
        
        # Recurse with updated state
        backtrack_template(nums, target, path, result, i + 1)
        
        # Backtrack - undo choice
        path.pop()
    
    return result

def main_function(input_params):
    result = []
    path = []
    backtrack_template(input_params, target, path, result, 0)
    return result
```

## 3. Common Variations
- **Subset Generation:** Generate all possible subsets - include/exclude each element
- **Permutation Generation:** Generate all arrangements - use visited array or swapping
- **Combination Generation:** Generate combinations of k elements - use start_index to avoid duplicates
- **Constraint Satisfaction:** N-Queens, Sudoku - check constraints before making moves
- **Path Finding:** Find all paths in graph/matrix - mark visited, unmark on backtrack
- **Advanced:** Optimization problems with pruning - use bounds to eliminate branches early

## 4. Key Insights
- **Core insight 1:** Backtracking is DFS on the solution space tree where each node represents a partial solution
- **Core insight 2:** The key is knowing when to prune - eliminating branches that cannot lead to valid solutions
- **Optimization insight:** Pruning dramatically reduces the search space from brute force enumeration
- **Trade-off insight:** You trade some complexity for completeness - guaranteed to find all solutions but can be slow without proper pruning

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(2^n) for subsets, O(n!) for permutations
- Average case: Depends on pruning effectiveness
- Worst case: O(2^n) to O(n!) depending on problem

**Space Complexity:**
- O(depth of recursion) = O(n) for call stack
- O(result size) for storing all solutions

**When is this optimal:** When you need ALL solutions and the problem has overlapping constraint checks that allow effective pruning

## 6. Edge Cases Checklist
□ **Empty input:** Return appropriate empty result ([], [[]])
□ **Single element:** Handle base case correctly
□ **Duplicate elements:** Use sorting + skipping to handle duplicates
□ **Invalid constraints:** Check if any solution is possible
□ **Large search space:** Ensure pruning is effective to avoid timeout
□ **Path copying:** Always copy current path when adding to results
□ **Index bounds:** Careful with start_index and loop bounds

## 7. Problem Examples
**Easy Level:**
- **Subsets (78)** - Basic backtracking template with include/exclude decisions
- **Letter Combinations of Phone Number (17)** - Multiple choice at each step

**Medium Level:**
- **Combination Sum (39)** - Can reuse elements, need target sum constraint
- **Permutations (46)** - Need visited array to track used elements
- **Generate Parentheses (22)** - Constraint checking with valid parentheses rules
- **Word Search (79)** - 2D backtracking with visited matrix
- **Subsets II (90)** - Handle duplicates with sorting and skipping

**Hard Level:**
- **N-Queens (51)** - Complex constraint checking for queen placement
- **Sudoku Solver (37)** - Multiple constraints, optimization needed

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Shallow copy issue:** Using `result.append(path)` instead of `result.append(path[:])` 
- **Index errors:** Not handling start_index correctly in combinations
- **Infinite recursion:** Forgetting to increment index or check base cases

**Logic Mistakes:**
- **Duplicate handling:** Not sorting array when dealing with duplicate elements
- **Constraint timing:** Checking constraints too late, missing pruning opportunities
- **Backtrack forgetting:** Not properly undoing choices (pop, unmark visited, etc.)

## 9. Interview Tips
**Recognition:**
- Look for words like "all possible", "generate all", "find every"
- If brute force would require nested loops of unknown depth, consider backtracking
- Ask: "Do I need to try multiple paths and remember the best/all solutions?"

**Implementation:**
- Start by identifying what constitutes a complete solution
- Define your choice space clearly (what options at each step)
- Implement constraint checking first, then the recursive structure
- Always code the backtrack step immediately after the recursive call

**Communication:**
- Explain the decision tree concept - "At each step we have X choices"
- Mention pruning opportunities early in explanation
- Walk through a simple example showing the backtrack process

**Follow-up Questions:**
- "How would you optimize this if you only needed one solution?" (early termination)
- "What if there were additional constraints?" (more pruning opportunities)
- "How would you handle very large inputs?" (iterative deepening, memory optimization)

## 10. Quick Reference
**Pattern Triggers:** Need all solutions, multiple sequential choices, constraint satisfaction
**Template Summary:** 
```python
def backtrack(choices, path, result):
    if complete: result.append(path[:])
    for choice in choices:
        if valid: path.append(choice); backtrack(...); path.pop()
```
**Complexity:** Time O(2^n to n!), Space O(recursion depth)
**Key Insight:** DFS through solution space with systematic choice-making and undoing

---

## Notes Section
**Pruning Strategies:**
- Sort input when dealing with duplicates
- Check constraints as early as possible
- Use bound checking for optimization problems
- Consider symmetry breaking for problems like N-Queens

**Memory Optimization:**
- Use iterative approach for very deep recursion
- Consider yielding results instead of storing all in memory
- Use bit manipulation for visited tracking when possible

**Debugging Tips:**
- Print path at each recursive call to visualize the tree
- Verify backtracking is working by checking path length
- Test with small inputs first to validate logic