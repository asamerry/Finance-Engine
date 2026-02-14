from options import Option
from pricers import BinomialPricer

o_style = "american"
stock_p = 41
strike_p = 40
exp_t = 1
vol = 0.3
int_r = 0.08

option = Option(o_style, stock_p, strike_p, exp_t, vol, int_r)
binom_pricer = BinomialPricer(option, periods=2, interval=1)
print(binom_pricer)
binom_pricer.plot()