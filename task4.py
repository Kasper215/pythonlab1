def process_text():
    text = input("Введите текст: ")
    
    words = text.split()
    
    long_words = [w for w in words if len(w) > 7]
    
    medium_words = [w for w in words if 4 <= len(w) <= 7]
    
    short_words = [w for w in words if len(w) < 4]
    
    print("\nСлова длиннее 7 символов:")
    print(" ".join(long_words))
    
    print("\nСлова длиной от 4 до 7 символов:")
    print(" ".join(medium_words))
    
    print("\nОстальные слова:")
    print(" ".join(short_words))

if __name__ == "__main__":
    process_text()
