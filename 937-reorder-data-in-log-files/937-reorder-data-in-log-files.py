class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLog = []
        letterLog = []
        for log in logs:
            if log.split()[1].isdigit():
                digitLog.append(log)
                
            else:
                letterLog.append(log)
        letterLog = sorted(letterLog, key= lambda x: (x.split()[1:], x.split()[0] ))
        letterLog.extend(digitLog)
        return letterLog