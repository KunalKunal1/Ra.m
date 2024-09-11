# Get two integers from the user
dividend = int(input('Please enter the number to be divided (dividend): '))
divisor = int(input('Please enter the number to divide by (divisor): '))

# If possible, divide them and report the result
if divisor != 0:
    quotient = dividend / divisor
    #print(f"{dividend} / {divisor} = {quotient}")
    print(quotient)
else:
    print("Error: Division by zero is not allowed.")