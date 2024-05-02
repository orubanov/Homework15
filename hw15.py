def test_factorial(n):
    if n == 1:
        return 1
    else:
        return n * test_factorial(n-1)


print(test_factorial(5))
print(test_factorial(6))
print(test_factorial(4))