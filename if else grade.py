# Get the percentage from the user
percent = float(input("Enter Percentage: "))

# Determine the grade based on the percentage
if percent >= 90.0:
    print('Congratulations, you got an A')
elif percent >= 80.0:
    print('You got a B')
elif percent >= 70.0:
    print('You got a C')
else:
    print('Your grade is less than a C')