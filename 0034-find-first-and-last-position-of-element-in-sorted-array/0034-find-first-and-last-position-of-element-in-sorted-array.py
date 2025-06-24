class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums) - 1 
        sol = []
        while (left < right):
            mid = int((right - left )/2 + left) 
            if target <= nums[mid]:    
                right = mid
            else:
                left = mid+1
        sol.append(right)

        left = 0 
        right = len(nums) - 1 
                
        while (left < right):
            mid = int((right - left +1)/2 + left)
            if target >= nums[mid]:
                left = mid 
            else:
                right = mid - 1
        sol.append(left)
       

        if left>=0 and left < len(nums):
            if nums[left] == target:
                return sol
        return [-1,-1]


        