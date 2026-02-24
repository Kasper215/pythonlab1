import re

def process_sentence():
    text = input("Введите предложение: ")
    
    def transform_word(match):
        word = match.group(0)
        if word[0].isupper():
            return word.upper()
        return word

    result = re.sub(r'\w+', transform_word, text)
    
    print(result)

if __name__ == "__main__":
    process_sentence()
