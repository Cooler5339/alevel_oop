class Oxygen:
    t_plav = -218
    t_gas = -182

    def agg_state(self, t):
        if t < self.t_plav:
            return('hard')

        elif t > self.t_gas:
            return('gas')
        return('liquid')

oxy = Oxygen()
print(oxy.agg_state(-400))

