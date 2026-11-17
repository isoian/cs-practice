from solution import reshape_rows, block, column_means, column_range


if __name__ == "__main__":
    assert reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3) == [
        [12.0, 14.5, 11.0],
        [13.0, 15.5, 10.5]
    ]
    assert reshape_rows([1, 2, 3], 2) == []
    assert reshape_rows([], 3) == []

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert block(matrix, [0, 2], [1, 2]) == [
        [2.0, 3.0],
        [8.0, 9.0]
    ]
    assert block(matrix, [2, 0], [2, 0]) == [
        [9.0, 7.0],
        [3.0, 1.0]
    ]
    assert block([], [], []) == []

    assert column_means([[1, 2], [3, 4], [5, 6]]) == [3.0, 4.0]
    assert column_means([]) == []
    assert column_means([[0], [0], [1]]) == [0.333333]

    assert column_range([[1, 2], [5, 7]], 1) == 5.0
    assert column_range([], 0) == 0.0
    assert column_range([[0], [1.12345678]], 0) == 1.123457

    print("All tests passed")