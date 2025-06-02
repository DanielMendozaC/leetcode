# Intervals Pattern Cheatsheet

## 1. Pattern Overview
**What it is:** A pattern for solving problems involving overlapping ranges, time periods, or any continuous segments that may intersect, merge, or conflict with each other.

**When to recognize/use this pattern:**
- **Key indicator 1:** Problem mentions "intervals", "ranges", "meetings", "time periods", or "schedules"
- **Key indicator 2:** Need to merge overlapping segments or find intersections between ranges
- **Key indicator 3:** Asked to detect conflicts, find minimum resources needed, or optimize scheduling
- **Keyword triggers:** "overlap", "merge", "conflict", "schedule", "booking", "calendar", "timeline"

## 2. Core Template/Algorithm Steps

### General Algorithm Steps:
1. **Setup:** Sort intervals by start time (usually), handle edge cases
2. **Main Logic:** Iterate through sorted intervals with pointer/index
3. **Process:** Compare current interval with previous/result intervals for overlap
4. **Termination:** Process all intervals or until specific condition met
5. **Return:** Modified intervals list, count, or boolean result

### Code Template:
```python
def intervals_template(intervals):
    # Step 1: Handle edge cases
    if not intervals or len(intervals) <= 1:
        return intervals
    
    # Step 2: Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 3: Initialize result
    result = [intervals[0]]
    
    # Step 4: Iterate and process overlaps
    for current in intervals[1:]:
        last = result[-1]
        
        # Check for overlap: current.start <= last.end
        if current[0] <= last[1]:
            # Merge: update end to maximum of both ends
            last[1] = max(last[1], current[1])
        else:
            # No overlap: add current interval
            result.append(current)
    
    return result
```

## 3. Common Variations
- **Merge Intervals:** Combine all overlapping intervals into non-overlapping set
- **Insert Interval:** Add new interval to existing sorted list and merge if needed
- **Meeting Rooms:** Detect if any two meetings conflict (boolean result)
- **Meeting Rooms II:** Find minimum rooms needed (count overlapping intervals)
- **Interval Intersection:** Find common parts between two interval lists
- **Advanced:** Non-overlapping intervals (remove minimum to make non-overlapping)

## 4. Key Insights
- **Core insight 1:** Sorting by start time transforms chaotic overlap detection into linear scan
- **Core insight 2:** Two intervals [a,b] and [c,d] overlap if max(a,c) ≤ min(b,d), or simply if c ≤ b when sorted
- **Optimization insight:** O(n log n) sorting + O(n) merge beats O(n²) pairwise comparison
- **Trade-off insight:** Space complexity varies - can modify in-place or use extra space for cleaner code

## 5. Complexity Analysis
**Time Complexity:**
- Best case: O(n log n) - dominated by sorting
- Average case: O(n log n) - sorting + linear scan
- Worst case: O(n log n) - same, even with all overlaps

**Space Complexity:**
- O(1) to O(n) - depends on whether modifying in-place or creating new result

**When is this optimal:** When dealing with ranges/intervals that need overlap detection or merging - no known better than O(n log n) for unsorted input

## 6. Edge Cases Checklist
□ **Empty input:** Return empty list or handle as specified
□ **Single element:** Usually return as-is, no merging needed
□ **Two elements:** Test basic overlap/merge logic
□ **All same elements:** Handle identical intervals (usually merge to one)
□ **Boundary conditions:** Adjacent intervals [1,2] and [2,3] - touching but not overlapping
□ **Pattern-specific edges:** Invalid intervals (start > end), negative values, very large ranges
□ **Invalid input:** Null arrays, malformed intervals, unsorted when expecting sorted

## 7. Problem Examples
**Easy Level:**
- **Merge Intervals (LC 56):** Classic merge problem - foundation of pattern
- **Meeting Rooms (LC 252):** Simple conflict detection using sorting

**Medium Level:**
- **Insert Interval (LC 57):** Insert and merge in sorted list without full re-sort
- **Meeting Rooms II (LC 253):** Count maximum overlapping intervals using heap/sweep line
- **Non-overlapping Intervals (LC 435):** Remove minimum intervals to make non-overlapping
- **Minimum Number of Arrows (LC 452):** Find minimum points to "burst" all intervals

**Hard Level:**
- **Calendar III (LC 732):** Track booking counts with overlapping events
- **Employee Free Time (LC 759):** Find gaps between all employees' schedules

## 8. Common Pitfalls & Mistakes
**Coding Mistakes:**
- **Forgetting to sort:** Always sort by start time unless input guaranteed sorted
- **Wrong overlap condition:** Use `current_start <= last_end` not `<` for inclusive intervals
- **Off-by-one errors:** Be careful with inclusive vs exclusive interval boundaries

**Logic Mistakes:**
- **Boundary confusion:** [1,2] and [2,3] are adjacent, not overlapping for most problems
- **Modifying while iterating:** Don't modify original array if you need to iterate over it
- **Incorrect merge logic:** New end should be `max(last_end, current_end)`, not just `current_end`

## 9. Interview Tips
**Recognition:**
- Keywords: "interval", "merge", "overlap", "conflict", "schedule", "meeting", "range"
- Ask: "Are intervals inclusive or exclusive?" "Is input sorted?" "Can intervals be invalid?"

**Implementation:**
- Start by handling edge cases (empty, single element)
- Always mention sorting as first step unless input is sorted
- Use clear variable names: `current`, `last`, `result`

**Communication:**
- Explain the overlap condition clearly: "Two intervals overlap if..."
- Walk through examples: show merging step-by-step
- Mention time complexity upfront: "We need to sort, so O(n log n)"

**Follow-up Questions:**
- "What if we need to find all intersections instead of merging?"
- "Can you do this without extra space?" (in-place modification)
- "What if intervals can have different weights/priorities?"

## 10. Quick Reference
**Pattern Triggers:** Problems with ranges, overlaps, scheduling, or merging segments
**Template Summary:** Sort by start → iterate → check overlap → merge or add to result
**Complexity:** O(n log n) time, O(1) to O(n) space
**Key Insight:** Sorting transforms overlap detection from O(n²) to O(n)

---

## Notes Section
**Personal Reminders:**
- Always ask about boundary conditions (inclusive vs exclusive)
- Draw timeline/number line to visualize overlaps
- Consider sweep line algorithm for complex overlap counting
- Remember: touching intervals [1,2][2,3] usually don't "overlap"

**Advanced Patterns:**
- Use heap for Meeting Rooms II (track end times)
- Sweep line for complex event processing
- Interval trees for dynamic interval queries