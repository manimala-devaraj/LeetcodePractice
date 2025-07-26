class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def compute(num1, num2, op):
            match op:
                case '+':
                    return num1 + num2
                case '-':
                    return num1 - num2
                case '*':
                    return num1 * num2
                case '/':
                    return int(num1 / num2)
                
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(compute(num1, num2, token))
            else:
                stack.append(int(token))
        return int(stack.pop())