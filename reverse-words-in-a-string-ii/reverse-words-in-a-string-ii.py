class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s) - 1 - i] =  s[len(s) - 1 - i], s[i]
        start = 0
        end = 0
        i = 0
        print(s)
        while i < len(s):
            if s[i] == " ":
                print(i, start, end)
                end -= 1
                while start <= end:
                    s[end], s[start] = s[start], s[end]
                    end -= 1
                    start += 1
                start = i + 1
                end = i
            i += 1
            end += 1
        print(start, end)
        end -= 1
        while start <= end:
            s[end], s[start] = s[start], s[end]
            end -= 1
            start += 1
        