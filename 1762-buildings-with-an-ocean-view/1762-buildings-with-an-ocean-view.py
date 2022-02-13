class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        maxHeight = heights[-1]
        for i in reversed(range(len(heights) - 1)):
            if heights[i] > heights[i+1] and heights[i] > maxHeight:
                print(heights[i])
                print(i)
                res.append(i)
                maxHeight = heights[i]
        res.reverse()
        return res