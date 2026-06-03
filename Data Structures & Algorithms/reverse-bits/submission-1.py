class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            n_i = (n >> i) & 1

            if n_i == 1:
                res |= (1 << (31 - i))

        return res