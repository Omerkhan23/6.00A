## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter portion of salary to be saved(i:e 0.1 for 10%): "))
cost_0f_dream_home = float(input("Enter the amount of your dream house: "))
semi_annual_raise = float (input("Enter the sami annual raise in decimal(i:e 0.1 for 10%): "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
down_payment = portion_down_payment * cost_0f_dream_home
monthly_salary = yearly_salary/12
annual_r = 0.05
monthly_r = annual_r/12
months = 1 # As the savings start when we get the salary of the first month
amuount_saved = 0
semi_annual_raise_amount = 0


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################


    
while amuount_saved < down_payment:
    if months % 6 == 0:
        semi_annual_raise_amount = yearly_salary * semi_annual_raise
        yearly_salary += semi_annual_raise_amount
        monthly_salary = yearly_salary/12       
    amuount_saved += (portion_saved * monthly_salary)
    amuount_saved += (amuount_saved * monthly_r)
    months += 1
print(f"Number of months : {months}")