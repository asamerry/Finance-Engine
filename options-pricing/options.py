class Option:
    def __init__(self, o_style, stock_p, strike_p, exp_t, vol, int_r):
        self.o_style: str = o_style
        self.stock_p: float = stock_p
        self.strike_p: float = strike_p
        self.exp_t: float = exp_t
        self.vol: float = vol
        self.int_r: float = int_r

    def __repr__(self):
        repr = f"{self.o_style.capitalize()} Option"
        repr += f"\nInitial Price: {self.stock_p}; Strike Price: {self.strike_p}" 
        repr += f"\nExpiration Date: {self.exp_t}; Volatility: {self.vol}; Interest Rate: {self.int_r}"
        return repr