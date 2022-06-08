from math import ceil
from .dsa import twodict
from typing import Tuple

def dlp(p: int, g: int, h: int) -> Tuple[int, int]:
    """
    Baby-Step, Giant-Step Algorithm for Discrete Log Problem

    >>> dlp(61, 2, 21)
    (-5, 60)
    >>> dlp(151, 6, 71)
    (-133, 150)
    >>> dlp(1979, 2, 123)
    (-413, 1978)
    """
    d = round(p ** 0.5)
    e = ceil((p-1)/d)
    mul = g ** d % p
    saved1, saved2 = 1, h

    store = twodict()

    for i in range(d):
        store[i] = saved1
        saved1 = (saved1 * g) % p
    
    for j in range(e):
        if(saved2 in store.values): break
        saved2 = (saved2 * mul) % p
    
    return (store.getKey(saved2) - j * d, p - 1)


def pohling_hellman(p: int, g: int, h: int):
    """
    Pohling-Hellman Algortihm for Discrete Log Problem
    """
    d = int((p-1) ** 0.5)
    while (p-1)%d != 0: d -= 1
    e = (p-1)//d
    r = 0
    while (g**(e*r) - h**e) % p:
        r += 1
        
