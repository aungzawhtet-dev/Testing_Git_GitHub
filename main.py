def calculate_total(amount, tax):
    tax_amount = amount * tax
    total = amount + tax_amount

    return total


amount = 10000
tax = 0.07

result = calculate_total(amount, tax)

print(result)
print("Hello Data Engineering")
