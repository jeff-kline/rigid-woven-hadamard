from math import factorial as F, log, log10, ceil, log2, comb, lgamma
from fractions import Fraction
# Claim 6
h = 20
a20 = 4*(20*19*18)*F(5)**4
print("a20 =", a20, a20 == 5673369600000)
L = (2**h * F(h))**(8*h)
gauge = 2**((h*h+h)//2)
mult = F(4*h)**2 * (2*a20)**(8*h) * gauge
# good > L/2, transposes identified /2
bound = Fraction(L, 4*mult)
q = bound.numerator // bound.denominator
print("claim6 floor digits:", len(str(q)), "leading:", str(q)[:12], " >10^1514:", q > 10**1514)
# Same with the old FINITE-1600 multiplicity (2^h per point, no gauge): sanity
old = Fraction(F(20)**160, 4*F(80)**2*a20**160)
print("old FINITE-1600 floor digits:", len(str(old.numerator//old.denominator)))
# Claim 7: Meisner m=40
m = 40; N = m*m
nmat = F(m-1)**(2*m) * 2**(m*m)
print("Meisner distinct matrices log10:", round(log10(F(m-1))*2*m + m*m*log10(2), 2))
a40 = 4*(40*39*38)*F(10)**4
r40 = ceil(2*log2(40)) + 2
for label, stab in [("2m*a40 (kernel<=2m words, finite a)", 2*m*a40),
                    ("(2m)^r (full Stab via distinguishing rows)", (2*m)**r40),
                    ("2*a40 (kernel {+-I}; not justified at m=0 mod 8)", 2*a40)]:
    for fib, fl in [("N^m", N**m), ("C(N,m)", comb(N, m))]:
        b = Fraction(nmat, 2*fl*F(m)**2*stab**(2*m))
        qq = b.numerator // b.denominator
        print(f"  Meisner classes >= floor with {label}, {fib}: digits {len(str(qq))}, >10^1280: {qq > 10**1280}")
# Stirling constants
def logD4(h):
    N = 4*h*h
    return 8*h*(h*log(2) + lgamma(h+1)) - (h*h+h)/2*log(2), N
for hh in [10**3, 10**4, 10**5, 10**6]:
    v, N = logD4(hh)
    print("four-group h=%d: (logD - NlogN)/N = %.6f  target %.6f" % (hh, (v - N*log(N))/N, -(2+log(2)/8)))
for mm in [10**3, 10**4, 10**5, 10**6]:
    N = mm*mm
    v = 2*mm*lgamma(mm) + N*log(2)
    print("Meisner m=%d: (log#-NlogN)/N = %.6f  target %.6f" % (mm, (v-N*log(N))/N, -(2-log(2))))

# Added 2026-11-24 for the release: Merchant's Theorem 5.2 at n = 50 (matrix order N = 32n = 1600),
# at least (16n-2)!/(2^10 n^3) rigid designs.
_n = 50
_merchant = F(16 * _n - 2) // (2 ** 10 * _n ** 3)
print("Merchant Thm 5.2 at n=50: floor((16n-2)!/(2^10 n^3)) has", len(str(_merchant)), "digits (> 10^1962)")

# Added 2026-11-24 for the release: the displayed Bush pinned-diagonal floor of the paper,
# C_B >= D_B / (2 N^m (m!)^2 (2m a_m)^{2m}) with D_B = 2^{m^2-m} ((m-1)!)^{2m}, at m = 40.
_m, _N = 40, 1600  # explicit: N is reassigned by the loop above
_a40 = 4 * _m * (_m - 1) * (_m - 2) * F(_m // 4) ** 4  # a_m^proj of the paper
_DB = 2 ** (_m * _m - _m) * F(_m - 1) ** (2 * _m)
_bush = _DB // (2 * _N ** _m * F(_m) ** 2 * (2 * _m * _a40) ** (2 * _m))
print("Bush pinned-diagonal floor at m=40 has", len(str(_bush)), "digits (> 10^1268)")
