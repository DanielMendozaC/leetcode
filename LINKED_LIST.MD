# Linked List Cheatsheet

## 1. Pattern Overview
**What it is:** Linear data structure where each node contains data and a pointer/reference to the next node, allowing dynamic memory allocation and efficient insertion/deletion.

**When to recognize/use this pattern:**
- Problem involves sequential data with frequent insertions/deletions
- Need to manipulate pointers or references
- Asked to solve "in-place" with O(1) extra space
- Problems mentioning "nth from end", "middle element", "cycle detection"
- Need to reverse, merge, or partition sequential data
- **Keyword triggers:** "linked list", "node", "pointer", "next", "cycle", "reverse", "merge"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Initialize pointers (current, previous, dummy if needed)
2. **Main Logic:** Traverse using while loop with null checks
3. **Process:** Manipulate pointers or extract data at each node
4. **Termination:** Stop when reaching null or meeting condition
5. **Return:** Return modified head or extracted value

### Code Template:
```python
def linked_list_template(head):
    # Step 1: Handle edge cases
    if not head:
        return head
    
    # Step 2: Initialize pointers
    dummy = ListNode(0)  # For modification problems
    dummy.next = head
    prev, curr = dummy, head
    
    # Step 3: Traverse and process
    while curr:
        # Process current node
        # Move pointers
        prev = curr
        curr = curr.next
    
    # Step 4: Return result
    return dummy.next  # or head, or extracted value
```

## 3. Common Variations
- **Dummy Node Pattern:** For modifications that might affect head - Use when removing nodes or building new lists
- **Two Pointer (Fast/Slow):** For cycle detection, finding middle - Fast moves 2 steps, slow moves 1 step
- **Two Pointer (Gap):** For nth from end problems - Create gap of n, then move both until end
- **Reversal Pattern:** For reversing entire or partial lists - Track prev, curr, next pointers
- **Merge Pattern:** For combining sorted lists - Compare values and link appropriately
- **Advanced:** K-group reversal, deep copy with random pointers, LRU cache implementation

## 4. Key Insights
- **Core insight 1:** Dummy nodes eliminate special case handling for head modifications by providing a stable starting point
- **Core insight 2:** Two pointers can solve many problems in single pass by maintaining specific relationships (distance, speed)
- **Optimization insight:** Linked lists provide O(1) insertion/deletion when you have the reference, vs O(n) for arrays
- **Trade-off insight:** Gain dynamic sizing and efficient insertion/deletion, sacrifice random access and cache locality

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(1) for insertion/deletion with reference
- Average case: O(n) for search/traversal operations
- Worst case: O(n) for operations requiring full traversal

**Space Complexity:**
- O(1) - Most linked list algorithms use constant extra space (just pointers)
- O(n) - When creating new lists or using recursion

**When is this optimal:** When you need frequent insertions/deletions, unknown size, or when implementing other data structures (stacks, queues)

## 6. Edge Cases Checklist
□ **Empty input:** head = None, return None or handle appropriately
□ **Single element:** Only one node, ensure no null pointer errors
□ **Two elements:** Minimum case for many algorithms (reversal, swapping)
□ **All same elements:** Ensure algorithms work with duplicate values
□ **Boundary conditions:** First node, last node, middle calculations
□ **Pattern-specific edges:** Cycles in list, nth greater than length, invalid positions
□ **Invalid input:** Null pointers during traversal, negative indices

## 7. Problem Examples
**Easy Level:**
- Reverse Linked List - Master the three-pointer technique
- Merge Two Sorted Lists - Learn basic merge logic
- Remove Duplicates from Sorted List - Practice deletion with dummy node

**Medium Level:**
- Remove Nth Node From End - Two pointer with gap technique
- Add Two Numbers - Handle carry and different lengths
- Linked List Cycle II - Fast/slow pointers + mathematical insight
- Reverse Linked List II - Partial reversal between positions
- Partition List - Rearrange based on value

**Hard Level:**
- Merge k Sorted Lists - Divide and conquer or priority queue
- Reverse Nodes in k-Group - Complex reversal with grouping logic

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Null pointer errors:** Always check `curr.next` before accessing - Use `while curr and curr.next`
- **Lost references:** Save `next` pointer before breaking links - `next_temp = curr.next`
- **Infinite loops:** Ensure pointers always progress - Verify movement in each iteration

**Logic Mistakes:**
- **Off-by-one in two pointers:** Draw examples to verify gap distance - Practice with small examples
- **Forgetting edge cases:** Not handling head removal - Use dummy node pattern consistently
- **Wrong return value:** Returning original head when it's been modified - Return `dummy.next` when using dummy

## 9. Interview Tips
**Recognition:**
- Ask "Does this involve sequential data manipulation?" - If yes, likely linked list problem
- Clarify if cycles are possible, if list is sorted, if values can be negative

**Implementation:**
- Start by drawing the list structure and desired outcome
- Implement dummy node first if any modification is needed
- Code the main logic, then handle edge cases
- Walk through with 0, 1, 2, and 3+ node examples

**Communication:**
- Explain your pointer strategy before coding
- Mention time/space complexity upfront
- Verbalize edge cases you're considering
- Draw diagrams to show pointer movements

**Follow-up Questions:**
- "What if the list has cycles?" - Discuss detection methods
- "Can you do it iteratively instead of recursively?" - Show both approaches
- "What if we want to preserve the original list?" - Discuss copying strategies

## 10. Quick Reference
**Pattern Triggers:** Sequential data, pointer manipulation, in-place operations, cycle detection, reversal/merging needs
**Template Summary:** 
```python
dummy = ListNode(0); dummy.next = head
while curr: process_and_move_pointers()
return dummy.next
```
**Complexity:** Time O(n), Space O(1) for most operations
**Key Insight:** Dummy nodes + two pointers solve 90% of linked list problems elegantly

---

## Notes Section
**Personal Reminders:**
- Always draw the problem first
- Dummy node for any head modifications
- Two pointers when you need relationships between nodes
- Check for cycles when not explicitly stated as acyclic

**Common Templates to Memorize:**
```python
# Reversal
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev, curr = curr, next_temp

# Two pointer (cycle detection)
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: return True
```