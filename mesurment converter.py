def convert_temperature(value, input_unit, output_unit):
    if input_unit == 'C' and output_unit == 'F':
        return (value * 9/5) + 32
    elif input_unit == 'F' and output_unit == 'C':
        return (value - 32) * 5/9
    else:
        raise ValueError("Invalid input/output units for temperature conversion")

# Example usage
celsius = 25
fahrenheit = convert_temperature(celsius, 'C', 'F')
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

#another way 
def convert_length(value, input_unit, output_unit):
    if input_unit == 'm' and output_unit == 'ft':
        return value * 3.28084
    elif input_unit == 'ft' and output_unit == 'm':
        return value / 3.28084
    else:
        raise ValueError("Invalid input/output units for length conversion")

# Example usage
meters = 10
feet = convert_length(meters, 'm', 'ft')
print(f"{meters} meters is equal to {feet} feet")
