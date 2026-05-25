class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        hashset = {'{','(','['}

        # stack 

        # 1. [ ( or { -> push
        # 2. ] ) or } -> pop see if it's expected matching parenbtheses
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            # c is left 
            if c in hashset:
                stack.append(c)
            # c is right
            else: 
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if c in hashmap and hashmap[c] == left:
                    continue
                return False
        if len(stack) != 0:
            return False
        return True
                