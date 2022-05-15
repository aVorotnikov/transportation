import numpy as np
from itertools import combinations

EPS = 1e-16


def get_basis_matrices(A):
    M, N = A.shape
    basis_matrs = []
    basis_combinations_indexes = []

    for i in combinations(range(N), M):
        basis_matr = A[:, i]
        if abs(np.linalg.det(basis_matr)) > 1e-12:
            basis_matrs.append(basis_matr)
            basis_combinations_indexes.append(i)

    return basis_matrs, basis_combinations_indexes


def get_vectors(A, b):
    M, N = A.shape
    vectors = []

    if M >= N:
        return vectors

    for matrix, indexes in zip(*get_basis_matrices(A)):
        sol = np.linalg.solve(matrix, b)
        if any(sol < -EPS) or any(sol > 1e16):
            continue

        vec = np.zeros((N, ))
        for i, index in enumerate(indexes):
            vec[index] = sol[i]
        vectors.append(vec)
    return vectors


def get_canonical(A, b, c):
    m = len(b)
    return np.concatenate((A, np.eye(m)), axis=1), b, np.pad(c, (0, m))


def solve_brute_force(A_in, b_in, c_in):
    n = len(c_in)
    A, b, c = get_canonical(A_in, b_in, c_in)

    from scipy.optimize import linprog
    res = linprog(-c, A_eq=A, b_eq=b, bounds=[(0, None)]*len(c))
    print(f'Scipy solution: {res.x, -res.fun}')

    vectors = get_vectors(A, b)
    if not vectors:
        return None

    solution = vectors[0]
    target_max = np.dot(solution, c)

    for vec in vectors:
        if np.dot(vec, c) > target_max:
            target_max = np.dot(vec, c)
            solution = vec

    return solution[:n], target_max
