# This code is downloaded from Google
def fibonacci_list(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage:
print(fibonacci_list(10))

