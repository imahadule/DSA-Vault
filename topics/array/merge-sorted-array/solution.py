"""LeetCode 88: Merge Sorted Array.

Merge nums2 into nums1 in place. nums1 has length m + n, where the last n
slots are placeholders (0s) to be overwritten. Both nums1[:m] and nums2 are
sorted ascending.
"""


 def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m + n -1
        j = m - 1
        k = n - 1

        while  j >= 0 and k >=0 :
            if(nums2[k] > nums1[j] ):
                print(k)
                nums1[i] = nums2[k] 
                k -= 1
            else :
                nums1[i] = nums1[j] 
                j -= 1
            i -= 1
        
        while k >= 0:
            nums1[i] = nums2[k]
            k -= 1
            i -= 1


if __name__ == "__main__":
    assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert merge([1], 1, [], 0) == [1]
    assert merge([0], 0, [1], 1) == [1]
    print("all tests passed")
