class _Option:
    def __init__(self, o_style, stock_p, strike_p, exp_t, vol, int_r):
        self.o_style: str = o_style
        self.o_type: str = ""
        self.stock_p: float = stock_p
        self.strike_p: float = strike_p
        self.exp_t: float = exp_t
        self.vol: float = vol
        self.int_r: float = int_r

        self.price: float = 0.0

    def __repr__(self):
        repr = f"{self.o_style.capitalize()} {self.o_type.capitalize()} Option"
        repr += f"\nInitial Price: {self.stock_p}"
        repr += f"\nStrike Price: {self.strike_p}" 
        repr += f"\nExpiration Date: {self.exp_t}"
        repr += f"\nVolatility: {self.vol}"
        repr += f"\nInterest Rate: {self.int_r}"
        repr += f"\nPrice: {self.price}"
        return repr

class CallOption(_Option):
    def __init__(self, o_style, stock_p, strike_p, exp_t, vol, int_r):
        super().__init__(o_style, stock_p, strike_p, exp_t, vol, int_r)
        self.o_type = "call"

class PutOption(_Option):
    def __init__(self, o_style, stock_p, strike_p, exp_t, vol, int_r):
        super().__init__(o_style, stock_p, strike_p, exp_t, vol, int_r)
        self.o_type = "put"