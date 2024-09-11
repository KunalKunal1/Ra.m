# Python Program to add two complex numbers

# Accept real and imaginary parts of the first complex number from user
real_part1 = float(input("Enter real part of the first complex number: "))
imaginary_part1 = float(input("Enter imaginary part of the first complex number: "))

# Accept real and imaginary parts of the second complex number from user
real_part2 = float(input("Enter real part of the second complex number: "))
imaginary_part2 = float(input("Enter imaginary part of the second complex number: "))

# Create complex numbers
complex_number1 = complex(real_part1, imaginary_part1)
complex_number2 = complex(real_part2, imaginary_part2)

# Add the complex numbers
result = complex_number1 + complex_number2

# Print the result
print("The sum of the two complex numbers is:", result)