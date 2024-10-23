class Calculator():
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "cannot be divided by 0"
        return a/b
def calculate():
    my_calculator=Calculator()
    while True:
        operation=input("Enter the opeartion (+,-,*,/) or 'q' to quit").strip()

        if operation.lower()=="q":
            print("Exiting calculator!")
            break

        if operation not in ["+","-","*","/"]:
            print("Invalid operation! Please enter one of +,-,*,/")
            continue

        a= float(input("Enter the first number"))
        b= float(input("Enter the second number"))
        if operation=="+":
            print(my_calculator.sum(a,b))
            continue
        if operation=="-":
            print(my_calculator.sub(a,b))
            continue
        if operation=="*":
            print(my_calculator.mul(a,b))
            continue
        if operation=="/":
            print(my_calculator.div(a,b))
            continue
        
        
    
    
            
