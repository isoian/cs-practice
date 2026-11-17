import numpy as np


# Задание 1. Создание векторов и матриц

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print("Задание 1")
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


# Задание 2. Индексы и срезы в векторе

print("\nЗадание 2")

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])


# Задание 3. Строки и столбцы таблицы

print("\nЗадание 3")

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)

print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0, :])
print("Последний столбец:", temperatures[:, -1])

print(
    "Первые две строки без первого столбца:\n",
    temperatures[:2, 1:]
)

central = temperatures[:2, 1:3]
print("Центральный фрагмент:\n", central)
print("Форма фрагмента:", central.shape)

# Задание 4
print("\nЗадание 4")

matrix = np.arange(1, 26).reshape(5, 5)

parts = [
    matrix[:3, :],
    matrix[-2:, :],
    matrix[:, :2],
    matrix[1:4, 2:5],
    matrix[-2:, -2:]
]

for part in parts:
    print(part)
    print("Форма:", part.shape)


# Задание 5
print("\nЗадание 5")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("Изменённый hours:", changed_hours)
print("Исходный hours:", hours)

# copy() нужна, чтобы исходный массив не изменился.

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Изменённая матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)


# Задание 6
print("\nЗадание 6")

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15.
