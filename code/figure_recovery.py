"""Figure: a Bush-type Meisner square of order 144, disguised, then re-sorted from its entries alone.

Input: the normalized Paley-type Hadamard matrix of order 12 (I + S, S skew, q = 11). Ensemble: the Bush square of
Section 2.1 with m = 12, N = 144, fixed seed.
Panel (a): the matrix as built, with its 12 x 12 grid of rank-one blocks.
Panel (b): after a random signed permutation of rows and columns.
Panel (c): panel (b) re-sorted by the divisibility test from the proof of Proposition 4.1 (two rows are related when
every extension by two further rows has fourth sum divisible by m), applied to rows and to columns; signs are left
as they are in (b). The test reads only the entries of (b).
At this small order a mixed quartet reaches N/2, so the branch selection in that proof, which is asymptotic, would
choose the other branch; the figure applies the divisibility branch directly. The script checks the recovered
partitions against the hidden ones.
Also checks the caption's tripwires: at this order the large-quartet branch fails, and at order 64 with the
Sylvester input the divisibility test relates every pair of rows.
Writes paper/fig-recovery.pdf and figures/recovery.png with --write; always prints a summary (used by make verify).
"""
import sys
import numpy as np

SEED = 20261124
m = 12
N = m * m


def paley12():
    q = 11
    sq = {(x * x) % q for x in range(1, q)}
    S = np.zeros((12, 12), dtype=np.int64)
    S[0, 1:] = 1
    S[1:, 0] = -1
    for i in range(q):
        for j in range(q):
            if i != j:
                S[1 + i, 1 + j] = 1 if (j - i) % q in sq else -1
    A = S + np.eye(12, dtype=np.int64)
    A = A * A[:, :1]
    A = A * A[:1, :]                  # first row and column all +1
    assert (A @ A.T == 12 * np.eye(12, dtype=np.int64)).all()
    return A


A = paley12()
rng = np.random.default_rng(SEED)


def bush_square():
    """H[(i,e),(j,r)] = s_i(j) t_j(i) A[e, p_i(j)] A[p'_j(i), r]; diagonal ports 0, diagonal signs +1."""
    p = np.zeros((m, m), dtype=int)
    q = np.zeros((m, m), dtype=int)
    s = np.ones((m, m), dtype=np.int64)
    t = np.ones((m, m), dtype=np.int64)
    for i in range(m):
        others = [j for j in range(m) if j != i]
        p[i, others] = rng.permutation(np.arange(1, m))
        s[i, others] = rng.choice([-1, 1], size=m - 1)
    for j in range(m):
        others = [i for i in range(m) if i != j]
        q[j, others] = rng.permutation(np.arange(1, m))
        t[j, others] = rng.choice([-1, 1], size=m - 1)
    H = np.zeros((N, N), dtype=np.int64)
    for i in range(m):
        for j in range(m):
            H[i * m:(i + 1) * m, j * m:(j + 1) * m] = s[i, j] * t[j, i] * np.outer(A[:, p[i, j]], A[q[j, i], :])
    return H


def divisibility_fibres(M, d):
    """Relate rows u, v when every fourth sum D(u, v, w, z), w, z distinct further rows, is divisible by d."""
    n = M.shape[0]
    iu, ju = np.triu_indices(n, 1)
    P = (M[iu] * M[ju]).astype(np.float64)   # exact: entries are small integers
    passed = np.ones(len(iu), dtype=bool)
    for a0 in range(0, len(iu), 1000):
        Dc = np.rint(P[a0:a0 + 1000] @ P.T).astype(np.int64)
        ia, ja = iu[a0:a0 + 1000, None], ju[a0:a0 + 1000, None]
        share = (ia == iu[None, :]) | (ia == ju[None, :]) | (ja == iu[None, :]) | (ja == ju[None, :])
        passed[a0:a0 + 1000] = ((Dc % d == 0) | share).all(axis=1)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in zip(iu[passed], ju[passed]):
        parent[find(u)] = find(v)
    groups = {}
    for x in range(n):
        groups.setdefault(find(x), []).append(x)
    return sorted(groups.values(), key=min), int(passed.sum())


def main():
    H = bush_square()
    assert (H @ H.T == N * np.eye(N, dtype=np.int64)).all()
    rp, cp = rng.permutation(N), rng.permutation(N)
    rs, cs = rng.choice([-1, 1], size=N), rng.choice([-1, 1], size=N)
    Hd = (rs[:, None] * H[rp][:, cp]) * cs[None, :]          # disguised: only this is read below
    row_f, row_pairs = divisibility_fibres(Hd, m)
    col_f, col_pairs = divisibility_fibres(Hd.T, m)
    ok_rows = len(row_f) == m and all(len(f) == m and len(set(rp[f] // m)) == 1 for f in row_f)
    ok_cols = len(col_f) == m and all(len(f) == m and len(set(cp[f] // m)) == 1 for f in col_f)
    Hr = Hd[np.ix_([r for f in row_f for r in f], [c for f in col_f for c in f])]
    rank_one = all(np.linalg.matrix_rank(Hr[a * m:(a + 1) * m, b * m:(b + 1) * m]) == 1
                   for a in range(m) for b in range(m))
    print(f"Bush square from Paley 12: m={m}, N={N}, seed {SEED}; Hadamard: True")
    print(f"divisibility test: {row_pairs} related row pairs, {col_pairs} related column pairs "
          f"(true: {m * m * (m - 1) // 2} each)")
    print(f"recovered {len(row_f)} row fibres and {len(col_f)} column fibres; "
          f"row fibres correct: {ok_rows}; column fibres correct: {ok_cols}; "
          f"re-sorted blocks all rank one: {rank_one}")
    tripwires(Hd, cp)
    if "--write" in sys.argv:
        draw(H, Hd, Hr)


def large_quartet_column_groups(M):
    """Large-quartet branch: pairs in quartets with |D| >= N/2 (four distinct rows); columns grouped by their lists."""
    n = M.shape[0]
    iu, ju = np.triu_indices(n, 1)
    P = (M[iu] * M[ju]).astype(np.float64)
    sel = set()
    for a0 in range(0, len(iu), 1000):
        Dc = np.abs(np.rint(P[a0:a0 + 1000] @ P.T))
        ia, ja = iu[a0:a0 + 1000, None], ju[a0:a0 + 1000, None]
        share = (ia == iu[None, :]) | (ia == ju[None, :]) | (ja == iu[None, :]) | (ja == ju[None, :])
        a_idx, b_idx = np.nonzero((Dc >= n // 2) & ~share)
        sel.update((a_idx + a0).tolist())
        sel.update(b_idx.tolist())
    lists = P[sorted(sel)].T
    keys = {}
    part = [keys.setdefault(tuple(lists[k]), len(keys)) for k in range(n)]
    return [[k for k in range(n) if part[k] == c] for c in range(len(keys))]


def tripwires(Hd, cp):
    """Checks behind the caption's tripwires."""
    global A, m, N
    groups = large_quartet_column_groups(Hd)
    ok = len(groups) == m and all(len(g) == m and len(set(cp[g] // m)) == 1 for g in groups)
    print(f"tripwire, order {N}: the large-quartet branch finds {len(groups)} column groups (true {m}); correct: {ok}")
    # Sylvester input, m = 8 (the only Hadamard matrix of order 8), same Bush ensemble
    saved = (A, m, N)
    S = np.array([[1]], dtype=np.int64)
    for _ in range(3):
        S = np.block([[S, S], [S, -S]])
    A, m, N = S, 8, 64
    H8 = bush_square()
    _, passed = divisibility_fibres(H8, m)
    print(f"tripwire, order 64 (Sylvester input): the divisibility test relates {passed} of {N * (N - 1) // 2} "
          f"row pairs (true {m * m * (m - 1) // 2})")
    A, m, N = saved


def draw(H, Hd, Hr):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    cmap = ListedColormap(["#1a1a1a", "#ffffff"])
    matplotlib.rcParams.update({"pdf.fonttype": 42, "font.family": "serif", "font.size": 10})
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.25))
    for ax, M, grid, lab in zip(axes, (H, Hd, Hr), (True, False, True), ("(a)", "(b)", "(c)")):
        ax.set_xlabel(lab, labelpad=3)
        ax.imshow(M, cmap=cmap, vmin=-1, vmax=1, interpolation="nearest")
        if grid:
            for k in range(1, m):
                ax.axhline(k * m - 0.5, color="#d62728", lw=0.3)
                ax.axvline(k * m - 0.5, color="#d62728", lw=0.3)
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color("#999999")
            sp.set_linewidth(0.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.08, wspace=0.06)
    fig.savefig("../paper/fig-recovery.pdf", metadata={"CreationDate": None, "Creator": None, "Producer": None})
    fig.savefig("../figures/recovery.png", dpi=220, metadata={"Software": None})
    print("wrote paper/fig-recovery.pdf and figures/recovery.png")


if __name__ == "__main__":
    main()
