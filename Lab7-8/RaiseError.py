def safe_divide(dividend, divisor, max_value):
    try:
        # Perform the division
        result = dividend / divisor
        
        # Check if the result exceeds the max_value
        if abs(result) > max_value:
            raise ArithmeticError(f"The result {result} exceeds the maximum allowed value of {max_value}.")
        
        return result
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ArithmeticError as e:
        return str(e)

# Example usage:
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))
max_value = float(input("Enter the maximum allowed value (M): "))

result = safe_divide(dividend, divisor, max_value)
print("Result:", result)
