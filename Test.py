import itertools

def generate_masks(n):
  """Generates all possible masks of length n.

  Args:
    n: The desired length of the masks.

  Returns:
    A list of all possible masks.
  """

  return list(itertools.product([True, False], repeat=n))

# Example usage:
n = 3
all_masks = generate_masks(n)
print(all_masks)