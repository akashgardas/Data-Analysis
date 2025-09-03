principle_amt = float(input("Principle Amount: "))
interest_rate = float(input("Interest Rate: "))
time = int(input("Time (in months): "))

print(f'Interest: {principle_amt*interest_rate*time / 100}')
