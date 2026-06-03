'''
    8 / 2 = 4 .. 0
    4 / 2 = 2 .. 0
    2 / 2 = 1 .. 0
    1 / 2 = 0 .. 1
'''



class Solution:
    def hammingWeight(self, n: int) -> int:
        bi_rep = ""

        # n = 8.     
        # 1000
        cnt = 0
        def convert_to_bi(n):
            nonlocal cnt
            bi_rep = ""
            while n != 0:
                mod = n % 2
                if mod == 1:
                    cnt += 1
                n = n // 2
                bi_rep += str(mod)
        
        convert_to_bi(n)

        return cnt