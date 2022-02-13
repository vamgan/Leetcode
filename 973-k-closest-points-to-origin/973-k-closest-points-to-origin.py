class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            distances.append(self.eucledianDistance(i[0],i[1]))
        distances,points = zip(*sorted(zip(distances,points)))
        return points[:k]
    def eucledianDistance(self,x,y):
        return math.sqrt(x**2 + y**2)
    