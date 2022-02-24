# Easy-to-medium DP problems.

from typing import List
import sys
import time


def stair_count_dp(num_stairs: int) -> int:
    stairs = [0] * num_stairs
    stairs[0] = 1
    stairs[1] = 2

    for idx in range(2, num_stairs):
        stairs[idx] = stairs[idx - 1] + stairs[idx - 2]
    
    return stairs[-1]


def coin_change(coins: List[int], amount: int) -> int:
    curr_min = sys.maxsize

    if amount == 0:
        return 0

    for c in coins:
        if amount - c < 0:
            continue

        num_coins = coin_change(coins, amount - c) + 1
        curr_min = min(num_coins, curr_min)
    
    return curr_min


def coin_change_dp(coins: List[int], amount: int) -> int:
    A = [0] + [sys.maxsize] * amount

    for coin in coins:
        A[coin] = 1

    for a in range(1, amount + 1):
        min_coin = sys.maxsize

        for coin in coins:
            if coin > a:
                continue
            elif coin == a:
                min_coin = 0
                break

            min_coin = min(min_coin, A[a - coin])
        
        A[a] = min_coin + 1
    
    return A[-1]


def longest_increasing_subsequence(sequence: List[int]) -> int:
    A = [1] * len(sequence)
    
    for idx in range(len(sequence)):
        max_len = 0

        for idx2 in range(idx):
            if sequence[idx2] < sequence[idx]:
                max_len = max(max_len, A[idx2])
        
        max_len += 1
        A[idx] = max_len
    
    return A[-1]


def main():
    print(stair_count_dp(10))

    coins = [1, 5, 10, 25]

    a = time.time()
    change = coin_change(coins, 35)

    print(f'Brute force solution: {change} coins ({time.time() - a:.4} seconds)')

    a = time.time()
    change = coin_change_dp(coins, 35)
    print(f'DP solution: {change} coins ({time.time() - a:.4} seconds)')

    print(longest_increasing_subsequence([1, 5, 3, 2, 4, 6, 7, 2, 9, 10, 15]))


if __name__ == '__main__':
    main()
