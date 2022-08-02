class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        print(points)
        balloon_shot = [points[0][1]]
        for i,x in enumerate(points[1:]):
            if x[0] <= balloon_shot[-1] and x[1] >= balloon_shot[-1]:
                continue
            else:
                balloon_shot.append(x[1])
        return len(balloon_shot)