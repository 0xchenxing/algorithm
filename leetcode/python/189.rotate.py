# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         l = len(nums)
#         k = k % l
#         nums1 = nums[:l - k]
#         for i in range(l):
#             if i < k:
#                 nums[i] = nums[i + l - k]
#             else:
#                 nums[i] = nums1[i - k]


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        l = len(nums)
        k = k % l
        left = 0
        right = l - k
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

