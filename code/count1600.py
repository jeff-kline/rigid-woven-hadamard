"""Exact integer evaluation of the gauge-sharpened class bound at h = 20 (order 1600).
  L      = (2^h h!)^(8h)                      signed labellings
  gauge  = 2^((h^2+h)/2)                      identical-output fibre size (proved: fibres are gauge orbits)
  mult   <= ((4h)!)^2 * (2 a_h)^(8h) * gauge   good labellings per class (|Stab| <= 2 a_h at h = 20: kernel is +-I)
  C      >= (good fraction > 1/2) * L / (2 * mult)   transposes identified
a_h = 4 (h)_3 ((h/4)!)^4 as in FINITE-1600.md. Previous bound for comparison: (20!)^160 / (4 (80!)^2 a^160)."""
from math import factorial as f
h = 20
a = 4 * h * (h - 1) * (h - 2) * f(h // 4) ** 4
assert a == 5673369600000
L = (2 ** h * f(h)) ** (8 * h)
gauge = 2 ** ((h * h + h) // 2)
mult = f(4 * h) ** 2 * (2 * a) ** (8 * h) * gauge
new = L // (4 * mult)                 # 1/2 good fraction and 1/2 for transposes
old = f(h) ** (8 * h) // (4 * f(4 * h) ** 2 * a ** (8 * h))
D = L // gauge
print("distinct outputs D: 10^%d" % (len(str(D)) - 1))
print("new class lower bound: %d digits (leading %s)" % (len(str(new)), str(new)[:12]))
print("old class lower bound: %d digits" % len(str(old)))
