# Программно задаваемый список
numbers = [1, 3, 5, 8, 12]

# Проверка, является ли последовательность возрастающей
# Используем генераторное выражение и функцию all()
is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1))

print(is_increasing)
