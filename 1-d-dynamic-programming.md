# 1-D Dynamic Programming Cheatsheet

## 1. Pattern Overview
**What it is:** A technique that solves complex problems by breaking them into simpler subproblems, storing results in a 1-dimensional array to avoid redundant calculations.

**When to recognize/use this pattern:**
- Problem asks for "number of ways" to do something
- Need to find optimal (max/min) value across a sequence
- Problem has overlapping subproblems and optimal substructure
- Can be solved recursively but has repeated calculations
- Sequential decision-making where each choice affects future options
- **Keyword triggers:** "ways to", "maximum", "minimum", "can you reach", "optimal", "count", "fibonacci-like", "climbing", "robber", "decode"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Create dp array of size n+1, initialize base cases
2. **Main Logic:** Iterate through array filling each position
3. **Process:** Use recurrence relation to calculate dp[i] from previous values
4. **Termination:** When all positions are filled
5. **Return:** Usually dp[n] or sometimes max/min of entire array

### Code Template:
```python
def dp_1d_template(n):
    # Step 1: Setup/Initialization
    dp = [0] * (n + 1)  # Create array
    
    # Step 2: Base cases
    dp[0] = base_case_0
    if n > 0:
        dp[1] = base_case_1
    
    # Step 3: Fill array using recurrence relation
    for i in range(2, n + 1):
        dp[i] = function_of(dp[i-1], dp[i-2], ...)  # Recurrence relation
    
    # Step 4: Return result
    return dp[n]

# Space-optimized version (when only need previous few values)
def dp_1d_optimized(n):
    if n <= 1: return base_cases
    
    prev2, prev1 = base_case_0, base_case_1
    for i in range(2, n + 1):
        current = function_of(prev1, prev2)
        prev2, prev1 = prev1, current
    
    return prev1
```

## 3. Common Variations
- **Bottom-up (Tabulation):** Fill dp array from smallest to largest subproblem - most common approach
- **Top-down (Memoization):** Recursive approach with caching - good for complex state transitions
- **Space-optimized:** Use variables instead of full array when only previous few values needed
- **Range DP:** dp[i] represents optimal solution for range [0...i] or [i...n]
- **Choice DP:** At each step, make optimal choice between multiple options
- **Advanced:** State compression, rolling arrays for very large inputs

## 4. Key Insights
- **Core insight 1:** If you can solve a problem recursively with overlapping subproblems, you can use DP to avoid redundant calculations
- **Core insight 2:** Optimal substructure - optimal solution contains optimal solutions to subproblems
- **Optimization insight:** Reduces exponential time complexity O(2^n) to linear O(n) by storing intermediate results
- **Trade-off insight:** Exchange space (O(n)) for time efficiency, but can often optimize space to O(1)
- **Recurrence relation is key:** The hardest part is figuring out how dp[i] relates to previous values

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(n) - single pass through array
- Average case: O(n) - each subproblem solved exactly once
- Worst case: O(n) - linear scan with constant work per element

**Space Complexity:**
- O(n) for standard approach - storing all intermediate results
- O(1) for space-optimized - only storing previous few values

**When is this optimal:** When problem has overlapping subproblems and you need all/most intermediate results, or when recursive solution has exponential time complexity

## 6. Edge Cases Checklist
□ **Empty input (n=0):** Usually requires special base case, often return 0 or 1
□ **Single element (n=1):** Second base case, handle separately from main loop
□ **Two elements (n=2):** First case where recurrence relation applies
□ **Negative inputs:** Check if problem allows negative numbers/indices
□ **Large inputs:** Consider integer overflow, may need modular arithmetic
□ **Array bounds:** Ensure dp array is large enough, watch for off-by-one errors
□ **Invalid input:** Handle impossible cases (e.g., negative steps in climbing stairs)

## 7. Problem Examples
**Easy Level:**
- Climbing Stairs - Classic fibonacci variant, dp[i] = dp[i-1] + dp[i-2]
- House Robber - Choice at each house: rob or skip, dp[i] = max(dp[i-1], dp[i-2] + nums[i])
- Fibonacci Number - Foundation problem, dp[i] = dp[i-1] + dp[i-2]

**Medium Level:**
- Coin Change - Minimum coins needed, dp[i] = min(dp[i-coin] + 1) for all coins
- Longest Increasing Subsequence - dp[i] = max length ending at position i
- Word Break - Can string be segmented, dp[i] = any(dp[j] and s[j:i] in dict)
- Decode Ways - Number of ways to decode string, consider 1-digit and 2-digit numbers
- House Robber II - Circular array variation, solve twice (include first or exclude first)

**Hard Level:**
- Regular Expression Matching - Complex state transitions with wildcards
- Edit Distance - Transform one string to another with minimum operations
- Palindrome Partitioning II - Minimum cuts to make all substrings palindromes

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Array bounds errors:** Accessing dp[i-1] when i=0, always check bounds or start loop from correct index
- **Wrong array size:** Creating dp[n] instead of dp[n+1], leads to index out of bounds
- **Incorrect base cases:** Not handling n=0, n=1 cases properly

**Logic Mistakes:**
- **Wrong recurrence relation:** Not correctly identifying how current state depends on previous states
- **Forgetting edge cases:** Not handling empty input, single elements, or boundary conditions
- **Optimal substructure violation:** Assuming problem has optimal substructure when it doesn't

## 9. Interview Tips
**Recognition:**
- Ask yourself: "Can I break this into smaller subproblems?" and "Do subproblems overlap?"
- Look for recursive structure with repeated calculations
- Keywords like "ways to", "maximum", "minimum" are strong indicators

**Implementation:**
- Start with recursive solution to understand the problem structure
- Identify base cases first - these become your dp initialization
- Write recurrence relation in comments before coding
- Consider space optimization after getting basic solution working

**Communication:**
- Explain the recursive structure first: "This problem can be broken down as..."
- Walk through small example to show how dp array fills up
- Mention that you're trading space for time to avoid redundant calculations
- If you get stuck, start with brute force recursive solution

**Follow-up Questions:**
- "Can you optimize the space complexity?" (Use rolling variables)
- "What if the constraints were much larger?" (Consider modular arithmetic)
- "How would you handle negative numbers?" (Adjust base cases)

## 10. Quick Reference
**Pattern Triggers:** Overlapping subproblems + optimal substructure, "ways to" or "optimal" problems
**Template Summary:** `dp[i] = f(dp[i-1], dp[i-2], ...)` with proper base cases
**Complexity:** O(n) time, O(n) space (optimizable to O(1) space)
**Key Insight:** Build solution incrementally using solutions to smaller subproblems

---

## Notes Section

**Common Recurrence Relations:**
```python
# Fibonacci-like (ways to reach)
dp[i] = dp[i-1] + dp[i-2]

# Choice problems (take or skip)
dp[i] = max(dp[i-1], dp[i-2] + value[i])

# Minimum cost problems
dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

# Counting with constraints
dp[i] = sum(dp[j] for j in valid_previous_states)
```

**Space Optimization Pattern:**
```python
# Instead of dp array
prev2, prev1 = base_case_0, base_case_1
for i in range(2, n + 1):
    current = prev1 + prev2  # or whatever recurrence
    prev2, prev1 = prev1, current
return prev1
```

**Debug Tips:**
- Print dp array at each step to verify logic
- Test with small inputs (n=0,1,2,3) manually
- Draw out the decision tree for recursive approach first
- Verify base cases handle all boundary conditions