class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []
        result = 0

        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                match tokens[i]:
                    case "+":
                        result = int(stack[-2]) + int(stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(result)
                    case "-":
                        result = int(stack[-2]) - int(stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(result)

                    case "*":
                        result = int(stack[-2]) * int(stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(result)
                    case "/":
                        result = int(stack[-2]) / int(stack[-1])
                        stack.pop()
                        stack.pop()
                        stack.append(result)

        return int(stack[-1])

                