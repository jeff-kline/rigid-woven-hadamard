# Generic rigidity and exact class counts for Meisner's square (woven) construction

23 November 2026. Theory only. Status: cold-examined 2026-11-23.
- Stage 1, isolated (`audit/meisner-stage1-initial.md`, sha256 6633550d…): no claim REFUTED. M3 was
  UNRESOLVED within its 120 CPU-s budget, nonrigid at m = 4 only.
- Stage 2 (`audit/meisner-stage2-proof-audit.md`, sha256 4ef9163c…): M1–M5 VERIFIED. Errata E1–E4 and
  stage-1 D1–D4 are applied below.
- Prior art on the conclusion: PRIOR-ART-CONCLUSION.md. Nearest is Merchant 2006 (rigid designs).
  Norman 1976, Dempwolff–Kantor 2008 and MathSciNet/zbMATH are not checked.
It reuses REGULAR-RIGIDITY.md (four-group recovery and rigidity) and RESULT.md (gauge and
multiplicity lemmas) almost line by line. Every substitution is stated.

## Construction

Fix a real Hadamard matrix A of order m ≡ 0 mod 4. There are m row points i and m column points j, each
carrying m ports. Port j at row point i faces column point j only, and port i at column point j faces
row point i only. A labelling consists of permutations p_i, p'_j of [m] and signs s_i(j), t_j(i):

  F^i_{e j} = s_i(j) A_{e, p_i(j)}      (columns of F^i = ports j),
  G^j_{i r} = t_j(i) A_{p'_j(i), r}     (rows of G^j = ports i),
  H_{(i,e),(j,r)} = F^i_{ej} G^j_{ir}.

This is Meisner (1992) Thm 1 with v = 1, equivalently Craigen's (1995) weaving with pattern J_m. Tile sign
factors ε_{ij} are absorbed into s and t. **Hadamard.** For rows (i,e) and (i',e') with i ≠ i', each j
contributes Σ_r G^j_{ir}G^j_{i'r} = 0. For i = i' the sum is Σ_j F^i_{ej}F^i_{e'j}·m = m²δ_{ee'}.
N = m², with L = (m! 2^m)^{2m} labellings.

**Bush variant.** Take A normalized. Fix p_i(i) = 1 = p'_j(j) (the all-one column and row) and
s_i(i) = t_j(j) = +1. Then tile (i,i) = J_m. Every other tile is (balanced column)·(balanced row)ᵀ, with
zero row and column sums. So H is Bush-type and regular with row sum m. There are
L_B = ((m−1)! 2^{m−1})^{2m} labellings. Everything below holds for both ensembles; the Bush variant only
changes constants (one fewer free port per point).

In the rank-one-tile framework this is the case k = 1: the basis-changed matrix W = F̂ᵀHĜ is a signed
permutation on flags, with row flag (i,j) matched to column flag (j,i).

## Gauge and exact distinct-output count

The flag graph is the perfect matching (i,j) ↔ (j,i), so every tile is one gauge component. Flipping
s_i(j) and t_j(i) together leaves H identical. The proof of Lemma 1 in RESULT.md applies verbatim: tiles
are rank-one ±1, every port lies in exactly one tile, and the columns and rows of A are projectively
distinct. So identical outputs differ exactly by the gauge, and

  D = 2^{m²} (m!)^{2m},   D_B = 2^{m² − m} ((m−1)!)^{2m}.

## Fibre recovery (transcription of REGULAR-RIGIDITY.md "Recovery, uniformly in the local basis")

Geometry substitutions:
- Two rows from one row point have an entrywise product constant on every column fibre:
  F^i_{ej}F^i_{e'j}(G^j_{ir})² is independent of r.
- Two rows from distinct row points i ≠ i' have product (sign)·(G^j_{i·} ∘ G^j_{i'·}) on column fibre j.
  This is nonconstant at **every** j, so all m column points separate them (the four-group case had at
  least h − 1 probe points). The same holds symmetrically for columns.

Physical rows of fibre i are rows of A (column-permuted and signed). Physical columns of fibre j are
columns of A. Run the dichotomy separately on the rows of A (for the row side) and the columns of A.

**A. Some four distinct rows x₁..x₄ of A have |D| ≥ m/2**, where D = Σ_k Π A_{x_l k}.
- In-fibre quartet (i, x₁..x₄): its global sum is Σ_j Π_l A_{x_l p_i(j)} · Σ_r (G^j_{ir})⁴ = m·D. So it
  reaches N/2 deterministically.
- Mixed quartet with a point of odd multiplicity: the fair signs s_i(·) enter to the first power. The sum
  is Σ_j s_i(j)c_j with |c_j| ≤ m, so P(|sum| ≥ m²/2) ≤ 2e^{−m/8} (Hoeffding).
- 2+2 quartet (points i, k): the port signs cancel (each appears squared). The sum is m·Σ_j u(j)v(j),
  with u = (A_x∘A_{x'})∘p_i depending only on p_i and v only on p_k, so u and v are independent and u
  is uniform over balanced words. The tail comes from the random permutation, not from signs:
  P(|Σ uv| ≥ m/2) ≤ (m+1)·2e^{−m/8}, conditioning a fair-sign word on balance. A direct hypergeometric
  Hoeffding bound gives 2e^{−m/16} too.
- Union over at most N⁴ = m⁸ quartets: o(1).
- Column lists: true column mates (j,r), (j,r') have identical lists, since F^i_{xj}F^i_{x'j} does not
  depend on r. For j ≠ j', at each of the m independent row points the word u_i takes equal values at j
  and j' with probability (m−2)/(2(m−1)) < 1/2, so a missed separation has probability ≤ C(m,2)2^{−m}.

**B. All four distinct rows of A have |D| < m/2.**
- Divisibility test: relate two rows if every extension by two other distinct rows has a four-row sum
  divisible by m.
- True pairs pass: each j-term is ±Σ_r G^j_{kr}G^j_{lr} ∈ {0, ±m}.
- False pair (i,e), (i',e'): take any column point y. Its ports a = i and b = i' are distinct. For each
  other port c ∉ {a, b, y}, take any fixed row from row point c (the exclusion of y matters only in the
  Bush variant).
- Expose everything except the signs t_y(c). The four-row sum is K_cd + σ_cd·D'_{abcd}·t_y(c)t_y(d),
  where D' is the four-row correlation of the rows of A in G^y's labelling.
- The edge graph {cd : D' ≠ 0} has no isolated vertex, and 0 < |2D'| < m. This needs case B; the source's
  bare orthogonality argument is not enough here, because port y is excluded from the auxiliary set
  (Sylvester-8 has isolated vertices under that exclusion: 336 of 1680, outside case B). *Repair
  (stage-2 audit E1, Parseval):* for fixed c, the coefficients of A_a∘A_b∘A_c on the rows of A
  square-sum to m², and each is below m/2 in case B. So at least five rows carry nonzero coefficients;
  removing a, b, c and the excluded y leaves at least one.
  A spanning forest has at least (m−3)/2 independent edge constraints, so a false pair passes with
  probability ≤ 2^{−(m−3)/2}. Union over C(N,2) pairs: o(1).

Recovering one side determines the other, and the decoder picks its branch from the output, exactly as in
the source. **Branch rule (stage-1 D1):** use branch A whenever some quartet reaches the threshold N/2.
This is essential. For Sylvester-type A every four-row sum of H is divisible by m, so the divisibility
test of branch B is blind there; but such A have closed quartets (|D| = m) and always take branch A.

Bush-ensemble constants (stage-2 E2): with the diagonal fixed, the odd-multiplicity bound becomes
2e^{3/8}e^{−m/8}, the 2+2 bound O(m)e^{−m/8+O(1)}, and Steps 1–2 below gain a factor 2. All remain o(1). **Conclusion:** uniformly in A, both fibre partitions are intrinsically recoverable with
probability 1 − o(1). The tests are invariant under signed equivalence.

## Rigidity

Let (U,V) be a side-preserving signed automorphism of a recoverable output. It induces point permutations
α (row points) and β (column points). Tile (i,j) goes to tile (αi, βj), so the port map at row point i
is j ↦ βj, and at column point j it is i ↦ αi.

**Moved points.**
- U_i F^i = F^{αi} Π_β D for some signs D. Here U_i ∈ Stab_A = {signed permutations U : UA = AΣ}, and
  |Stab_A| ≤ a = (2m)^r with r = ⌈2 log₂ m⌉ + 2 (REGULAR-RIGIDITY.md: r distinguishing coordinates
  determine U).
- Given F^i, β and U_i, the labelling at αi is fixed up to its port signs. Its probability is therefore
  at most a/m! (Bush: a/(m−1)!). The column side is symmetric with α as the port map: there
  V_j ∈ Stab_{Aᵀ}, with the same (2m)^r bound (stage-2 E3).
- Expose labellings along each cycle. For any fixed (α, β) of total support s, the cost is at most
  (a/(m−1)!)^{s/2}. There are at most (2m)^s such pairs, none with s = 1 on either side.
- Σ_{s≥2} (2m·√(a/(m−1)!))^s = o(1). The point maps are prescribed before labellings are drawn, so all
  bounds are unconditional.

**All points fixed.**
- Then U_i F^i = F^i diag(d_i) and G^j V_jᵀ = diag(d'_j) G^j. Tile invariance gives d_i(j)d'_j(i) = 1.
  So the sign matrix X with X_{ij} = d_i(j) has row i in K_i and column j in K'_j, where K_i is the
  kernel word set at row point i.
- From REGULAR-RIGIDITY.md: K_i ⊆ {±(A_{x,·} ∘ A_{y,·}) ∘ p_i : y}, so |K_i| ≤ 2m. Each word is constant or
  balanced, and K_i depends only on the port permutation p_i.
- Each nonconstant word of K_i is uniform over the balanced words (Bush variant: over those with the
  diagonal coordinate fixed).

*Step 1 (separation).* Fix δ = 1/4. Consider two distinct row points and words from their kernel sets,
or a negation. The chance that two nonconstant such words are within Hamming distance δm is at most
(m+1)2^{(H(1/4) − 1)m}. A union bound over m² point pairs and (2m)²·2 word pairs gives o(1). Constant
versus nonconstant words are at distance m/2.

*Step 2.* On the separation event, take a valid X ≠ ±J.
- If all rows are equal, the common row w lies in K_1 ∩ K_2. A nonconstant w is excluded by Step 1, so
  w = ±1 and X = ±J.
- Otherwise two rows differ in at least δm positions, so at least δm columns of X are nonconstant.
  Condition on the F labellings. There are at most (2m)^m candidates X. For each, the G labellings are
  independent, and a fixed nonconstant word lies in K'_j with probability at most 2m(m+1)2^{−m}.
- The union bound is (2m)^m (2m(m+1)2^{−m})^{δm} = 2^{−δm² + O(m log m)} = o(1).

So X = ±J. Each U_i satisfies U_i F^i = ±F^i, hence U_i = ±I, with the same sign everywhere. **With
probability 1 − o(1) the output is rigid:** its signed automorphism group is {(I,I), (−I,−I)}.

## Class count

The multiplicity argument of RESULT.md Lemma 2 applies with (4h)!² replaced by (m!)², and with 2m point
occurrences each contributing |Stab| ≤ a. Lemma 3's whole-fibre flips give 2^{2m−1} distinct matrices per
class in the general ensemble. Hence, with transposes identified,

  (1 − o(1)) D / (2 (m!)² a^{2m}) ≤ C_rigid ≤ C ≤ 2D / 2^{2m},
  log C = N log N − (2 − log 2) N + O(√N log² N).

The Bush ensemble has the same leading two terms, using the upper bound C_B ≤ D_B. Lemma 3's whole-fibre
flips need s_i(i) to be free, so they are not available there. **So there are at least
exp(N log N − (2 − log 2)N − O(√N log² N)) inequivalent rigid regular (Bush-type) Hadamard matrices at
every order N = m² with H(m)**, m ≡ 0 mod 4, m → ∞. In the Bush ensemble the count of rigid classes is
in fact exp(N log N − (2 − log 2)N + O(√N log² N)).

**The result is asymptotic only.** Small m is genuinely nonrigid. At m = 4 with Sylvester A every
sampled output had a large automorphism group (stage-1 exact computation: orders 10321920 and 294912).
The cause is a translation symmetry: an F₂-linear system with m² equations and 2m(log₂ m + 1)
unknowns, which is underdetermined at m = 4. The kernel argument below absorbs it, but only once m is
large. No finite range is claimed; the mixed-quartet union bound is still above 1 at m = 256.

**Rigid designs (M5).** A design automorphism of the normalized matrix lifts to a matrix automorphism
fixing the normalizing row and column. So a rigid matrix yields only rigid Hadamard designs, and
inequivalent matrices yield non-isomorphic designs. The count above therefore gives N^{(1+o(1))N}
rigid Hadamard designs. Merchant (J. Algebraic Combin. 24 (2006), Thm 5.2) gives about (N/2)! at matrix
order N = 32n, given H(N/8). Wherever both apply (H(m) and H(m²/8)), the exponent doubles, from
(1/2)N log N to N log N.

Comparison with the four-group construction (RESULT.md): it has the same leading term and a smaller
second-order constant (−(2 + log 2/8) against −(2 − log 2)). Its orders 4h² are a subset of {m²}, taking
m = 2h. The four-group instance contributes a visible incidence design and the order-1600 finite theorem;
the Meisner instance gives the stronger general statement.

## Open points for the examiner
1. Case A's 2+2 bound is transcribed from the source's balanced-conditioning step. Check that the
   independence of u and v holds here (they come from different row points, so yes; the diagonal
   coordinate is fixed in the Bush variant).
2. The "no isolated vertex" claim in case B uses that A_a∘A_b∘A_c is orthogonal to rows a, b, c of A and
   has a nonzero coefficient on another row. Check that it holds when the basis is indexed by rows here.
3. No finite effective range is claimed. The 10^{1268} figure for Meisner at order 1600 (RESULT.md 1b)
   counts classes, not rigid classes. A finite rigid count at m = 40 would need explicit constants.
4. In the Bush variant, separation of a column pair (j, j') at row points i ∈ {j, j'} involves a diagonal
   port. Those two points can simply be dropped, leaving m − 2 probes.

Redacted 2026-11-24 for privacy (local paths and session identifiers only); the sealed hash refers to the unredacted original.
