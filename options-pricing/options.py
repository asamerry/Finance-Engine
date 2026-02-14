class Option:
    def __init__(self, o_style, stock_p, strike_p, exp_t, sigma, int_r):
        self.o_style: str = o_style
        self.stock_p: float = stock_p
        self.strike_p: float = strike_p
        self.exp_t: float = exp_t
        self.sigma: float = sigma
        self.int_r: float = int_r

        self.call_p = 0
        self.put_p = 0

    def __repr__(self):
        repr = f"{self.o_style.capitalize()} Option"
        repr += f"\nInitial Price: {self.stock_p}; Strike Price: {self.strike_p}" 
        repr += f"\nExpiration Date: {self.exp_t}; Volatility: {self.sigma}; Interest Rate: {self.int_r}"
        repr += f"\nCall Price: {self.call_p:.2f}; Put Price: {self.put_p:.2f}"
        return repr