# Stage 2 proof audit: generic rigidity and class counts for Meisner's square construction

STAGE: PROOF-AUDIT (cold-examiner Stage 2), 2026-11-23.
Audited: `MEISNER-RIGIDITY.md` (sha256 98e9c8eb…f0c8b3d) against claims M1–M5 of `audit/MEISNER-PACKET.md`
(sha256 1a29d52f…e122ff). Full hashes are under EXPOSURE.

## VERDICT

| Section / claim | Verdict |
|---|---|
| M1. Construction is Hadamard; Bush variant is Bush-type and regular (row sum m) | VERIFIED |
| M2. Gauge lemma, D = 2^{m²}(m!)^{2m}, D_B = 2^{m²−m}((m−1)!)^{2m} | VERIFIED |
| Separation geometry (all m opposite points separate) | VERIFIED |
| Case A: in-fibre sum m·D; odd-multiplicity Hoeffding; 2+2 bound; union bound | VERIFIED (Bush constants, E2) |
| Case A: column-list separation | VERIFIED |
| Case B: true pairs; exposure of t_y(c); forest count; union bound | VERIFIED |
| Case B: no-isolated-vertex claim with the port y excluded | VERIFIED after a one-line repair (E1). As written the justification is incomplete |
| Decoder branch choice; invariance under signed equivalence | VERIFIED |
| Rigidity: moved points (U_i ∈ Stab_A, a = (2m)^r, cycle exposure, (2m)^s count) | VERIFIED (column side uses Stab_{Aᵀ}, E3) |
| Rigidity: all points fixed (K_i, uniformity, Step 1, Step 2, conditioning on F) | VERIFIED |
| M3 overall (recovery and rigidity w.p. 1 − o(1), uniformly in A, both ensembles) | VERIFIED, conditional on E1's repair |
| M4. Class bounds and log C = N log N − (2 − log 2)N + O(√N log² N), both ensembles | VERIFIED |
| Sylvester-type A (closed quartets, maximal kernel, large Stab) | VERIFIED: covered uniformly |
| M5. Rigid matrix ⇒ rigid designs; inequivalent ⇒ non-isomorphic; N^{(1+o(1))N} rigid designs | VERIFIED |
| M5. "Double the exponent at the common orders (squares divisible by 32)" vs Merchant 2006 Thm 5.2 | VERIFIED as a comparison of log-counts. The parenthetical over-describes the common orders (E4) |

Overall: the transcription is correct. No step fails. There is one gap in the written justification (E1), closed
here by a short argument that uses the case-B hypothesis. Everything else is either a constant change or wording.
The results are asymptotic only: none of the bounds is below 1 at m = 40 (order 1600); see EXPOSURE.

## CLAIM

For A a Hadamard matrix of order m ≡ 0 mod 4, labellings (p_i, s_i, p'_j, t_j) give H_{(i,e),(j,r)} =
s_i(j)A_{e,p_i(j)} · t_j(i)A_{p'_j(i),r}, of order N = m². The general ensemble is uniform over (m!2^m)^{2m}
labellings. The Bush ensemble has A normalized, p_i(i) = p'_j(j) = 1 and s_i(i) = t_j(j) = +1. The claims are
M1–M5 of the packet: the gauge-exact count, intrinsic fibre recovery and rigidity with probability 1 − o(1)
uniformly in A, the two-sided class count with Stirling constant −(2 − log 2), and the transfer to rigid
Hadamard designs with the comparison to Merchant.

## EVIDENCE

### M1
Rows (i,e), (i',e'). The sum over (j,r) is Σ_j F^i_{ej}F^{i'}_{e'j}(G^jG^{jᵀ})_{ii'} = m δ_{ii'} Σ_j F^i_{ej}F^i_{e'j}
= m² δ_{ii'}δ_{ee'}.

In the Bush ensemble, column i of F^i is column 1 of A, which is all ones, and row j of G^j is row 1 of A, so
tile (i,i) = J. Every other column of a normalized A is orthogonal to column 1 and is therefore balanced, and the
same holds for rows. So every off-diagonal tile has zero margins. The row sum of row (i,e) is
Σ_j F^i_{ej}Σ_r G^j_{ir} = F^i_{ei}·m = m, and columns behave the same way. This is Bush-type with blocks of
order m = 2n, where N = 4n².

Script check (`meisner_audit_checks.py` §1): Sylvester-8, Paley-12 and Paley-20, both ensembles. All six outputs
were Hadamard; the three Bush outputs had diagonal J tiles, zero off-diagonal margins and row sum m.

### M2
Tile (i,j) is f gᵀ, where f is column j of F^i and g is row i of G^j. These vectors appear in no other tile.

Suppose two labellings give the same H. Equal rank-one ±1 tiles force f' = c f and g' = c g. The columns of A
are pairwise orthogonal, hence projectively distinct, so p'_i(j) = p_i(j). Likewise for the rows. The sign
ratios then satisfy d_{ij}e_{ij} = 1, which is exactly the pairwise gauge. Conversely, the gauge multiplies each
tile by σ² = 1.

The gauge group has order 2^{m²}, or 2^{m²−m} in the Bush ensemble, where the diagonal signs are fixed on both
sides. It acts freely. So D = 2^{2m²}(m!)^{2m}/2^{m²} and D_B = 2^{2m(m−1)}((m−1)!)^{2m}/2^{m²−m}, as claimed.
Script check §1: a joint flip of s_0(1) and t_1(0) leaves H unchanged, and a single flip changes it.

### Separation geometry
- Two rows from one row point: on column fibre j their product is F^i_{ej}F^i_{e'j}(G^j_{ir})², which is
  constant in r.
- Two rows from points i ≠ i': on column fibre j their product is a constant times G^j_{i·}∘G^j_{i'·}. These
  are two distinct signed rows of A, so the product is balanced at every j, including j ∈ {i, i'} in the Bush
  case.
- Columns behave the same way, using columns of F^i.

So all m opposite points separate. Either partition determines the other deterministically.

### Case A (rows of A; |D| ≥ m/2 for some distinct x₁..x₄)
- **In-fibre.** The quartet sum is Σ_j s_i(j)⁴ Π_l A_{x_l p_i(j)} · Σ_r (G^j_{ir})⁴ = m·D, because p_i is a
  bijection. Script check §1: 0 mismatches in 30 random quartets per instance.
- **Odd multiplicity at row point i** (patterns 3+1, 2+1+1, 1+1+1+1). The sign s_i(j) appears to an odd
  power, and it occurs nowhere else (G involves only t and p'). Conditioning on everything else gives
  Σ_j s_i(j)c_j with |c_j| ≤ m. Hoeffding at threshold m²/2 gives exponent (m²/2)²/(2·m·m²) = m/8.
- **2+2 at points i, k.** The coefficient Σ_r(G^j_{ir})²(G^j_{kr})² = m, so the sum is m Σ_j u(j)v(j). The port
  signs cancel in u = (A_x∘A_{x'})∘p_i, so u depends only on p_i, and v depends only on p_k. Since p_i and p_k are
  independent, u and v are independent. For a uniform p_i, u is uniform over balanced words. Comparing with
  fair signs conditioned on balance costs P(balance)⁻¹ ≤ m + 1, which gives (m+1)·2e^{−m/8}.
- **Exhaustiveness.** The patterns 4, 3+1, 2+2, 2+1+1 and 1+1+1+1 cover every quartet. The union over m⁸
  quartets is 2m⁸(m+1)e^{−m/8} = o(1).
- **Column lists.** On the good event every threshold quartet is in-fibre, so every listed pair product
  F^i_{ej}F^i_{e'j} is constant on column fibres. At every row point i the predetermined quartet (i, x₁..x₄)
  crosses the threshold deterministically. So u_i = (A_{x₁}∘A_{x₂})∘p_i is available at all m points, and the
  u_i are independent.

  For a uniform permutation, P(u_i(j) = u_i(j')) = 2(m/2)(m/2−1)/(m(m−1)) = (m−2)/(2(m−1)). This matches exactly
  at m = 8, 12 and 40 (script §5). The union bound is C(m,2)2^{−m}. List equality is invariant: row signs scale a
  whole list coordinate uniformly, and column signs cancel in products.

### Case B (all |D| < m/2)
- **True pair.** The j-term is ±Σ_r G^j_{kr}G^j_{lr} ∈ {0, ±m}, even if k or l equals i. Script check §1: no
  non-divisible sums in 200 random extensions per instance.
- **Exposure.** t_y(·) occurs only in G^y. The auxiliary rows (c, e_c) are fixed indices, chosen independently of
  t. So the sum is K_cd + σ_cd D'_{αβγδ} t_y(c)t_y(d), where α..δ = p'_y(a..d) are four distinct rows of A.
  K_cd and σ_cd are exposed. Under B, 0 < |2D'| < m, so at most one value of t_y(c)t_y(d) passes.
- **Forest.** There are at least m − 3 vertices with no isolated vertex (see E1), so a spanning forest has at
  least ⌈(m−3)/2⌉ edges. Edge products of independent vertex signs on a forest are independent and uniform, so a
  false pair passes with probability at most 2^{−(m−3)/2}. The union over C(N,2) pairs is
  m⁴2^{−(m−3)/2} = o(1).
- **No isolated vertex (open point 2).** Rows of a Hadamard matrix form an orthogonal basis. w = A_α∘A_β∘A_γ is
  orthogonal to A_α, A_β and A_γ, so it has a nonzero coefficient on some fourth row. That proves the source's
  claim when every other port is a vertex. Here the port y is excluded (the doc says "c ∉ {a, b, y}"), so the
  fourth row could be p'_y(y). See E1 for the repair under B.

  Script check §3: Paley-12 (case B, D ∈ {±4}) gives 0 isolated vertices in 11880 (α, β, excluded, c)
  instances. Sylvester-8 (case A) gives 336/1680 isolated instances under exclusion. So the case-B hypothesis is
  genuinely needed for the excluded-port version.
- **Decoder.** It uses case A if some quartet crosses N/2, and case B otherwise. In case B an in-fibre quartet
  has |mD| < N/2, so a wrong branch requires a mixed threshold quartet, which has probability o(1). All tests use
  |quartet sum|, divisibility or list equality, all of which are invariant under signed permutations. So the
  decoder is equivariant.

### Rigidity, moved points
- **Block structure.** Recovery and equivariance make U block-monomial: U_i takes fibre i to fibre αi. Equal
  rank-one tiles give U_i(col j of F^i) = ±(col βj of F^{αi}). So U_iF^i = F^{αi}Q_βD. With F^i = AP_iS_i this
  gives U_iA = AΣ, that is, U_i ∈ Stab_A.
- **Bound on Stab_A.** a = (2m)^r is a bound on all of Stab_A, not only on the induced permutations. Some r
  coordinates distinguish the columns up to sign: the expected number of collisions is C(m,2)2^{1−r} ≤ 1/4. The
  preimages and signs of these coordinates determine Σ, and hence U = AΣA⁻¹.
- **Cycle exposure.** Given p_i, β and U_i, p_{αi} is determined, so it lies in a set of at most a
  permutations. The probability is a/m!, or a/(m−1)! in the Bush ensemble, where the determined permutation may
  violate p(αi) = 1, which only lowers the probability. Exposing along cycles gives ≥ s/2 constraints. Row
  constraints use p and column constraints use p', so the two sides are independent.
- **Counting point actions.** The number of (α, β) with total support s is ≤ Σ_{s₁+s₂=s} m^{s₁}m^{s₂} ≤ (2m)^s.
  No permutation has support 1. The geometric ratio 2m√(a/(m−1)!) has log ratio −62 at m = 64 and −2944 at
  m = 1024 (script §7). The event is contained in a union of labelling-defined events for prescribed (α, β), so
  the bound is unconditional.

### Rigidity, all points fixed
- **Kernel words.** U_iF^i = F^i diag(d_i). Row x gives d_i = ±(A_x∘A_y)∘p_i, so there are at most 2m words,
  each constant or balanced. Equivalently K_i = K_A∘p_i, where K_A = {w : A diag(w) A⁻¹ is a signed
  permutation}. This depends only on p_i.
- **Uniformity.** A fixed nonconstant w composed with a uniform p_i is uniform on balanced words. In the Bush
  ensemble it is uniform on balanced words with coordinate i fixed to w(1), which costs a factor 2.
- **Columns.** On the column side G^jV_jᵀ = diag(d'_j)G^j gives K'_j = K_{Aᵀ}∘p'_j. Tile invariance gives
  d_i(j)d'_j(i) = 1, so column j of X equals d'_j ∈ K'_j.
- **Step 1.** The ball of radius m/4 has at most 2^{H(1/4)m} points, and C(m,m/2) ≥ 2^m/(m+1). H(1/4) = 0.8113.
  The union over m² point pairs, (2m)² word pairs and a sign gives 8m⁴(m+1)2^{−0.1887m} = o(1). This is above 1
  until m ≈ 256 (script §5). A constant word and a balanced word are at distance m/2.
- **Step 2.**
  - Equal rows: the common row lies in K₁ ∩ K₂, so it is constant.
  - Two different rows: either both are nonconstant (then at distance > m/4 by Step 1), or the distance is m/2
    or m. Either way at least m/4 columns are nonconstant.
  - Separation is an event in p only. For each fixed p in it, the candidates X ∈ ΠK_i number at most (2m)^m.
    Each has at least m/4 fixed nonconstant columns that must lie in the independent K'_j, which are independent
    of p. So conditioning on F is legitimate.
  - P(fixed nonconstant z ∈ K'_j) ≤ 2m/C(m,m/2) ≤ 2m(m+1)2^{−m}; the Bush ensemble adds a factor 2. The
    log₂ bound is m log₂(2m) − m²/4 + O(m log m) → −∞ (−368 at m = 64).
- **Conclusion.** X = ±J gives U_i = ±I and V_j = ±I with one global sign.

### Sylvester-type A
Closed quartets put Sylvester in case A, with D = m. Script §2 gives row-quartet values {0, 8} at m = 8 and
{0, 16} at m = 16. The kernel K_A is maximal: |K_A| = 2m, giving 16 and 32 (script §4). Stab_A is large,
2^{Θ(log² m)}. The proof uses only:
- |K_i| ≤ 2m;
- marginal uniformity of each nonconstant word (union bounds never need joint independence within K_i);
- |Stab_A| ≤ (2m)^r, which is proved for every Hadamard A.

Case B's excluded-port subtlety (E1) does not arise for Sylvester, because Sylvester is in case A. Coverage is
uniform. For contrast, Paley-12 is case B with |K_A| = 2, and Paley-20 is case A, since |D| = 12 ≥ 10.

### M4
- **Lower bound.** Lemma 2 transcribes correctly. Point maps give (m!)² choices. The blocks U_i ∈ Stab_A and
  V_j ∈ Stab_{Aᵀ} give a^{2m}. Each tuple fixes UHVᵀ, so a class meets at most (m!)²a^{2m} distinct good
  outputs. Good-and-rigid is a property of H, so it is a union of gauge orbits, and the number of distinct good
  rigid outputs is at least (1 − o(1))D. Transposes cost a factor 2.
- **Upper bound.** Lemma 3 negates all port signs at chosen points, giving D_RHD_Q. All entries are nonzero, so
  this yields 2^{2m−1} distinct matrices. This needs s_i(i) to be free, so it holds in the general ensemble only.
  The doc correctly uses C_B ≤ D_B for the Bush ensemble.
- **Stirling.** 2m log m! = N log N − 2N + m log(2πm) + O(1). Adding m² log 2 gives
  log D = N log N − (2 − log 2)N + O(√N log N). For the Bush ensemble, log D_B = log D − 2m log m − m log 2.
  Script §6: (log D − main)/(√N log N) runs from 0.75 down to 0.59, and the Bush version from −0.34 down to −0.45,
  for m from 40 to 40000.
- **Loss.** The lower-bound loss is log 2 + 2 log m! + 2m·r log(2m) = O(√N log² N); the ratio is about 1.7 for
  large m. The upper-bound loss is O(√N).
- **Comparison with the four-group constant.** −(2 + log 2/8) is about −2.087, against −1.307 here. 4h²
  is m² with m = 2h ≡ 0 mod 8, and H(2h) = H(2)⊗H(h). The comparison is correct.

### M5
- **Rigid matrix gives rigid designs.** Normalize at (x, y) by diagonal signs, H' = D₁HD₂. A design
  automorphism (P, Q) extends to (P⊕1, Q⊕1), which stabilizes H'. Then U = D₁(P⊕1)D₁ and V = D₂(Q⊕1)D₂
  stabilize H. Rigidity forces U = ±I, and the fixed coordinate x forces the sign +, so P = I. In a symmetric
  design, P determines Q.
- **Inequivalent matrices give non-isomorphic designs.** An isomorphism of the designs lifts to (P⊕1)H'₁(Q⊕1)ᵀ
  = H'₂. So isomorphic designs come from equivalent matrices, and the count is at least C ≥ e^{N log N − O(N)}.
- **Comparison with Merchant.** Merchant gives (16n − 2)!/(2¹⁰n³) at N = 32n, with log of about
  (N/2) log N. This bound gives log of about N log N. The ratio of exponents is 2.

## COVERAGE
Every substitution listed in the assignment was checked: separation geometry; in-fibre m·D; Hoeffding;
2+2 and the independence of u and v; column lists; case-B exposure; the no-isolated-vertex claim; the forest
count; the union bound; the cycle bound; Stab membership; K_i; uniformity; Step 1 (δ = 1/4); Step 2 with
conditioning; class counts and Stirling for both ensembles; the Bush diagonal; M5; Sylvester. The open points
1–4 of the doc are resolved as follows:
1. Independence holds.
2. The claim holds under B with the E1 repair.
3. No finite range: confirmed, see EXPOSURE.
4. Diagonal ports need not be dropped. The collision probability there is (m/2−1)/(m−1) < 1/2, and dropping
   them is also fine.

## DEPENDENCIES
- REGULAR-RIGIDITY.md (sha256 e4f5bc1d…3e0e33), as audited in recovery-cold-audit.md and count-cold-audit.md.
  Each borrowed step was re-derived here for the Meisner geometry rather than cited.
- RESULT.md Lemmas 1–3 (stage-2 VERIFIED in audit/stage2-proof-audit.md), also re-derived.
- The Merchant Thm 5.2 statement is taken as quoted in PRIOR-ART-CONCLUSION.md §3 item 1. It was not re-read
  at source.

## ERRATA

Correctness defects (none changes a stated result):
- **E1 (justification gap, case B).** "No isolated vertex (same orthogonality argument)" is insufficient once
  port y is excluded. The required fourth row may be p'_y(y). Sylvester-8 shows this happens when closed quartets
  exist. Repair under B: Parseval gives Σ_δ⟨w, A_δ⟩² = m·‖w‖² = m², with zero coefficients on α, β, γ and
  |⟨w, A_δ⟩| = |D| < m/2 on every other row. So at least 5 rows carry nonzero coefficients, and at most one is
  excluded. Alternatives:
  - in the general ensemble, keep y as a vertex (m − 2 vertices; the source argument applies verbatim);
  - in the Bush ensemble, keep y as a vertex with the fixed sign t_y(y) = +1, which acts as a known root.
- **E2 (constants, Bush).** The displayed bounds are the general-ensemble constants. With the diagonal fixed:
  - Hoeffding has m − 1 free signs plus one fixed term: 2e^{3/8}e^{−m/8}.
  - 2+2 conditions on a composition-(m/2 − 1, m/2) word on m − 1 coordinates, with threshold m/2 − 1:
    e^{−m/8 + O(1)}·O(m).
  - Step 1 and Step 2 each gain a factor 2.

  All of these remain o(1). The doc's sentence "only changes constants" is correct, but the constants are not
  written.
- **E3 (wording).** "The column side is symmetric" should name Stab_{Aᵀ}: V_jG^{jᵀ} = G^{βjᵀ}Q gives
  V_j ∈ Stab_{Aᵀ}. It is bounded by the same (2m)^r using rows of A. The class count
  already uses a^{2m} for both.

Optional precision:
- **E4 (M5).** Merchant's Thm 5.2 requires a Hadamard design of order n = N/32, i.e. H(N/8). The orders where
  both theorems apply are N = m² with 8 | m, H(m) and H(m²/8). That H(m) implies H(m²/8) was not checked and is
  not obvious, so "squares divisible by 32" over-describes the common set. The doubling of the exponent holds
  wherever both apply. Where only this result applies, it has no Merchant comparator.
- **E5.** The vertex count can be m − 2 in the general ensemble (see E1), which slightly improves 2^{−(m−3)/2}.

## EXPOSURE
This audit read the following files, with their SHA-256 hashes:
- MEISNER-RIGIDITY.md 98e9c8eb423f22e277ccc3208e182c31b444111d1dea81c611ef9fd20f0c8b3d
- MEISNER-PACKET.md 1a29d52f2be64676c33e59bf1865c64943f190f0b933f2d48b3910d665e122ff
- RESULT.md 24417244ad5fab620ebd3aa5b5d58cbf0deb2126aedcd656e26123e1af0c4c46
- PRIOR-ART-CONCLUSION.md 2d7c9f69802276687c0c106404ed3685ce83a0454bac9136e39dc8fe4a81c222
- REGULAR-RIGIDITY.md e4f5bc1d8514915056543b30f7216d31efe487eed482fba8beb7032cb67e0e33
- recovery-cold-audit.md 27e0b0a4cae243f5cc46a2c035a06d36a622b9307551233e64c9e3107c5b3ae7
- count-cold-audit.md b4811faae18412177b964a112dc5100361253594932d20cf0c10dfb4585a4192
- credit-bush.md 659baf2ac537a96243542655d70360f7edc26519221d34332f1a9d54616cd765

It also read meisner_equal_terms.py and the first part of audit/stage2-proof-audit.md. This audit is not
independent of the doc: the auditor read the proof before checking it (Stage 2 by design).

Scope: all statements are asymptotic. At m = 64 the mixed-quartet union bound is 2^{43.5}, and at m = 256 it is
still 2^{26.8}. The Step 1 bound is 2·10⁶ at m = 64. No finite consequence (e.g. at order 1600) follows, as the
doc's open point 3 says.

## RESOURCES
Theory plus one script:
`meisner_audit_checks.py` (session scratchpad; not retained; sha256 below)
(sha256 d6328d8aa164f1ba682fe5ab2edbd058d20418aaec704e0a47a2cee309e00459). It ran under
Python 3 in a virtual environment on a single core in 3.5 CPU-seconds, with no searches. It checks:
- §1: construction, Bush and gauge properties;
- §2: quartic-sum spectra;
- §3: isolated vertices under exclusion;
- §4: kernel sizes;
- §5: collision probabilities and bound magnitudes;
- §6: Stirling residuals;
- §7: the moved-point ratio.
