from options import CallOption, PutOption
from pricers import BinomialPricer

o_style = "american"
stock_p = 0
strike_p = 0
exp_t = 0
vol = 0
int_r = 0

option = CallOption(o_style, stock_p, strike_p, exp_t, vol, int_r)
#print(option)
bin_pricer = BinomialPricer()
bin_pricer.price(option)
print(option)