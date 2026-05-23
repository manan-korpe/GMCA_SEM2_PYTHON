import math
from pylab import *

class InterestCalculator:
    def __init__(self, p, r, n):
        self.p = p
        self.r = r
        self.n = n

    def simpleInterest(self):
        SI = []
        years = []
        for i in range(1, self.n + 1):
            simple_interest = self.p + (self.p * self.r * i) / 100
            SI.append(simple_interest)
            years.append(i)
        return years, SI

    def compoundInterest(self):
        CI = []
        for i in range(1, self.n + 1):
            compound_interest = self.p * ((1 + (self.r / 100)) ** i)
            CI.append(math.floor(compound_interest))
        return CI


obj = InterestCalculator(10000, 2, 8)

print(obj.simpleInterest())
print(obj.compoundInterest())

x, y = obj.simpleInterest()
z = obj.compoundInterest()

plot(x, y, marker='o')
plot(x, z, marker='o')

grid()
xlabel("Years")
ylabel("Amount")
show()