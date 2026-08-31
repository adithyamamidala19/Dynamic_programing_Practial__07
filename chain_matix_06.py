import time


def matrix_chain_order(p):
    n = len(p) - 1

    # m[i][j] stores minimum multiplication cost
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # s[i][j] stores the position where the split occurs
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):
            j = i + length - 1

            m[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


# Print optimal parenthesization
def print_parenthesis(s, i, j):
    if i == j:
        return f"M{i}"

    k = s[i][j]

    left = print_parenthesis(s, i, k)
    right = print_parenthesis(s, k + 1, j)

    return f"({left} × {right})"


# -------------------------------
# User Input
# -------------------------------

n = int(input("Enter number of matrices: "))

dimensions = []

print("\nEnter dimensions of matrices:")

for i in range(n):
    rows = int(input(f"Enter rows of M{i + 1}: "))
    cols = int(input(f"Enter columns of M{i + 1}: "))

    # Check compatibility
    if i > 0 and dimensions[-1] != rows:
        print("Error: Matrix dimensions are not compatible.")
        exit()

    dimensions.append(rows)
    dimensions.append(cols)

# Convert dimensions into p array
p = [dimensions[0]]

for i in range(1, len(dimensions), 2):
    p.append(dimensions[i])


# -------------------------------
# Measure Execution Time
# -------------------------------

start_time = time.perf_counter()

m, s = matrix_chain_order(p)

end_time = time.perf_counter()

execution_time = end_time - start_time


# -------------------------------
# Output
# -------------------------------

print("\n-----------------------------------")
print("CHAIN MATRIX MULTIPLICATION")
print("-----------------------------------")

print("Number of matrices:", n)

print("\nMatrix Dimensions:")

for i in range(n):
    print(f"M{i + 1}: {p[i]} × {p[i + 1]}")

print("\nMinimum number of scalar multiplications:")
print(m[1][n])

print("\nOptimal Parenthesization:")
print(print_parenthesis(s, 1, n))

print("\nExecution Time:")
print(f"{execution_time:.9f} seconds")

print("\nTime Complexity: O(n³)")
print("Space Complexity: O(n²)")