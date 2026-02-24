import re

def check_password_strength():
    password = input("Введите пароль для проверки: ")
    
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Пароль слишком короткий (минимум 8 символов).")

    if len(password) >= 12:
        score += 1

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Добавьте хотя бы одну цифру.")

    if re.search(r"[a-z]", password) or re.search(r"[а-я]", password):
        score += 1
    else:
        feedback.append("Добавьте строчные буквы.")

    if re.search(r"[A-Z]", password) or re.search(r"[А-Я]", password):
        score += 1
    else:
        feedback.append("Добавьте заглавные буквы.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Добавьте специальные символы (например, !, @, #, $).")

    print(f"\nАнализ пароля: {password}")
    if score <= 2:
        status = "СЛАБЫЙ"
    elif score <= 4:
        status = "СРЕДНИЙ"
    else:
        status = "НАДЕЖНЫЙ"

    print(f"Уровень надежности: {status} ({score} из 6)")
    
    if feedback:
        print("Советы по улучшению:")
        for note in feedback:
            print(f"- {note}")

if __name__ == "__main__":
    check_password_strength()
