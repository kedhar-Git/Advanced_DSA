'''
#1480. Running Sum of 1d Array 
from typing import List
def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
nums = [1,2,3,4]
print(runningSum(nums))

#traditional way
nums = [1,2,3,4]
res=[0]*len(nums)
for i in range(len(nums)):      
    curr_sum = 0
    for j in range(i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)
'''

'''
#1732. Find the Highest Altitude
from typing import List
def largestAltitude(gain: List[int]) -> int:
    max_altitude = 0
    current_altitude = []
    for i in range(len(gain)):
        if i == 0:
            current_altitude.append(gain[i])
        else:
            current_altitude.append(current_altitude[i-1] + gain[i])
        max_altitude = max(max_altitude, current_altitude[i])
    return max_altitude
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

             #or
from typing import List
def largestAltitude(gain: List[int]) -> int:
    max_altitude = 0
    current_altitude = 0
    for i in range(len(gain)):
        current_altitude += gain[i]
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))
'''

'''
#1991. Find the Middle Index in Array
from typing import List
def findMiddleIndex(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
nums = [2,3,-1,8,4]
print(findMiddleIndex(nums))
''' 

#724. Find Pivot Index
from typing import List
def pivotIndex(nums: List[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))