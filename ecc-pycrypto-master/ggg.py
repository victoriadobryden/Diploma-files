import matplotlib.pyplot as plt

# Дані для графіка
file_sizes = [1, 2, 5]  # Розміри файлів (у мегабайтах)
regular_encryption_times = [367095, 735500, 1824322]  # Час шифрування звичайним Ель-Гамалем (у мілісекундах)
elliptic_encryption_times = [280241, 1401276, 2803615]  # Час шифрування Ель-Гамалем в еліптичній криптографії (у мілісекундах)

# Перетворення часу на секунди
regular_encryption_times = [t / 1000 for t in regular_encryption_times]
elliptic_encryption_times = [t / 1000 for t in elliptic_encryption_times]

# Побудова графіка
plt.plot(file_sizes, regular_encryption_times, label='Алгоритм Ель-Гамаля')
plt.plot(file_sizes, elliptic_encryption_times, label='Еліптичний алгоритм Ель-Гамаля')

# Налаштування графіка
plt.xlabel('Розмір файла (MB)')
plt.ylabel('Час шифрування (s)')
plt.title('Порівняння часу шифрування')
plt.legend()

# Відображення графіка
plt.show()