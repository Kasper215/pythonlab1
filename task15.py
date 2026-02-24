import functools

def pre_process(a=0.97):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(s, *args, **kwargs):
            if not isinstance(s, list):
                return func(s, *args, **kwargs)
                
            filtered_s = []
            for i in range(len(s)):
                if i == 0:
                    filtered_s.append(s[i])
                else:
                    val = s[i] - a * s[i-1]
                    filtered_s.append(round(val, 10))
            
            return func(filtered_s, *args, **kwargs)
        return wrapper
    return decorator

@pre_process(a=0.93)
def plot_signal(s):
    print("Обработанный сигнал:")
    for sample in s:
        print(sample)

if __name__ == "__main__":
    test_signal = [100, 150, 200, 300]
    print(f"Исходный сигнал: {test_signal}")
    print(f"Параметр a = 0.93")
    plot_signal(test_signal)
    
    @pre_process()
    def process_default(s):
        print(f"\nС дефолтным a=0.97: {s}")
        
    process_default([100, 100, 100])
