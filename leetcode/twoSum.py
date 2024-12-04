# Two Sum
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we
# return [0, 1].
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example 3:
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
# Follow - up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum_bruteforce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [0, 1]
        for idx, num in enumerate(nums):
            for idxi, rem in enumerate(nums[idx+1:]):
                if target == (num + rem):
                    res = [idx, idx + idxi +1]
                    return res

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            if (target-num) in nums[idx+1:]:
                return [idx, nums[idx+1:].index(target-num)+idx+1]

    def twoSum_best(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [i, d[target - n]]
            d[n] = i

def main():
    p = Solution()
    print(p.twoSum([2, 7, 11, 15], 9))
    print(p.twoSum([3, 2, 4], 6))
    print(p.twoSum([3, 3], 6 ))

main()
