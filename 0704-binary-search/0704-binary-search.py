class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            i = (left + right) // 2

            if nums[i] == target:
                return i
            elif nums[i] < target:
                left = i + 1
            else:
                right = i - 1

        return -1