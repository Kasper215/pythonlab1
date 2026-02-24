def mask_card_number():
    # Ввод номера карты с клавиатуры
    card_number = input("Введите 16-значный номер дебетовой карты: ").replace(" ", "").replace("-", "")

    # Проверка на корректность ввода
    if len(card_number) != 16 or not card_number.isdigit():
        print("Ошибка: Номер карты должен состоять из 16 цифр.")
        return

    # Извлечение частей номера
    first_four = card_number[:4]
    last_four = card_number[-4:]
    
    # Форматирование вывода: первые 4, две группы по ****, последние 4
    masked_number = f"{first_four} **** **** {last_four}"
    
    print(masked_number)

if __name__ == "__main__":
    mask_card_number()
