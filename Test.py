def add_with_bitwise(a, b):
    """
    Adds two integers using bitwise operators.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.
    """

    while b != 0:
        # calculate carry
        carry = a & b

        # calculate sum without carry
        a = a ^ b

        # carry is shifted one bit left
        b = carry << 1
        print(bin(carry))

    return a

# Example usage
a = 1001
b = 5868

result = add_with_bitwise(a, b)
print(f"Result of {a} + {b} using bitwise operators: {result}")