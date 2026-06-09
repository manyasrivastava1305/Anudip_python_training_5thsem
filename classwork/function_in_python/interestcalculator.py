#function to calculate simple interest
def simple_interest(principal, rate, time):
    #calculate simple interest
    interest = (principal * rate * time) / 100
   #return the calculated interest
    return interest
#-------------------------------------
#function to calculate compound interest
def compound_interest(principal, rate, time):
    #calculate compound interest
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    #return the calculated interest
    return interest
