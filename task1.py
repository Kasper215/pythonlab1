try:
    user_input = input("Введите вещественное число: ").replace(',', '.')
    amount = float(user_input)

    if amount < 0:
        raise ValueError("Отрицательное число")

    total_kopecks = int(round(amount * 100))
    rubles = total_kopecks // 100
    kopecks = total_kopecks % 100

    print(f"{rubles} руб. {kopecks:02d} коп.")

except ValueError:
    print("Некорректный формат!")
except Exception as e:
    print(f"Произошла ошибка: {e}")
