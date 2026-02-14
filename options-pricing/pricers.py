from options import _Option

# Binomial Model
# Black-Scholes Model
# Finite Difference Model
# GARCH Model
# Heston Model
# Jump Diffusion Model
# Local Volatility Model
# Monte Carlo Simulation
# Stochastic Volatility Model

class _Pricer:
    def __init__(self):
        pass

    def price(self, option: _Option):
        option.price = 10

class BinomialPricer(_Pricer):
    def __init__(self):
        pass

    def price(self):
        pass  