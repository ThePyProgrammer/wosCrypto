from numpy import log2, ceil

class Feistel:
    def __init__(self, function, keys, rounds):
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
             \             /
              \           /
               \         /
                \       /
                 \     /
                  \   /
                   \ /
                    \
                   / \
                  /   \
                 /     \
                /       \
               /         \
              /           \
             /             \
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
        self.K = keys
        self.n = rounds
    
    def forward(self, input):
        x = ceil(log2(input)/2)*2
        L, R = divmod(input, 2**(x//2))
        for i in range(self.n):
            R, L = L ^ self.F(R, self.K[i]), R
        return L*(2**(x//2))+R

    def backward(self, output):
        x = ceil(log2(output)/2)*2
        L, R = divmod(output, 2**(x//2))
        for i in range(self.n-1, -1, -1):
            L, R = R ^ self.F(L, self.K[i]), L
        return L*(2**(x//2))+R
