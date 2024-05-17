import numpy as np

def task10(matrix_10: np.ndarray) -> np.ndarray:
    matrix_res = [[0] * len(matrix_10) for i in range(len(matrix_10))]

    for i in range(len(matrix_10)):
        for j in range(len(matrix_10)):
            matrix_res[i][j] = np.linalg.norm(matrix_10[i]-matrix_10[j])
    
    return matrix_res



print(task10(np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [-2, 5, 4]])))