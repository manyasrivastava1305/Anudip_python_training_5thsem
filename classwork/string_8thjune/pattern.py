#to ask to the user to input rows and then diplay i.e. n=5
# *
# **  
# ***
# ****
# *****
n = int(input("Enter the number of rows: "))
if (n<0):
    print("Please enter a positive integer.")
else:
    for i in range(1, n+1):
        print("*" * i)
