"""Meisner square construction (v = 1, order N = m^2) counted on the same signed terms as the four-group bound.
Unsigned deduction (credit-bush.md):  ((m-1)!)^(2m) / (2 N^m (m!)^2 a_m^(2m)),  finite a_m = 4 (m)_3 ((m/4)!)^4.
Signed version: labellings gain 2^(2 m^2) port signs; each tile is its own gauge component (gauge 2^(m^2));
per-point signed frames |Stab| <= 2m * a_m (kernel <= 2m sign words, REGULAR-RIGIDITY.md).
  C_M >= ((m-1)!)^(2m) 2^(m^2) / (2 N^m (m!)^2 (2m a_m)^(2m)).
Also: distinct outputs D_M = ((m-1)!)^(2m) 2^(m^2) versus four-group D = (2^h h!)^(8h) / 2^((h^2+h)/2)."""
from math import factorial as f, log10
m, h = 40, 20
N = m * m
a_m = 4 * m * (m - 1) * (m - 2) * f(m // 4) ** 4
unsigned = f(m - 1) ** (2 * m) // (2 * N ** m * f(m) ** 2 * a_m ** (2 * m))
signed = (f(m - 1) ** (2 * m) * 2 ** (m * m)) // (2 * N ** m * f(m) ** 2 * (2 * m * a_m) ** (2 * m))
DM = f(m - 1) ** (2 * m) * 2 ** (m * m)
D4 = (2 ** h * f(h)) ** (8 * h) // 2 ** ((h * h + h) // 2)
print("Meisner unsigned lower bound digits:", len(str(unsigned)))
print("Meisner signed lower bound digits:  ", len(str(signed)))
print("distinct outputs: Meisner 10^%d, four-group 10^%d" % (len(str(DM)) - 1, len(str(D4)) - 1))
