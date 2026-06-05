class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = {"+", "-", "*", "/"}
        stack = []

        for c in tokens:
            if c not in oper:
                stack.append(int(c))
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                res = 0
                if c == "+":
                    res = first + second
                elif c == "-":
                    res = first - second
                elif c == "*":
                    res = first * second
                elif c == "/":
                    res = int(first / second)

                stack.append(res)
        print(stack)
        return stack[-1]
        
                        

