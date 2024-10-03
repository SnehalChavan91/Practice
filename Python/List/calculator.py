class Calculator():
    def add(self,a,b):
        return a+b
    
    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b==0:
            return "Can not be divide"
        return a/b

def calculate():
    my_calculator=Calculator()
    
    while True:
        operation = input("Enter the operation (+, -, *, /) or 'q' to quit: ").strip()
        if operation.lower() == 'q':
            print("Exiting calculator!")
            break


        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation! Please enter one of +, -, *, or /.")
            continue


        a=float(input("Enter the first number").strip())
        b=float(input("Enter the second number").strip())

        if operation == "+":
            print(f"Result: {my_calculator.add(a, b)}")
        elif operation == "-":
            print(f"Result: {my_calculator.subtract(a, b)}")
        elif operation == "*":
            print(f"Result: {my_calculator.multiply(a, b)}")
        elif operation == "/":
            print(f"Result: {my_calculator.divide(a, b)}")
if __name__ == "__main__":
    calculate()
