def get_frames(signal, size, overlap):
    step = int(size * (1 - overlap))
    
    if step < 1:
        step = 1
        
    for i in range(0, len(signal), step):
        frame = signal[i : i + size]
        
        if len(frame) > 0:
            yield frame
        
        if i + size >= len(signal):
            break

if __name__ == "__main__":
    signal = list(range(16))
    print(f"Сигнал: {signal}")
    print(f"Размер окна: 4, Перекрытие: 0.5 (шаг 2)\n")
    
    for frame in get_frames(signal, size=4, overlap=0.5):
        print(frame)
