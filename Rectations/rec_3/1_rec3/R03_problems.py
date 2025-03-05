# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0 
high = x
ans = (low + high)/2.0
while abs(ans**4 - x) >= epsilon:
    if ans**4 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print(f"{ans} is the fourth root of {x}")            




# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 
def num_in(start,end,k):
    for i in range(start,end+1):
        if i == k:
            return True
print(num_in(1,10,4))        


    






# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
def is_perfect(n):

    num = 0
    for j in range(1,n):
        if n%j == 0:
            num += j
    return n == num
            
print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(496))






# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
y = int(input("Enter a number "))
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0
if y < 0:
    print("Enter a positive number")
else:    
    while abs(ans**4 - y) >= epsilon and ans**4 < y:
        if ans**4 < y:
            ans += increment
        num_guesses += 1
    print(num_guesses)        
    if abs(ans**4 - x) >= epsilon:
        print("Cant find the fourth root of",y)
        print("the last ans was",ans)
        print("the last ans**4 was",ans**4)
    else:
        print(f"{ans} is the fourth root of {y}")





