class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Initialize a table to store palindrome information
        dp = [[False] * n for _ in range(n)]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        start, max_len = 0, 1

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        return len(s[start:start + max_len])


# Example usage:
s = "dccaccd"
obj = Solution()
result = obj.longestPalindrome(s)
print(result)
