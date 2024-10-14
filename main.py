def tuple_average(tup):
    if len(tup) == 0:
        return 0  # Avoid division by zero for empty tuples
    return sum(tup) / len(tup)

# Example usage:
my_tuple = (10, 20, 30, 40, 50)
average = tuple_average(my_tuple)

print("The average of the tuple is:", average)