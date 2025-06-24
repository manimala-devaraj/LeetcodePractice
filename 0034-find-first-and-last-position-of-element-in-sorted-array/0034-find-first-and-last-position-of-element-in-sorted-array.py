class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
            




# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         l=len(nums)
#         medi=l//2
#         ra=nums[:medi]
#         for i in ra:
#             if i==target:
#                 return (nums.index[i,i])
#             else:
#                 return [-1,-1]

#         s=nums[medi:]
#         for j in s:
#             if j==target:
#                 return (num.index[i,i])
#             else:
#                 return [-1,-1]

            