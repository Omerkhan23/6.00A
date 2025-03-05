## 6.100A PSet 1: Part A
## Name:Omer Khan
## Time Spent:
## Collaborators:None

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter portion of salary to be saved(i:e 0.1 for 10%): "))
cost_of_dream_home = float(input("Enter the amount of your dream house: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
down_payment = portion_down_payment * cost_of_dream_home
monthly_salary = yearly_salary/12
annual_r = 0.05
monthly_r = annual_r/12
months = 1 # As the savings start when we get the salary of the first month
amuount_saved = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amuount_saved < down_payment:
    amuount_saved += (portion_saved * monthly_salary)
    amuount_saved += (amuount_saved * monthly_r)
    months += 1
print(f"Number of months : {months}")
