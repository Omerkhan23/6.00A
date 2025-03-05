## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial_deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_house = 800000
down_payment = 0.25 * cost_house
epsilon = 100
amount_saved = initial_deposit
months = 36
low = 0
high = 1
r = (low+high)/2
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit >= (down_payment - 100):
    r = 0.0
    print(f"we already got enough deposit for downpayment")
else:
    while abs(amount_saved - down_payment) >= epsilon:
        steps += 1
        amount_saved = initial_deposit * (1+(r/12))**months
        
        if amount_saved < down_payment:
            low = r
        else:
            high = r
        r = (low+high) / 2
        if high - low < 1e-7:
            r = None
            break
if r is None:
    print(f'Impossible to save within given time between 0% and 100% of r')
print(f'the best r is {r}')    
print(f'steps = {steps}')
# some other solutions in chapter 4 jupyter notebook  