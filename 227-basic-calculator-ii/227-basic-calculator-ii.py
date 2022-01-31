class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        ope = "+"
        stack = []
        opeset = ("+", "-", "/", "*")
        ch = 0
        for c,i in enumerate(s):
            if i.isdigit():
                ch = ch*10 + int(i)
            if i in opeset or c == len(s) - 1:
                if ope == "+":
                    stack.append(ch)
                elif ope == "-":
                    stack.append(-ch)
                elif ope == "/":
                    num = stack.pop()
                    stack.append(int(num / ch))
                elif ope == "*":
                    num = stack.pop()
                    stack.append(num * ch)
                ch = 0
                ope = i
                print(ope)

        return sum(stack)