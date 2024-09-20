#Subject: Data Structure and Algorithm
#Lab Activity: Python review 
#Deadline: September 22, 2024 11:59pm
#Name: Richard Vladimir C. Natividad

#Exercise 2: Ohm’s Law Calculator
#Instructions:
#1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
#2.	Based on their choice, prompt the user to input the appropriate values.
#3.	Use Ohm's Law to calculate the missing variable and display the result.
#4.	Handle cases where division by zero might occur.


calculation_type = input("What do you want to calculate? (Choose in these three choice: Voltage, Current, Resistance): ")

if calculation_type.lower() == "voltage":
    current = float(input("Enter the current (in Ampheres): "))
    resistance = float(input("Enter the resistance (in Ohms): "))
    voltage = current*resistance
    print ("The voltage is", voltage, "Volts.")
elif calculation_type.lower() == "current":
    voltage = float(input("Enter the voltage (in Volts): "))
    resistance = float(input("Enter the resistance (in Ohms): "))

    try:
        current = voltage / resistance
        print("The current", current, "Ampere.")
    except ZeroDivisionError:
        print ("Error! Division by zero is not applicable.Learn your Division!")

elif calculation_type.lower() == "resistance":
    current = float(input("Enter the current (in Amperes): "))
    voltage = float(input("Enter the voltage (in Volts): "))

    try:
        resistance = voltage / current
        print("The resistance", resistance,"Ohms")
    except ZeroDivisionError:
        print ("Error! Division by zero is not applicable. Learn your Division! ")

else:
    print("Invalid Calculation. Please choose only in the three! (Voltage, Current, Resistance)")