class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        mh = heights[-1]
        for i in range(len(heights) -2,-1,-1):
            if heights[i] > mh:
                mh = heights[i]
                res.append(i)
        return res[::-1]