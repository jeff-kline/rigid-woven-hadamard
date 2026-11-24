"""Stage-1 exact checks for th:tworank (sharp form) and cor:twist.

Independent implementation (examiner-written; does not import release code).
Single core, pure Python + numpy-free GF(2) elimination.
Run: python3 twist_stage1_checks.py
"""
import itertools
import sys


# ---------- GF(2) rank (rows as Python ints) ----------
def rk2(rows01):
    basis = {}
    r = 0
    for row in rows01:
        v = 0
        for b in row:
            v = (v << 1) | (b & 1)
        while v:
            h = v.bit_length() - 1
            if h in basis:
                v ^= basis[h]
            else:
                basis[h] = v
                r += 1
                break
    return r


def beta(H):
    return [[(1 - x) // 2 for x in row] for row in H]


def is_hadamard(H):
    N = len(H)
    for i in range(N):
        for j in range(N):
            s = sum(H[i][k] * H[j][k] for k in range(N))
            if s != (N if i == j else 0):
                return False
    return True


def normalize(H):
    N = len(H)
    H = [row[:] for row in H]
    for j in range(N):
        if H[0][j] < 0:
            for i in range(N):
                H[i][j] = -H[i][j]
    for i in range(N):
        if H[i][0] < 0:
            H[i] = [-x for x in H[i]]
    return H


# ---------- constructions ----------
def sylvester(k):
    H = [[1]]
    for _ in range(k):
        H = [r + r for r in H] + [r + [-x for x in r] for r in H]
    return H


def is_prime(q):
    return q > 1 and all(q % d for d in range(2, int(q ** 0.5) + 1))


def chi(a, q):
    a %= q
    if a == 0:
        return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1


def paley1(q):  # q = 3 mod 4 prime, order q+1
    idx = ["inf"] + list(range(q))
    N = q + 1
    S = [[0] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            x, y = idx[a], idx[b]
            if x == "inf" and y == "inf":
                S[a][b] = 0
            elif x == "inf":
                S[a][b] = 1
            elif y == "inf":
                S[a][b] = -1
            else:
                S[a][b] = chi(y - x, q)
    return [[S[a][b] + (1 if a == b else 0) for b in range(N)] for a in range(N)]


def paley2(q):  # q = 1 mod 4 prime, order 2(q+1)
    idx = ["inf"] + list(range(q))
    n = q + 1
    C = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            x, y = idx[a], idx[b]
            if x == "inf" and y == "inf":
                C[a][b] = 0
            elif x == "inf" or y == "inf":
                C[a][b] = 1
            else:
                C[a][b] = chi(y - x, q)
    I = lambda a, b: 1 if a == b else 0
    H = [[0] * (2 * n) for _ in range(2 * n)]
    for a in range(n):
        for b in range(n):
            H[a][b] = C[a][b] + I(a, b)
            H[a][b + n] = C[a][b] - I(a, b)
            H[a + n][b] = C[a][b] - I(a, b)
            H[a + n][b + n] = -C[a][b] - I(a, b)
    return H


def kron(A, B):
    return [[a * b for a in ra for b in rb] for ra in A for rb in B]


# ---------- check 1: 2-ranks of normalized and border-negated forms ----------
def border_negate(Hn):
    H = [row[:] for row in Hn]
    N = len(H)
    H[0] = [-x for x in H[0]]
    for i in range(N):
        H[i][0] = -H[i][0]
    return H


def check_ranks():
    mats = []
    mats.append(("Sylvester", 8, sylvester(3)))
    mats.append(("Sylvester", 16, sylvester(4)))
    mats.append(("Sylvester", 32, sylvester(5)))
    for q in [11, 19, 23, 31, 43]:
        mats.append(("PaleyI q=%d" % q, q + 1, paley1(q)))
    for q in [5, 13, 17]:
        mats.append(("PaleyII q=%d" % q, 2 * (q + 1), paley2(q)))
    mats.append(("PaleyI(11) x H2", 24, kron(paley1(11), sylvester(1))))
    mats.append(("PaleyII(5) x H2", 24, kron(paley2(5), sylvester(1))))
    mats.append(("PaleyI(19) x H2", 40, kron(paley1(19), sylvester(1))))
    print("check 1: rk2 beta(normalized), rk2 beta(border-negated), claimed bound")
    ok = True
    for name, N, H in mats:
        assert len(H) == N and is_hadamard(H), name
        Hn = normalize(H)
        r0 = rk2(beta(Hn))
        r1 = rk2(beta(border_negate(Hn)))
        if N % 8 == 4:
            claim = N
        elif N % 16 == 8:
            claim = N // 2 + 1
        else:
            claim = None
        flag = "" if claim is None or r1 == claim else "  <-- MISMATCH"
        if claim is not None and r1 != claim:
            ok = False
        print("  %-18s N=%3d  rk2(normalized)=%3d  rk2(border-neg)=%3d  claim=%s%s"
              % (name, N, r0, r1, claim, flag))
    return ok


# ---------- check 2: upper bound rk2 beta <= |X|+|Y| on random signings ----------
def check_upper_bound_on_pairings():
    import random
    rnd = random.Random(1)
    print("check 2: Paley II involution pairing, rk2 under 200 random signings <= |X|+|Y| = N")
    for q in [5, 13]:
        H = paley2(q)
        N = len(H)
        mx = 0
        for _ in range(200):
            r = [rnd.choice([1, -1]) for _ in range(N)]
            c = [rnd.choice([1, -1]) for _ in range(N)]
            Hs = [[r[i] * H[i][j] * c[j] for j in range(N)] for i in range(N)]
            mx = max(mx, rk2(beta(Hs)))
        print("  q=%d N=%d max rk2 over signings = %d (bound |X|+|Y| = %d)" % (q, N, mx, N))


# ---------- check 3: exhaustive pairings at N=12 ----------
def perfect_matchings(elems, ok):
    if not elems:
        yield []
        return
    a = elems[0]
    for k in range(1, len(elems)):
        b = elems[k]
        if ok(a, b):
            rest = elems[1:k] + elems[k + 1:]
            for m in perfect_matchings(rest, ok):
                yield [(a, b)] + m


def theta_rank_one(H, rp, cp):
    # Theta[r][c] = H[i][j]*H[i'][j'] for rank-one 2x2 blocks; rank one as sign matrix
    T = [[H[i][j] * H[i2][j2] for (j, j2) in cp] for (i, i2) in rp]
    base = T[0]
    for row in T:
        s = row[0] * base[0]
        if any(row[k] != s * base[k] for k in range(len(base))):
            return False
    return True


def check_exhaustive_12(H, label):
    N = len(H)
    assert is_hadamard(H)
    rows = list(range(N))
    n_rowp = n_pairs = n_untw = 0
    for rp in perfect_matchings(rows, lambda a, b: True):
        n_rowp += 1
        prods = [[H[i][j] * H[i2][j] for j in range(N)] for (i, i2) in rp]
        sig = [tuple(p[j] for p in prods) for j in range(N)]
        for cp in perfect_matchings(rows, lambda a, b: sig[a] == sig[b]):
            n_pairs += 1
            # sanity: every block rank one
            for (i, i2) in rp:
                for (j, j2) in cp:
                    assert H[i][j] * H[i2][j2] == H[i][j2] * H[i2][j]
            if theta_rank_one(H, rp, cp):
                n_untw += 1
    print("check 3 (%s): row pairings=%d, (row,col) pairings with all blocks rank one=%d, untwisted=%d"
          % (label, n_rowp, n_pairs, n_untw))
    return n_untw


# ---------- check 4: K-conjugation / weighing matrix on an untwisted example ----------
def check_untwisted_sylvester16():
    # Sylvester 16 with pairing {i, i xor 8}: H = [[A,A],[A,-A]] -> B=A, -A? check block form
    H = sylvester(4)
    N = 16
    for m in (1, 3):
        rp = [(i, i ^ m) for i in range(N) if i < i ^ m]
        cp = rp
        ok_rank = all(H[i][j] * H[i2][j2] == H[i][j2] * H[i2][j] for (i, i2) in rp for (j, j2) in cp)
        print("check 4: Sylvester 16 pairing {i,i^%d}: rank-one=%s untwisted=%s"
              % (m, ok_rank, ok_rank and theta_rank_one(H, rp, cp)))
    # positive control for the K-step: sign so theta=+1, permute to [[A,B],[B,A]], test U=(A+B)/2
    rp = [(i, i ^ 3) for i in range(N) if i < i ^ 3]
    T = [[H[i][j] * H[i2][j2] for (j, j2) in rp] for (i, i2) in rp]
    u = [T[a][0] * T[0][0] for a in range(len(rp))]
    v = [T[0][b] for b in range(len(rp))]
    rs = [1] * N
    cs = [1] * N
    for a, (i, i2) in enumerate(rp):
        rs[i2] = u[a]
    for b, (j, j2) in enumerate(rp):
        cs[j2] = v[b]
    Hs = [[rs[i] * H[i][j] * cs[j] for j in range(N)] for i in range(N)]
    order = [p[0] for p in rp] + [p[1] for p in rp]
    P = [[Hs[i][j] for j in order] for i in order]
    h = N // 2
    A = [r[:h] for r in P[:h]]
    B = [r[h:] for r in P[:h]]
    form_ok = all(P[h + a][h + b] == A[a][b] and P[h + a][b] == B[a][b] for a in range(h) for b in range(h))
    U = [[(A[a][b] + B[a][b]) // 2 for b in range(h)] for a in range(h)]
    UUt = [[sum(U[a][k] * U[c][k] for k in range(h)) for c in range(h)] for a in range(h)]
    w_ok = all(UUt[a][c] == (N // 4 if a == c else 0) for a in range(h) for c in range(h))
    print("check 4b: after signing, [[A,B],[B,A]] form=%s, U=(A+B)/2 is W(%d,%d)=%s" % (form_ok, h, N // 4, w_ok))


def main():
    ok = check_ranks()
    check_upper_bound_on_pairings()
    u1 = check_exhaustive_12(paley2(5), "Paley II q=5, N=12")
    u2 = check_exhaustive_12(paley1(11), "Paley I q=11, N=12")
    check_untwisted_sylvester16()
    print("RESULT ranks_ok=%s untwisted_at_12=%d,%d" % (ok, u1, u2))


if __name__ == "__main__":
    main()
# Redacted 2026-11-24 for privacy (local paths and session identifiers only); the sealed hash refers to the unredacted original.
