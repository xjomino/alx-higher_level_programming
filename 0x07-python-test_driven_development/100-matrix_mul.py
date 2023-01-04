#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    def validate_matrix(m):
        if not isinstance(m, list):
            raise TypeError(f"{m} must be a list")
        if not all(isinstance(x, list) for x in m):
            raise TypeError(f"{m} must be a list of lists")
        if not m or any(not x for x in m):
            raise ValueError(f"{m} can't be empty")
        if not all(isinstance(x, (int, float)) for row in m for x in row):
            raise TypeError(f"{m} should contain only integers or floats")
        if not all(len(row) == len(m[0]) for row in m):
            raise TypeError(f"each row of {m} must be of the same size")
    
    validate_matrix(m_a)
    validate_matrix(m_b)
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result

