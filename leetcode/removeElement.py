# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place. The order of the
# elements may be changed. Then return the number of elements
# in nums which are not equal to val.
# Consider the number of elements in nums which are not equal
# to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of
# nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well
# as the size of nums.
# Return k.
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = 0
        start = 0
        finish = len(nums)-1
        while start <= finish:
            if nums[start] == val:
                while nums[start] is val:
                    nums[start] = "_"
                    nums[start], nums[finish] = nums[finish], nums[start]
                    finish -= 1
                ans += 1
            else:
                ans += 1
            start += 1
        j = len(nums) - 1
        while j>= 0 and nums[j] == "_":
            del nums[j]
            j = len(nums) -1
        ans = len(nums)
        print(nums)
        return ans

    def removeElement_Best(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = len(nums) - 1
        i = 0
        while i <= index:
            if nums[i] == val:
                nums[i] = nums[index]
                index -= 1
            else:
                i += 1
        print(nums)
        return index + 1


def main():
    p = Solution()
    print("Q1 ", p.removeElement([3,2,2,3], 3))
    print("Q2 ", p.removeElement([0,1,2,2,3,0,4,2], 2))
    print("Q3 ", p.removeElement([1], 1))
    print("Q4 ", p.removeElement_Best([3,3], 3))
    print("Q5 ", p.removeElement_Best([4, 5], 5))

main()
