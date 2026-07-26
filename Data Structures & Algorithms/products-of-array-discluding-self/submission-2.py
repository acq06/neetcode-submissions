class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        left_products = {}
        right_products = {}
        
        last_prod = 1

        for i in range(len(nums)):
            if i == 0:
                prod = last_prod 
            else:
                prod = last_prod * nums[i-1]
            left_products[i] = prod
            last_prod = prod

        last_prod = 1
        
        for i in range(len(nums), 0, -1):
            if i == len(nums):
                prod = last_prod
            else:
                prod = last_prod * nums[i]
            right_products[i-1] = prod
            last_prod = prod

        for i in range(len(nums)):
            products.append(left_products[i] * right_products[i])

        return products