class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                prod *= nums[j]
            products.append(prod)
        return products