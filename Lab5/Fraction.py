import math

class Fraction:
    def __init__(self, numerator, denominator):
        # Validate the denominator is not zero
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        # Simplify the fraction upon creation
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        # Ensure the denominator is always positive
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            # Add fractions: a/b + c/d = (a*d + b*c) / (b*d)
            new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self + Fraction(other, 1)  # Treat integers as fractions

    def __sub__(self, other):
        if isinstance(other, Fraction):
            # Subtract fractions: a/b - c/d = (a*d - b*c) / (b*d)
            new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self - Fraction(other, 1)  # Treat integers as fractions

    def __mul__(self, other):
        if isinstance(other, Fraction):
            # Multiply fractions: (a/b) * (c/d) = (a*c) / (b*d)
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self * Fraction(other, 1)  # Treat integers as fractions

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            # Divide fractions: (a/b) / (c/d) = (a*d) / (b*c)
            if other.numerator == 0:
                raise ValueError("Cannot divide by zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        elif isinstance(other, int):
            return self / Fraction(other, 1)  # Treat integers as fractions

    def __eq__(self, other):
        return (self.numerator == other.numerator) and (self.denominator == other.denominator)

    def __float__(self):
        # Convert fraction to float for arithmetic
        return self.numerator / self.denominator

    def to_mixed(self):
        # Convert to a mixed number (quotient + remainder)
        if abs(self.numerator) < self.denominator:
            return str(self)
        else:
            quotient, remainder = divmod(abs(self.numerator), self.denominator)
            sign = '-' if self.numerator < 0 else ''
            if remainder == 0:
                return f"{sign}{quotient}"
            else:
                return f"{sign}{quotient} {remainder}/{self.denominator}"
                
    def shorten(self):
        gcd = math.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // gcd, self.denominator // gcd)

f1 = Fraction(3, 4)
f2 = Fraction(5, 6)
print("Fraction 1:", f1)
print("Fraction 2:", f2)

# Addition
print("Addition:", f1 + f2)

# Subtraction
print("Subtraction:", f1 - f2)

# Multiplication
print("Multiplication:", f1 * f2)

# Division
print("Division:", f1 / f2)

# Equality check
print("Equality check:", f1 == f2)

# Convert to float
print("As float:", float(f1))

# Mixed number
print("Mixed number representation:", f1.to_mixed())

f3 = Fraction(4, 6)
print(f3.shorten())
