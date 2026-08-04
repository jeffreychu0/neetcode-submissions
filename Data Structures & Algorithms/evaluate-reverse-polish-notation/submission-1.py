class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                A = int(stack.pop())
                B = int(stack.pop())

                stack.append(A + B)
            elif token == "*":
                A = int(stack.pop())
                B = int(stack.pop())

                stack.append(A * B)
            elif token == "-":
                A = int(stack.pop())
                B = int(stack.pop())

                stack.append(B - A)
            elif token == "/":
                A = int(stack.pop())
                B = int(stack.pop())

                stack.append(B / A)
            else:
                stack.append(token)

        return int(stack.pop())

