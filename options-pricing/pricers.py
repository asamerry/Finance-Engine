import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image
from graphviz import Digraph

from options import Option

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
    def __init__(self, option, periods, interval):
        self.title = ""
        self.option = option
        self.periods = periods
        self.interval = interval
        self.call_p, self.put_p = 0, 0

    def __repr__(self):
        repr = f" -=-=-=- {self.title} Pricing Model -=-=-=- "
        repr += f"\n{self.option}"
        repr += f"\nCall Price: {self.call_p:.2f}; Put Price: {self.put_p:.2f}"
        return repr

class BinomialPricer(_Pricer):
    def __init__(self, option: Option, periods: int, interval: float):
        super().__init__(option, periods, interval)
        self.title = "Binomial"

        delta = 0
        u = np.exp((option.int_r - delta) * self.interval + option.vol * np.sqrt(self.interval))
        d = np.exp((option.int_r - delta) * self.interval - option.vol * np.sqrt(self.interval))
        p = (np.exp((option.int_r - delta) * self.interval) - d) / (u - d)

        self.S_arr = [np.array([option.stock_p])]
        for idx in range(self.periods):
            new = np.array([d * self.S_arr[idx][0]] + list(self.S_arr[idx] * u))
            self.S_arr.append(new)
        
        Ss = self.S_arr[-1]
        Cs = np.array([max(S - option.strike_p, 0) for S in Ss])
        Ps = np.array([max(option.strike_p - S, 0) for S in Ss])

        self.C_arr = [Cs]
        self.P_arr = [Ps]

        while len(Cs) > 1:
            Cs = np.exp(-option.int_r * self.interval) * (Cs[1:] * p + Cs[:-1] * (1 - p))
            Ps = np.exp(-option.int_r * self.interval) * (Ps[1:] * p + Ps[:-1] * (1 - p)) 

            self.C_arr.append(Cs)
            self.P_arr.append(Ps)

        self.C_arr.reverse()
        self.P_arr.reverse()

        self.call_p = Cs.item()
        self.put_p = Ps.item()

    def plot(self):
        arrays = [self.P_arr, self.C_arr, self.S_arr]
        dot = Digraph(name="ThreeTrees")
        dot.attr(rankdir="LR")
        names = ["Put Price", "Call Price", "Stock Call"]

        for k, array in enumerate(arrays):
            with dot.subgraph(name=f"cluster_{k}") as sub:
                sub.attr(label=names[k])
                sub.attr(rankdir="TB")
                
                # plot nodes
                for layer_idx, layer in enumerate(array):
                    for node_idx, value in enumerate(layer):
                        node_id = f"T{k}_L{layer_idx}_N{node_idx}"
                        sub.node(node_id, label=f"{float(value):.2f}")
                    
                # plot edges
                for layer_idx in range(len(array) - 1):
                    for node_idx in range(len(array[layer_idx])):
                        src = f"T{k}_L{layer_idx}_N{node_idx}"
                        flat = f"T{k}_L{layer_idx+1}_N{node_idx}"
                        down = f"T{k}_L{layer_idx+1}_N{node_idx+1}"

                        sub.edge(src, flat)
                        sub.edge(src, down)

        img_bytes = dot.pipe(format='png')
        img = Image.open(io.BytesIO(img_bytes))
        plt.imshow(img)
        plt.axis("off")
        plt.show()