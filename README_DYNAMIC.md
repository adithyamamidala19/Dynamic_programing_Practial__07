# Dynamic Programming — Fibonacci (Memoization & Tabulation)

A Python program that calculates the nth Fibonacci number using two
Dynamic Programming strategies — **memoization (top-down)** and
**tabulation (bottom-up)** — and prints the execution time and
time/space complexity of each. A naive recursive version (no DP) is
included too, so you can see the difference DP makes.

## 📌 Overview

| Approach                     | Time Complexity | Space Complexity |
|-------------------------------|------------------|--------------------|
| Naive Recursive (no DP)        | O(2ⁿ)             | O(n) — call stack   |
| Memoization (Top-Down DP)      | O(n)              | O(n) — cache        |
| Tabulation (Bottom-Up DP)      | O(n)              | O(n) — table        |

## 🧠 Approach Details

### Naive Recursive (no DP)
Directly follows `fib(n) = fib(n-1) + fib(n-2)`. Simple, but
re-solves the same sub-problems over and over — the call count grows
exponentially, so it's only run here for small `n`.

### Memoization (Top-Down DP)
Same recursive structure as above, but every result is cached the
first time it's computed. Later calls for the same `n` are served
from the cache instead of recomputing — bringing it down to linear
time.

### Tabulation (Bottom-Up DP)
Builds a table iteratively from `fib(0)` up to `fib(n)`, with no
recursion at all. Same linear time as memoization, generally with
less overhead since there's no call stack involved.

## ▶️ Usage

```bash
python fibonacci_dp.py
```

You'll be prompted to enter a number:

```
Enter a non-negative integer (n for Fibonacci): 20

Calculating Fibonacci(20)...

Naive Recursive (no DP)
  Result            : 6765
  Execution Time    : 0.00181276 seconds
  Time Complexity   : O(2^n)
  Space Complexity  : O(n)

Dynamic Programming - Memoization (Top-Down)
  Result            : 6765
  Execution Time    : 0.00001322 seconds
  Time Complexity   : O(n)
  Space Complexity  : O(n)

Dynamic Programming - Tabulation (Bottom-Up)
  Result            : 6765
  Execution Time    : 0.00000752 seconds
  Time Complexity   : O(n)
  Space Complexity  : O(n)
```

> Note: for `n > 30` the naive recursive version is skipped
> automatically since O(2ⁿ) growth would make it impractically slow.

## 🗂 Project Structure

```
dynamic-programming/
├── README.md
└── fibonacci_dp.py
```

## 📝 License

MIT — free to use for learning and reference.
