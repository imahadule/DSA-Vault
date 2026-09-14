"""LeetCode 88: Merge Sorted Array.

Merge nums2 into nums1 in place. nums1 has length m + n, where the last n
slots are placeholders (0s) to be overwritten. Both nums1[:m] and nums2 are
sorted ascending.
"""


def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1


if __name__ == "__main__":
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert merge([1], 1, [], 0) == [1]
    assert merge([0], 0, [1], 1) == [1]
    print("all tests passed")
