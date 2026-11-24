"""Small exact checks for the Meisner rigidity audit (single core, bounded)."""
import itertools, math, random
import numpy as np

rng = random.Random(20261123)

def sylvester(k):
    H = np.array([[1]])
    for _ in range(k):
        H = np.block([[H, H], [H, -H]])
    return H

def paley1(q):  # q prime, q % 4 == 3 -> order q+1
    sq = {(x * x) % q for x in range(1, q)}
    chi = lambda x: 0 if x % q == 0 else (1 if x % q in sq else -1)
    Q = np.array([[chi(j - i) for j in range(q)] for i in range(q)])
    S = np.zeros((q + 1, q + 1), dtype=int)
    S[0, 1:] = 1; S[1:, 0] = -1; S[1:, 1:] = Q
    H = np.eye(q + 1, dtype=int) + S
    return H

def normalize(A):
    A = A * A[:, [0]]          # first column -> +1
    A = A * A[[0], :]          # first row -> +1
    return A

def is_hadamard(H):
    n = H.shape[0]
    return np.array_equal(H @ H.T, n * np.eye(n, dtype=int))

def build(A, lab):
    m = A.shape[0]
    p, s, pp, t = lab
    F = [np.array([[s[i][j] * A[e, p[i][j]] for j in range(m)] for e in range(m)]) for i in range(m)]
    G = [np.array([[t[j][i] * A[pp[j][i], r] for r in range(m)] for i in range(m)]) for j in range(m)]
    H = np.zeros((m * m, m * m), dtype=int)
    for i in range(m):
        for j in range(m):
            H[i*m:(i+1)*m, j*m:(j+1)*m] = np.outer(F[i][:, j], G[j][i, :])
    return H, F, G

def random_lab(m, bush):
    p, s, pp, t = [], [], [], []
    for i in range(m):
        if bush:
            rest = list(range(1, m)); rng.shuffle(rest)
            perm = rest[:i] + [0] + rest[i:]
            sg = [rng.choice([1, -1]) for _ in range(m)]; sg[i] = 1
        else:
            perm = list(range(m)); rng.shuffle(perm)
            sg = [rng.choice([1, -1]) for _ in range(m)]
        p.append(perm); s.append(sg)
    for j in range(m):
        if bush:
            rest = list(range(1, m)); rng.shuffle(rest)
            perm = rest[:j] + [0] + rest[j:]
            sg = [rng.choice([1, -1]) for _ in range(m)]; sg[j] = 1
        else:
            perm = list(range(m)); rng.shuffle(perm)
            sg = [rng.choice([1, -1]) for _ in range(m)]
        pp.append(perm); t.append(sg)
    return p, s, pp, t

def quartic(A, rows):
    return int(np.prod(A[list(rows), :], axis=0).sum())

print("== 1. Construction, Bush, gauge, in-fibre quartet, true-pair divisibility ==")
for name, A0 in [("Sylvester8", sylvester(3)), ("Paley12", paley1(11)), ("Paley20", paley1(19))]:
    A = normalize(A0); m = A.shape[0]; N = m * m
    assert is_hadamard(A)
    for bush in (False, True):
        lab = random_lab(m, bush)
        H, F, G = build(A, lab)
        ok_h = is_hadamard(H)
        msg = f"{name} bush={bush}: Hadamard={ok_h}"
        if bush:
            diagJ = all((H[i*m:(i+1)*m, i*m:(i+1)*m] == 1).all() for i in range(m))
            offz = all((H[i*m:(i+1)*m, j*m:(j+1)*m].sum(0) == 0).all() and (H[i*m:(i+1)*m, j*m:(j+1)*m].sum(1) == 0).all()
                       for i in range(m) for j in range(m) if i != j)
            msg += f" diagJ={diagJ} offdiag-zero-margins={offz} rowsum={set(H.sum(1))}"
        # gauge flip on a (non-diagonal) pair
        p, s, pp, t = lab
        s2 = [row[:] for row in s]; t2 = [row[:] for row in t]
        s2[0][1] *= -1; t2[1][0] *= -1
        H2, _, _ = build(A, (p, s2, pp, t2))
        s3 = [row[:] for row in s]; s3[0][1] *= -1
        H3, _, _ = build(A, (p, s3, pp, t))
        msg += f" gauge-invariant={np.array_equal(H, H2)} single-flip-changes={not np.array_equal(H, H3)}"
        # in-fibre quartet = m*D
        bad = 0
        for _ in range(30):
            i = rng.randrange(m); xs = rng.sample(range(m), 4)
            tot = int(np.prod(H[[i*m + x for x in xs], :], axis=0).sum())
            if tot != m * quartic(A, xs): bad += 1
        # true pair divisibility
        badd = 0
        for _ in range(200):
            i = rng.randrange(m); e, e2 = rng.sample(range(m), 2)
            others = [r for r in range(N) if r not in (i*m+e, i*m+e2)]
            u, v = rng.sample(others, 2)
            tot = int(np.prod(H[[i*m+e, i*m+e2, u, v], :], axis=0).sum())
            if tot % m: badd += 1
        msg += f" infibre-mismatch={bad} truepair-nondiv={badd}"
        print(msg)

print("\n== 2. Quartic sums D of distinct row quartets; case A/B ==")
for name, A0 in [("Sylvester8", sylvester(3)), ("Sylvester16", sylvester(4)), ("Paley12", paley1(11)), ("Paley20", paley1(19)), ("Paley28", paley1(27 if False else 23) if False else None)]:
    if A0 is None: continue
    A = normalize(A0); m = A.shape[0]
    vals = set()
    for q in itertools.combinations(range(m), 4):
        vals.add(quartic(A, q))
    caseA = max(abs(v) for v in vals) >= m / 2
    print(f"{name}: row-quartet D values {sorted(vals)}; case {'A' if caseA else 'B'}")

print("\n== 3. Case-B no-isolated-vertex with one excluded row (Bush y-exclusion) ==")
def isolated_check(A):
    m = A.shape[0]
    worst = 0; fails = 0; total = 0
    for al, be in itertools.permutations(range(m), 2):
        for excl in range(m):
            if excl in (al, be): continue
            verts = [c for c in range(m) if c not in (al, be, excl)]
            for c in verts:
                total += 1
                if not any(quartic(A, (al, be, c, d)) != 0 for d in verts if d != c):
                    fails += 1
    return fails, total
for name, A0 in [("Paley12", paley1(11)), ("Paley20", paley1(19)), ("Sylvester8 (case A, contrast)", sylvester(3))]:
    A = normalize(A0)
    f, tot = isolated_check(A)
    print(f"{name}: isolated-vertex instances {f} / {tot}")
# Parseval: under case B each coefficient^2 < m^2/4, sum = m^2 => at least 5 nonzero coefficients outside the triple.
A = normalize(paley1(19)); m = 20
mn = min(sum(1 for d in range(m) if d not in (a, b, c) and quartic(A, (a, b, c, d)) != 0)
         for a, b, c in itertools.combinations(range(m), 3))
print(f"Paley20: min number of rows d with D_abcd != 0 over all triples: {mn}")

print("\n== 4. Kernel word sets K_A = {w : A diag(w) A^-1 signed perm} ==")
def kernel(A):
    m = A.shape[0]; ks = []
    for y in range(m):
        for sg in (1, -1):
            w = sg * A[0] * A[y]
            M = A @ np.diag(w) @ A.T  # = m * A diag(w) A^-1
            if (np.abs(M) == m).sum(1).tolist() == [1] * m and ((np.abs(M) == m) | (M == 0)).all():
                ks.append(tuple(w))
    return ks
for name, A0 in [("Sylvester8", sylvester(3)), ("Sylvester16", sylvester(4)), ("Paley12", paley1(11)), ("Paley20", paley1(19))]:
    A = normalize(A0)
    print(f"{name}: |K_A| = {len(kernel(A))} (bound 2m = {2*A.shape[0]})")

print("\n== 5. Column-list collision probability and Step-1/2 exponents ==")
for m in (8, 12, 40):
    # exact P(w(p(j)) == w(p(j'))) for a balanced word under a uniform permutation
    pr = 2 * (m // 2) * (m // 2 - 1) / (m * (m - 1))
    print(f"m={m}: P(equal)={pr:.6f}  (m-2)/(2(m-1))={(m-2)/(2*(m-1)):.6f}")
H14 = -(0.25 * math.log2(0.25) + 0.75 * math.log2(0.75))
print(f"H(1/4) = {H14:.6f}; 1-H(1/4) = {1-H14:.6f}")
for m in (64, 256, 1024, 4096):
    s1 = 8 * m**4 * (m + 1) * 2 ** ((H14 - 1) * m)
    s2_log2 = m * math.log2(2*m) + 0.25*m*(math.log2(2*m*(m+1)) - m)
    case_b = math.log2(m**4) - (m - 3) / 2
    mixed = math.log2(2) + 8*math.log2(m) + math.log2(m+1) - (m/8)/math.log(2)
    print(f"m={m}: Step1 bound {s1:.3e}; log2 Step2 bound {s2_log2:.1f}; log2 caseB union {case_b:.1f}; log2 mixed-quartet union {mixed:.1f}")

print("\n== 6. Stirling: residual of log D - (N log N - (2 - log2) N), scaled by sqrt(N) log N ==")
for m in (8, 40, 400, 4000, 40000):
    N = m * m
    logD = N * math.log(2) + 2 * m * math.lgamma(m + 1)
    logDB = (N - m) * math.log(2) + 2 * m * math.lgamma(m)
    main = N * math.log(N) - (2 - math.log(2)) * N
    sc = math.sqrt(N) * math.log(N)
    r = 2*m*math.log(2*m)/math.log(2) + 2  # r = ceil(2 log2 m)+2, use real upper bound for loss
    rr = math.ceil(2*math.log2(m)) + 2
    loss = math.log(2) + 2*math.lgamma(m+1) + 2*m*rr*math.log(2*m)
    print(f"m={m}: (logD-main)/sqrtN logN = {(logD-main)/sc:.4f}; (logD_B-main)/sqrtN logN = {(logDB-main)/sc:.4f}; "
          f"lower-bound loss/(sqrtN log^2 N) = {loss/(math.sqrt(N)*math.log(N)**2):.4f}")

print("\n== 7. Moved-point ratio 2m*sqrt(a/(m-1)!) with a=(2m)^r ==")
for m in (64, 128, 256, 512, 1024):
    rr = math.ceil(2*math.log2(m)) + 2
    lr = math.log(2*m) + 0.5*(rr*math.log(2*m) - math.lgamma(m))
    print(f"m={m}: log ratio = {lr:.1f}")
