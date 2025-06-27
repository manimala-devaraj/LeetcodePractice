class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        res=[-1]*n
        for i in range(2 * n):
            new= nums[i % n]
            while st and nums[st[-1]] < new:
                res[st.pop()] =new
            if i < n:
                st.append(i)
        return res
