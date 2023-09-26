def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage outside of the functions:
celsius_value = float(input("Enter temperature in Celsius: "))
converted_fahrenheit = celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value}°C is equal to {converted_fahrenheit}°F")

fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
converted_celsius = fahrenheit_to_celsius(fahrenheit_value)
print(f"{fahrenheit_value}°F is equal to {converted_celsius}°C")
