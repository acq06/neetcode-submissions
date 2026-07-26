class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue

            
            left = i+1
            right = len(nums) - 1
            
            while left < right:
                summed = num + nums[left] + nums[right]

                if summed > 0:
                    right -= 1
                elif summed < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result
