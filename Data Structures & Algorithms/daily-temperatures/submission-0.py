'''
    monotonic decreasing stack stores index
    when we meet a bigger one, we pop out until the top of the stack is bigger or not stack
        we mark their index as the cooresponding value = cur_idx - stack.pop()
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if stack and temperatures[stack[-1]] < t:
                while stack and temperatures[stack[-1]] < t:
                # top of stack is smaller than t
                    cur_idx = stack.pop()
                    res[cur_idx] = i - cur_idx
                
            stack.append(i)
        print(stack)
        return res