#!/usr/bin/env python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    min_coins = float('inf')
    stack = [(total, 0, 0)]

    while stack:
        remaining, start, count = stack.pop()

        if remaining == 0:
            min_coins = min(min_coins, count)

        for i in range(start, len(coins)):
            coin = coins[i]
            new_remaining = remaining - coin

            if new_remaining >= 0 and count + new_remaining // coin + 1 < min_coins:
                stack.append((new_remaining, i, count + 1))

    return min_coins if min_coins != float('inf') else -1