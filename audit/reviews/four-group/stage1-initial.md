STAGE: INITIAL

VERDICT:
1. NOT-BROKEN
2. NOT-BROKEN (for the unregularized output H = F̂MĜᵀ as the packet defines it; see the scope note below)
3. NOT-BROKEN
4. NOT-BROKEN
5. NOT-BROKEN
6. NOT-BROKEN
7. NOT-BROKEN (depends on reading the Meisner ensemble as "diagonal all-one port fixed, all port signs free"; see below)

No counterexample or contradiction found.

EVIDENCE:

Claim 1. On a fixed line L, M restricted to its 4 row and 4 column flags is h(K+I), which has no zero entries, so the component is K_{4,4}. On a pair {L, πL}, the K-edges give the bipartite graph K_{4,4} minus a matching on each line, which is connected. The P-edges (i,L)–(i,πL) join the two halves, giving one 16-flag component. Each point lies on exactly one fixed line, and a fixed line has 4 points, so there are h fixed lines. The count is h + (h²−h)/2 = (h²+h)/2.
Computed: at h=4 (F₄; directions ∞,0,ω,ω²) there are 4 fixed lines and 10 components. At h=5 (F₅; ∞,0,2,3) there are 15. At h=20 (the F₄×F₅ product, same group names, simultaneous swap) there are 20 fixed lines and 210 components. External-join uniqueness and the ordered-pair property were asserted and passed in all three geometries. MMᵀ = 4h²I holds at h=4 and h=5.

Claim 2. If H(λ) = H(λ′), then M = U M Vᵀ with U = F̂⁻¹F̂′ and V = Ĝ⁻¹Ĝ′. Because F̂_x = AᵀT_x with T_x a signed permutation, U is block-diagonal by point and each block is a signed permutation of the flags at that point; V is the same. A K-edge (i,L)–(j,L) with i≠j must go to an edge, which forces σ_x(L) = τ_y(L). That line passes through x and through y, which lie in distinct groups, so it equals L. Hence all flag permutations are trivial. The remaining signs satisfy ε_f δ_g = 1 on every edge, so they are constant on components, which is exactly the gauge. Labelling ↦ F̂_x is injective because the columns of A are pairwise non-proportional. The gauge acts freely (any nontrivial element changes some port sign), so D = L/2^{(h²+h)/2} exactly.
Numerical check at h=4 with a random labelling and a nonsymmetric A: the output is Hadamard of order 64. Gauge on a paired component and on a fixed component each leaves H identical. The same flips applied on the row side only change H.

SCOPE NOTE (not a refutation): the regularized representative R does not have these fibres. At h=4, gauge on a fixed-line component changes R, while flipping all port signs at a single row point changes H but leaves R identical (both checked). The regularizing signs use the signed fixed-line column, so they absorb pointwise flips. On regular representatives the fibre is therefore 2^{8h−1} times larger. D and claim 2 are correct only for the unregularized H. The class counts are unaffected.

Claim 3. Suppose λ and λ′ are both good and H(λ′) = P H(λ) Q. Then P and Q map fibres to fibres, giving at most ((4h)!)² point actions. Each tile is rank one, so P_x maps every column of F̂_x to ± a column of F̂′_{x′}. A flag is determined by its set of 4 opposite points, so the flag map is fixed by the point action. Hence P_x Aᵀ = Aᵀ W_x, so P_x ∈ Stab_{Aᵀ}, and Q_yᵀ ∈ Stab_A. With the point action and all P_x, Q_y fixed, the remaining sign choices satisfying (ΠΣ)⁻¹M(Π′Σ′)⁻ᵀ = M form one gauge coset or none. This gives at most ((4h)!)² |Stab_{Aᵀ}|^{4h} |Stab_A|^{4h} 2^{(h²+h)/2} choices of λ′. The bound needs only fibre recovery on both labellings, not rigidity.
The kernel bound is correct. If UB = B·diag(e), then e = ±(row₁ ∘ row_k), which gives at most 2h words, and U = B·diag(e)·B⁻¹ is determined by e.
The 2h factor is redundant. REGULAR-RIGIDITY's distinguishing-row argument already bounds the whole of Stab by (2h)^r: once the r preimages and their signs are specified, UB is determined, and hence U. So (2h·a)^{8h} is conservative, not wrong.

Claim 4. Pointwise flips (negating every port sign at one point) negate a row or column fibre, so they stay in the same class. A pointwise flip that is also a gauge element must satisfy ε_x = δ_y for every ordered point pair with a nonzero tile. Every pair has one: an external pair through its common line (K), and an internal pair through the ordered-pair property (P). So the intersection is {±global}, and claim 2 gives 2^{8h}/2 = 2^{8h−1} distinct outputs per class.

Claim 5. The lower bound follows from claim 3, the (1−o(1)) good-rigid proportion, and a factor 2 for transposes. The upper bound is D/2^{8h−1} by claim 4.
log D = 8h²·log 2 + 8h·log h! − ((h²+h)/2)·log 2. Since 8h·log h! = N log N − 2N log 2 − 2N + O(√N log N), this gives log D = N log N − (2 + log 2/8)N + O(√N log N). The losses log((4h)!)² and 8h·log(2ha) are O(√N log² N).
Numerical: (log D − N log N)/N = −2.08663 at h=10⁶, against the target −2.086643.

Claim 6. a₂₀ = 4·(20·19·18)·(5!)⁴ = 5673369600000 (exact). For h=20 ≡ 4 mod 8 the kernel is {±I}: a nonscalar e gives a fixed-point-free row involution, and two disjoint pairs give a quartet with |D| = h, which the FINITE-1600 quartet argument excludes. So |Stab| ≤ 2a₂₀.
The bound is (2²⁰·20!)¹⁶⁰ / (4·(80!)²·(2a₂₀)¹⁶⁰·2²¹⁰). Its exact floor has 1515 decimal digits and begins 587135898904, so it exceeds 10^1514. As a cross-check, the old FINITE-1600 formula reproduces its 663 digits.

Claim 7. Ensemble: a fixed normalized H(40); the diagonal port is the all-ones column; the other m−1 ports are permuted at each of the 2m point occurrences; all port signs are free. Each tile is its own gauge component, so there are m² components and the tile signs s_ij are exactly free, 2^{m²} of them. Every sign choice stays Hadamard: row orthogonality only uses s_ij² = 1. The map (p, q, s) → matrix is injective because each rank-one tile determines its projective column and row and its sign. So the count is exactly ((m−1)!)^{2m}·2^{m²}.
The class lower bound uses multiplicity ≤ 2·N^m·(m!)²·|Stab|^{2m}. At m=40 ≡ 0 mod 8 the {±I} kernel argument does NOT apply, so one must use 2m·a₄₀ or (2m)^r. Exact floors:
- 2m·a₄₀ with N^m: 1281 digits (> 10^1280, thin margin)
- 2m·a₄₀ with C(N,m): 1329 digits
- (2m)^r with r = 13: 1983 digits
Asymptotically, 2m·log(m−1)! + m²·log 2 = N log N − (2 − log 2)N + O(√N log N). Numerically −1.306865 at m=10⁶, against −1.306853. The multiplicity loss is exp(O(√N log² N)). Since −1.307 > −2.087, Meisner's count is larger at second order, as claimed.
Fragility: if the ensemble instead forces the diagonal tiles to +J (Bush-normalized, diagonal signs not free), there are only 2^{m²−m} distinct matrices. The class count is unchanged, because row-fibre flips normalize s_ii. But the 2m·a₄₀ with N^m route then gives only 1269 digits and would not certify 10^1280. The C(N,m) and (2m)^r routes still would.

COVERAGE:
Tried:
- component structure, including fixed versus paired lines;
- the fibre "only if" direction against symmetries of A (irrelevant, since U is forced block-diagonal), port-permutation coincidences, fixed lines, and regularization (this is where the scope gap is);
- the quantifiers in claims 3 and 4;
- the kernel and Stab usage;
- the Stirling constants;
- the exact 1600 bound;
- Meisner gauge, sign freedom and exact count.
Unchecked:
- what Meisner's printed Theorem 1 actually permits (source not accessible here; I relied on credit-bush.md's reading);
- REGULAR-RIGIDITY's (1−o(1)) recovery and rigidity theorem and FINITE-1600's >70% (taken as audited dependencies);
- the Meisner multiplicity argument at the level of checking every step of credit-bush's fibre-guess (accepted after a sketch check);
- no enumeration of the h=4 stabilizer group was done.

DEPENDENCIES:
Verified here: the geometry properties at h=4, 5 and 20; MMᵀ = 4h²I; a₂₀; the kernel {±I} for h ≡ 4 mod 8 (argument re-derived); the (2h)^r full-Stab bound (argument re-derived).
Relied on, unresolved here: the asymptotic recovery and rigidity proportions (recovery-cold-audit.md, count-cold-audit.md); the good fraction > 1/2 at h=20 (FINITE-1600.md); the Meisner ensemble definition (credit-bush.md).

EXPOSURE:
Read STATEMENT-PACKET.md and, in incidence-order-extensions-2026-11-23/, CONSTRUCTIONS.md, REGULAR-RIGIDITY.md, FINITE-1600.md, credit-bush.md, count-cold-audit.md and recovery-cold-audit.md. No other files in four-group-gauge-2026-11-23/ were opened.
Tools: Python 3 in a virtual environment running scratchpad scripts geom_check.py, reg_check.py, prod_check.py and arith.py (exact integer and Fraction arithmetic).

RESOURCES: under 1 CPU-second in total, single core; wall time about 2 seconds of compute. No sign-space search.

Redacted 2026-11-24 for privacy (local paths and session identifiers only); the sealed hash refers to the unredacted original.
