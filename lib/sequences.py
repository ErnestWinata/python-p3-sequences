#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []

    if length <= 0:
        print(sequence)
        return
    
    sequence = [0, 1] if length >=2 else [0]
    
    while len(sequence) < length:
        fibonacci_sequence = sequence[-1] + sequence[-2]
        sequence.append(fibonacci_sequence)

    print(sequence)