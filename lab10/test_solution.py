from solution import *

assert make_table(2, 3) == [[0, 1, 2], [3, 4, 5]]
assert rectangle([[1, 2], [3, 4]], 0, 2, 1, 2) == [[2], [4]]
assert replace_rectangle([[1, 2]], 0, 1, 0, 1, 9) == [[9, 2]]
assert matrix_vector_product([[1, 2], [3, 4]], [1, 2]) == [5, 11]
assert matrix_multiply([[1, 2]], [[3], [4]]) == [[11]]
assert transpose_matrix([[1, 2]]) == [[1], [2]]
assert solve_system([[2, 1], [1, -1]], [7, 1]) == [2.666667, 1.666667]
assert tensor_channel_mean([[[1, 2, 3]]]) == [[2]]
assert point_distance([0, 0], [3, 4]) == 5.0

print("All tests passed")