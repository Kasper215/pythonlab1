numbers = [1, 3, 5, 8, 12]

is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1))

print(is_increasing)
