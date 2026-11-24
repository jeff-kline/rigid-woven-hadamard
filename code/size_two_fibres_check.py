"""Exact check of the size-two fibre proposition on Paley II matrices (rigidity paper, Section 'Fibres of size two').

For each prime q = 1 mod 4 in the list, build the symmetric Paley II Hadamard matrix H of order N = 2(q+1)
and the involution sigma (x -> -x on F_q in both halves, fixing infinity and 0). Then check:
  1. H is a symmetric Hadamard matrix, and H[sigma i, sigma j] = H[i, j];
  2. sigma fixes exactly four indices, and their diagonal signs can be paired equally;
  3. with the pairing of the proposition, all N^2/4 two-by-two blocks have rank one;
  4. the pairing is twisted: the block signs theta have a nonzero 2x2 minor;
  5. Theorem 'Rank-one blocks': rk_2 beta(H) = N = |X| + |Y| (the theorem's bound, met exactly);
  6. Corollary 'Unavoidable twist': reports which orders are 12 mod 16 (q = 5 mod 8).
Exact integer arithmetic only; runs in well under a second. Usage: python size_two_fibres_check.py
"""
import numpy as np

PRIMES = [5, 13, 17, 29, 37, 41, 53]


def paley_ii(q):
    chi = [0] + [1 if pow(a, (q - 1) // 2, q) == 1 else -1 for a in range(1, q)]
    n = q + 1                                   # index 0 = infinity, index 1 + x = x in F_q
    C = np.zeros((n, n), dtype=np.int64)
    C[0, 1:] = 1
    C[1:, 0] = 1
    for x in range(q):
        for y in range(q):
            C[1 + x, 1 + y] = chi[(y - x) % q]
    I = np.eye(n, dtype=np.int64)
    H = np.block([[C + I, C - I], [C - I, -C - I]])
    sig_half = [0] + [1 + (-x) % q for x in range(q)]
    sigma = sig_half + [n + s for s in sig_half]
    return H, sigma


def rank_gf2(B):
    rows = [int("".join(map(str, r)), 2) for r in B.tolist()]
    rank, ncols = 0, B.shape[1]
    for bit in reversed(range(ncols)):
        piv = next((i for i in range(rank, len(rows)) if rows[i] >> bit & 1), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i] >> bit & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def check(q):
    H, sigma = paley_ii(q)
    N = H.shape[0]
    assert (H == H.T).all() and (H @ H.T == N * np.eye(N, dtype=np.int64)).all()
    s = np.array(sigma)
    assert (H[np.ix_(s, s)] == H).all() and (s[s] == np.arange(N)).all()
    fixed = [i for i in range(N) if sigma[i] == i]
    assert len(fixed) == 4
    # pair fixed indices with equal diagonal signs
    plus = [i for i in fixed if H[i, i] == 1]
    minus = [i for i in fixed if H[i, i] == -1]
    assert len(plus) % 2 == 0 and len(minus) % 2 == 0
    pairs = [tuple(plus[k:k + 2]) for k in range(0, len(plus), 2)]
    pairs += [tuple(minus[k:k + 2]) for k in range(0, len(minus), 2)]
    pairs += sorted({tuple(sorted((i, sigma[i]))) for i in range(N) if sigma[i] != i})
    assert len(pairs) == N // 2 and sorted(i for p in pairs for i in p) == list(range(N))
    theta = np.zeros((N // 2, N // 2), dtype=np.int64)
    for a, P in enumerate(pairs):
        for b, Q in enumerate(pairs):
            T = H[np.ix_(P, Q)]
            assert T[0, 0] * T[1, 1] == T[0, 1] * T[1, 0]          # rank one
            theta[a, b] = T[0, 0] * T[1, 1]                     # swapping both pairs multiplies T by theta
    # Re-signing rows/columns multiplies theta by alpha_a * beta_b, so the pairing is untwisted iff the
    # sign matrix theta has rank one, i.e. theta == theta[0,0] * outer(theta[:, 0], theta[0, :]).
    twisted = not (theta == theta[0, 0] * np.outer(theta[:, 0], theta[0, :])).all()
    beta = ((1 - H) // 2).astype(np.int64)
    r2 = rank_gf2(beta)
    assert N % 8 == 4 and r2 == N
    return N, r2, twisted


if __name__ == "__main__":
    print(" q     N   rk2(beta)  |X|+|Y|  twisted  N mod 16")
    for q in PRIMES:
        N, r2, tw = check(q)
        assert tw
        print(f"{q:2d} {N:5d} {r2:9d} {N:8d}  {tw!s:7}  {N % 16:4d}")
    # Negative control: Sylvester H_ij = (-1)^{i.j}, order 32, indices in F_2^5.
    # Pairing {i, i xor 3} on both sides: every block rank one, and untwisted.
    # Deliberate-error control: pairing {2i, 2i+1} must FAIL the rank-one test.
    idx = np.arange(32)
    S = np.array([[(-1) ** bin(i & j).count("1") for j in idx] for i in idx], dtype=np.int64)
    assert (S @ S.T == 32 * np.eye(32, dtype=np.int64)).all()

    def blocks(pairs):
        th = np.zeros((16, 16), dtype=np.int64)
        rank_one = True
        for a_, P in enumerate(pairs):
            for b_, Q in enumerate(pairs):
                T = S[np.ix_(P, Q)]
                rank_one &= bool(T[0, 0] * T[1, 1] == T[0, 1] * T[1, 0])
                th[a_, b_] = T[0, 0] * T[1, 1]
        return rank_one, th

    good = [(i, i ^ 3) for i in range(32) if i < i ^ 3]
    ok1, th = blocks(good)
    assert ok1 and (th == th[0, 0] * np.outer(th[:, 0], th[0, :])).all()
    bad = [(2 * i, 2 * i + 1) for i in range(16)]
    ok2, _ = blocks(bad)
    assert not ok2
    print("control: Sylvester 32, pairs {i, i^3}: all blocks rank one, untwisted; pairs {2i,2i+1}: rejected")
    print("all checks passed")
