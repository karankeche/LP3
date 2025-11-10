#fibonacci Series

# Fibonacci using Iteration (Non-Recursive)
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a=0
    b=1
    for i in range(2, n):
        c = a + b
        a, b = b, c
    return b


# Fibonacci using Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Driver code
n = int(input("Enter the position of Fibonacci number: "))

print("\n--- Non-Recursive (Iterative) ---")
print(f"Fibonacci({n}) =", fibonacci_iterative(n))

print("\n--- Recursive ---")
print(f"Fibonacci({n}) =", fibonacci_recursive(n))
