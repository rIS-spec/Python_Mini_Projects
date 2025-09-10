unit = input("Is this tempetature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == 'C':
    converted_temp = round((temp * 9/5) + 32)   # round to nearest integer
    print(f"{temp}°C is equal to {converted_temp}°F")
elif unit == 'F':
    converted_temp = round((temp - 32) * 5/9)
    print(f"{temp}°F is equal to {converted_temp}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")    



