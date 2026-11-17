import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []

    a = np.asarray(values, dtype=float)
    return a.reshape(-1, width).round(6).tolist()


def block(
    matrix: list[list[float]], rows: list[int], columns: list[int]
) -> list[list[float]]:
    if not matrix:
        return []

    a = np.asarray(matrix, dtype=float)
    return a[np.ix_(rows, columns)].round(6).tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    a = np.asarray(matrix, dtype=float)
    if a.size == 0:
        return []

    return a.mean(axis=0).round(6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    a = np.asarray(matrix, dtype=float)
    if a.size == 0:
        return 0.0

    values = a[:, column]
    return float(np.round(values.max() - values.min(), 6))