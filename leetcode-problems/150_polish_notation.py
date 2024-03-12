class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for current in tokens:

            if current.isdigit() or len(current) > 1:
                stack.append(int(current))
                continue
            
            if current == "+":
                result = stack.pop(-1) + stack.pop(-1)
            elif current == "*":
                result = stack.pop(-1) * stack.pop(-1)
            elif current == "-":
                a = stack.pop(-1)
                b = stack.pop(-1)
                result = b - a
            elif current == "/":
                a = stack.pop(-1)
                b = stack.pop(-1)
                if b / a < 0:
                    result = -(b // -a)
                else:
                    result = b // a
            stack.append(result)
         
        return stack[0]