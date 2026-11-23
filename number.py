from collections import Counter


def sum_numbers(numbers):
    """Return the sum of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
    return total


def average(numbers):
    """Return the average (mean) of a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")
    return sum_numbers(numbers) / len(numbers)


def median_and_mode(numbers):
    """Return (median, mode) of a list of numbers.

    The mode is returned as a list, since several values can tie
    for the most frequent.
    """
    if not numbers:
        raise ValueError("The list is empty.")


    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    median = s[mid] if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2

  
    counts = Counter(s)
    highest = max(counts.values())
    mode = [value for value, count in counts.items() if count == highest]

    return median, mode


if __name__ == "__main__":
    data = [4, 1, 2, 2, 3, 5, 2, 4]

    print("Sum:", sum_numbers(data))             
    print("Average:", average(data))                
    median, mode = median_and_mode(data)
    print("Median:", median)                          
    print("Mode:", mode)                            
