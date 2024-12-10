# Search Insert Position
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the
# index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Example 2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
# Example3:
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, 0, len(nums)-1, target)

    def binarySearch(self, nums, left, right, element):
        middle = int((left + right)/2)
        if nums[middle] == element:
            return int(middle)
        if left >= right:
            if element < nums[middle]:
                if middle < 0:
                    middle = 0
                return int(middle)
            elif nums[middle] < element:
                return int(middle+1)
        if element < nums[middle]:
            return self.binarySearch(nums, left, middle-1, element)
        elif nums[middle] < element:
            return self.binarySearch(nums, middle+1, right, element)

def main():
    p = Solution()
    print( p.searchInsert([1,3,5,6], 5))
    print(p.searchInsert([1,3,5,6], 2))
    print(p.searchInsert([1, 3, 5, 6], 7))
    print(p.searchInsert([1, 3], 0))
    print(p.searchInsert([1, 3, 5, 6], 0))

main()
