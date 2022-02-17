class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] *  n
        stack = []
        prev_time = 0
        for i in logs:
            _id,_indicator,_time = i.split(':')
            _id,_time = int(_id), int(_time)
            print(_id,_time)
            if _indicator == 'start':
                if stack:
                    res[stack[-1]] += _time - prev_time
                stack.append(_id)
                prev_time = _time
            else:
                res[stack.pop()] += _time - prev_time + 1
                prev_time = _time + 1
        return res
                
            