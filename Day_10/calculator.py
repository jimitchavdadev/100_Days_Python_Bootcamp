def add(num1, num2):
    return float(num1+num2)
def sub(num1, num2):
    return float(num1-num2)
def mult(num1, num2):
    return float(num1*num2)
def div(num1, num2):
    return float(num1/num2)

ops=["+","-","*","/"]

op=input("pick an operation: + - * / : ")
op1=int(input("enter operand 1: "))
op2=int(input("enter operand 2: "))

while(True):
    if op not in ops:
        print("invalid operand selected, enter again")
        continue
    if op=="+":
        ans=add(op1, op2)
        print(f"the answer is {ans}")
    elif op=="-":
        ans=sub(op1, op2)
        print(f"the answer is {ans}")
    elif op=="*":
        ans=mult(op1, op2)
        print(f"the answer is {ans}")
    elif op=="/":
        ans=div(op1, op2)
        print(f"the answer is {ans}")
    choice=input(f"y to continue with {ans} as first operand, n for new operation, q to quit: ")
    if choice=="y":
        op1=ans
        op=input("pick an operation: + - * / : ")
        op2=int(input("enter operand 2: "))
    elif choice=="n":
        op=input("pick an operation: + - * / : ")
        op1=int(input("enter operand 1: "))
        op2=int(input("enter operand 2: "))
    else:
        break