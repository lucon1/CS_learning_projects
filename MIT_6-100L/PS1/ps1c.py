## 6.100A PSet 1: Part C
## Name: Lucas Harlien
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Please enter the initial amount deposited: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_home = 800000
portion_down_payment = 0.25 # percentage of total cost needed
down_payment_needed = portion_down_payment * cost_of_dream_home # down payment needed to purchase home
epsilon = 100 # acceptable distance to down payment
months = 36 # months to save
amount_saved = initial_deposit
r = 0 # rate of return
steps = 0 # number of steps to find answer
high = 1
low = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

# check if down payment is feasable at any rate
if initial_deposit*(1+(1/12))**months < down_payment_needed:
    print("You will not be able to save enough with this initial investment")
    r = None
# check for lowest rate
else:
    r = (high+low)/2 # initialize guess
    while abs(down_payment_needed-amount_saved) >= epsilon: 
        # check amount saved with current rate
        amount_saved = initial_deposit*(1+(r/12))**months
        
        # check if too low or high
        if amount_saved < down_payment_needed :
            low = r
        else:
            high = r
        r = (high+low)/2
        steps += 1

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")