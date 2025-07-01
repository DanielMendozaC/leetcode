# Pattern to memorize
# Bottom-up DP template
dp[0] = base_case
for i in range(1, target + 1):
    for choice in choices:
        if valid(choice, i):
            dp[i] = optimize(dp[i], dp[i - cost] + 1)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity: O(amount × len(coins))
        # - Outer loop runs 'amount' times (from 1 to amount)
        # - Inner loop runs 'len(coins)' times for each amount
        # - Total operations: amount × len(coins)
        
        # Space Complexity: O(amount)
        # - We create dp array of size (amount + 1)
        # - No other significant space usage
        
        # dp[i] = minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):          # O(amount) iterations
            # Try each coin to see which gives minimum result
            for coin in coins:                   # O(len(coins)) iterations
                if coin <= i:  # Can only use coin if it's <= current amount
                    # Either keep current min, or use this coin + min coins for remaining
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return result if possible, otherwise -1 for impossible
        return dp[amount] if dp[amount] != float('inf') else -1





class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def backtrack(start, end, current_sum, num_coins, min_coins, amount):
            if current_sum == amount and num_coins < min_coins:
                min_coins = num_coins
                return min_coins
            elif current_sum > amount:
                return inf

            num_coins += 1

            for i in range(start, end):
                current_sum += coins[i]
                min_coins_res = backtrack(i, end, current_sum=current_sum , num_coins=num_coins, min_coins=min_coins, amount=amount)
                if min_coins_res < min_coins:
                    min_coins = min_coins_res
                current_sum -= coins[i]
                
            num_coins -= 1

            return min_coins 
            
        min_coins = backtrack(0, n, 0, 0, inf, amount)
        return min_coins
