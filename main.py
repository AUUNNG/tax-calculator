def Tax(income):
    if income <= 150000:
        return  0
    elif income <= 300000:
        return (income-150000)*.05
    elif income <= 500000:
        return (income-(150000+150000))*.1 + 7500
    elif income <= 750000:
    elif income <= 1000000:
    elif income <= 2000000:
    elif income <= 5000000:
    elif income > 5000000:

print(f"tax = {Tax(5000000)}")
