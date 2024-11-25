import math
import pickle  # Для роботи з двійковими файлами

# Функція для обчислення виразу y = cos(2x) / ctg(3x - 1)
def calculate_expression(x):
    """
    Обчислює значення y = cos(2x) / ctg(3x - 1) для заданого значення x.
    """
    try:
        numerator = math.cos(2 * x)
        denominator = 1 / math.tan(3 * x - 1)  # ctg(3x - 1) = 1/tan(3x - 1)
        y = numerator / denominator
        return y
    except ZeroDivisionError:
        print("Помилка: ділення на нуль. Значення (3x - 1) не може дорівнювати π/2 + π*k.")
        return None

# Функція для запису результату у текстовий файл
def write_text_file(filename, data):
    """
    Записує значення у текстовий файл.
    """
    try:
        with open(filename, 'w') as file:
            file.write(f"Результат обчислення: {data}\n")
    except IOError:
        print(f"Помилка: не вдалося записати дані у файл {filename}.")

# Функція для запису результату у двійковий файл
def write_binary_file(filename, data):
    """
    Записує значення у двійковий файл.
    """
    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
    except IOError:
        print(f"Помилка: не вдалося записати дані у двійковий файл {filename}.")

# Функція для читання результату з текстового файлу
def read_text_file(filename):
    """
    Читає значення з текстового файлу.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Помилка: файл {filename} не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося відкрити файл {filename} для читання.")

# Функція для читання результату з двійкового файлу
def read_binary_file(filename):
    """
    Читає значення з двійкового файлу.
    """
    try:
        with open(filename, 'rb') as file:
            content = pickle.load(file)
        return content
    except FileNotFoundError:
        print(f"Помилка: файл {filename} не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося відкрити двійковий файл {filename} для читання.")
    except pickle.UnpicklingError:
        print("Помилка: дані у файлі не можуть бути прочитані.")

# Основна частина програми
try:
    # Введення значення x
    x = float(input("Введіть значення x: "))

    # Обчислення виразу
    result = calculate_expression(x)

    if result is not None: 
        # Виведення результату
        print(f"Результат обчислення y = cos(2x) / ctg(3x - 1) для x = {x} дорівнює {result}")

        # Запис результату у текстовий файл
        write_text_file("result.txt", result)
        print("Результат записано у текстовий файл result.txt")

        # Запис результату у двійковий файл
        write_binary_file("result.bin", result)
        print("Результат записано у двійковий файл result.bin")

        # Читання результату з текстового файлу
        text_content = read_text_file("result.txt")
        if text_content is not None:
            print("\nЗчитано з текстового файлу: ", text_content)

        # Читання результату з двійкового файлу
        binary_content = read_binary_file("result.bin")
        if binary_content is not None:
            print("\nЗчитано з двійкового файлу: ", binary_content)
    else:
        print("Обчислення не вдалося через помилку ділення на нуль.")

except ValueError:
    print("Помилка: введене значення має бути числом.")


