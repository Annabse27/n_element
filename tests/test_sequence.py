import unittest
from src.sequence import generate_sequence

class TestGenerateSequence(unittest.TestCase):

    def test_zero_elements(self):
        """Проверка на ноль: при n = 0 возвращается пустой список"""
        self.assertEqual(generate_sequence(0), [])

    def test_one_element(self):
        """Проверяем, что при n = 1 возвращается [1]"""
        self.assertEqual(generate_sequence(1), [1])

    def test_two_elements(self):
        """Проверяем, что при n = 2 возвращается [1, 2]"""
        self.assertEqual(generate_sequence(2), [1, 2])

    def test_five_elements(self):
        """Проверяем, что при n = 5 возвращается [1, 2, 2, 3, 3]"""
        self.assertEqual(generate_sequence(5), [1, 2, 2, 3, 3])

    def test_fifteen_elements(self):
        """Проверяем, что при n = 15 возвращается [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]"""
        self.assertEqual(generate_sequence(15), [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])

    def test_large_number(self):
        """Проверяем корректность для более крупных значений n"""
        result = generate_sequence(30)
        expected_start = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8]
        self.assertEqual(result, expected_start)

    def test_type_error(self):
        """Проверяем, что функция вызывает ошибку, если входной параметр не является числом"""
        with self.assertRaises(TypeError):
            generate_sequence("abc")  # Неверный тип
        with self.assertRaises(TypeError):
            generate_sequence(None)  # NoneType

    def test_negative_number(self):
        """Проверяем, что при отрицательном n выбрасывается ValueError"""
        with self.assertRaises(ValueError):
            generate_sequence(-5)

if __name__ == '__main__':
    unittest.main()

