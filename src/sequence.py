def generate_sequence(n):

    """Функция генерирует первые n элементов последовательности 1223334444..."""

    if not isinstance(n, int):
        raise TypeError("Параметр n должен быть целым числом")
    if n < 0:
        raise ValueError("Параметр n не может быть отрицательным")

    sequence = []
    num = 1  # начальное число
    while len(sequence) < n:
        sequence.extend([num] * num)  # добавляем число num именно num раз
        num += 1  # переходим к следующему числу
    return sequence[:n]  # обрезаем до n элементов
