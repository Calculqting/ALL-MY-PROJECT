num1 = float(input("Enter First Number: "))
op = input("Choose Operations (+, -, *, /,):")
num2 =float(input("Enter Second Number: " ))



if op == "+":
    Result = int(num1 + num2)
    
    
elif op == "-":
    Result = int(num1 - num2)
    
elif op == "*":
    Result = int(num1 * num2)      
    
elif op == "/":
    Result = int(num1 / num2)  
    if num2 != 0:
        Result = int(num1 / num2)
        
    else: 
        Result = "Error Cannot be divided by zero"
    
else:
    Result = "Invaid Operator"    
    
    
    
print("Result", Result)




