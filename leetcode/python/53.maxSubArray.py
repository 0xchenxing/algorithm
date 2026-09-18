from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         right = 1
#         sum = nums[0] #代表以right结尾的最优子数组的和
#         ans = nums[0]
#         while right < len(nums):
#             if sum >= 0:
#                 sum = nums[right] + sum
#             else:
#                 sum = nums[right]
#             ans = max(ans, sum)
#             right += 1
#         return ans

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        sumLeft = 0
        maxSumLeft = nums[mid-1]
        for i in range(mid-1, -1, -1):
            sumLeft += nums[i]
            maxSumLeft = max(maxSumLeft, sumLeft)
        sumRight = 0
        maxSumRight = nums[mid]
        for i in range(mid, len(nums)):
            sumRight += nums[i]
            maxSumRight = max(maxSumRight, sumRight)
        return max(self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]), maxSumLeft + maxSumRight)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
