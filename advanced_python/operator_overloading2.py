'''
Operator Overloading in Python:
- Python that allows the same operator to have different
meaning according to the context is called operator overloading.

- same operator behaves differently with different types.


common operators
__add__()
__sub__()
__mul__()
__pow__()
__le__()
__eq__()

'''

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        newReal = self.real + other.real
        newImg = self.imaginary + other.imaginary
        return ComplexNumber(newReal, newImg)

    def __sub__(self, other):
        newReal = self.real - other.real
        newImg = self.imaginary - other.imaginary
        return ComplexNumber(newReal, newImg)

    def __eq__(self, other):
        if self.real==other.real and self.imaginary == other.imaginary:
            return  True
        else:
            return  False

    def __ne__(self, other):
        if self.real != other.real or self.imaginary != other.imaginary:
            return  True
        else:
            return  False

    def __lt__(self, other):
        if self.real < other.real:
            return True
        elif self.real == other.real:
            if self.imaginary < other.imaginary:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.real > other.real:
            return True
        elif self.real == other.real:
            if self.imaginary > other.imaginary:
                return True
            else:
                return False
        else:
            return False


    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

c1  = ComplexNumber(1,9)  # 1 + 2i
c2  = ComplexNumber(1,5)  # 1 + 6i
print('c1+c2: ', c1  + c2)
print('c1-c2: ', c1  - c2)
print('c1==c2: ', c1 == c2)
print('c1<c2: ', c1 < c2)
print('c1>c2: ', c1 > c2)
print('c1 != c2: ', c1 != c2)























