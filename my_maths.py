


def calculate(num1, num2, operation):
    def add():
        return num1 + num2
    def subtract():
        return num1-num2
    def divide():
        return num1/num2
    def multiply():
        return num1*num2
    
    if operation.lower() == "add":
        return add()
    elif operation.lower() == "subtract":
        print (subtract())
    elif operation.lower() == "multiply":
        print (multiply())
    elif operation.lower() == "divide":
        print (divide())
            
            
print (calculate(23,3,"add"))

