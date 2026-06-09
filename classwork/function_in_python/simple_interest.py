#to import module
import interestcalculator
#main program
principal_amount = float(input("Enter the principal amount: "))
#validate the input for principal amount
if principal_amount < 0:
    exit("Principal amount cannot be negative.")
#input rate of interest
rate_of_interest = float(input("Enter the rate of interest: "))
#validate the input for rate of interest
if rate_of_interest < 0:
    exit("Rate of interest cannot be negative.")    
#input time period
time_period = float(input("Enter the time period in years: "))
#validate the input for time period
if time_period < 0:
    exit("Time period cannot be negative.")
print("-" * 30)
#call the function to calculate simple interest
interest = interestcalculator.simple_interest(principal_amount, rate_of_interest, time_period)
print("The simple interest is:",interest)
print("-" * 30)
#call the function to calculate compound interest
compound_interest = interestcalculator.compound_interest(principal_amount, rate_of_interest, time_period)
print("The compound interest is:",compound_interest)
