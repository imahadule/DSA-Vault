# LeetCode 27: Remove Element

## Problem
Remove all occurrences of `val` from `nums` in-place. Order can change. Return k = count of elements != val. First k slots of `nums` must hold those elements; rest of array irrelevant.

## Approach: two pointers, overwrite in place
Since order doesn't matter, no need to shift remaining elements — just overwrite.

Pointers:
- `i` read pointer, scans every index 0..len(nums)-1
- `k` write pointer, starts at 0, counts kept elements

Loop over `i`:
- if `nums[i] != val`: write `nums[k] = nums[i]`, increment k
- else: skip (val gets overwritten later)

Return k.

## Complexity
Time O(n), space O(1).

## Trace example
`nums=[0,1,2,2,3,0,4,2], val=2`

| i | nums[i] | keep? | k before | action | k after |
|---|---|---|---|---|---|
| 0 | 0 | yes | 0 | nums[0]=0 | 1 |
| 1 | 1 | yes | 1 | nums[1]=1 | 2 |
| 2 | 2 | no | 2 | skip | 2 |
| 3 | 2 | no | 2 | skip | 2 |
| 4 | 3 | yes | 2 | nums[2]=3 | 3 |
| 5 | 0 | yes | 3 | nums[3]=0 | 4 |
| 6 | 4 | yes | 4 | nums[4]=4 | 5 |
| 7 | 2 | no | 5 | skip | 5 |

Final k=5, nums[:5] = [0,1,3,0,4] — all != 2, order preserved (not required, but this approach happens to preserve it since read never overtakes write when no removal ahead).

## Edge cases
- Empty array: loop never runs, k=0.
- No matches: every element written back to itself, k=len(nums).
- All matches: k=0, nothing written.
