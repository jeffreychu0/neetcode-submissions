class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []

        digits[-1] += 1
        carry = 0
        for i in range(len(digits) - 1, -1, -1):

            ans.append((digits[i] + carry) % 10)

            if digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0

        if carry == 1:
            ans.append(carry)

        return list(reversed(ans))
            