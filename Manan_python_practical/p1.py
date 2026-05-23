import matplotlib.pyplot as plt

class Interest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

class SimpleInterest(Interest):
    def calculate_si(self):
        si_values = []

        for t in range(1, self.time + 1):
            si = (self.principal * self.rate * t) / 100
            amount = self.principal + si
            si_values.append(amount)

        return si_values

class CompoundInterest(Interest):
    def calculate_ci(self):
        ci_values = []

        for t in range(1, self.time + 1):
            amount = self.principal * ((1 + self.rate / 100) ** t)
            ci_values.append(amount)

        return ci_values

def main():
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Rate of Interest: "))
    time = int(input("Enter Time (in years): "))

    si_obj = SimpleInterest(principal, rate, time)
    ci_obj = CompoundInterest(principal, rate, time)

    si_values = si_obj.calculate_si()
    ci_values = ci_obj.calculate_ci()

    years = list(range(1, time + 1))

    print("\nYear\tSimple Interest Amount\tCompound Interest Amount")
    for i in range(time):
        print(f"{years[i]}\t{si_values[i]:.2f}\t\t\t{ci_values[i]:.2f}")

    plt.plot(years, si_values, marker='o', label='Simple Interest')
    plt.plot(years, ci_values, marker='s', label='Compound Interest')

    plt.title("Simple Interest vs Compound Interest")
    plt.xlabel("Years")
    plt.ylabel("Amount")
    plt.legend()
    plt.grid(True)

    plt.show()

main()