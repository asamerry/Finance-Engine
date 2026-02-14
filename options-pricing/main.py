import numpy as np

from options import Option
from pricers import BinomialPricer, BlackScholesPricer

o_style = "european"
stock_p = 41
strike_p = 40
exp_t = 2
sigma = 0.3
int_r = 0.08
option = Option(o_style, stock_p, strike_p, exp_t, sigma, int_r)

#S_range = np.linspace(35, 45, 10)
#vol_range = np.linspace(0.1, 0.5, 10)
#options = [[Option(o_style, price, strike_p, exp_t, vol, int_r) for price in S_range] for vol in vol_range]

binom_pricer = BinomialPricer()
binom_pricer.price(option, plot=False, interval=1)
#binom_pricer.heatmap(options)

bs_pricer = BlackScholesPricer()
bs_pricer.price(option)
#bs_pricer.heatmap(options)