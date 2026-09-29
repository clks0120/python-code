class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = abs(x)
        b = x
        z = 0
        if (a != 0 and a % 10 == 0):
            return False
        while (x != 0): 
          y = abs(x) % 10
          x = abs(x) // 10 
          z = z * 10 + y
        if (z == a and b >= 0):
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(-121))       