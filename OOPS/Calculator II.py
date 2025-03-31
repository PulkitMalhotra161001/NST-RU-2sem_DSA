class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return -1
        return self.num1 / self.num2

num1, num2 = map(int, input().split())
calc = Calculator(num1, num2)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(int(calc.divide()))
