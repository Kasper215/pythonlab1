import functools

def non_empty(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, list):
            return [item for item in result if item != '' and item is not None]
        
        return result
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', None, 'line1']

if __name__ == "__main__":
    print("Результат вызова get_pages():")
    pages = get_pages()
    print(pages)
    
    @non_empty
    def test_func():
        return [None, 'valid', '', 'another']
    
    print("\nРезультат вызова test_func():")
    print(test_func())
