import numpy as np


def make_table(rows: int, columns: int) -> list[list[int]]:
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix: list[list[float]], row_start: int,
              row_stop: int, column_start: int,
              column_stop: int) -> list[list[float]]:
    a = np.asarray(matrix, dtype=float)
    return a[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix: list[list[float]], row_start: int,
                      row_stop: int, column_start: int,
                      column_stop: int, value: float) -> list[list[float]]:
    a = np.asarray(matrix, dtype=float).copy()
    a[row_start:row_stop, column_start:column_stop] = value
    return a.tolist()


def matrix_vector_product(matrix: list[list[float]],
                          vector: list[float]) -> list[float]:
    a = np.asarray(matrix, dtype=float)
    b = np.asarray(vector, dtype=float)
    return (a @ b).tolist()


def matrix_multiply(left: list[list[float]],
                    right: list[list[float]]) -> list[list[float]]:
    a = np.asarray(left, dtype=float)
    b = np.asarray(right, dtype=float)
    return (a @ b).tolist()


def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    a = np.asarray(matrix, dtype=float)
    return a.T.tolist()


def solve_system(matrix: list[list[float]],
                 vector: list[float]) -> list[float]:
    a = np.asarray(matrix, dtype=float)
    b = np.asarray(vector, dtype=float)
    return np.linalg.solve(a, b).round(6).tolist()


def tensor_channel_mean(tensor: list) -> list:
    a = np.asarray(tensor, dtype=float)
    return a.mean(axis=-1).tolist()


def point_distance(first: list[float], second: list[float]) -> float:
    a = np.asarray(first, dtype=float)
    b = np.asarray(second, dtype=float)
    return round(float(np.linalg.norm(a - b)), 6)