class Solution:
    def maxArea(self, height: List[int]) -> int:
        le=0
        ri=len(height)-1
        hsmm=0
        while le<ri:
            h=min(height[le],height[ri])
            w=ri-le
            area=h*w
            hsmm=max(hsmm,area)
            if height[le]<height[ri]:
                le+=1
            else:
                ri-=1
        return hsmm