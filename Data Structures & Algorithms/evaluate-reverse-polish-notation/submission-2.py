class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b, 
            "*": lambda a, b: a * b, 
            "/": lambda a, b: int(a / b)
        }

        nums = []

        for token in tokens:
            if token in operators:
                right = nums.pop()
                left  = nums.pop()
                nums.append(operators[token](left, right))
            else:
                nums.append(int(token))

        return nums[-1]