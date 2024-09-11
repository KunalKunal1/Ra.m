# Python Program to calculate area and perimeter of a rectangle

# Accept length and breadth of the rectangle from user
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

# Calculate area of the rectangle
area = length * breadth

# Calculate perimeter of the rectangle
perimeter = 2 * (length + breadth)

# Print the results
print("Area of the rectangle: ", area)
print("Perimeter of the rectangle: ", perimeter)