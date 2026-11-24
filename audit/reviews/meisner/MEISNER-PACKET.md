# Statement packet (revision 1, 2026-11-23): generic rigidity of Meisner's square construction

Claims only; no proof. Try to break them.

## Definitions
Fix a real Hadamard matrix A of order m ≡ 0 mod 4. There are row points i ∈ [m] and column points
j ∈ [m]. A labelling consists of permutations p_i, p'_j of [m] and signs s_i(j), t_j(i):
  F^i_{ej} = s_i(j) A_{e,p_i(j)},  G^j_{ir} = t_j(i) A_{p'_j(i),r},  H_{(i,e),(j,r)} = F^i_{ej} G^j_{ir}.
N = m². General ensemble: all labellings, L = (m! 2^m)^{2m}, uniform. Bush ensemble: A normalized,
p_i(i) = p'_j(j) = 1 (the all-one column/row), s_i(i) = t_j(j) = +1, other choices uniform.
Equivalence = signed row and column permutations; transposes identified when counting classes.
Rigid = signed automorphism group {(I,I), (−I,−I)}. (This is Meisner 1992 Thm 1 with v = 1 /
Craigen 1995 weaving with pattern J_m; see
reviews/four-group/credit-bush.md.)

## Claims
M1. H is Hadamard for every labelling. In the Bush ensemble H is Bush-type (the diagonal m×m tiles are
    J, all other tiles have zero row and column sums), hence regular.
M2. Two labellings give the identical H iff they differ by flipping s_i(j) and t_j(i) together for some
    set of pairs (i,j) (Bush: off-diagonal pairs only). Hence there are exactly D = 2^{m²}(m!)^{2m}
    distinct outputs (Bush: D_B = 2^{m²−m}((m−1)!)^{2m}).
M3. Uniformly in A, with probability 1 − o(1) as m → ∞ (in both ensembles) the row and column point
    fibres are intrinsically recoverable from H by tests invariant under signed equivalence, and H is
    rigid.
M4. The number C of equivalence classes (transposes identified) of rigid outputs satisfies
    log C = N log N − (2 − log 2) N + O(√N log² N), in both ensembles. In particular there are that many
    inequivalent rigid Bush-type (regular) Hadamard matrices at every order N = m² with H(m), m → ∞.
M5. A rigid Hadamard matrix yields only rigid Hadamard designs (2-(N−1, N/2−1, N/4−1) after normalizing
    at any row and column). Inequivalent matrices yield non-isomorphic designs. So M4 gives
    N^{(1+o(1))N} pairwise non-isomorphic rigid Hadamard designs at these orders. Compare Merchant,
    J. Algebraic Combin. 24 (2006) Thm 5.2: at least (16n−2)!/(2^{10} n³) rigid Hadamard designs of
    order 8n, i.e. about (N/2)! at matrix order N = 32n. The claim is that M4/M5 double the exponent
    at the common orders (squares divisible by 32).

## Allowed sources
reviews/four-group/REGULAR-RIGIDITY.md (an
analogous, already audited proof for a different construction: you may read it), credit-bush.md,
PRIOR-ART-CONCLUSION.md (internal working file; not released) (Merchant
statement). Do NOT open MEISNER-RIGIDITY.md, RESULT.md or other files in four-group-gauge-2026-11-23/
except this packet, PRIOR-ART-CONCLUSION.md and your own output file.
