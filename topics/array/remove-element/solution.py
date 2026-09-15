"""LeetCode 27: Remove Element.

Remove all occurrences of val from nums in-place. Order may change.
Return k, the count of elements not equal to val; first k slots of nums
must hold those elements (rest of the array is irrelevant).
"""


def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    k = remove_element(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = remove_element(nums, 2)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

    nums = []
    k = remove_element(nums, 5)
    assert k == 0

    print("all tests passed")
