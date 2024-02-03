#Logical Operators 



has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for Loan")
elif has_high_income or has_good_credit:
    print("Eligible for Interview")


#AND : Both conditions should be true
#OR : One should be true to execute the conditionals 
#NOT : Inverses the condition e.g not TRUE -> False
    
#Comparison Operators

temprature = 30

if temprature > 30:
    print("Hot Day")
elif temprature == 30:
    print("Pleasent Day")

# > , >= , < , <= , ==