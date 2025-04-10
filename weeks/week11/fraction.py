from __future__ import annotations
import math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero (Have 0 as your denominator)")
        elif numerator == 0:
            denominator = 1

        sign = 1
        if numerator/ denominator < 0:
            sign = -1
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        while math.gcd(int(numerator), int(denominator)) != 1:
            gcd = math.gcd(numerator, denominator)
            numerator /= gcd
            denominator /= gcd
             
        self.numerator = int(sign * numerator)
        self.demominator = int(denominator)

    def __repr__(self):
        return f"{self.numerator} / {self.demominator}"

    def __add__(self, other_fraction: Fraction):
        first_top = self.numerator * other_fraction.demominator
        second_top = self.demominator * other_fraction.numerator

        added_top = first_top + second_top
        added_bottom = self.demominator * other_fraction.demominator

        return Fraction(added_top, added_bottom)
    
    def __sub__(self, other_fraction: Fraction):
        first_top = self.numerator * other_fraction.demominator
        second_top = self.demominator * other_fraction.numerator

        substracted_top = first_top - second_top
        substracted_bottom = self.demominator * other_fraction.demominator

        return Fraction(substracted_top, substracted_bottom)
    
    def __eq__(self, other_fraction: Fraction) -> bool:
        return self.numerator / self.demominator == other_fraction.numerator / other_fraction.demominator
    
    def __lt__(self, other_fraction: Fraction) -> bool:
        return self.numerator / self.demominator < other_fraction.numerator / other_fraction.demominator
    


frac1 = Fraction(1, 12)
print(frac1)
frac2 = Fraction(11, 12)
print(frac1 + frac2)
print(frac2 - frac1)
print(frac1 < frac2)