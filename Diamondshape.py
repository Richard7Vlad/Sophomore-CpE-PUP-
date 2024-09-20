#Subject: Data Structure and Algorithm
#Lab Activity: Python review 
#Deadline: September 22, 2024 11:59pm
#Name: Richard Vladimir C. Natividad

#Exercise 3:  Diamond Shape (advance topic):

#Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.
#For n = 5, the output should be:

#    *
#   ***
#  *****
#   ***
#    *
# Note: If an even number is passed, the function should return "Please provide an odd integer."

def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd number"
    #upper half (including the middle row)
    for i in range(n // 2 + 1):  
        spaces = (n // 2) - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars)  
    
   #lower half (mirror of the upper half)
    for i in range(n // 2 - 1, -1, -1):
        spaces = (n // 2) - i
        stars = 2 * i + 1
        print(' ' * spaces + '*' * stars) 

while True: 
    try: 
        n = int(input(" Please enter a number: "))
        if n % 2 == 1:
            print_diamond(n)
            break
        else: 
            print("Please enter an odd number and t75ry Again")
    except ValueError:
        print("Invalid input. Please learn what is odd and even then try again.")
