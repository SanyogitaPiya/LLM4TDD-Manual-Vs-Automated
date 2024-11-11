def max_deletions(s: str) -> int:
    n = len(s)
    dp = [1] * n  # Minimum 1 deletion for each position

    for i in range(1, n):
        for length in range(1, (i + 1) // 2 + 1):
            # Check if we have a repeat pattern ending at i
            if s[i - 2 * length + 1:i - length + 1] == s[i - length + 1:i + 1]:
                dp[i] = max(dp[i], dp[i - length] + 1)

    return dp[-1]
