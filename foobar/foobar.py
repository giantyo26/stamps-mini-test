def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    # Check if n is even number(not prime)
    if n % 2 == 0:
        return False
    # Check if n divisible by odd number
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
    return True

# Create a list of number from 1 to 100
nums = range(1, 101)

# Loop through list in reverse order
for num in reversed(nums):
    if is_prime(num):
        continue
    elif num % 3 == 0 and num % 5 == 0:
        print("FooBar", end=", ")
    elif num % 3 == 0:
        print("Foo", end=", ")
    elif num % 5 == 0:
        print("Bar", end=", ")
    else:
        print(num, end=", ")
