# Meisner square construction: Stage 1 cold examination (isolated failure search)

STAGE: INITIAL (statement packet revision 1 only; proof file not opened)

Sources read: MEISNER-PACKET.md, incidence-order-extensions-2026-11-23/REGULAR-RIGIDITY.md, incidence-order-extensions-2026-11-23/credit-bush.md, four-group-gauge-2026-11-23/PRIOR-ART-CONCLUSION.md. Nothing else in four-group-gauge-2026-11-23/ was opened.

## VERDICT

| Claim | Verdict | One-line reason |
|---|---|---|
| M1 | NOT-BROKEN | Hadamard and Bush-type checked by hand; also asserted exactly on 20 random outputs at m = 4 |
| M2 | NOT-BROKEN | Rank-one tile decomposition forces port index and joint sign; both counts recomputed |
| M3 | UNRESOLVED | No asymptotic counterexample. Rigidity fails for every output at m = 4. The Sylvester residual symmetry family is underdetermined at m = 4 and square at m = 8. For Sylvester A the modular (branch-B-type) fibre test is vacuous |
| M4 | NOT-BROKEN (conditional on M3) | Constant −(2 − log 2) is correct for log D and log D_B; "that many" should read "at least that many" |
| M5 | NOT-BROKEN, with a scope exposure | rigid matrix ⇒ rigid designs holds; exponent doubling holds; "common orders = squares divisible by 32" silently assumes H(m²/8) exists |

No claim is REFUTED.

## EVIDENCE

### M1
Tile (i,j) equals u v^T with u = s_i(j) A[:,p_i(j)] and v = t_j(i) A[p'_j(i),:]. For rows (i,e) and (i',e'), the r-sum is the inner product of rows p'_j(i) and p'_j(i') of A. It equals m δ_{ii'} because p'_j is a bijection. Then F^i is a signed column permutation of A, so the remaining j-sum gives m δ_{ee'}. Bush case: p_i(i) = p'_i(i) = 1 with A normalized, so the diagonal tile is J. Off-diagonal ports differ from 1, so u and v are balanced and the rank-one tile has zero row and column sums. Each row sum is m = √N. The script asserts H H^T = N I, J diagonal tiles and zero-margin off-diagonal tiles on 10 general and 10 Bush samples at m = 4. It passes.

### M2
The ±1 rank-one tile u v^T fixes u and v up to one common sign. Distinct columns of A are orthogonal, so they are never ± each other. Hence u fixes p_i(j), and v fixes p'_j(i). The only freedom left is the joint flip (s_i(j), t_j(i)) → (−s_i(j), −t_j(i)). No other identical-output coincidence exists, for any A, including Sylvester.

Counts: L = (m! 2^m)^{2m}, and the gauge has order 2^{m²}, so D = 2^{m²}(m!)^{2m}. In the Bush ensemble a diagonal flip is excluded by s_i(i) = t_i(i) = +1. Labellings number ((m−1)!)^{2m} 2^{2m(m−1)} and the gauge has order 2^{m(m−1)}, so D_B = 2^{m²−m}((m−1)!)^{2m}. Both agree with the packet.

### M3: what I checked

1. **Small-m nonrigidity (exact, dreadnaut).** Signed automorphism group sizes of outputs at m = 4 (N = 16) with Sylvester A:
   - general ensemble, 10 samples: |Aut| = 10321920 (4 samples), 294912 (6 samples);
   - Bush ensemble, 10 samples: 294912 (7 samples), 10321920 (3 samples).

   Nonrigid at rate 10/10 and 10/10. This is expected, since every H(16) has a large group. It does not touch an asymptotic claim. My attempted m = 8 run (N = 64, 20 samples) did not finish: dreadnaut on the 256-vertex Hadamard graph exceeded the CPU cap, and I killed it. **The m = 8 and m = 12 rates are unmeasured.**

2. **Residual symmetry family for structured A (analytic).** Restrict to automorphisms that fix every point. Each point then acts by a signed permutation with P A = A·diag(w); call w the point's word. Write w_i for row point i and w'_j for column point j. The tiles force w_i(p_i(j)) · w'_j(p'_j(i)) = 1 for all i and j.

   For Sylvester A of order m = 2^k the admissible words are the 2m signed characters. P is a translation e ↦ e + a. This gives the F_2-linear system

   a_i·p_i(j) + b_j·p'_j(i) + α_i + β_j = 0 for all (i,j), with unknowns a_i, b_j ∈ F_2^k and α_i, β_j ∈ F_2.

   The system has m² equations and 2m(k+1) unknowns, against a trivial solution space of dimension 1 (the case ±(I,I)):
   - m = 4: 24 unknowns, 16 equations. The kernel dimension is at least 8, so every labelling is nonrigid. This matches the exact runs.
   - m = 8: 64 unknowns, 64 equations. Rigidity against this family is a rank question with non-negligible failure probability (not measured).
   - m = 16: 160 unknowns, 256 equations.

   A union bound gives failure probability → 0. Each nontrivial solution forces random balanced words p_i ↦ a_i·p_i(·) to match prescribed words, at probability about 2/C(m, m/2) per row. In the all-a_i-nonzero, b = 0 sub-case the bound is about m^m (2/C(m, m/2))^{m−1}, roughly 2.5e−4 at m = 8. So this family does not break the asymptotics. It is a concrete hidden symmetry that survives random labelling at small m. Any proof must defeat it with a kernel bound that is uniform over A; Sylvester has the largest word set.

   Point-moving lifts need p_{π(i)} τ p_i^{-1} ∈ G for all i, where G is the column action of Aut(A). For Sylvester, |G| = m^{O(log m)}. The union (m!)²(|G|/m!)^m → 0.

   Global operations from Aut(A) applied at every point, and transposition-like maps, change port indices. Undoing them needs the fibre-permutation compatibility above, so they are excluded for generic labellings. I found no global symmetry shared by all outputs at large m.

3. **Fibre recovery for Sylvester A (every quartet closed).**
   - **The modular test is vacuous for Sylvester.** For any four rows of H, the four-row sum is Σ_j (u-product) · Σ_r (product of four signed rows of A). The inner sum is 0 or ±m for Sylvester. So every row quartet of H has sum divisible by m, and the "every extension divisible by m" relation is the complete graph. A recovery argument resting on that test (as in branch B of REGULAR-RIGIDITY) fails outright for Sylvester and for any A whose row quartets are all closed.
   - **The high-quartet branch does work.** Four rows in one fibre with e1+e2+e3+e4 = 0 have sum N. For mixed quartets, patterns 3+1 and 2+1+1 give exactly 0 (the r-sum is an off-diagonal inner product). Pattern 1+1+1+1 is a sum carrying independent port signs. Pattern 2+2 at points i and k equals m Σ_c x(c) y(σ(c)), where x = A_e∘A_{e'}, y = A_f∘A_{f'} and σ = p_k p_i^{-1}.
   - **2+2 carries no sign randomness:** s_i(j)² = 1 cancels. Its tail bound must come from the random permutation (hypergeometric overlap of two balanced words), not from a fair-sign sum. A hypergeometric bound exp(−Θ(m)) against at most N^4 quartets gives o(1), but only for m in the hundreds.
   - **Recovery for Sylvester is not refuted. It hinges on branch selection.** The decoder must select the threshold-quartet branch whenever A has closed quartets.

   I could not see the actual proof, so these are DEPENDENCIES, not failures.

4. **Bush diagonal.** The fixed port 1 at the diagonal removes one random port per point. In the kernel system the diagonal equation reads w_i(1) = w'_i(1). Unsigned translations satisfy it automatically (χ_a(0) = 1), so it creates no extra symmetry family. The loss of randomness is O(1) ports per point.

### M4
log D = m² log 2 + 2m log m! = N log N − 2N + N log 2 + O(√N log N) = N log N − (2 − log 2)N + O(√N log N), using 2 log m = log N.

log D_B differs by −m log 2 − 2m log m = O(√N log N). So the stated second-order constant holds in both ensembles.

The lower bound loses log(2 (m!)² a^{2m}) = O(m log² m) = O(√N log² N), with a = (2m)^{O(log m)} uniformly in A (the distinguishing-coordinate argument of REGULAR-RIGIDITY). This matches the stated error, given M3.

Wording: C is defined as the number of classes from this ensemble, but "there are that many inequivalent rigid Bush-type matrices" reads as a statement about all of them. Only "at least" is supported.

### M5
- **Rigid matrix ⇒ rigid designs.** Normalizing at row x and column y gives H_n = D_1 H D_2, whose automorphism group is conjugate to Aut(H). A nontrivial design automorphism is a nonidentity point permutation (blocks are distinct). It extends to unsigned permutations fixing the border, which is a nontrivial matrix automorphism different from ±(I,I). This contradicts rigidity.
- **Inequivalent matrices ⇒ non-isomorphic designs.** Isomorphic designs give permutation-equivalent normalized matrices.
- **Merchant comparison.** Take Merchant's "Hadamard design of order n" as 2-(4n−1, 2n−1, n−1), the convention the packet and PRIOR-ART use; I could not check it in a primary source within scope. Then order 8n corresponds to matrix order N = 32n, and (16n−2)! = (N/2 − 2)!, whose logarithm is (1/2) N log N (1 + o(1)). M4 gives N log N (1 + o(1)), so the exponent doubles.
- **Scope exposure.** Merchant needs a Hadamard design of order n = N/32 > 2, i.e. H(m²/8) and m ≥ 16. M4 needs H(m) with 4 | m. "Squares divisible by 32" means 8 | m, so m = 8k, and it silently assumes H(8k²) exists. I know of no theorem deriving H(8k²) from H(8k) for odd k. Agaian-type multiplication gives H(16k), and Kronecker gives H(64k²); neither gives H(8k²). The common orders should be stated as {m² : 8 | m, m ≥ 16, H(m) and H(m²/8) exist}. m = 8 (N = 64) is excluded by Merchant's n > 2.

## COVERAGE
- **M1, M2:** complete hand derivations. M1 also has exact numerical checks at m = 4.
- **M3:** analytic search over three families: fixed-point kernel symmetries, point-moving lifts, and global Aut(A) and transposition-like maps. Quartet-pattern analysis for fibre recovery. Exact automorphism groups at m = 4 only (20 samples). m = 8, m = 12 and m = 16 are not measured. No non-Sylvester A beyond order 4 was tested.
- **M4:** arithmetic of both constants and of the error term.
- **M5:** logic of both implications and of the exponent comparison. The order-set issue is noted. Merchant's convention was taken from in-scope restatements, not from the paper.
- **Not covered:** the actual Meisner proof (not in packet scope); non-fibre-preserving automorphisms at m ≥ 8; transposes, which the count identifies anyway.

## DEPENDENCIES (the Meisner proof must contain these, or M3 is unproved)
- D1. For A with all row quartets closed (Sylvester), fibre recovery cannot use the divisibility-by-m relation, because it is the complete graph. The branch rule must route such A to the high-quartet test.
- D2. The 2+2 mixed-quartet bound must use permutation randomness: the hypergeometric overlap of x and y∘σ. Fair signs cancel there.
- D3. A uniform kernel bound against shared nonconstant eigenvalue words. Sylvester gives 2m words per point, and the F_2 system above is the exact instance.
- D4. log a = O(log² m) uniformly in A, so that the error term is O(√N log² N).

## EXPOSURE
- Small m: every output at m = 4 is nonrigid. At m = 8 with Sylvester A (the unique H(8)), the translation system is square, and the claim's effective range is unknown. Any finite-order statement needs its own certificate.
- M4 "that many" overreaches; it should read "at least that many".
- M5 "common orders" overreaches unless H(m²/8) is added as a hypothesis.

## RESOURCES
Single core, Python 3 in a virtual environment, with nauty's dreadnaut from a local SageMath installation.
- m = 4 runs: about 0.5 CPU-s.
- One m = 8 run (N = 64, 20 samples) ran about 120 s wall before I killed it, without output. Its cost was underestimated: nauty on unrefined Hadamard graphs of order 64 is slow.
- Total is about 120 CPU-s, at the cap. No further compute was run. A survivor check by PID after the kill showed no remaining process.

Script: `meis.py` (session scratchpad; not retained).

Redacted 2026-11-24 for privacy (local paths and session identifiers only); the sealed hash refers to the unredacted original.
