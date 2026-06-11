import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, arg1: float, arg2: float = None) -> float:
        if arg2 is None:
            # arg1 is a radius
            return round(math.pi * (arg1 ** 2), 2)
        return arg1 * arg2
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
