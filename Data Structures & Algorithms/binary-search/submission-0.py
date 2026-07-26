class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            m = (left + right) // 2
            item = nums[m]
            if item > target:
                right = m - 1
            elif item < target:
                left = m + 1
            else:
                return m    
        return -1