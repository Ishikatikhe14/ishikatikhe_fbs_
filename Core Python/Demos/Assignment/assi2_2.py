#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# C= int(input("Enter temperature in Celsius: "))

# F = (C * 9 / 5) + 32
# print("Temperature in Fahrenheit is:", F)


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Based on the formula: (C / 5) * 9 + 32
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Take dynamic user input 
celsius_input = float(input("Enter temperature in Celsius: "))

# Calculate the result
fahrenheit_output = celsius_to_fahrenheit(celsius_input)

# Display the converted value rounded to 2 decimal places
print(f"{celsius_input}°C is equal to {fahrenheit_output:.2f}°F")
