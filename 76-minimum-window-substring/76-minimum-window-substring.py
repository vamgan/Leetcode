class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        mapp = collections.Counter(t)
        count = len(mapp)
        i = 0
        j = 0
        subs = ''
        while i <= j:
            if count == 0:
                if not subs or (j-i) < len(subs):
                    subs = s[i:j]
                if s[i] in mapp:
                    if mapp[s[i]] == 0:
                        count += 1
                    mapp[s[i]] += 1
                i += 1
            else:
                if j >= len(s):
                    break
                if s[j] in mapp:
                    mapp[s[j]] -= 1
                    if mapp[s[j]] == 0:
                        count -= 1
                j += 1
        return subs