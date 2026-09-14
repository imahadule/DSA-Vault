# LeetCode 88: Merge Sorted Array

## Problem
`nums1` length m+n, first m slots real data (sorted), last n slots zero placeholders. `nums2` length n, sorted. Merge `nums2` into `nums1` in place, result sorted.

## Approach: three pointers, fill from back
Forward merge needs shifting (O(n) per insert). Fill from end instead — no shifting.

Pointers:
- `i = m - 1` last real elem of nums1
- `j = n - 1` last elem of nums2
- `k = m + n - 1` last slot of nums1 (write position)

Loop while `j >= 0` (nums2 not exhausted):
- if `i >= 0` and `nums1[i] > nums2[j]`: place `nums1[i]` at `k`, decrement i
- else: place `nums2[j]` at `k`, decrement j
- decrement k each iteration

Loop stops once `j < 0` — remaining nums1[i+1] already in correct place, no copy needed.

## Complexity
Time O(m+n), space O(1).

## Trace example
`nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3`

| step | i,j,k before | compare | action | nums1 after |
|---|---|---|---|---|
| 1 | 2,2,5 | nums1[2]=3 vs nums2[2]=6 | 3<6, take nums2[2]=6, j=1,k=4 | [1,2,3,0,0,6] |
| 2 | 2,1,4 | nums1[2]=3 vs nums2[1]=5 | 3<5, take nums2[1]=5, j=0,k=3 | [1,2,3,0,5,6] |
| 3 | 2,0,3 | nums1[2]=3 vs nums2[0]=2 | 3>2, take nums1[2]=3, i=1,k=2 | [1,2,3,3,5,6] |
| 4 | 1,0,2 | nums1[1]=2 vs nums2[0]=2 | not >, take nums2[0]=2, j=-1,k=1 | [1,2,2,3,5,6] |

j<0, loop ends. Remaining nums1[:i+1]=[1,2] already in place. Final: `[1,2,2,3,5,6]`.

Edge cases handled: `nums2` empty (`n=0`) → loop never runs, nums1 unchanged. `nums1` initial real part empty (`m=0`) → i starts -1, always takes from nums2.
