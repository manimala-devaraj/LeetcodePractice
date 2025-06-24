class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  
        for i in nums:
            new= []
            for subset in result:
                new.append(subset + [i])
            result.extend(new)

        return result

        # n = len(nums)
        # res = []
        # for i in range(2**n): 
        #     subset = []
        #     for j in range(n):
        #         if (i >> j) & 1:
        #             subset.append(nums[j])
        #     res.append(subset)
        # return res

        # res = []
        # def backtrack(start, path):
        #     res.append(path[:])  
        #     for i in range(start, len(nums)):
        #         path.append(nums[i])           
        #         backtrack(i + 1, path)         
        #         path.pop()                     
        # backtrack(0, [])
        # return res
