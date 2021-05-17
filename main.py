
from calc.calc import *

if __name__ == '__main__':
    a, b = 2, 5
    print('a = 2, b = 5\na + b = ', sum(a, b), '\na - b = ', sum(a, b), '\na * b = ', mul(a, b),
          '\na / b = ', div(a, b), '\na ^ b = ', pow(a, b), '\ne ^ a = ', exp(a), '\nlog_b(a) = ', log(a, b),
          '\nlog2(a) = ', log2(a))

