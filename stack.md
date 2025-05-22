# Stack Cheatsheet

## 1. Pattern Overview
**What it is:** LIFO (Last In First Out) data structure that supports push (add to top) and pop (remove from top) operations in O(1) time.

**When to recognize/use this pattern:**
- Problems involving nested structures (parentheses, brackets, tags)
- Need to track "most recent" or "last seen" elements
- Expression evaluation or parsing problems
- Undo/redo functionality or backtracking scenarios
- Converting recursion to iteration
- Problems asking for "next greater/smaller" element
- **Keyword triggers:** "valid parentheses", "nested", "most recent", "last in first out", "bracket matching", "expression", "next greater", "monotonic"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Initialize empty stack (list in Python)
2. **Main Logic:** Iterate through input elements
3. **Process:** Push/pop based on current element and stack top
4. **Termination:** Process all elements or until stack meets condition
5. **Return:** Stack contents, boolean result, or computed value

### Code Template:
```python
def stack_template(input_data):
    # Step 1: Initialize stack
    stack = []
    
    # Step 2: Process each element
    for element in input_data:
        # Step 3: Stack operations based on element
        if condition_to_push:
            stack.append(element)
        elif condition_to_pop and stack:
            popped = stack.pop()
            # Process popped element
        
        # Additional logic here
    
    # Step 4: Return result
    return result  # could be stack, boolean, computed value
```

## 3. Common Variations
- **Basic Stack:** Simple push/pop operations - Use for parentheses matching, expression evaluation
- **Monotonic Stack:** Maintain increasing/decreasing order - Use for next greater/smaller element problems
- **Stack with Min/Max:** Track minimum/maximum alongside values - Use when need O(1) min/max access
- **Two Stacks:** Use two stacks for specific algorithms - Use for implementing queues or special operations
- **Advanced:** Stack for DFS traversal, expression parsing with operators and precedence

## 4. Key Insights
- **Core insight 1:** LIFO property naturally handles nested structures and maintains "most recent" relationships
- **Core insight 2:** Monotonic stacks can solve O(n²) brute force problems in O(n) by maintaining useful elements only
- **Optimization insight:** Stack eliminates need for recursion in many tree/graph traversals, avoiding call stack overhead
- **Trade-off insight:** Gain O(1) access to most recent element, sacrifice random access to middle elements

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(1) for push/pop/peek operations
- Average case: O(n) for processing n elements
- Worst case: O(n) for traversing all elements

**Space Complexity:**
- O(n) - Stack can grow to size of input in worst case
- O(1) - For operations on existing stack

**When is this optimal:** When you need LIFO access pattern, nested structure processing, or converting recursion to iteration

## 6. Edge Cases Checklist
□ **Empty input:** Empty string/array, return appropriate default (True for parentheses, empty stack, etc.)
□ **Single element:** One character/number, handle push/pop logic correctly
□ **Two elements:** Minimum case for testing stack interactions
□ **All same elements:** Ensure algorithm works with duplicates
□ **Boundary conditions:** Very large inputs, nested depth limits
□ **Pattern-specific edges:** Unmatched brackets, invalid expressions, empty stack operations
□ **Invalid input:** Null input, non-matching types, popping from empty stack

## 7. Problem Examples
**Easy Level:**
- Valid Parentheses - Classic bracket matching with stack
- Implement Stack using Arrays - Understand basic operations
- Baseball Game - Simple push/pop with score calculation

**Medium Level:**
- Daily Temperatures - Monotonic decreasing stack for next warmer day
- Asteroid Collision - Stack simulation with collision logic
- Evaluate Reverse Polish Notation - Stack-based expression evaluation
- Next Greater Element - Monotonic stack pattern
- Min Stack - Stack with O(1) minimum tracking

**Hard Level:**
- Largest Rectangle in Histogram - Monotonic increasing stack with area calculation
- Basic Calculator - Complex expression parsing with parentheses and operators

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Empty stack access:** Always check `if stack:` before `stack.pop()` or `stack[-1]`
- **Wrong LIFO logic:** Using `stack[0]` instead of `stack[-1]` for top element
- **Index errors:** Forgetting that stack might be empty during operations

**Logic Mistakes:**
- **Monotonic stack direction:** Confusing increasing vs decreasing order requirements
- **When to pop vs push:** Not clearly defining the condition for each operation
- **Result construction:** Forgetting to handle remaining elements in stack after main loop

## 9. Interview Tips
**Recognition:**
- Ask "Do I need to remember the most recent elements?" - If yes, likely stack
- Look for nested patterns, matching problems, or "next X" type questions

**Implementation:**
- Start with basic stack operations, then add problem-specific logic
- For monotonic stacks, clearly state whether maintaining increasing/decreasing order
- Handle empty stack checks consistently throughout

**Communication:**
- Explain LIFO principle and why it fits the problem
- Walk through stack state changes with small examples
- Mention when you're using stack to avoid recursion

**Follow-up Questions:**
- "Can you implement this with constant extra space?" - Discuss space optimization
- "What if we need to access elements in the middle?" - Compare with other data structures
- "How would you handle very large inputs?" - Discuss memory limitations

## 10. Quick Reference
**Pattern Triggers:** Nested structures, most recent access, next greater/smaller, expression evaluation, recursion to iteration
**Template Summary:** 
```python
stack = []
for element in input:
    while stack and condition: stack.pop()
    stack.append(element)
return process(stack)
```
**Complexity:** Time O(n), Space O(n) for most problems
**Key Insight:** Stack's LIFO property naturally solves problems requiring "most recent" or nested structure handling

---

## Notes Section
**Personal Reminders:**
- Always check if stack is empty before pop/peek
- For monotonic stacks, be clear about increasing vs decreasing
- Draw out stack states for complex problems
- Remember that each element is pushed and popped at most once in monotonic stack problems

**Common Templates to Memorize:**
```python
# Basic bracket matching
for char in s:
    if char in "({[":
        stack.append(char)
    elif stack and matches(stack[-1], char):
        stack.pop()
    else:
        return False
return len(stack) == 0

# Monotonic decreasing stack (next greater element)
result = [-1] * len(nums)
stack = []  # indices
for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        idx = stack.pop()
        result[idx] = num
    stack.append(i)
```