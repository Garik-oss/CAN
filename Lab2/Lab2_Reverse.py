number = int(input("Number: "))

#Sum
result = 0

number = abs(number)
while number > 0:
    result += number % 10
    number //= 10

#Reverse
reversed_number = ""
while result > 0:
    reversed_number += str(result % 10)  # Shift left and add last digit
    result //= 10 

print(f"The sum of the digits of {number} is: {reversed_number}")
