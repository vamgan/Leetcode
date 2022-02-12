class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x: x[0])
        groups = UnionFind(n)
        for time, person1, person2 in logs:
            if groups.union(person1,person2):
                n -= 1
            if n == 1:
                return time
        return -1
    
class UnionFind:

    def __init__(self, size):
        self.group = [group_id for group_id in range(size)]
        self.rank = [0] * size

    def find(self, person):
        if self.group[person] != person:
            self.group[person] = self.find(self.group[person])
        return self.group[person]

    def union(self, a, b):
        """
            return: true if a and b are not connected before
                otherwise, connect a with b and then return false
        """
        group_a = self.find(a)
        group_b = self.find(b)
        is_merged = False
        if group_a == group_b:
            return is_merged

        is_merged = True
        # Merge the lower-rank group into the higher-rank group.
        if self.rank[group_a] > self.rank[group_b]:
            self.group[group_b] = group_a
        elif self.rank[group_a] < self.rank[group_b]:
            self.group[group_a] = group_b
        else:
            self.group[group_a] = group_b
            self.rank[group_b] += 1

        return is_merged