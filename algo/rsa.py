from util import Primes
from modulo import FastModulo


class RSA:
    def __init__(self, n: int, e: int):
        self.n = n
        self.e = e
        self.phi = len(Primes.listPrimes(n-1))

    def encrypt(self, m: int):
        return FastModulo.exponentCalculate(m, self.e, self.n)