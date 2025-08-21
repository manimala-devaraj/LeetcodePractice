class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fi = sec = float('inf') 
        for n in nums: 
            if n <= fi: 
                fi = n
            elif n <= sec:
                sec = n
            else:
                return True
        return False