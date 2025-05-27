# Heap/Priority Queue Pattern Cheatsheet

## 1. Pattern Overview
**What it is:** A data structure that efficiently maintains elements in priority order, allowing O(1) access to the min/max element and O(log n) insertion/deletion.

**When to recognize/use this pattern:**
- Need to find the kth largest/smallest element
- Need to merge k sorted arrays/lists
- Need to process elements in priority order (scheduling, task management)
- Need efficient access to min/max while dynamically adding/removing elements
- Need to maintain a running median or top-k elements
- **Keyword triggers:** "kth largest", "kth smallest", "top k", "merge k sorted", "median", "priority", "largest", "smallest"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Initialize heap (min-heap by default in most languages)
2. **Population:** Add elements to heap based on problem requirements
3. **Processing:** Extract elements in priority order or maintain heap size
4. **Maintenance:** Keep heap at desired size (for top-k problems)
5. **Return:** Extract final result from heap or use heap state

### Code Template:
```python
import heapq

def heap_pattern_template(nums, k=None):
    # Step 1: Initialize heap
    heap = []
    
    # Step 2: Populate heap based on problem type
    for num in nums:
        heapq.heappush(heap, num)  # or -num for max heap
        
        # Step 3: Maintain heap size if needed (top-k problems)
        if k and len(heap) > k:
            heapq.heappop(heap)
    
    # Step 4: Extract result
    result = []
    while heap:
        result.append(heapq.heappop(heap))
    
    return result

# Alternative: Using heap as max-heap (negate values)
def max_heap_template(nums):
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    return -heapq.heappop(max_heap)  # Get maximum
```

## 3. Common Variations
- **Min Heap (default):** heapq in Python, smallest element at root
- **Max Heap:** Negate values when pushing/popping, or use custom comparator
- **Top-K Problems:** Maintain heap of size k, opposite heap type (max heap for k smallest)
- **Heap with Custom Objects:** Use tuples or implement __lt__ method
- **Two Heaps:** For median problems (max heap for smaller half, min heap for larger half)
- **Advanced:** Lazy deletion, heap with custom priority functions

## 4. Key Insights
- **Core insight 1:** Heap provides O(log n) insertion/deletion with O(1) peek, making it ideal for priority-based problems
- **Core insight 2:** For top-k problems, use opposite heap type - max heap for k smallest, min heap for k largest
- **Optimization insight:** Heap is much more efficient than sorting repeatedly (O(n log n) vs O(n log k))
- **Trade-off insight:** Uses O(k) extra space but provides much better time complexity than naive approaches
- **Python-specific:** heapq only provides min-heap, simulate max-heap by negating values

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(n log k) for top-k problems
- Average case: O(n log n) for full heap operations
- Worst case: O(n log n) for building heap from unsorted data

**Space Complexity:**
- O(k) for top-k problems
- O(n) for problems requiring full heap

**When is this optimal:** When you need repeated access to min/max elements, or when k << n in top-k problems

## 6. Edge Cases Checklist
□ **Empty input:** Handle empty arrays/lists, return appropriate default
□ **Single element:** Heap operations on single element
□ **k equals or exceeds array length:** Handle when k >= len(nums)
□ **All same elements:** Ensure algorithm works with duplicates
□ **Negative numbers:** Be careful with max-heap negation
□ **k = 0 or negative k:** Invalid input handling
□ **Heap underflow:** Popping from empty heap

## 7. Problem Examples
**Easy Level:**
- Kth Largest Element in Array - Use min-heap of size k
- Last Stone Weight - Max heap simulation with negation

**Medium Level:**
- Top K Frequent Elements - Combine frequency counting with min-heap
- Kth Largest Element in Stream - Maintain min-heap of size k
- Merge k Sorted Lists - Use heap to track smallest current elements
- Find Median from Data Stream - Two heaps approach
- Task Scheduler - Priority queue for task management

**Hard Level:**
- Merge k Sorted Arrays - Extension of merge k sorted lists
- Smallest Range Covering Elements from K Lists - Track elements from each list
- Sliding Window Median - Two heaps with rebalancing

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Forgetting to negate for max-heap:** Remember to negate both when pushing and popping
- **Wrong heap type for top-k:** Use min-heap for k largest, max-heap for k smallest
- **Not handling empty heap:** Always check if heap is empty before popping

**Logic Mistakes:**
- **Confusing min/max heap usage:** Think about what you want at the root
- **Not maintaining heap size:** For top-k problems, pop when size exceeds k
- **Incorrect final result extraction:** Remember to reverse or negate results if needed

## 9. Interview Tips
**Recognition:**
- Look for keywords: "kth", "top k", "largest", "smallest", "merge sorted", "median"
- Ask: "Do I need to repeatedly access min/max elements?"
- Consider: "Is this more efficient than sorting?"

**Implementation:**
- Start by clarifying if you need min or max heap
- Mention Python's heapq limitation (min-heap only)
- Code the basic heap operations first, then add problem-specific logic

**Communication:**
- Explain why heap is better than sorting: "O(n log k) vs O(n log n) when k << n"
- Walk through heap state changes with small examples
- Mention space-time tradeoffs

**Follow-up Questions:**
- "What if k is very large?" (Consider sorting instead)
- "What if we need to handle streaming data?" (Maintain heap continuously)
- "Can you optimize space?" (Discuss in-place heapify when possible)

## 10. Quick Reference
**Pattern Triggers:** Need efficient min/max access, top-k problems, merge sorted structures, running medians
**Template Summary:** `heapq.heappush(heap, item)`, `heapq.heappop(heap)`, negate for max-heap
**Complexity:** O(n log k) for top-k, O(n log n) general, O(k) or O(n) space
**Key Insight:** Use opposite heap type for top-k problems (min-heap for k largest elements)

---

## Notes Section
**Python Heap Operations:**
```python
import heapq

# Create heap
heap = []
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # O(n) heapification

# Basic operations
heapq.heappush(heap, item)    # O(log n)
min_item = heapq.heappop(heap)  # O(log n)
min_item = heap[0]            # O(1) peek

# Advanced operations
heapq.pushpop(heap, item)     # Push then pop
heapq.heapreplace(heap, item) # Pop then push
n_largest = heapq.nlargest(k, heap)
n_smallest = heapq.nsmallest(k, heap)
```

**Max Heap Simulation:**
```python
# For max heap, negate values
max_heap = []
heapq.heappush(max_heap, -value)
max_value = -heapq.heappop(max_heap)
```

**Custom Objects in Heap:**
```python
# Using tuples (priority, value)
heapq.heappush(heap, (priority, value))

# Custom class with __lt__ method
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    
    def __lt__(self, other):
        return self.priority < other.priority
```