from math import log, floor, ceil
from util import Primes, gcd
from modulo import FastModulo
from typing import Tuple

def p1(n: int, B: int = 8, a: int = 2) -> Tuple[int, int]:
    """
    Pollard's p-1 Solution
    """
    M = 1
    r = a**M

    for q in Primes.listPrimes(B):
        e = floor(log(n, q))
        r = FastModulo.superExponentCalculate(r, q, e, n)
        val = gcd(r-1, n)
        if 1 < val < n: return sorted(val, n//val)


    return (1, n)


def rho(n: int, a: int = 5) -> Tuple[int, int]:
    """
    Pollard's Rho Solution
    """
    val = 1
    b = a
    f = lambda x: (x**2 + 1) % n
    while val != 1:
        a = f(a)
        b = f(f(b))
        val = gcd(n, abs(a-b))
        if val == n: return rho(n, a+1)
    
    return (val, n//val)

def quadraticSieve(n: int, B: int = 25, r: int = 1, offrange: int = 14):
    """
    Quadratic Sieve Algorithm
    
    """
    x0 = int((r*n)**0.5)
    store = {}

    for x in range(x0 - offrange, x0 + offrange+1):
        if x == x0: continue
        d = x**2 - r*n
        val, primes = Primes.primeFac(abs(d), 2, B)
        if val == 1: store[x] = primes
    
    # Do the weird Gaussian Elimination Crap



