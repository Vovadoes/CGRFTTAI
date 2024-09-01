import math


# from Charts import *

# from scipy.stats import t

# CONST
# None

class Calculation:
    def __init__(self, h, n, i):
        self.r = None
        self.i = i
        self.n = n
        self.h = h

    def f1(self):
        self.r = (((1 + self.n * self.i / 100) * pow(1 + self.i / 100, self.n)) - 1) / self.n

    def f2(self):
        self.r = self.h + self.i + self.i * self.h / 100


if __name__ == "__main__":
    h = 7
    n = 0.25
    i = 22

    calculation = Calculation(h, n, i)
    calculation.f1()
    print(calculation.r)
    calculation.f2()
    print(calculation.r)

    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
