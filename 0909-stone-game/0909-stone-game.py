class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Alice = []
        Bob = []

        while len(piles) > 0:
            if piles[0] >= piles[-1]:
                Alice.append(piles[0])
                piles.remove(piles[0])
                Bob.append(piles[-1])
                piles.remove(piles[-1])
            else:
                Alice.append(piles[-1])
                piles.remove(piles[-1])
                Bob.append(piles[0])
                piles.remove(piles[0])

        return sum(Alice) > sum(Bob)