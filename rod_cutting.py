from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію.

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    memo = {}

    def dp(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = 0
        best_cut = []
        for i in range(n):
            profit, cuts = dp(n - (i + 1))
            profit += prices[i]
            if profit > max_profit:
                max_profit = profit
                best_cut = [i + 1] + cuts

        memo[n] = (max_profit, best_cut)
        return memo[n]

    max_profit, cuts = dp(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію.

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for n in range(1, length + 1):
        for i in range(n):
            profit = prices[i] + dp[n - (i + 1)]
            if profit > dp[n]:
                dp[n] = profit
                cuts[n] = [i + 1] + cuts[n - (i + 1)]

    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1
    }