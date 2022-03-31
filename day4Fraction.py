class Fraction:
    numerator = 0
    denominator = 1
    def __init__(self, N, M):
        self.numerator = N
        self.denominator = M
    def __str__(self):
        out = str(self.numerator) + "/" + str(self.denominator)
        return out
    def simplify(self):
        for i in range(2, min(self.numerator, self.denominator)):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator //= i
                self.denominator //= i
    def decimal(self):
        return self.numerator / self.denominator
    def reciprocal(self):
        temp = self.numerator
        self.numerator = self.denominator
        self.denominator = temp
    def __add__(self, other):
        newN = self.numerator * other.denominator + self.denominator * other.numerator
        newM = self.denominator * other.denominator
        sumFract = Fraction(newN, newM)
        return sumFract


f = Fraction(6,8)
print(f)
f.simplify()
print(f)
f.reciprocal()
print(f)
print(f.decimal())
A = Fraction(16, 3)
B = Fraction(19, 6)
sumFract = A + B
print(sumFract)
sumFract.simplify()
print(sumFract)