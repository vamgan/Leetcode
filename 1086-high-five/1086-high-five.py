class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = defaultdict(list)
        print(scores)
        for id_, score in items:
            scores[id_].append(score)
        d = sorted(scores.items())
        res = []
        for key, value in d:
            value.sort(reverse = True)
            res.append([key, sum(value[:5]) // 5])
        return res
        