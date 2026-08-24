import time

def factorial_dp(n):
    # Create DP array
    dp = [1] * (n + 1)

    # Build factorial values from bottom to top
    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]

    return dp[n]


# Taking user input
n = int(input("Enter a number: "))

# Start execution timer
start_time = time.perf_counter()

# Calculate factorial
result = factorial_dp(n)

# End execution timer
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display results
print("\nFactorial using Dynamic Programming")
print("Factorial of", n, "=", result)
print("Execution Time:", execution_time, "seconds")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")