#Subject: Data Structure and Algorithm
#Lab Activity: Python review 
#Deadline: September 22, 2024 11:59pm
#Name: Richard Vladimir C. Natividad

#Exercise 1: Temperature Converter
#Create a program that converts temperatures between Celsius and Fahrenheit.

#Instructions:
#1.	Ask the user to input a temperature.
#2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
#3.	Perform the appropriate conversion and print the result.


Temp = str(input("Input a Temperature: "))
type = input("Select conversion type (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): ")

if type == "1":
    celsius = float(Temp)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}")
elif type == "2":
    fahrenheit = float(Temp)
    celsius = (fahrenheit - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius}")
else:
    print("Invalid conversion type selected.")
