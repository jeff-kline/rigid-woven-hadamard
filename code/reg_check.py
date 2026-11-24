import runpy, numpy as np
g = runpy.run_path('geom_check.py')
pts, fl_at, lab, output, apply_flip, pi, pt, A, h, nL = [g[k] for k in ['pts','fl_at','lab','output','apply_flip','pi','pt','A','h','nL']]
d = [-1, 1, 1, 1]
def regularize(lab):
    H = output(lab)
    cs = np.zeros(64, dtype=int)
    for k, p in enumerate(pts):
        i = p[0]
        perm, sg = lab[('c', p)]
        for m, flag in enumerate(fl_at[p]):
            if pi[flag % nL] == flag % nL:
                cs[k*h:(k+1)*h] = d[i] * sg[m] * A[:, perm[m]]
    Hc = H * cs[None, :]
    rs = Hc.sum(1)
    assert (np.abs(rs) == 2*h).all()
    R = Hc * np.sign(rs)[:, None]
    assert (R.sum(1) == 2*h).all() and (R.sum(0) == 2*h).all()
    return R
R = regularize(lab)
Lf = next(L for L in range(nL) if pi[L] == L)
cf = set(i*nL + Lf for i in range(4))
print("fixed-line gauge leaves regularized R identical:", (regularize(apply_flip(lab, cf, cf)) == R).all())
p0 = pts[5]
allp = set(fl_at[p0])
lab2 = {k: (list(v[0]), list(v[1])) for k, v in lab.items()}
lab2[('r', p0)] = (lab2[('r', p0)][0], [-s for s in lab2[('r', p0)][1]])
print("pointwise row flip: H identical:", (output(lab2) == output(lab)).all(), " R identical:", (regularize(lab2) == R).all())
