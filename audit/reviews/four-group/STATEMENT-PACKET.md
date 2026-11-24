# Statement packet (revision 1, 2026-11-23): gauge-exact class count for the four-group construction

You receive claims only; no proof. Try to break them.

## Definitions
Read CONSTRUCTIONS.md in the four-group working folder (its released files are in `audit/reviews/four-group/`),
section "A line involution supplies the repair using ordinary Hadamard bases": four groups of h points,
h² lines, line involution π with the ordered-pair property, flags (i,L), M = h(K⊗I + I⊗Π) with the
fixed skew conference K of order 4, output H = F̂ M Ĝᵀ after local basis changes at every point.

Labelling (as in `REGULAR-RIGIDITY.md` in the same folder): fix one real Hadamard A of order h. On each
of the 4h row points use Aᵀ and on each of the 4h column points use A, after a port permutation (a
bijection from the h incident flags to the basis columns) and port signs (a sign on each basis column).
L = (2^h h!)^{8h} signed labellings; N = 4h². "Good" = the intrinsic fibre-recovery procedure of
REGULAR-RIGIDITY.md / FINITE-1600.md succeeds. Equivalence = signed row and column permutations;
"transposes identified" = H ~ Hᵀ also counted as the same class.

Gauge 𝒢: the bipartite graph B on row flags and column flags with an edge where M ≠ 0; a gauge
element is a sign per connected component of B, multiplied into the port signs of every flag of that
component, on both sides.

## Claims
1. B has exactly (h² + h)/2 connected components, namely the π-orbits of lines.
2. (Fibres.) Two signed labellings produce the identical matrix iff they differ by a gauge element.
   Hence the number of distinct output matrices is exactly D = (2^h h!)^{8h} / 2^{(h²+h)/2}.
3. (Upper multiplicity.) For a good labelling λ, the number of good labellings whose outputs are
   signed-equivalent (side-preserving) to H(λ) is at most ((4h)!)² · |Stab_A|^{4h} · |Stab_{Aᵀ}|^{4h} · 2^{(h²+h)/2},
   where Stab_B = {signed permutations U : UB = BΣ for some signed permutation Σ}.
4. (Lower multiplicity.) Every equivalence class that meets the image contains at least 2^{8h−1}
   distinct output matrices.
5. Consequently (1 − o(1)) D / (2((4h)!)² (2h·a)^{8h}) ≤ C_rigid ≤ C ≤ 2D / 2^{8h}, with a = (2h)^r,
   r = ⌈2 log₂ h⌉ + 2, and log C = N log N − (2 + (log 2)/8) N + O(√N log² N).
6. (Order 1600, h = 20, local Paley basis, product geometry over F₄ × F₅.) There are more than 10^{1514}
   rigid classes, transposes identified, using |Stab| ≤ 2·a₂₀ with a₂₀ = 4·(20·19·18)·(5!)^4 and the
   good fraction > 1/2 from FINITE-1600.md.
7. (Meisner comparison, `credit-bush.md` in the same folder, square construction v = 1, m = 40.) On
   signed terms Meisner's construction yields exactly ((m−1)!)^{2m} 2^{m²} distinct matrices and more
   than 10^{1280} classes. Asymptotically its log class count is N log N − (2 − log 2)N + O(√N log² N),
   larger than the four-group count at second order.

## Allowed dependencies (already audited; you may rely on or check them)
In the four-group working folder (its released files are in `audit/reviews/four-group/`): CONSTRUCTIONS.md,
REGULAR-RIGIDITY.md, FINITE-1600.md, recovery-cold-audit.md, count-cold-audit.md, credit-bush.md.
Do NOT open anything in the gauge working folder (not released) except
this packet and your own output file.
