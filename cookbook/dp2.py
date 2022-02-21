# Hard DP questions.

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


def main():
    rand_str = ''.join('()'[random.randint(0, 1)] for _ in range(10))

    print(rand_str)
    print(longest_valid_parentheses(rand_str))


if __name__ == '__main__':
    main()
