from typing import List


# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         left = 0
#         right = 1
#         sum = nums[0]
#         ans = len(nums)
#         if sum >= target:
#             return 1
#         while right < len(nums):
#             sum += nums[right]
#             while sum >= target:
#                 ans = min(ans, right - left + 1)
#                 sum -= nums[left]
#                 if sum < target:
#                     sum += nums[left]
#                     break
#                 left += 1
#             right += 1
#         if left == 0 and sum < target:
#             return 0
#         return ans


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        preSum = [0]
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            preSum.append(sum)
        if sum < target:
            return 0
        ans = len(nums)
        for i in range(len(preSum)):
            left = i+1
            right = len(preSum)-1
            while left <= right:
                mid = (left+right)//2
                if preSum[mid]-preSum[i] < target:
                    left = mid+1
                else:
                    right = mid-1
                    ans = min(ans, mid - i)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
