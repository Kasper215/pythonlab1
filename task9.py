def atm_simulation():
    banknotes = {
        5000: 10,
        2000: 10,
        1000: 20,
        500: 50,
        200: 100,
        100: 100,
        50: 200,
        10: 500
    }

    try:
        amount = int(input("Введите сумму для снятия: "))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Некорректная сумма!")
        return

    result = []
    temp_amount = amount
    
    for denomination in sorted(banknotes.keys(), reverse=True):
        if temp_amount <= 0:
            break
            
        count_needed = temp_amount // denomination
        count_to_give = min(count_needed, banknotes[denomination])
        
        if count_to_give > 0:
            result.append(f"{count_to_give}*{denomination}")
            temp_amount -= count_to_give * denomination

    if temp_amount == 0:
        print(" + ".join(result))
    else:
        print("Операция не может быть выполнена!")

if __name__ == "__main__":
    atm_simulation()
