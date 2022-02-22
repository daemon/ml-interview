# Hard DP questions.

from typing import List
import heapq
import random


def longest_valid_parentheses(string: str) -> int:
    if not string:
        return 0

    # Setting up state.
    A = [0] * len(string)
    matched = [False] * len(string)
    stack = []

    # Transition equation.
    for idx, c in enumerate(string):
        if c == '(':
            stack.append(idx)
        elif c == ')':
            if stack:
                match_idx = stack.pop()
                matched[match_idx] = True
                matched[idx] = True

                if matched[max(match_idx - 1, 0)]:
                    A[idx] = (idx - match_idx + 1) + A[max(match_idx - 1, 0)]
                else:
                    A[idx] = 2 + A[idx - 1]
            else:
                A[idx] = 0
    
    return max(A)


def paint_fence(n: int, k: int) -> int:
    # Set up state: last one repeated, last one unrepeated
    num_repeated = 0
    num_unrepeated = k

    # Transition equation.
    for idx in range(1, n):
        last_num_unrepeated = num_unrepeated
        num_unrepeated = (num_unrepeated + num_repeated) * (k - 1)
        num_repeated = last_num_unrepeated
    
    return num_unrepeated + num_repeated


def paint_house2(costs: List[List[int]]) -> int:
    # Set up state: min cost of painting the last house with the kth color.
    num_k = len(costs[0])
    min_last_costs = [(costs[0][color_idx], color_idx) for color_idx in range(num_k)]
    
    heapq.heapify(min_last_costs)
    min_first = heapq.heappop(min_last_costs)
    min_second = heapq.heappop(min_last_costs)

    # Transition equation.
    for house_idx in range(1, len(costs)):
        new_min_costs = []

        for color_idx in range(num_k):
            new_cost = costs[house_idx][color_idx]            
            new_cost += min_second[0] if color_idx == min_first[1] else min_first[0]
            new_min_costs.append((new_cost, color_idx))
        
        heapq.heapify(new_min_costs)
        min_first = heapq.heappop(new_min_costs)
        min_second = heapq.heappop(new_min_costs)
    
    return min_first[0]


def edit_distance(str1: str, str2: str) -> int:
    # Set up state.
    A = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    for idx in range(len(str1) + 1):
        A[idx][0] = idx
    
    for idx in range(len(str2) + 1):
        A[0][idx] = idx

    # Transition equation.
    for idx1 in range(1, len(str1) + 1):
        si = idx1 - 1

        for idx2 in range(1, len(str2) + 1):
            sj = idx2 - 1

            sub_dist = int(str1[si] != str2[sj]) + A[idx1 - 1][idx2 - 1]
            rm_dist = A[idx1][idx2 - 1] + 1
            add_dist = A[idx1 - 1][idx2] + 1

            A[idx1][idx2] = min(sub_dist, rm_dist, add_dist)
    
    return A[len(str1)][len(str2)]


def main():
    rand_str = ''.join('()'[random.randint(0, 1)] for _ in range(10))

    print(rand_str)
    print(longest_valid_parentheses(rand_str))

    print(paint_fence(3, 3))

    print(paint_house2([[1, 5, 3], [2, 9, 4]]))

    print(edit_distance('abcfghijklabc', 'dabcefghijklabc'))


if __name__ == '__main__':
    main()
