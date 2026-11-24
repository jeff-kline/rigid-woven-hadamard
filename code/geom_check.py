import numpy as np, itertools, random

# F4: elements 0,1,2(=w),3(=w^2); add = xor
def f4mul(a, b):
    if a == 0 or b == 0: return 0
    la = {1: 0, 2: 1, 3: 2}[a]; lb = {1: 0, 2: 1, 3: 2}[b]
    return {0: 1, 1: 2, 2: 3}[(la + lb) % 3]

def field(q):
    if q == 4:
        return (lambda a, b: a ^ b), f4mul
    return (lambda a, b: (a + b) % q), (lambda a, b: (a * b) % q)

def geometry(q, dirs):
    add, mul = field(q)
    lines = [(a, b) for a in range(q) for b in range(q)]
    idx = {L: k for k, L in enumerate(lines)}
    def ell(d, L):
        a, b = L
        return b if d == 'inf' else add(a, mul(d, b))
    pi = [idx[(b, a)] for (a, b) in lines]
    pt = [[ell(d, L) for L in lines] for d in dirs]  # pt[i][L]
    return lines, pi, pt

def check(q, dirs):
    lines, pi, pt = geometry(q, dirs)
    h = q; nL = h * h
    # external joins unique
    for i in range(4):
        for j in range(4):
            if i == j: continue
            pairs = set((pt[i][L], pt[j][L]) for L in range(nL))
            assert len(pairs) == nL
    # ordered pair property
    for i in range(4):
        pairs = set((pt[i][L], pt[i][pi[L]]) for L in range(nL))
        assert len(pairs) == nL, ('ordered pair fails', i)
    assert all(pi[pi[L]] == L for L in range(nL))
    K = np.array([[0, 1, 1, 1], [-1, 0, 1, -1], [-1, -1, 0, 1], [-1, 1, -1, 0]])
    nF = 4 * nL
    f = lambda i, L: i * nL + L
    M = np.zeros((nF, nF), dtype=int)
    for i in range(4):
        for L in range(nL):
            for j in range(4):
                M[f(i, L), f(j, L)] += h * K[i, j]
            M[f(i, L), f(i, pi[L])] += h
    assert (M @ M.T == 4 * h * h * np.eye(nF, dtype=int)).all()
    # components of bipartite support graph
    parent = list(range(2 * nF))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for r in range(nF):
        for c in range(nF):
            if M[r, c] != 0:
                parent[find(r)] = find(nF + c)
    comps = len(set(find(x) for x in range(2 * nF)))
    fixed = sum(1 for L in range(nL) if pi[L] == L)
    print(f"q={q}: fixed lines={fixed}, components={comps}, (h^2+h)/2={(h*h+h)//2}")
    return lines, pi, pt, M, K

lines, pi, pt, M, K = check(4, ['inf', 0, 2, 3])
check(5, ['inf', 0, 2, 3])

# Build outputs at h=4
h = 4; nL = 16; nF = 64
A = np.array([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])
A = A[:, [0, 2, 1, 3]] * np.array([1, -1, 1, 1])  # any Hadamard, not symmetric
# points: (i, value); flags at point
fl_at = {}
for i in range(4):
    for L in range(nL):
        fl_at.setdefault((i, pt[i][L]), []).append(i * nL + L)
pts = sorted(fl_at)

def rand_lab(rng):
    lab = {}
    for side in 'rc':
        for p in pts:
            perm = list(range(h)); rng.shuffle(perm)
            sg = [rng.choice([1, -1]) for _ in range(h)]
            lab[(side, p)] = (perm, sg)
    return lab

def output(lab):
    Fh = np.zeros((nF, nF), dtype=int); Gh = np.zeros((nF, nF), dtype=int)
    for pi_, p in enumerate(pts):
        for side, Mat, B in (('r', Fh, A.T), ('c', Gh, A)):
            perm, sg = lab[(side, p)]
            for k, flag in enumerate(fl_at[p]):
                Mat[pi_ * h:(pi_ + 1) * h, flag] = sg[k] * B[:, perm[k]]
    Hm = Fh @ M @ Gh.T
    assert (Hm % h == 0).all()
    return Hm // h

rng = random.Random(1)
lab = rand_lab(rng)
H = output(lab)
assert (np.abs(H) == 1).all() and (H @ H.T == 64 * np.eye(64, dtype=int)).all()
print("h=4 output is Hadamard of order 64")

# all point-pair tiles nonzero
nz = all(np.any(H[a*h:(a+1)*h, b*h:(b+1)*h] != 0) for a in range(16) for b in range(16))
print("all tiles nonzero (trivially, entries +-1):", nz)

# gauge: flip one non-fixed component and one fixed component
def comp_flags(L):
    s = {L, pi[L]}
    return [i * nL + Lx for i in range(4) for Lx in s]
def apply_flip(lab, flagset_r, flagset_c):
    new = {k: (list(v[0]), list(v[1])) for k, v in lab.items()}
    for side, fs in (('r', flagset_r), ('c', flagset_c)):
        for p in pts:
            for k, flag in enumerate(fl_at[p]):
                if flag in fs:
                    new[(side, p)][1][k] *= -1
    return new
Lnf = next(L for L in range(nL) if pi[L] != L)
Lf = next(L for L in range(nL) if pi[L] == L)
for L in (Lnf, Lf):
    cf = set(comp_flags(L))
    H2 = output(apply_flip(lab, cf, cf))
    print("gauge on component of line", L, "fixed" if pi[L] == L else "paired", "identical:", (H2 == H).all())
    H3 = output(apply_flip(lab, cf, set()))
    print("  row-side-only flip identical:", (H3 == H).all())
