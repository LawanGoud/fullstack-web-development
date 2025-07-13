input_string = input()

unit = input_string[-1]

number_part = input_string[:-1]

numeric_value = int(number_part)

if unit == "T":
    result = numeric_value * 10
elif unit == "H":
    result = numeric_value * 100
elif unit == "K":
    result = numeric_value * 1000
else:
    result = numeric_value

print(result)