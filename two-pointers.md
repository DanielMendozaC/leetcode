# Two Pointers Pattern Cheatsheet

## 📝 Pattern Description

The Two Pointers pattern uses two pointers to iterate through a data structure (usually an array or linked list) in a single pass. By properly managing these pointers, we can solve problems more efficiently than with nested loops.

## 🔍 When to Recognize This Pattern

Look for these clues in the problem statement:
- Working with sorted arrays
- Need to find pairs/triplets that satisfy certain conditions
- Questions involving palindromes
- Problems asking for subarrays/substrings with specific properties
- Need to compare elements from opposite ends
- Finding a cycle in a linked list

## 🧩 Common Variations

### 1. Opposite Direction (Left & Right)
- Start pointers at opposite ends (beginning and end)
- Move toward each other until they meet
- **Examples**: Two Sum II, Container With Most Water, Trapping Rain Water

### 2. Same Direction (Slow & Fast)
- Both pointers start at beginning
- Fast pointer moves at a different pace than slow pointer
- **Examples**: Remove Duplicates, Finding Cycles, Middle of Linked List

### 3. Sliding Window Variant
- Both pointers move in the same direction but maintain a window
- **Examples**: Minimum Size Subarray Sum, Longest Substring Without Repeating Characters

### 4. Multiple Arrays
- One pointer per array, usually moving in sync
- **Examples**: Merge Sorted Arrays, Intersection of Arrays

## ⚙️ General Algorithm Steps

1. Initialize pointers based on the variation (opposite ends or same start point)
2. Iterate while pointers haven't crossed or met condition
3. At each step:
  - Check if current elements satisfy the target condition
  - If yes, process result or return answer
  - If no, move pointer(s) based on comparison logic
4. Return the appropriate result (might be processed during iteration)

## 🧠 Key Insights

- Two pointers often transforms O(n²) solutions to O(n)
- For sorted arrays, compare current sum with target to determine which pointer to move
- For linked list cycles, if fast and slow pointers ever meet, a cycle exists
- In sliding window variations, carefully define when to expand vs. contract the window
- Pay attention to edge cases: empty arrays, single elements, duplicates

## ⚠️ Common Mistakes

- Not checking boundary conditions properly
- Forgetting to handle duplicates in certain problems
- Incorrect pointer movement logic
- Not considering what happens when pointers cross
- Off-by-one errors when moving pointers

## 📊 Complexity Analysis

- Time Complexity: Typically O(n) where n is the input size
- Space Complexity: Usually O(1) since we only use two pointers regardless of input size
- Much better than nested loop approaches that would be O(n²)

## 🔗 Classic Problems

1. Two Sum II (sorted array)
2. Remove Duplicates from Sorted Array
3. Container With Most Water
4. 3Sum (and variations)
5. Palindrome Verification
6. Trapping Rain Water
7. Linked List Cycle Detection
8. Middle of the Linked List
9. Reverse Words in a String
10. Move Zeroes

## 💡 Interview Tips

- Verbalize your approach before coding
- Consider sorting the input if it isn't already sorted (changes time complexity)
- Draw out examples with arrows showing pointer movements
- Handle edge cases explicitly (empty arrays, single elements)
- Consider all possible outcomes of pointer movements
- Practice explaining why this approach is optimal compared to alternatives

---