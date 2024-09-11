# Python Program to calculate salary of an employee

# Accept employee wages and number of days worked from user
wages_per_day = float(input("Enter employee wages/money earn per day: "))
number_of_days_worked = int(input("Enter number of days worked: "))

# Calculate Basic Pay
basic_pay = wages_per_day * number_of_days_worked

# Calculate DA, HRA, and PF
da = basic_pay * 0.53
hra = basic_pay * 0.10
pf = basic_pay * 0.12
ta = basic_pay * 0.12

# Calculate Gross Pay
gross_pay = basic_pay + da + hra

# Calculate Net Pay
net_pay = gross_pay - pf

# Print the results
print("Basic Pay: ₹", basic_pay)
print("DA: ₹", da)
print("HRA: ₹", hra)
print("PF: ₹", pf)
print("Gross Pay: ₹", gross_pay)
print("Net Pay: ₹", net_pay)