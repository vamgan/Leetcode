class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # if len(a) < 4:
        #     a = Solution.formatBinary(a)
        # if len(b) == 1:
        #     b = Solution.formatBinary(b)
        # print(a,b)
        num1 = int(a,2)
        num2 = int(b,2)
        print(num1,num2)
        return bin(num1 + num2).replace("0b","")
    def formatBinary(num):
        diff = 4 - len(num)
        return "0" * diff + num