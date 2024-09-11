
# Python Program to calculate simple and compound interest

# Accept principal amount, rate, and time from user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (in %): "))
time = float(input("Enter time (in years): "))

# Calculate simple interest
simple_interest = (principal * time * rate) / 100

# Calculate compound interest
compound_interest = principal * ((1 + rate/100) ** time - 1)

# Print the results
print("Simple Interest: ", simple_interest)
print("Compound Interest: ", compound_interest)