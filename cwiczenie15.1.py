class Calculator:

    @staticmethod
    def sum(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            print(a + b)
        else:
            print("Sum is not defined")

    @staticmethod
    def sub(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            print(a - b)
        else:
            print("Subtraction is not defined")

    @staticmethod
    def mul(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            print(a * b)
        else:
            print("Multiplication is not defined")

    @staticmethod
    def div(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            try:
                print(a / b)
            except ZeroDivisionError:
                print("Division by 0 is not defined")
        else:
            print("Division is not defined")


Calculator.sum(1.1, 0.0)
