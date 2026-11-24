# Stage 2 proof audit: gauge-exact count (RESULT.md Parts 1 and 1b)

STAGE: PROOF-AUDIT

## VERDICT

| Claim | Verdict |
|---|---|
| Gauge, component count c = (h²+h)/2, h fixed lines | VERIFIED |
| Lemma 1 (identical outputs ⇔ gauge orbit), D = L/2^c exact | VERIFIED |
| Lemma 2 (upper multiplicity) | VERIFIED |
| Stab ≤ 2h·a (general h) | VERIFIED (correct but over-generous; see E1) |
| Stab ≤ 2·a₂₀ at h = 20 (kernel ±I) | VERIFIED |
| Lemma 3 (2^{8h−1} distinct matrices per class) | VERIFIED |
| Theorem: two-sided bounds, transpose factor, Stirling term −(2 + log2/8)N, error terms | VERIFIED |
| Order 1600: C > 10^{1514} (`count1600.py`) | VERIFIED |
| Part 1b: Meisner D_M exact, signed bound > 10^{1280}, asymptotic −(2 − log 2)N | VERIFIED (definitions left implicit; see E3, E4) |
| Part 1b framing: "the 1600 ordering *only reflects* looser constants" | GAP (an unproved inference; reword, see X1) |

Part 1 overall: VERIFIED, conditional on the previously audited recovery and FINITE-1600 dependencies. No correctness defect affects any stated number or inequality.

## CLAIM

Part 1: B has (h²+h)/2 components. Two signed labellings give the same H iff they differ by a gauge element, so D = (2^h h!)^{8h}/2^{(h²+h)/2}. The upper multiplicity is ((4h)!)²|Stab_A|^{4h}|Stab_{Aᵀ}|^{4h}2^c and the lower multiplicity is 2^{8h−1}. Together these give (1−o(1))D/(2((4h)!)²(2ha)^{8h}) ≤ C_rigid ≤ C ≤ 2D/2^{8h}, with log C = N log N − (2 + log2/8)N + O(√N log² N). At h = 20, C > 10^{1514}.
Part 1b: Meisner v = 1 gives D_M = ((m−1)!)^{2m}2^{m²} and C_M > 10^{1280} at m = 40, with log D_M = N log N − (2 − log 2)N + O(√N log N), an equivalence loss of O(√N log² N), and the framing consequences that follow.

## EVIDENCE

**Tile structure (checked from CONSTRUCTIONS.md).** For row point x in group i and column point y in group j, the block M_{xy} restricted to the ports has exactly one nonzero entry. If i ≠ j it is hK_{ij}, on the unique common line. If i = j it is h, at the unique L with ℓ_i(L) = x and ℓ_i(πL) = y. The ordered-pair property also covers x = y, where L is fixed. So the tile is (1/h)F_x M_{xy} G_yᵀ = ε f_p g_qᵀ, with no other contributions. Every row flag (i,L) meets the column flags (j,L), j ≠ i, so every port faces at least one (in fact four) opposite points. The same holds for column flags.

**Components.** The edges of B are the K-edges (i,L)–(j,L) for i ≠ j and the P-edges (i,L)–(i,πL). These supports are disjoint because K has a zero diagonal. On one line the K-edges form K_{4,4} minus a perfect matching, which is connected. A P-edge stays inside line L when L is fixed and joins L to πL otherwise. So the components are exactly the π-orbits of lines.

Fixed lines: each point x has exactly one line L with x on both L and πL (the diagonal pair (x,x)), and that line is fixed. A fixed line meets group i in one point, so x ↦ (its fixed line) is a bijection from each group to the fixed lines, giving h fixed lines. Hence c = h + (h²−h)/2. `gauge_check.py` confirms 10 components at h = 4.

**Lemma 1.** Suppose ε f gᵀ = ε f′ g′ᵀ with all entries ±1. Then f′ = c f and g′ = c g with c = f′₁/f₁ ∈ {±1}. Every port faces some point, so each port column of F′_x equals ± the same column of F_x. Columns of Aᵀ (and of A) are pairwise orthogonal, hence projectively distinct, so the port permutations agree. Write d_p = s′_p/s_p and e_q = t′_q/t_q for the sign ratios. Then d_p e_q = 1 on every edge of B. On a connected component this makes d and e one common constant on both sides, which is exactly a gauge element. Conversely, a gauge element multiplies each tile by σ² = 1. The action is free because a nontrivial element changes some port sign.

Fixed lines enter only through the count c. Regularization plays no role: D counts the unregularized H = F̂MĜᵀ, and the regular representative D_R H D_Q is used only inside equivalence classes.

**Lemma 2.**
- *Equivariance.* Both λ and λ′ are good, and the decoder (REGULAR-RIGIDITY, or the unique 20-clique partition of FINITE-1600) is a deterministic function of the matrix, equivariant under signed permutations. So U maps the decoded, and therefore true, row partition of H(λ) onto that of H(λ′). Both partitions are the same fixed block partition {(x,·)}, so U is block-monomial, with U_x carrying block x to block αx. Goodness of λ′ is needed for this step. That is why Lemma 2 counts only good λ′, and the lower bound applies it only to good, rigid labellings, which is legitimate.
- *U_x ∈ Stab.* The tile identity U_x f gᵀ V_yᵀ ε = ε′ f′ g′ᵀ gives U_x f = ±f′. As y varies, every port of x occurs, so U_x maps each projective column of Aᵀ to a projective column of Aᵀ. Because U_x is invertible, U_x Aᵀ = Aᵀ Σ.
- *Counting.* (α, β, (U_x), (V_y)) fixes the target matrix U H Vᵀ, and Lemma 1 caps the labellings that produce it at 2^c. The bound is correct as stated.

**Stab bounds.**
- *Kernel.* Let UB = B diag(e). Row 1 gives e = ±(row 1)∘(row u(1)), so there are at most 2h words, and each e determines U = B diag(e) B⁻¹. Together with REGULAR-RIGIDITY's a = (2h)^r this gives |Stab| ≤ 2h·a. A distinguishing set of r = ⌈2 log₂ h⌉ + 2 coordinates exists, since the expected number of colliding pairs, C(h,2)·2^{1−r}, is below 1. Recomputed: 0.186 at h = 20 and 0.238 at h = 1000.
- *h = 20, induced permutations.* a₂₀ = 4·(20)₃·(5!)⁴ = 5 673 369 600 000 bounds the *induced projective permutations* (FINITE-1600; count-cold-audit item 3). It does not bound Stab itself, so the kernel factor is genuinely needed here.
- *h = 20, kernel.* A nonconstant e induces a fixed-point-free involution k ↦ u(k) on the local rows: row k ∘ e = ±row u(k), and applying e twice returns row k. Two disjoint pairs then give a four-row product equal to ±𝟙, that is |D| = h. This is excluded at h ≡ 4 (mod 8): a fifth vector would need zero sum on cells of odd size h/4 = 5. The argument applies to rows and columns of any H(20), so it holds for both A and Aᵀ. Hence the kernel is {±I} and |Stab| ≤ 2a₂₀.

**Lemma 3.** Negating all port signs at a row point negates its row block, and likewise for column points, so the output is D_R H D_Q. Every entry is ±1. Hence D_R H D_Q = D_{R′} H D_{Q′} iff, for every (x,y), membership of x in R△R′ equals membership of y in Q△Q′. That forces (R△R′, Q△Q′) to be (∅,∅) or (all, all). The result is 2^{8h}/2 = 2^{8h−1} distinct matrices, all in one class. Every class meeting the image contains such a set, so C ≤ C_side ≤ D/2^{8h−1}. Identifying transposes only lowers C.

**Theorem.**
- *Lower bound.* C_rigid ≥ |G|/(2·mult), where G is the set of good and rigid labellings, |G| ≥ (1−o(1))L, and mult = ((4h)!)²(2ha)^{8h}2^c. The extra factor 2 is for transposes: each transpose class holds at most two side-preserving classes. Substituting L/2^c = D gives the displayed bound.
- *Loss.* The loss log D − log C lies between (8h−1) log 2 and log 2 + 2 log(4h)! + 8h log(2ha) + o(1) = O(h log² h). With h = √N/2 this is Θ(√N) at the low end and O(√N log² N) at the high end.
- *Stirling.*
  - 8h²log 2 = 2N log 2.
  - 8h log h! = 2N log h − 2N + 4h log(2πh) + O(1).
  - 2N log h = N log N − 2N log 2.
  - The gauge contributes −(N/8 + √N/4) log 2.

  The total is N log N − (2 + log2/8)N + 4h log(2πh) − (h/2) log 2 + O(1). Numerically, the residual matches the predicted 4h log(2πh) − (h/2) log 2 to within the constant 2/3 at h = 20, 100, 10³ and 10⁵. The residual divided by √N log N stays bounded (1.29 down to 1.09).

**Order 1600.** Checked against the proof, factor by factor:

| Factor | Source |
|---|---|
| 4 | good fraction > 1/2 (FINITE-1600 gives > 70%; count-cold-audit gives > 2/3), times 2 for transposes |
| (80!)² | ((4h)!)², from the point maps |
| (2a₂₀)^{160} | 8h = 160 point occurrences, |Stab| ≤ 2a₂₀ |
| 2^{210} | 2^c with c = (400+20)/2 |

The script divides with floor, and the bound is strict, so C > L/(4·mult) ≥ ⌊·⌋. I reran `count1600.py` and independently recomputed in scratch:

| Quantity | Value |
|---|---|
| Lower bound | 1515 digits, leading 587135898904, so > 10^{1514} |
| Old bound | 663 digits |
| D | 3842 digits (≈ 10^{3841}) |
| Upper bound 2D/2^{160} | 3794 digits |

**Part 1b.**
- *Tiles and gauge.* For v = 1, Z_{(i,e),(j,r)} = ε_{ij} F^i_{ej} G^j_{ir}, so tile (i,j) uses port j at row point i and port i at column point j. The flag graph is the perfect matching (i,j) ↔ (j,i), and the gauge is 2^{m²}.
- *Free tile signs.* Checked directly, without relying on Meisner's text: (ZZᵀ)_{(i,e),(i′,e′)} = Σ_j ε_{ij}ε_{i′j} F^i_{ej}F^{i′}_{e′j} (G^j G^{jᵀ})_{ii′} = m δ_{ii′} · m δ_{ee′} for every ε.
- *Gauge-orbit lemma.* The Lemma 1 proof transfers: every port faces exactly one point, and the columns of H(m) are projectively distinct. The ensemble keeps the diagonal port pinned to the all-ones column and leaves port signs free. So D_M = ((m−1)!)^{2m}2^{2m²}/2^{m²}. The ε_{ij} are absorbed by the port signs.
- *Multiplicity.* The recovery step of credit-bush.md is deterministic and needs no goodness: guess one row fibre (≤ N^m ways), then column restrictions are projectively distinct per port. The block U_x lies in Stab by the same tile argument as above.
- *Stab at m = 40.* m = 40 ≡ 0 (mod 8), so the ±I-kernel argument is unavailable. The general kernel bound 2m is used correctly, giving |Stab| ≤ 2m·a_m. The finite a_m = 4(m)₃((m/4)!)⁴ is valid because the three-row cells have size m/4 = 10 for any H(40).
- *Count.* The formula matches the derivation. I reran `meisner_equal_terms.py` and recomputed independently: signed bound 1281 digits, unsigned control 952, D_M 4187 digits (≈ 10^{4186}).
- *Asymptotic.* 2m log(m−1)! + m² log 2 = N log N − (2 − log 2)N + O(√N log N). The residual divided by √N log N is about −0.25 to −0.42 for m from 40 to 10⁵. The difference from the four-group exponent is (log 2 + log2/8)N = (9/8)N log 2, which is valid at equal N with m = 2h, since H(2h) exists whenever H(h) does. Both counts are two-sided to e^{Õ(√N)} (C_M ≤ D_M), so the asymptotic ordering is proved.

**`gauge_check.py`** (rerun, 0.16 s): all five checks print True. It is a single-instance sanity check, not evidence of generality.

## COVERAGE
Every step listed in the assignment for Parts 1 and 1b was checked: Lemmas 1–3, the component count, the Stab and kernel bounds for general h and h = 20, the theorem's inequalities and transpose factor, the Stirling expansion and error terms, the 1600 constants, and the Part 1b tiles, gauge, freeness, multiplicity, asymptotic and framing. Not covered:
- Part 2 (out of scope).
- The asymptotic recovery dichotomy and the 1−o(1) rigidity probability (taken from prior audits).
- The credit-bush.md B6 separation, which is cited in the framing paragraph and was not re-audited. A brief read found it plausible.

## DEPENDENCIES
- REGULAR-RIGIDITY.md (sha256 e4f5bc1d…) and FINITE-1600.md (sha256 a95c5a9e…) are byte-identical to the revisions examined in count-cold-audit.md, which gave VERIFIED.
- recovery-cold-audit.md: VERIFIED for recovery A, B and the order-20 refinement.
- CONSTRUCTIONS.md: the ordered-pair property and the fixed-line paragraph.
- credit-bush.md: Meisner Thm 1 formula (p. 236 as quoted) and the unsigned deduction. Meisner's paper itself was not consulted; orthogonality was re-derived directly instead.

## ERRATA

**Correctness defects:** none found.

**Imprecisions, recommended fixes:**
- **E1. Misattributed bound (RESULT l.44–45).** RESULT says REGULAR-RIGIDITY bounds the induced projective permutations by a = (2h)^r. In fact that argument bounds the signed row permutations themselves: fixing the preimages and signs of r coordinates determines U. So |Stab| ≤ a already, and the extra factor 2h is redundant. This is conservative and changes the lower bound only by e^{O(h log h)}. At h = 20 the distinction is real and is handled correctly: a₂₀ bounds induced permutations, and the kernel is ±I.
- **E2. C_rigid is never defined.** Define it as the number of transpose-identified classes containing a good, rigid output. State that G (good and rigid) is a union of gauge orbits, since both properties depend only on the matrix. That fact is what justifies "almost every distinct output is rigid" (equal fibre sizes 2^c).
- **E3. Part 1b ensemble left implicit.** RESULT does not define its signed ensemble (fixed normalized H(m), diagonal port pinned to the all-ones column, free port signs, with ε absorbed). It also does not write out the gauge-orbit lemma for it. Both appear only in the script docstring. Add them.
- **E4. Which a_m in the asymptotic.** The Part 1b loss "O(√N log² N)" requires the general a_m = (2m)^r. The finite a_m = 4(m)₃((m/4)!)⁴ gives an O(N log N) loss. State which a_m is meant.
- **E5. Identification wording.** "Only 2^{N/8} of that is real identification": identical-output identification is exactly 2^{N/8 + √N/4}. Equivalence adds a further e^{Θ̃(√N)}. Minor.

**Optional strengthenings (not defects):**
- Use |Stab| ≤ a for general h.
- Use the good fraction > 2/3 at h = 20. This adds less than 1 digit.
- Replace the N^m guess in the Meisner deduction by fibre recovery from a single row. Neither changes any conclusion.

## EXPOSURE
- **X1. Framing paragraph, "only reflects looser finite constants (a₄₀, N^m)".** This is not proved. The proved quantities at 1600 are: four-group C between 10^{1514} and about 10^{3793}, and Meisner C_M between 10^{1280} and 10^{4186}. These do not order the true class counts at 1600. The true Stab of a particular H(40), for example a product H(2)⊗H(20), may be genuinely larger than that of H(20). Only the asymptotic ordering, at second order, and the D_M > D comparison at 1600 are proved.

  Suggested wording: "The proved lower bounds at 1600 do not decide which construction has more classes; asymptotically Meisner's has more."

  The conclusion "the class count is not a point of superiority" is correct and should stay.
- **X2. Unaudited citation.** The cited separation from all nontrivial Meisner outputs (credit-bush B6 follow-up) was not part of this audit.

## RESOURCES
Theory audit plus reruns with Python 3 in a virtual environment:

| Script | CPU time |
|---|---|
| `gauge_check.py` | 0.16 s |
| `count1600.py` | 0.03 s |
| `meisner_equal_terms.py` | 0.03 s |
| scratch recomputation `audit_check.py` (in the session scratchpad) | < 0.1 s |

Total under 1 CPU-second on a single core, with no sign-space search. Files reviewed (sha256):

| File | sha256 |
|---|---|
| RESULT.md | 2bde946c8b40760220de21efbbb64611e02ce3e1c71231bd48f649f52e95ef39 |
| gauge_check.py | 63a88ca8… |
| count1600.py | 2457c5a2… |
| meisner_equal_terms.py | 563a9b6c… |
| CONSTRUCTIONS.md | 87e117fe… |
| credit-bush.md | 659baf2a… |
