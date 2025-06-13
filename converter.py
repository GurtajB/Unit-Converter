

def inches_to_cm():
    inches = float(input("Enter Inches: "))
    centimeters = inches * 2.54
    print(f"{centimeters:.2f} centimeters")
def cm_to_inches():
    centimeters = float(input("Enter Centimeters: "))
    inches = centimeters / 2.54
    print(f"{inches:.2f} inches")
def pounds_to_kilograms():
    pounds = float(input("Enter Pounds: "))
    kilos = pounds * 0.453592
    print(f"{kilos:.2f} kilograms")
def kilograms_to_pounds():
    kilos = float(input("Enter Kilograms: "))
    pounds = kilos / 0.453592
    print(f"{pounds:.2f} pounds")
def fahren_to_celsius():
    fahren = float(input("Enter Fahrenheit: "))
    celsius = (fahren - 32) * 5/9
    print(f"{celsius:.2f} degrees celsius")
def celsius_to_fahrenheit():
    celsius = float(input("Enter Celsius: "))
    fahren = (celsius * 9/5) + 32
    print(f"{fahren:.2f} degrees Fahrenheit")

def main():
    menu = """
# Welcome to the Unit Converter!
a) Inches to Centimeters
b) Centimeters to Inches
c) Pounds to Kilograms
d) Kilograms to Pounds
e) Fahrenheit to Celsius
f) Celsius to Fahrenheit
"""
    print(menu)
    choice = input("What would you like to convert? ").lower()

    if (choice == "a"):
        inches_to_cm()
    elif (choice == "b"):
        cm_to_inches()
    elif (choice == "c"):
        pounds_to_kilograms()
    elif (choice == "d"):
        kilograms_to_pounds()
    elif (choice == "e"):
        fahren_to_celsius()
    elif (choice == "f"):
        celsius_to_fahrenheit()
    else:
        print("invalid, enter one of the letters")

main()
