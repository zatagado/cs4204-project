import math
import numpy as np

class Shader:
    # Return 1 is a is greater or equal to b, otherwise return 0
    @staticmethod
    def step(a, b):
        return 1 if a >= b else 0
    
    # Return a rounded down to the nearest step multiple
    # ex. a = 0.45, steps = 0.2, return 0.4
    # ex. a = a = 0.79, steps = 0.2, return 0.6
    @staticmethod
    def posterize(a, steps):
        return (a // steps) * steps

    # Return the value clamped between 0 and 1
    @staticmethod
    def clamp01(a):
        return max(min(a, 1), 0)

class Vector2:
    @staticmethod
    def add(a: np.ndarray, b: np.ndarray):
        return np.array([a[0] + b[0], a[1] + b[1]], dtype=float)
    
    @staticmethod
    def sub(a: np.ndarray, b: np.ndarray):
        return np.array([a[0] - b[0], a[1] - b[1]], dtype=float)
    
    @staticmethod
    def mul(a: np.ndarray, b):
        if isinstance(b, float) or isinstance(b, int):
            return np.array([a[0] * b, a[1] * b])
        elif isinstance(b, np.ndarray) or isinstance(b, list):
            return np.array([a[0] * b[0], a[1] * b[1]])
        else:
            raise Exception('b was not correct type.')
    
    @staticmethod
    def div(a: np.ndarray, b: float):
        return np.array([a[0] / b, a[1] / b])

    @staticmethod
    def to_Vector3(a: np.ndarray):
        # return np.append(a, 1)
        return np.array([a[0], a[1], 1], dtype=float)
    
    def copy(a: np.ndarray):
        return np.copy(a)

class Vector3:
    @staticmethod
    def forward():
        return np.array([0, 1, 0], dtype=float)
    
    @staticmethod
    def up():
        return np.array([0, 0, 1], dtype=float)
    
    @staticmethod
    def right():
        return np.array([1, 0, 0], dtype=float)

    @staticmethod
    def negate(a):
        return np.array([-a[0], -a[1], -a[2]], dtype=float)

    @staticmethod
    def dot(a, b):
        return (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])

    @staticmethod
    def cross(a, b):
        return np.array([((a[1] * b[2]) - (a[2] * b[1])), ((a[2] * b[0]) - (a[0] * b[2])), ((a[0] * b[1]) - (a[1] * b[0]))])
    
    # project a onto b
    @staticmethod
    def project(a, b):
        b_mag = Vector3.magnitude(b)
        return Vector3.mul(b, Vector3.dot(a, b) / (b_mag * b_mag))
    
    @staticmethod
    def magnitude(a: np.ndarray):
        return math.sqrt(Vector3.dot(a, a))

    @staticmethod
    def normalize(a: np.ndarray):
        return Vector3.div(a, Vector3.magnitude(a))

    @staticmethod
    def dist(a: np.ndarray, b: np.ndarray):
        return Vector3.magnitude(Vector3.sub(a, b))

    @staticmethod
    def add(a: np.ndarray, b: np.ndarray):
        return np.array([a[0] + b[0], a[1] + b[1], a[2] + b[2]], dtype=float)
    
    @staticmethod
    def sub(a: np.ndarray, b: np.ndarray):
        return np.array([a[0] - b[0], a[1] - b[1], a[2] - b[2]], dtype=float)
    
    @staticmethod
    def mul(a: np.ndarray, b):
        if isinstance(b, float) or isinstance(b, int):
            return np.array([a[0] * b, a[1] * b, a[2] * b])
        elif isinstance(b, np.ndarray) or isinstance(b, list):
            return np.array([a[0] * b[0], a[1] * b[1], a[2] * b[2]])
        else:
            raise Exception('b was not correct type.')

    @staticmethod
    def clamp(a: np.ndarray, min, max):
        return np.clip(a, min, max)
    
    @staticmethod
    def div(a: np.ndarray, b: float):
        if b == 0:
            b = 0.0000001
        return np.array([a[0] / b, a[1] / b, a[2] / b], dtype=float)
    
    @staticmethod
    def equals(a: np.ndarray, b: np.ndarray):
        return abs(a[0] - b[0]) < 0.0001 and abs(a[1] - b[1]) < 0.0001 and abs(a[2] - b[2]) < 0.0001
    
    @staticmethod
    def to_vertical(a: np.ndarray):
        # return np.swapaxes([a], 0, 1)
        return np.array([[a[0]], [a[1]], [a[2]]], dtype=float)
    
    @staticmethod
    def to_horizontal(a: np.ndarray):
        # return np.swapaxes(a, 0, 1)[0]
        return np.array([a[0][0], a[1][0], a[2][0]], dtype=float)

    @staticmethod
    def to_Vector2(a: np.ndarray):
        # return a[:2]
        return np.array([a[0], a[1]], dtype=float)

    @staticmethod
    def to_Vector4(a: np.ndarray):
        # return np.append(a, 1)
        return np.array([a[0], a[1], a[2], 1], dtype=float)
    
    def copy(a: np.ndarray):
        return np.copy(a)

class Vector4:
    @staticmethod
    def add(a: np.ndarray, b: np.ndarray):
        return np.array([a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]], dtype=float)
    
    @staticmethod
    def sub(a: np.ndarray, b: np.ndarray):
        return np.array([a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3]], dtype=float)

    @staticmethod
    def mul(a: np.ndarray, b):
        if isinstance(b, float):
            return np.array([a[0] * b, a[1] * b, a[2] * b, a[3] * b], dtype=float)
        elif isinstance(b, np.ndarray) or isinstance(b, list):
            return np.array([a[0] * b[0], a[1] * b[1], a[2] * b[2], a[3] * b[3]], dtype=float)
        else:
            raise Exception('b was not correct type.')

    @staticmethod
    def div(a: np.ndarray, b: float):
        if b == 0:
            b = 0.0000001
        return np.array([a[0] / b, a[1] / b, a[2] / b, a[3] / b], dtype=float)

    @staticmethod
    def to_vertical(a: np.ndarray):
        # return np.swapaxes([a], 0, 1)
        return np.array([[a[0]], [a[1]], [a[2]], [a[3]]], dtype=float)
    
    @staticmethod
    def to_horizontal(a: np.ndarray):
        # return np.swapaxes(a, 0, 1)[0]
        return np.array([a[0][0], a[1][0], a[2][0], a[3][0]], dtype=float)

    @staticmethod
    def to_Vector3(a: np.ndarray):
        # return a[:3]
        return np.array([a[0], a[1], a[2]], dtype=float)

class Matrix:
    # Overwrite part of a with b. 
    # Use column and row to choose where to begin replacing.
    @staticmethod
    def overwrite(a: np.ndarray, b: np.ndarray, column: int, row: int):
        new_matrix = a.copy()
        for i in range(b.shape[0]):
            for j in range(b.shape[1]):
                new_matrix[i + column][j + row] = b[i][j]
        return new_matrix

    # inclusive from and to
    @staticmethod
    def submatrix(a, column_from, row_from, column_to, row_to):
        new_matrix = np.ndarray(shape=(1 + column_to - column_from, 1 + row_to - row_from), dtype=float)
        for i in range(column_from, column_to + 1):
            for j in range(row_from, row_to + 1):
                new_matrix[i - column_from][j - row_from] = a[i][j]
        return new_matrix

    @staticmethod
    def negate(a: np.ndarray):
        new_matrix = np.ndarray(shape=a.shape, dtype=float)
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                new_matrix[i][j] = -a[i][j]
        return new_matrix
