class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ind_stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1] < temperatures[i]:
                ans[ind_stack[-1]] = i - ind_stack[-1]
                stack.pop()
                ind_stack.pop()

            stack.append(temperatures[i])
            ind_stack.append(i)

        return ans