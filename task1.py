try:
    # Ввод числа с клавиатуры. Заменяем запятую на точку для корректного преобразования во float
    user_input = input("Введите вещественное число: ").replace(',', '.')
    amount = float(user_input)

    # Проверка на отрицательное число с вызовом исключения
    if amount < 0:
        raise ValueError("Отрицательное число")

    # Преобразование в рубли и копейки
    # Используем round для избежания проблем с точностью float (например, 12.5 * 100 может быть 1249.999...)
    total_kopecks = int(round(amount * 100))
    rubles = total_kopecks // 100
    kopecks = total_kopecks % 100

    print(f"{rubles} руб. {kopecks:02d} коп.")

except ValueError:
    print("Некорректный формат!")
except Exception as e:
    print(f"Произошла ошибка: {e}")
