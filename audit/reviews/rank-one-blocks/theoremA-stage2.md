# Cold examination, Stage 2 (proof audit), 2026-11-24

Examiner: the same Claude subagent (Opus 5.5) that wrote Stage 1. INTERNAL, NONINDEPENDENT of the author's model.
Stage 1 sealed before any exposure: `audit/stage1-initial.md`,
sha256 `8548ea82eaefdea2c21f97ca91ff39162a5d20d0ffd6c1df0124a23ca6efab1b`.
Reviewed: `FABLE-REPORT.md` (282 lines, §§1–4 and §6; §5 skimmed), `fable_rank_checks.py`, `fable_mc_construct.py`,
`fable_mc36_check.py` as on disk 2026-11-24. All three scripts were rerun (venv interpreter, `-I`); all assertions pass.
Not opened: CREDIT.md, PRIOR-ART.md, SEED.md, TRANSPOSE-AND-RANK-REVIEW.md.

## Summary

| Statement | Verdict | Defect |
|---|---|---|
| A0 | VERIFIED | none |
| A1 | VERIFIED | none |
| Theorem A | VERIFIED | none |
| A2 (mosaics) | VERIFIED | proof not written (erratum); the "dual family" paragraph is not audited |
| A3 | VERIFIED | one step left implicit (erratum) |
| Theorem C | VERIFIED | none; the Σ_x ≠ ±I case is now checked |
| Lemma D (i)–(iii) | VERIFIED | minor errata |
| Lemma D (iv) | VERIFIED as stated in the packet | the report's broader bullet-4 claim is a GAP |
| Theorem C outputs list ≤ 10⁴ | VERIFIED, conditional on two inputs | count figures omit N = 36 (erratum) |
| Theorem C count bound | VERIFIED | none |
| **Lemma Z** | **REFUTED** | proof drops the ZZᵀ term (§4 M2, line 223) |
| Class S1 | VERIFIED, conditional on the classical W(n,k) criterion | minor errata |

---

## A0

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
CLAIM: H Hadamard of order N: rk₂ β(H) ≥ N − 4 if N ≡ 4 mod 8; ≥ N/2 − 3 if N ≡ 8 mod 16.
EVIDENCE: Report §2, lines 70–74, step by step.
  - Hᵀ = N·H⁻¹ gives d_i d_{N+1−i} = N. Correct (Smith form of Hᵀ is N·(Smith form of H)⁻¹ reversed).
  - H ≡ J mod 2 has rank 1, so exactly one invariant is odd (d₁). Correct.
  - v₂(N) = 2: pairing v₂(d_i) + v₂(d_{N+1−i}) = 2, only d₁ has v₂ = 0, so only d_N has v₂ = 2 and all
    others have v₂ = 1. v₂(N) = 3: others lie in {1, 2}, paired, so (N−2)/2 of each. Correct.
  - Normalize, subtract row 1, then clear column 1: H ~ [1] ⊕ (C − J) = [1] ⊕ (−2B′). Correct.
  - #(v₂(d_i) = 1, i ≥ 2) = #(odd Smith invariants of B′) = rk₂ B′: N − 2, resp. N/2 − 1. Correct.
  - Re-signing adds r·1ᵀ + 1·cᵀ over 𝔽₂: rank change ≤ 2. Correct.
COVERAGE: every step. Independent Stage 1 derivation reached the same normalized ranks. Script output
  reproduced (normalized ranks equal predictions at 13 matrices; random re-signings ≥ prediction − 2).
DEPENDENCIES: none beyond the Smith normal form.
ERRATA: fable_rank_checks.py labels a 2⊗Paley I(20) matrix "Paley II 40?" (cosmetic). Tightness of the
  −2 re-signing slack is not claimed and not established; no re-signing in either examiner's samples reached it.
EXPOSURE: report rev. on disk 2026-11-24; stage1-initial.md (sha256 8548ea82…ab1b).
RESOURCES: < 5 s CPU.
```

## A1 and Theorem A

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
CLAIM: (A1) rank-one tiling ⇒ rk₂ β(M) ≤ |X| + |Y|; (A) A0 + A1, no fibre-size hypothesis.
EVIDENCE: Report lines 79–80. β[(x,e),(y,r)] = η_xy + φ_xy(e) + γ_xy(r) is the bit form of f gᵀ. Column (y,r)
  = c_y + Σ_x γ_xy(r) 1_{R_x} with c_y[(x,e)] = η_xy + φ_xy(e), independent of r. So the column space lies in
  span{c_y} + span{1_{R_x}}. Correct. (Stage 1 used the row form of the same argument.) Theorem A follows
  directly; no step uses fibre sizes, squareness, or the Gram structure.
COVERAGE: complete. Script check (rk₂ ≤ p + q on four exact weaves) rerun: passes.
DEPENDENCIES: A0.
ERRATA: none.
```

## Corollary A2 (mosaics)

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED (for the packet statement)
CLAIM: block partition, block i with its own rank-one tiling ⇒ Σ_i (|X_i| + |Y_i|) ≥ N − 4 (resp. N/2 − 3).
EVIDENCE: The report (lines 92–93) states it with no proof. The routine argument: β(H) = Σ_i (β of block i,
  zero-padded); rank is subadditive; A1 applies to each rectangular block. Holds for any partition into
  rectangles, not only a grid.
COVERAGE: packet statement complete. NOT audited: the "column-split dual family" sentences (lines 94–97);
  "the two partitions coincide" is asserted, not proved. INCOMPLETE for that add-on.
ERRATA: add the one-line subadditivity proof.
```

## Corollary A3 (correctors, borders)

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
CLAIM: H = T + R, T rank-one-tiled ⇒ rank_ℚ R ≥ N − 4 − |X| − |Y| (resp. N/2 − 3 − …); border of width k
  needs 2k ≥ N − 4 − |X| − |Y|.
EVIDENCE: Report lines 98–101. Unstated step: R ∈ {0, ±2} and β(H) = β(T) + (R/2 mod 2) over 𝔽₂, so
  rk₂ β(H) ≤ rk₂ β(T) + rk₂(R/2 mod 2). Then rk₂ of a reduction ≤ rank_ℚ(R/2) = rank_ℚ R. The 𝔽₂ vs ℚ
  inequality points the right way. Border: R supported on k rows ∪ k columns gives rank ≤ 2k. "Fibres ≥ 3 ⇒
  rank ≥ N/3 − 4": |X|, |Y| ≤ N/3, so N − 4 − 2N/3. Correct.
COVERAGE: complete.
ERRATA: write out β(H) = β(T) + (R/2 mod 2).
```

## Theorem C

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
CLAIM: packet Theorem C (a = 4u², unbiased pair, linear space with a lines per point, line matrices M_L).
EVIDENCE: Report lines 129–135. With flags (x,L), S = ⊕_L M_L after ordering flags by line, so
  SSᵀ = (n/a)I. Block (x,y) of F̂ S Ĝ is Σ_{L∋x,y} M_L[x,y] f_{x,L} g_{y,L}ᵀ, which equals the stated tiles.
  F_x = F⁰_xΣ_x is still Hadamard, so F̂F̂ᵀ = ĜĜᵀ = aI and HHᵀ = a·(n/a)·a·I = NI. Self tile:
  Σ_x diag(M_L[x,x]) = I/(2u), so D_x = F⁰_xG_x/(2u), ±1 by hypothesis 1. Correct.
COVERAGE: algebra complete. §6 item 2 is confirmed: the report's scripts exercise only Σ_x = +I
  (fable_mc_construct.py: zero-diagonal K2, K4 with self tile +FG/(2u)) and Σ_x = −I (fable_mc36_check.py).
  Discharged by the Stage 1 checks: K5, AG(2,3), PG(2,3) with random equivalences of each M_L (6–29 entries
  of Σ_x equal to −1 per instance) and N = 272 (u = 2) are all Hadamard. Negative control: without Σ_x the
  self tile has entries {−4, 0, 4}.
DEPENDENCIES: none for the implication. Hypotheses are jointly satisfiable (N = 20, 36, 52, 272 built).
ERRATA: none.
```

## Lemma D

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED for (i), (ii), (iii), (iv) as stated in the packet; GAP in the report's broader bullet 4.
CLAIM: packet Lemma D (i)–(iv).
EVIDENCE:
  (i) Lines 138–140. Off-diagonal: (KKᵀ)_xy + (K_xy d_y + K_yx d_x)/(2u) = 0, where the first term is an integer
      and the second lies in {0, ±1/u}. For u ≥ 2 both vanish: K conference, KD skew, so KD + I is skew Hadamard and
      |L| ∈ {2} ∪ 4ℤ. Same size from the diagonal: |L| − 1 + 1/a = n/a. Correct.
  (ii) Lines 141–146. Parity of (KKᵀ)_xy = parity of |L|. Even: forced 0, skew-conference type. Odd: the term is
      ±1 on every pair, so K_xy d_y = d_x K_yx, K′ = KD symmetric, KKᵀ = K′², MMᵀ = K′² + K′ + I/4, so
      K′² + K′ = (|L| − 1)I. Trace 0 and integral multiplicities: s irrational forces equal multiplicities and
      |L| even (contradiction); s an odd integer needs s | 3. s = 3 gives |L| = 3, K′ ~ I − J under switching,
      M = ((3/2)I − J)D. Fisher gives k + 1 ≤ a = 4, so N ∈ {20, 36, 52}. Correct.
  (iii) Lines 147–149. K symmetric with K_xy t_y + K_yx t_x = 0 gives t_x = −t_y on all pairs, impossible for
      |L| ≥ 3. Applies after reducing any order-≡ 2 mod 4 conference matrix to symmetric form by equivalence.
      Correct.
  (iv) Packet form: n = ak + 1 is odd, v₂(a) = 2 + 2v₂(u). Immediate.
  GAP: report bullet 4 (lines 150–152) claims more: any block-diagonal corrector ⊕T_x "must be diagonal in the
      port basis (each e_L is an eigenvector of T_x)", and "uniform modulus" forces τ = 1/√a. The eigenvector
      claim is asserted without argument, and "uniform modulus" is an added assumption. This does not affect the
      packet statement but does affect the §0 sentence "never gives v₂ = 3 except by doubling" if read beyond
      the Theorem C class.
COVERAGE: all bullets.
ERRATA: (a) Uniform line size holds for every u, not only u ≥ 2 (from the diagonal of MMᵀ). (b) s = 1 (|L| = 1)
  is omitted; harmless, since it forces n = 1.
```

## Theorem C outputs and count

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED (list conditional on inputs; count unconditional)
CLAIM: u odd outputs ≤ 10⁴ are 20, 36, 52, 1332, 3924; admissible orders ≤ x number ≤ √x/3 + O(x^{1/3}).
EVIDENCE: Independent enumeration in Stage 1 (Fisher, line rule, integral b) gives exactly this list; 9108
  (u = 3, k + 1 = 8) is excluded because b is not integral. Count: #k ≤ min(4u², x/16u⁴) per u (Fisher k < a;
  N ≥ a²k). Summing, both ranges give √x/6, the crossover at u ≍ x^{1/6}, and rounding gives O(x^{1/3}).
  Correct. Observed (Fisher only): 329, 3282, 33196 at 10⁶, 10⁸, 10¹⁰ vs √x/3 = 333, 3333, 33333.
DEPENDENCIES: 1332 and 3924 need a real unbiased Hadamard pair of order 36. This is cited [memory]
  (Holzmann–Kharaghani–Orrick 2010) and is UNVERIFIED here; the credit check owns it. 3924 also needs
  S(2,4,109) (Hanani, 109 ≡ 1 mod 12; from memory, standard). Both orders are known anyway (Paley I), so no
  novelty depends on the citation.
ERRATA: fable_mc_construct.py enumerates k ∈ {1} ∪ {3, 7, 11, …} and so omits the u = 1, |L| = 3 line
  (N = 36). Its counts "10, 62, 306, 1367" (report line 191) should be 11, 63, 307, 1368 if 36 is admissible,
  and the printed "outputs with u odd" list lacks 36 although the report's table includes it. The upper bound
  is unaffected.
```

## Lemma Z

```text
STAGE: PROOF-AUDIT
VERDICT: REFUTED
CLAIM: p even, q ≥ 3 ⇒ every F^i is diagonally equivalent to a skew matrix and q ≡ 0 mod 4 (and the transpose);
  hence p, q ≥ 3 ⇒ 16 | pq.
EVIDENCE:
  Counterexample (Stage 1, rechecked): S is a skew Hadamard matrix of order p, G = S − I, K = [[0,1],[−1,0]] ⊗ I_{p/2},
  T = SK, C a symmetric conference matrix of order q. Then H = S ⊗ C + T ⊗ I is Hadamard (S Tᵀ is skew), and
  W = G ⊗ C (F^i = C, G^j = G), with Z = H − W = I ⊗ C + T ⊗ I being ±1 exactly on the rook pattern. Exact checks:
  (p,q) = (2,6), (4,6), (4,14), (12,6) (and (6,2) transposed). C is symmetric of order ≡ 2 mod 4, not diagonally
  equivalent to skew. (4,6) gives order 24, 16 ∤ 24, so the "hence" sentence is false too.
  Defect location: FABLE-REPORT.md §4 M2, Lemma Z proof, first sentence (line 223): "H Hadamard needs
  WZᵀ + ZWᵀ = 0." The correct condition is WZᵀ + ZWᵀ + ZZᵀ = (p + q − 1)I. The ZZᵀ entry at rows (i,e), (i,e′)
  is the inner product of rows e, e′ of the diagonal block Z[(i,·),(i,·)] (q terms), which need not vanish.
  In the counterexample, ZZᵀ has off-diagonal entries ±2 and WZᵀ + ZWᵀ ≠ 0; only the sum vanishes.
  The parity check in fable_mc_construct.py ("s_e odd") tests the surviving ingredient, not the dropped term.
  Internal inconsistency: line 229 ("p = 2 … is ordinary doubling") concedes p = 2 instances, which the
  statement covers, and lines 230–232 (H = A ⊗ C + B ⊗ I, B = AK) are this counterexample whenever A is skew
  Hadamard (A ⊗ C = (A − I) ⊗ C + I ⊗ C is a zero-carrying weave).
  Same error in §3 (line 113): "the completion Z is an anti-amicable disjoint W(N, N − w)" is false in general.
COVERAGE: every step. Repaired version: if one adds the hypothesis ZZᵀ = (p + q − 1)I (Z itself a weighing
  matrix, i.e. an OD(N; w, N − w)), the rest of the proof holds: s_e is odd, s_{e′} = −ω(e,e′)s_e, and
  diag(t)·F^i is skew. VERIFIED for that repaired statement only.
DEPENDENCIES: none.
ERRATA / downstream: §0 row 3 ("No for v₂(N) ≤ 3. PROVED (Lemma Z)") and the M2 heading ("DEAD for v₂ ≤ 3")
  are unsupported. What is established is narrower: at v₂ = 3 (p ≡ 0, q ≡ 2 mod 4) such weaves exist and are
  Williamson-type A ⊗ C + B ⊗ I (a collapse, not a kill). The actual M2 target, p ≡ q ≡ 2 mod 4 with both ≥ 6
  (v₂(N) = 2), is UNRESOLVED: the counterexample family does not reach it, and no proof covers it.
  (p = 2, q ≡ 2 mod 4 gives v₂ = 2 only as doubling.)
```

## Class S1

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED (untwisted nonexistence conditional on the classical W(n,k) criterion)
CLAIM: 2×2 tiling ⇔ H = [[A, B], [C, A∘B∘C]]; untwisted [[A, B], [B, A]] impossible at 4p, p ≡ 3 mod 4 prime.
EVIDENCE: Report lines 240–248. A ±1 2×2 block is rank one iff d = abc; reordering pairs gives the form. With
  U = (A + B)/2 and V = (A − B)/2, H = U ⊗ J₂ + V ⊗ [[1,−1],[−1,1]], and AAᵀ + BBᵀ = 2nI, ABᵀ + BAᵀ = 0 give
  UUᵀ = VVᵀ = (n/2)I: complementary W(n, n/2). n = 2p ≡ 2 mod 4 and p ≡ 3 mod 4 is not a sum of two squares.
DEPENDENCIES: "W(n,k), n ≡ 2 mod 4 ⇒ k a sum of two squares" is cited as "classical" with no reference;
  not re-verified here (standard; Geramita–Seberry). The twisted-Θ equivalence (P H Q = H ∘ (Θ ⊗ J₂)) and the
  S1 search results were not audited.
ERRATA: N ≡ 4 mod 8 is not needed for the equivalence, which holds for every ±1 matrix of even order; the
  packet uses N and "order 2n" without stating N = 2n.
```

## §6 attack list

1. A0 Smith step: checked, correct (see A0).
2. Re-signing Σ_x: the report's own checks use only Σ_x = ±I (confirmed in code). Nontrivial Σ_x checked in
   Stage 1: Hadamard in all 15 + 1 instances. The algebraic proof covers it.
3. Lemma D, u ≥ 2 integrality: correct.
4. [memory] citations, UNVERIFIED, not researched here (credit check owns them):
   - Unbiased Hadamard pair of order 36 (Holzmann–Kharaghani–Orrick 2010), together with the attached claim
     "they also bound the number at 2 for a = 4u², u odd". Load-bearing only for 1332 and 3924 as Theorem C
     outputs; both orders are already known.
   - de Launey–Gordon baseline x·exp(−C(log x)^{2/3}). Load-bearing only for the "not denser" comparison,
     which Paley I alone (≍ x/log x) already settles.
5. Missing from the list: Lemma Z, which is where the defect is.

RESOURCES (Stage 2): three report scripts (~2 s CPU total) and one gap demonstration (< 1 s), single core.
