from typing import Tuple, List

def gcd(x: int, y: int) -> int:
    """
    Implementation of Euler's Method for Greatest Common Divisor (GCD).
    Time Complexity: O(log(min(x, y)))

    Uses concept that:
    gcd(x, y) = gcd(y, x%y)
    """
    if x < y: x, y = y, x
    while y: x, y = y, x % y
    return x

class Primes:
    @staticmethod
    def isPrime(n: int) -> bool:
        """
        Very Slow Primality Test (useful for checking small primes)
        Time Complexity: O(sqrt(N))
        """
        for i in range(2, int(n**0.5)):
            if n % i == 0: return False
        return True

    @staticmethod
    def primeFac(n: int, lower: int = 2, upper:int = None) -> Tuple[int, dict]:
        """
        Slow Prime Factorization method for Bounded Case (lower bound inclusive, upper bound exclusive)

        Time Complexity: O(log(N))
        """
        if upper is None: upper = int(n**0.5)+1
        primes = {}
        for q in range(lower, upper):
            if n % q == 0:
                primes[q] = 0
            while n % q == 0:
                n //= q
                primes[q] += 1
        
        primes[n] = primes.get(n, 0) + 1
        return (n, primes)

    @staticmethod
    def listPrimes(n: int) -> List[int]:
        numbers = set(range(n, 1, -2)) if n % 2 else set(range(n-1, 1, -2))
        primes = [2] if n >= 2 else []
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(p, n+1, 2*p)))
        return primes
