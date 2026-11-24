import runpy
g = runpy.run_path('geom_check.py')
geometry = g['geometry']
l4, p4, t4 = geometry(4, ['inf', 0, 2, 3])
l5, p5, t5 = geometry(5, ['inf', 0, 2, 3])
lines = [(x, y) for x in range(16) for y in range(25)]
idx = {L: k for k, L in enumerate(lines)}
nL = len(lines); h = 20
pi = [idx[(p4[x], p5[y])] for (x, y) in lines]
pt = [[(t4[i][x], t5[i][y]) for (x, y) in lines] for i in range(4)]
for i in range(4):
    assert len(set(pt[i])) == h
    for j in range(4):
        if i != j: assert len(set(zip(pt[i], pt[j]))) == nL
    assert len(set((pt[i][L], pt[i][pi[L]]) for L in range(nL))) == nL
parent = list(range(2 * 4 * nL))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
f = lambda i, L: i * nL + L
for i in range(4):
    for L in range(nL):
        for j in range(4):
            if j != i: parent[find(f(i, L))] = find(4*nL + f(j, L))
        parent[find(f(i, L))] = find(4*nL + f(i, pi[L]))
comps = len(set(find(x) for x in range(8 * nL)))
print("h=20 product geometry OK; fixed lines:", sum(pi[L] == L for L in range(nL)), "components:", comps, "expected", (h*h+h)//2)
