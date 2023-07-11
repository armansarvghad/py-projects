import operator

class Interpreter:
    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def evaluate(self, expression):
        tokens = expression.split()
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(float(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise SyntaxError("Invalid expression")
                b = stack.pop()
                a = stack.pop()
                operator_fn = self.operators[token]
                result = operator_fn(a, b)
                stack.append(result)
            else:
                raise SyntaxError("Invalid token")

        if len(stack) != 1:
            raise SyntaxError("Invalid expression")

        return stack[0]

# Create an interpreter instance
interpreter = Interpreter()

# Evaluate arithmetic expressions
result = interpreter.evaluate("5 + 2 * 3")
print(result)  # Output: 11

result = interpreter.evaluate("(4 + 6) / 2")
print(result)  # Output: 5.0