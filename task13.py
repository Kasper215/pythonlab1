def extra_enumerate(x):
    total_sum = sum(x)
    cumulative_sum = 0
    
    for i, elem in enumerate(x):
        cumulative_sum += elem
        fraction = cumulative_sum / total_sum if total_sum != 0 else 0
        yield i, elem, cumulative_sum, fraction

if __name__ == "__main__":
    x = [1, 3, 4, 2]
    print(f"Исходный список: {x}")
    print("Результат extra_enumerate:")
    
    for i, elem, cum, frac in extra_enumerate(x):
        print(f"({elem}, {cum}, {frac})", end=" ")
    print()
