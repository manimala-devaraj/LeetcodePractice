class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s=max(candies)
        p=[]
        for i in candies:
            if i+extraCandies>=s:
                p.append(True)
            else:
                p.append(False)
        return p

            