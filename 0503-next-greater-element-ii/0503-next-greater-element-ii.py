class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        res=[-1]*n
        for i in range(n):
            for j in range(1,n):
                if nums[(i+j)%n]>nums[i]:
                    res[i]=nums[(i+j)%n]
                    break
        return res
        # for i in range(2 * n):
        #     new= nums[i % n]
        #     while st and nums[st[-1]] < new:
        #         res[st.pop()] =new
        #     if i < n:
        #         st.append(i)
        # return res
