
'''
Defination:-The Interpreter Pattern is a behavioral design pattern that defines a grammar for a language 
and provides an interpreter to interpret sentences in that language.
It is useful when dealing with language parsing, mathematical expressions, or DSLs (Domain-Specific Languages).

'''

class Interpreter:
    def interpret(self, expression):
        tokens = expression.split()  # Split the expression into parts
        left = int(tokens[0])        # First number
        operator = tokens[1]         # Operator (+ or -)
        right = int(tokens[2])       # Second number
        
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        else:
            return "Unknown operation"

# Client code
interpreter = Interpreter()
expression = "10 + 5"
result = interpreter.interpret(expression)
print(f"Result of '{expression}' is: {result}")
