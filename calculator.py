# Give code for calculator pro  including features as basic operations +,-,*,/ and Advanced features like history tracking, continuos calculation, scintific functions and error handeling
class CalculatorPro:
    def __init__(self):
        self.history = []
        self.current_result = 0

    def add_to_history(self, operation, result):
        self.history.append((operation, result))

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.current_result = result
            self.add_to_history(expression, result)
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()

    def get_current_result(self):
        return self.current_result
    
# Example usage
if __name__ == "__main__":
    calc = CalculatorPro()
    print(calc.calculate("2 + 3"))  # Output: 5
    print(calc.calculate("10 * 5"))  # Output: 50
    print(calc.get_history())  # Output: [('2 + 3', 5), ('10 * 5', 50)]
    print(calc.get_current_result())  # Output: 50
    print(calc.calculate("10 / 0"))  # Output: Error: division by zero      
    calc.clear_history()
    print(calc.get_history())  # Output: [] 