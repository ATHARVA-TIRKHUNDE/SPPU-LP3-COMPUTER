def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":

    n = int(input("Enter the Number: "))

    print(f"Fibonacci sequence using iterative approach:")
    for i in range(n + 1):
        print(f"Fib(",i,")",fibonacci_iterative(i))

    print("\nFibonacci sequence using recursive approach:")
    for i in range(n + 1):
        print(f"Fib(",i,")",fibonacci_recursive(i))
