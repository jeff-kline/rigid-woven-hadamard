"""Explicit regular Hadamard matrix of order 1600 from the four-group construction (Python port of check1600.mjs).

Fixed TD(4,20) from F4 x F5 and a Paley basis of order 20; no sign search. Builds every entry, then checks
that all entries are signs, all row and column sums are 40, and H H^T = 1600 I (equivalently, all 1279200 pairs of
rows are at Hamming distance 800). Exact integer arithmetic; about a second on one core.
"""
import numpy as np

h, k = 20, 4
n = k * h * h
multiply4 = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]
slopes = [None, 0, 2, 3]  # same integer representatives in the two fields


def direction(i, a, b):
    if slopes[i] is None:
        return b
    x = (a // 5) ^ multiply4[slopes[i]][b // 5]
    y = (a % 5 + slopes[i] * (b % 5)) % 5
    return 5 * x + y


line_join = [[[-1] * (h * h) for _ in range(k)] for _ in range(k)]
point = [[0] * (h * h) for _ in range(k)]
port = [[0] * (h * h) for _ in range(k)]
for a in range(h):
    for b in range(h):
        l = h * a + b
        for i in range(k):
            point[i][l] = direction(i, a, b)
            port[i][l] = direction(i, b, a)
        for i in range(k):
            for j in range(k):
                s = point[i][l]
                r = port[i][l] if i == j else point[j][l]
                assert line_join[i][j][h * s + r] == -1
                line_join[i][j][h * s + r] = l
assert all(l >= 0 for groups in line_join for pair in groups for l in pair)

squares = {((i + 1) ** 2) % 19 for i in range(18)}
A = [[1 if (a == b or a == 0) else (-1 if b == 0 else (1 if (19 + b - a) % 19 in squares else -1))
      for b in range(h)] for a in range(h)]
An = np.array(A, dtype=np.int64)
assert (An @ An.T == h * np.eye(h, dtype=np.int64)).all()

K = [[0, 1, 1, 1], [-1, 0, 1, -1], [-1, -1, 0, 1], [-1, 1, -1, 0]]
d = [-1, 1, 1, 1]
H = np.zeros((n, n), dtype=np.int64)
for i in range(k):
    for s in range(h):
        for a in range(h):
            row = (i * h + s) * h + a
            for j in range(k):
                for r in range(h):
                    l = line_join[i][j][s * h + r]
                    first = A[a][port[i][l]]
                    second_port = s if i == j else port[j][l]
                    c = 1 if i == j else K[i][j]
                    scalar = A[a][s] * c * first * d[j]
                    col0 = (j * h + r) * h
                    H[row, col0:col0 + h] = scalar * An[:, second_port] * An[:, r]

assert set(np.unique(H)) <= {-1, 1}
assert (H.sum(axis=1) == 2 * h).all() and (H.sum(axis=0) == 2 * h).all()
assert (H @ H.T == n * np.eye(n, dtype=np.int64)).all()
print("Regular order 1600: all 2560000 sign entries checked; all row and column sums 40; "
      "all 1279200 row-pair distances 800.")
