"""Sanity check (no search) of the gauge lemma for the four-group construction at h = 4 (order 64).
Geometry: lines (a,b) in F_4^2, groups given by forms a, b, a+wb, a+w^2 b, involution (a,b)->(b,a).
M = h(K (x) I + I (x) Pi) on flags (i,L). Local basis A = Sylvester H4 at every point, labelled by
random port permutations and signs. Checks:
  1. H is a +-1 matrix with H H^T = 64 I.
  2. The bipartite flag graph of M has (h^2+h)/2 components.
  3. Flipping port signs by a random nontrivial gauge (constant on components, both sides) leaves H identical.
  4. Flipping one port sign (not a gauge) changes H.
  5. Two labellings giving the same H differ by a gauge: reconstruct port permutations and signs from
     the tiles of H and compare (identical-output fibres are gauge orbits).
"""
import itertools, random
import numpy as np

random.seed(1)
h = 4
LOG = {1: 0, 2: 1, 3: 2}; EXP = [1, 2, 3]
def mul(x, y): return 0 if x == 0 or y == 0 else EXP[(LOG[x] + LOG[y]) % 3]
dirs = [(1, 0), (0, 1), (1, 2), (1, 3)]
lines = [(a, b) for a in range(4) for b in range(4)]
lidx = {L: n for n, L in enumerate(lines)}
pi = [lidx[(b, a)] for (a, b) in lines]
ell = lambda i, n: mul(dirs[i][0], lines[n][0]) ^ mul(dirs[i][1], lines[n][1])
K = np.array([[0, 1, 1, 1], [-1, 0, 1, -1], [-1, -1, 0, 1], [-1, 1, -1, 0]])
nL = h * h
flags = [(i, n) for i in range(4) for n in range(nL)]
fidx = {f: k for k, f in enumerate(flags)}
Nf = len(flags)
M = np.zeros((Nf, Nf), dtype=int)
for i in range(4):
    for n in range(nL):
        for j in range(4):
            if K[i, j]: M[fidx[(i, n)], fidx[(j, n)]] += h * K[i, j]
        M[fidx[(i, n)], fidx[(i, pi[n])]] += h
assert np.array_equal(M @ M.T, 4 * h * h * np.eye(Nf, dtype=int))
points = [(i, c) for i in range(4) for c in range(4)]
ports = {x: [fidx[(x[0], n)] for n in range(nL) if ell(x[0], n) == x[1]] for x in points}
assert all(len(p) == h for p in ports.values())
A = np.array([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])

def rand_label():
    return {x: (random.sample(range(h), h), [random.choice((1, -1)) for _ in range(h)]) for x in points}

def build(rowlab, collab):
    """Fhat[(x,r), flag] = A^T[r, perm[p]] * sign[p] / sqrt(h) for flag = ports[x][p]; output order 64."""
    def basis(lab, B):
        Fh = np.zeros((Nf, Nf))
        for xi, x in enumerate(points):
            perm, sg = lab[x]
            for p, f in enumerate(ports[x]):
                Fh[xi * h:(xi + 1) * h, f] = B[:, perm[p]] * sg[p]
        return Fh / np.sqrt(h)
    H = basis(rowlab, A.T) @ M @ basis(collab, A).T
    Hi = np.rint(H).astype(int)
    assert np.allclose(H, Hi)
    return Hi

R, C = rand_label(), rand_label()
H = build(R, C)
ok1 = set(np.unique(H)) == {-1, 1} and np.array_equal(H @ H.T, 64 * np.eye(64, dtype=int))
# components of bipartite flag graph (row flag u ~ column flag v iff M[u,v] != 0)
parent = list(range(2 * Nf))
def find(a):
    while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
    return a
for u, v in zip(*np.nonzero(M)):
    parent[find(u)] = find(Nf + v)
comp = [find(a) for a in range(2 * Nf)]
ncomp = len(set(comp))
ok2 = ncomp == (h * h + h) // 2
# random nontrivial gauge
cs = {c: random.choice((1, -1)) for c in set(comp)}
while all(v == 1 for v in cs.values()) or all(v == -1 for v in cs.values()):
    cs = {c: random.choice((1, -1)) for c in set(comp)}
def apply(lab, off):
    out = {}
    for x in points:
        perm, sg = lab[x]
        out[x] = (perm, [sg[p] * cs[comp[off + f]] for p, f in enumerate(ports[x])])
    return out
ok3 = np.array_equal(build(apply(R, 0), apply(C, Nf)), H)
R2 = {x: (list(v[0]), list(v[1])) for x, v in R.items()}
R2[points[0]][1][0] *= -1
ok4 = not np.array_equal(build(R2, C), H)
# 5: recover (perm, sign) up to gauge from H alone, given geometry: tile (x,y) = eps * (A^T col) (A col)^T
def recover(Hm):
    rp, cp = {}, {}
    for xi, x in enumerate(points):
        for yi, y in enumerate(points):
            T = Hm[xi * h:(xi + 1) * h, yi * h:(yi + 1) * h]
            fr = [f for f in ports[x] for g in ports[y] if M[f, g]]
            gc = [g for f in ports[x] for g in ports[y] if M[f, g]]
            assert len(fr) == 1 and len(gc) == 1
            u = T[:, 0] * T[0, 0]; v = T[0, :] * T[0, 0]      # T = u v^T up to sign
            rp[(x, fr[0])] = next(k for k in range(h) if abs(A.T[:, k] @ u) == h)
            cp[(y, gc[0])] = next(k for k in range(h) if abs(A[:, k] @ v) == h)
    return rp, cp
rp, cp = recover(H)
ok5 = all(rp[(x, f)] == R[x][0][p] for x in points for p, f in enumerate(ports[x])) and \
      all(cp[(y, g)] == C[y][0][p] for y in points for p, g in enumerate(ports[y]))
print(f"1 Hadamard order 64: {ok1}\n2 flag components = {ncomp} (expect {(h*h+h)//2}): {ok2}\n"
      f"3 gauge leaves H identical: {ok3}\n4 single non-gauge port flip changes H: {ok4}\n"
      f"5 port permutations recovered from H alone: {ok5}")
