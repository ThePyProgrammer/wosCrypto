from math import floor, ceil, log

class FastModulo:
    @staticmethod
    def exponentCalculate(base, exp, mod):
        val = 1
        for i in range(exp):
            val = val * base % mod
        return val

    @staticmethod
    def superExponentCalculate(base, exp, superexp, mod):
        for i in range(superexp):
            base = FastModulo.exponentCalculate(base, exp, mod)
        return base
