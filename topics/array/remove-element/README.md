# Remove Element (LeetCode #27)

## Problem Statement
Given integer array `nums` and integer `val`, remove all occurrences of `val` in-place. Order may change. Return k = count of elements not equal to `val`; first k slots of `nums` must hold those elements.

## Constraints
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

## Intuition
Only elements != val matter, and order doesn't matter. So walk the array once, and every time you see a keeper, drop it into the next free slot at the front. No shifting, no extra space.

## Approach
1. `k = 0` — write pointer / count of kept elements.
2. Scan `i` from 0 to len(nums)-1.
3. If `nums[i] != val`: write `nums[i]` to `nums[k]`, increment k.
4. Return k.

## Complexity
- Time: O(n)
- Space: O(1)

## Code
See [`solution.py`](./solution.py).

```python
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
```

## Test Cases
| Input | Expected Output | Notes |
|-------|------------------|-------|
| nums=[3,2,2,3], val=3 | k=2, nums[:2] is some order of [2,2] | basic |
| nums=[0,1,2,2,3,0,4,2], val=2 | k=5, nums[:5] is some order of [0,0,1,3,4] | multiple occurrences |
| nums=[], val=5 | k=0 | empty array |
