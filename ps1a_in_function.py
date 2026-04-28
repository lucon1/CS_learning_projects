def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	    
	print(f"Number of months: {months}")
	return months