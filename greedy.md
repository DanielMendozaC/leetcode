# Greedy Algorithm Cheatsheet

## 1. Pattern Overview
**What it is:** Make the locally optimal choice at each step, trusting it leads to a globally optimal solution.

**When to recognize/use this pattern:**
- **Optimization problems:** "Find minimum/maximum", "fewest/most", "optimal way"
- **Selection problems:** "Choose items", "schedule tasks", "assign resources"
- **Can make irrevocable decisions:** Once you choose, you never need to reconsider
- **Intuitive "best choice" exists:** There's an obvious "greedy" choice at each step
- **Keyword triggers:** "minimum", "maximum", "optimal", "earliest", "latest", "shortest", "longest"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Sort input by the appropriate criteria (this is often the key insight!)
2. **Initialize:** Set up result storage and tracking variables
3. **Iterate:** Go through sorted elements one by one
4. **Greedy Choice:** At each step, make the locally optimal decision
5. **Update:** Update your result and continue to next element

### Code Template:
```python
def greedy_template(items):
    # Step 1: Sort by appropriate criteria (KEY INSIGHT!)
    items.sort(key=lambda x: x[relevant_field])
    
    # Step 2: Initialize result and tracking variables
    result = []  # or count = 0, total = 0, etc.
    last_chosen = None  # track previous choice if needed
    
    # Step 3: Iterate through sorted items
    for current_item in items:
        # Step 4: Make greedy choice (locally optimal)
        if should_choose(current_item, last_chosen):
            result.append(current_item)  # or count += 1
            last_chosen = current_item
    
    return result  # or count, total, etc.

def should_choose(current, last):
    # Define your greedy criteria here
    # Examples: no overlap, better value, etc.
    pass
```

## 3. Common Variations
- **Activity Selection:** Sort by end time, pick non-overlapping activities
- **Fractional Knapsack:** Sort by value/weight ratio, take highest ratios first
- **Scheduling:** Sort by deadline, penalty, or duration depending on objective
- **Advanced Interval Problems:** Sort by start/end time based on specific requirements

## 4. Key Insights
- **Greedy Choice Property:** Making locally optimal choice leads to globally optimal solution
- **Optimal Substructure:** Problem can be broken down into subproblems with optimal solutions
- **Irrevocable Decisions:** Once you make a choice, you never need to undo it
- **Sorting is Critical:** 90% of greedy problems require sorting by the RIGHT criteria
- **Proof Challenge:** The hardest part is proving your greedy choice is correct

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(n) - if input already sorted
- Average case: O(n log n) - dominated by sorting
- Worst case: O(n log n) - still dominated by sorting

**Space Complexity:**
- O(1) to O(n) - depends on whether you store results or just count

**When is this optimal:** When the greedy choice property holds and you can prove correctness

## 6. Edge Cases Checklist
□ **Empty input:** Return 0, empty array, or default value
□ **Single element:** Usually just return that element or count of 1
□ **Two elements:** Test your greedy logic on minimal case
□ **All same elements:** Ensure your comparison logic handles equality
□ **Already optimal input:** Should return input as-is
□ **Impossible cases:** When no valid solution exists
□ **Boundary values:** Maximum/minimum possible inputs

## 7. Problem Examples
**Easy Level:**
- Best Time to Buy and Sell Stock - Choose minimum buy day, maximum sell day
- Assign Cookies - Sort both arrays, match greedily

**Medium Level:**
- Maximum Subarray (Kadane's) - At each step, decide: extend current or start new
- Jump Game - Greedily track furthest reachable position
- Non-overlapping Intervals - Sort by END time, keep non-overlapping
- Gas Station - Track cumulative gas difference
- Partition Labels - Greedy expansion of partition boundaries

**Hard Level:**
- Candy - Two-pass greedy (left-to-right, then right-to-left)
- Meeting Rooms II - Sort by start time, use heap for room management

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Wrong sort criteria:** Sorting by start time when you need end time (or vice versa)
- **Off-by-one in comparisons:** Using `<` instead of `<=` for boundary conditions
- **Forgetting edge cases:** Not handling empty input or single elements

**Logic Mistakes:**
- **Assuming greedy works:** Not all optimization problems have greedy solutions
- **Wrong greedy choice:** Choosing based on intuition without mathematical proof
- **Missing global optimum:** Local choices don't always lead to global optimum

## 9. Interview Tips
**Recognition:**
- Look for words: "minimum", "maximum", "optimal", "schedule", "select"
- Ask: "Can I make an irrevocable choice at each step?"
- Ask: "What's the obvious 'best' choice at each moment?"

**Implementation:**
- Start by identifying what to sort by (this is usually the key insight)
- Implement basic greedy logic first
- Add edge case handling last

**Communication:**
- Explain WHY your greedy choice is correct
- Walk through a small example to show it works
- Mention that greedy doesn't always work, but explain why it works here

**Follow-up Questions:**
- "What if we needed to maximize instead of minimize?"
- "How would this change if we had additional constraints?"
- "Can you prove this greedy approach is optimal?"

## 10. Quick Reference
**Pattern Triggers:** Optimization problems where you can make locally optimal choices
**Template Summary:** Sort → Iterate → Make greedy choice → Update result
**Complexity:** O(n log n) time, O(1) to O(n) space
**Key Insight:** The sorting criteria determines if greedy works - this is usually the main challenge

---

## Notes Section
**Critical Insight:** In interval problems:
- Sort by START time: when you need to process events chronologically (merging, inserting)
- Sort by END time: when you want to maximize count or minimize removals

**Proof Strategy:** To prove greedy is optimal:
1. Show that greedy choice is always part of some optimal solution
2. Show that after greedy choice, remaining problem has optimal substructure
3. Conclude that greedy choice + optimal solution to subproblem = optimal solution to original

**Interview Red Flags:** If you can't quickly identify what to sort by, the problem might not be greedy!