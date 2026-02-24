def frange(start, stop, step):
    current = float(start)
    if step > 0:
        # Используем малую дельту, чтобы избежать включения stop из-за ошибок округления
        while current < stop - 1e-10:
            yield round(current, 10)
            current += step
    elif step < 0:
        while current > stop + 1e-10:
            yield round(current, 10)
            current += step

if __name__ == "__main__":
    print("Тест frange(1, 5, 0.1):")
    for x in frange(1, 5, 0.1):
        print(x, end=" ")
    print("\n")

    print("Тест frange(10, 8, -0.2):")
    for x in frange(10, 8, -0.2):
        print(x, end=" ")
