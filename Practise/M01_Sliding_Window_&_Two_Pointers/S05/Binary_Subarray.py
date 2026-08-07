'''
#1493. Longest Subarray of 1's After Deleting One Element
def longestSubarray(nums):
    left = 0
    max_length = 0
    zero_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_length = max(max_length, right - left)
    return max_length
nums = [1,1,0,1]
print(longestSubarray(nums))
'''

'''
#1004. Max Consecutive Ones III
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
solution = Solution()
print(solution.longestOnes(nums, k))
'''
'''
#930. Binary Subarrays With Sum
from typing import List
def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    prefix_sum = 0
    sum_count = {0: 1}
    result = 0
    for num in nums:
        prefix_sum += num
        if prefix_sum - goal in sum_count:
            result += sum_count[prefix_sum - goal]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    return result

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSum(nums, goal))
'''