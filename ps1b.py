## 6.100A PSet 1: Part B
## Name: Lucas Harlien
## Time Spent:
## Collaborators:

print("Welcome to the dream home savings estimator")       

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary = float(input("Please enter your yearly salary: "))
portion_saved = float(input("How much do you want to save a month? (please enter in decimal form as a percentage of monthly salary): "))
cost_of_dream_home = float(input("Please enter the cost of your dream home: "))
semi_annual_raise = float(input("How much do you expect to get as a semi annual raise? (please enter in decimal form as a percentage of monthly salary): "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25 # percentage of total cost needed\
down_payment_needed = portion_down_payment * cost_of_dream_home # down payment needed to purchase home
amount_saved = 0 # amount saved so far
r = 0.05 # rate of return on savings
months = 0 # months till saved

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < down_payment_needed:
    amount_saved += (portion_saved*(yearly_salary/12)) + (amount_saved*(r/12))
    months += 1
    if months%6 == 0:
        yearly_salary += yearly_salary*semi_annual_raise
    
print(f"Number of months: {months}")