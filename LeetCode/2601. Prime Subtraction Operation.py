class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def primes_less_than(n):
            if n <= 2:
                return []
            sieve = [True] * n  # Create a boolean array for marking primes
            sieve[0] = sieve[1] = False  # 0 and 1 are not primes
            for p in range(2, int(n**0.5) + 1):
                if sieve[p]:
                    for i in range(p * p, n, p):
                        sieve[i] = False
            return [p for p in range(2, n) if sieve[p]]

        n = 1000
        primes = primes_less_than(n)  # Output: Primes less than 1000
        ret_arr = []
        for i in range(len(nums)):
            max_prime = -1
            if i == 0:
                for prime in primes:
                    if nums[i] - prime > 0:
                        max_prime = prime
                    else:
                        break
                if max_prime == -1:
                    ret_arr.append(nums[i])
                else:
                    ret_arr.append(nums[i] - max_prime)
            else:
                for prime in primes:
                    if nums[i] - prime > ret_arr[-1]:
                        max_prime = prime
                    else:
                        break
                if max_prime == -1:
                    ret_arr.append(nums[i])
                else:
                    ret_arr.append(nums[i] - max_prime)
        for i in range(1, len(ret_arr)):
            if ret_arr[i] <= ret_arr[i-1]:
                return False
        return True
