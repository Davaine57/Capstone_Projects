import math
# Introduction to user options
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print()
# User select's either 'investment' or 'bond'
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
# User selects 'investment' - Should not matter how they capitalize their choice


if choice.lower() == "investment":
    deposit = float(input("Please enter the amount of money you are depositing: "))
    rate = 0
    # User input's interest rate - If number is less than 0 an error is shown
    while rate <= 0:
        rate = float(input("Please enter the interest rate (as a percentage)? "))
        if rate <= 0:
            print("Invalid interest rate. Please enter a positive number.")
    rate /= 100
    years = 0
    # User input's term of investment - If number is less than 0 error is also shown
    while years <= 0:
        years = int(input("How many years will you invest? "))
        if years <= 0:
            print("Invalid number of years. Please enter a positive number.")
    interest_type = input("Would you like compound or simple interest? Enter 'simple' or 'compound'. ")
    # User selects the type of interest they would like - Should not matter how they capitalize
    # If incorrect word is detected error is shown
    if interest_type.lower() == "simple":
        interest_amount = deposit * (1 + rate * years)
    elif interest_type.lower() == "compound":
        interest_amount = deposit * math.pow(1 + rate, years)
    else:
        print("Invalid input for interest type.")
        exit()
    # User is shown their return on investment following completion of their term


    print(f"The total amount you will get back after {years} years is: {interest_amount:.2f}")
# User selects 'bond' - Should not matter how they capitalize
elif choice.lower() == "bond":
    # User input's current value of the house
    current_value = float(input("Please enter the current value of the house: "))
    interest_rate = 0
    # User input's interest rate - If number is less than 0 an error is shown
    while interest_rate <= 0:
        interest_rate = float(input("Please enter the interest rate (as a percentage)? "))
       # User input's interest rate - If number is less than 0 an error message is also shown
        if interest_rate <= 0:
            print("Invalid interest rate. Please enter a positive number.")
    months = 0
    # User input's term for bond - If number is less than 0 an error is shown
    while months <= 0:
        months = int(input("How many months will you take to repay the bond? "))
        if months <= 0:
            print("Invalid number of months. Please enter a positive integer.")
    # User is shown monthly repayment costs
    monthly_interest = (interest_rate / 100) /12
    monthly_repayment = (monthly_interest * current_value) / (1 - math.pow(1 + monthly_interest, -months))
    print(f"The amount you will have to repay each month is: {monthly_repayment:.2f}")
    
# Otherwise an error message is as the user did not input 'investment' or 'bond'
else:
    print("Invalid input detected.")
    