'''
    in s2 can we find a window that has 0 length of the freq_ctr

    s1 = "abc", coutner = n = 3. -> i:i+n
                counter = 2
                l isn't in the freq_ctr,  no operation
                
                
                c is in the freq_ctr, drop it off, if it's originally == 0, we introduced a new mismatch count += 1
                b is in the freq_ctr, do -1 , if == 0 after -1, count -= 1

          i
    s2 = "lecnbac"

    s1="abc"
    s2="lecaabee"

    s1="adc"
    s2="dcda"

'''

from collections import defaultdict

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):

            return False

        freq_ctr = defaultdict(int)

        for c in s1:

            freq_ctr[c] += 1

        

        n = len(s1)

        m = len(s2)

        need = n

        # first window

        for c in s2[:n]:

            if c in freq_ctr:

                if freq_ctr[c] > 0:

                    need -= 1

                freq_ctr[c] -= 1

        if need == 0:

            return True

        i = 1

        while i < m - n + 1:

            left = s2[i - 1]

            right = s2[i + n - 1]

            # remove left char from window

            if left in freq_ctr:

                if freq_ctr[left] >= 0:

                    need += 1

                freq_ctr[left] += 1

            # add right char into window

            if right in freq_ctr:

                if freq_ctr[right] > 0:

                    need -= 1

                freq_ctr[right] -= 1

            if need == 0:

                return True

            i += 1

        return False