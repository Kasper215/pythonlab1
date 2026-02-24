import random
import math

def generate_padded_array():
    n = random.randint(1, 10000)
    print(f"Сгенерировано n = {n}")

    array = [random.randint(1, 100) for _ in range(n)]
    
    power = math.ceil(math.log2(n))
    target_size = 2 ** power
    
    padding_size = target_size - n
    array.extend([0] * padding_size)
    
    print(f"Ближайшая степень двойки: {target_size}")
    print(f"Добавлено нулей: {padding_size}")
    print(f"Итоговый размер массива: {len(array)}")
    
    if len(array) <= 128:
        print("Массив:", array)
    else:
        print("Первые 10 элементов:", array[:10])
        print("Последние 10 элементов:", array[-10:])

if __name__ == "__main__":
    generate_padded_array()
