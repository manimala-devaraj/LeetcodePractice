class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = highest = 0

        for num in gain:
            total += num
            highest = max(total,highest)
        
        return highest