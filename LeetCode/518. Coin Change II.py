class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        @cache
        def solve(amount=amount, i=0):
            if i == N:
                return 0
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            return solve(amount-coins[i], i) + solve(amount,i+1)
            
        return solve()

        
