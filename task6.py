def find_unique_chars():
    text = input("Введите предложение: ")
    
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    unique_chars = [char for char in text if char_counts[char] == 1]
    
    if unique_chars:
        print("Символы, встречающиеся ровно один раз:")
        print("".join(unique_chars))
    else:
        print("Нет символов, встречающихся ровно один раз.")

if __name__ == "__main__":
    find_unique_chars()
