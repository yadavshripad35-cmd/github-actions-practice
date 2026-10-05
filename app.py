def fibonacci_list(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage:
print(fibonacci_list(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
