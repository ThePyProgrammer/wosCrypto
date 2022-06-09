from functools import partial
from math import log2, ceil, log
from typing import Callable, Dict, List, Iterable
from .dsa import twodict
from abc import ABC, abstractmethod

class Feistel:
    def __init__(self, function: Callable, keys: List[int], rounds: int):
        """
        A Basic Implementation of an Abstract Feistel Network.

        :param function: Function taking in two integers (the plain text + the key)
        :param keys: List of keys for each iteration step
        :param rounds: Number of rounds to execute

        Structure of a Feistel Network:

             ---------------
             | plain  text |
             ---------------
                    |
            -----------------
            | L(0)          | R(0)
            .               .
            .               .
            .       Ki      .
            | L(i)  |       | R(i)
          /-|-\   -----     |
          |-+-|---| F |------
          \-|-/   -----     |
            \               /
              \           /
                \       /
                  \   /
                    \
                  /   \
                /       \
              /           \
            /               \
            | L(i+1)        | R(i+1)
            .               .
            .               .
            .               .
            | L(n)          | R(n)
            -----------------
                    |
             ---------------
             | cipher text |
             ---------------
            


        """
        self.F = function
        self.K = list(keys)
        self.n = rounds
    
    def forward(self, input: int):
        x = ceil(log2(input)/2)*2
        L, R = divmod(input, 2**(x//2))
        for i in range(self.n):
            R, L = L ^ self.F(R, self.K[i]), R
        return L*(2**(x//2))+R

    def backward(self, output: int):
        x = ceil(log2(output)/2)*2
        L, R = divmod(output, 2**(x//2))
        for i in range(self.n-1, -1, -1):
            L, R = R ^ self.F(L, self.K[i]), L
        return L*(2**(x//2))+R


class AESNode(ABC):
    @abstractmethod
    def forward(self, input: int, index: int = None): pass
    
    @abstractmethod
    def backward(self, output: int, index: int = None): pass

class XORGate(AESNode):
    def __init__(self, keys: Iterable[int]):
        self.keys = keys
    
    def forward(self, input: int, index: int):
        return self.keys[index] ^ input

    def backward(self, output: int, index: int = None):
        return self.keys[index] ^ output


class SubWords(AESNode):
    def __init__(self, map: Dict[int, int], base: int = 16):
        self.map = twodict(map.keys(), map.values())
        self.base = base

    def forward(self, input: int, index: int = 0):
        output = input
        n_considered = ceil(log(output, self.base))
        for i in range(n_considered):
            value = output // (self.base**i) % (self.base**(i+1))
            output += (map.value(value) - value)*(self.base ** i)
        return output

    def backward(self, output: int, index: int = 0):
        input = output
        n_considered = ceil(log(input, self.base))
        for i in range(n_considered):
            value = input // (self.base**i) % (self.base**(i+1))
            input += (map.key(value) - value)*(self.base ** i)
        return input

class ShiftRows(AESNode):
    def __init__(self, map: Dict[int, int], base=2):
        super().__init__()
        self.map = twodict(map.keys(), map.values())
        self.base = base

    def forward(self, input: int, index: int = 0):
        output = 0
        n_considered = ceil(log(output, self.base))
        for i in range(n_considered):
            

            value = output // (self.base**i) % (self.base**(i+1))
            output = input (self.base**map.value(i)
            output += (map.value(value) - value)*(self.base ** i)
        return output

    def backward(self, output: int):
        input = output
        n_considered = ceil(log(input, self.base))
        for i in range(n_considered):
            value = input // (self.base**i) % (self.base**(i+1))
            input += (map.key(value) - value)*(self.base ** i)
        return input

class AES:
    def __init__(self, *args, n = 5, IV = 0):
        self.pipeline = list(args)
        self.n = n
        self.iv = IV
    
    def add(self, *args):
        self.pipeline.extend(args)
        return self

    def forward(self, input: int):
        output = self.iv ^ input
        for i in range(self.n):
            for operation in self.pipeline:
                output = operation.forward(output, i)
        return output

    def backward(self, output: int):
        input = output
        for i in range(self.n):
            for operation in self.pipeline[::-1]:
              input = operation.backward(input, i)
        return input ^ self.IV  
    

if __name__ == "__main__":
    import requests
    import pandas as pd

    df = pd.read_html(requests.get("https://en.wikipedia.org/wiki/Rijndael_S-box").content)[0].iloc[:16].applymap(partial(
        int, base=16)).rename(columns={"Unnamed: 0": "index"}).set_index("index").rename(columns=partial(int, base=16)).stack()
    df.index = df.index.map(sum)
    rijndael = df.to_dict()
    aes = AES(
        SubWords(rijndael),
        ShiftRows()
    )

