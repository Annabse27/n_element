from src.sequence import generate_sequence


def main():
    """Основная функция для ввода и вывода"""
    while True:
        try:
            n = input("Введите количество элементов последовательности: ").strip()

            # Проверка на целое число
            if not n.isdigit():
                raise ValueError("Вы вводите неверное значение. Введите положительное целое число.")

            n = int(n)  # Преобразуем строку в число

            # Проверка на отрицательные числа
            if n < 0:
                raise ValueError("Вы вводите неверное значение. Введите положительное целое число.")

            if n == 0:
                print("Вы ввели ноль — результат ноль!")
                break  # Завершаем цикл, так как пользователь ввёл 0

            # Генерируем последовательность
            result = generate_sequence(n)

            # Выводим результат
            for i in range(len(result)):
                if i != len(result) - 1:
                    print(result[i], end=" ")
                else:
                    print(result[i])

            break  # Завершаем цикл после успешного ввода и вывода

        except ValueError as ve:
            print(ve)  # Показываем сообщение об ошибке
        except TypeError as te:
            print(te)  # Показываем сообщение об ошибке


if __name__ == "__main__":
    main()
