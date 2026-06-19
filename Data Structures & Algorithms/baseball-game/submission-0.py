class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        
        for op in operations:
            if op == '+':
                # Add the sum of the last two scores
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Double the last score
                stack.append(stack[-1] * 2)
            elif op == 'C':
                # Remove the last score
                stack.pop()
            else:
                # It's an integer, convert and add to stack
                stack.append(int(op))
                
        return sum(stack)