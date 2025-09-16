def exceptionhandling(a,b):
    try:
        r = a / b
        print(f"division result: {r}")
    except:
        print("Error: Division by zero is not allowed")

num, den = map(int,input("Enter two values: ").split())
exceptionhandling(num,den)