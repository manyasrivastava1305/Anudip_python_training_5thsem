#function to calculate addition of two numbers
def add(num1, num2):
    #calculate the sum
    result = num1 + num2
    #return the calculated sum
    return result
#--------------------------------------------------
#function to calculate subtraction of two numbers
def subtract(num1, num2):
    #calculate the difference
    result = num1 - num2
    #return the calculated difference
    return result
#--------------------------------------------------
#function to calculate multiplication of two numbers    
def multiply(num1, num2):
    #calculate the product
    result = num1 * num2
    #return the calculated product
    return result
#--------------------------------------------------
#function to calculate division of two numbers
def divide(num1, num2):
    #validate the divisor
    if num2 == 0:
        exit("Divisor cannot be zero.")
    #calculate the quotient
    result = num1 / num2
    #return the calculated quotient
    return result
#--------------------------------------------------
#function to calculate modulus of two numbers
def modulus(num1, num2):
    #validate the divisor
    if num2 == 0:
        exit("Divisor cannot be zero.")
    #calculate the modulus
    result = num1 % num2
    #return the calculated modulus
    return result
#--------------------------------------------------
#function to calculate floor division of two numbers
def floor_division(num1, num2):
    #validate the divisor
    if num2 == 0:
        exit("Divisor cannot be zero.")
    #calculate the floor division
    result = num1 // num2
    #return the calculated floor division
    return result
#--------------------------------------------------
#function to calculate exponentiation of two numbers
def exponentiation(num1, num2):
    #calculate the exponentiation
    result = num1 ** num2
    #return the calculated exponentiation
    return result
#----------------------------------------------
