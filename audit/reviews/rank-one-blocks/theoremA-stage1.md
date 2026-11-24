# Cold examination, Stage 1 (isolated), 2026-11-24

Examiner: Claude subagent (Opus 5.5), same model family as the author: INTERNAL, shares model priors.
Input: `audit/STATEMENTS.md` only. No proofs, report, or scripts in this directory were opened before this file was sealed.

```text
STAGE: INITIAL
VERDICT: REFUTED (Lemma Z); NOT-BROKEN (A0, A1, Theorem A, A2, A3, Theorem C, Lemma D (i)-(iv),
         Theorem C outputs list and count bound, Class S1)
EVIDENCE: see per-statement sections below
COVERAGE: see per-statement sections; what remains unchecked is listed at the end
DEPENDENCIES: Geramita–Seberry W(n,k), n ≡ 2 mod 4 => k a sum of two squares (memory, not re-verified);
              existence of an unbiased Hadamard pair of order 36 (memory, not verified);
              Hanani: S(2,4,v) exists iff v ≡ 1,4 mod 12 (memory); Newman: Smith invariants of a
              Hadamard matrix satisfy d_i d_{N+1-i} = N (memory; re-derived below from H^{-1} = H^T/N)
EXPOSURE: STATEMENTS.md (2026-11-24 packet); the cold-examiner protocol; own scripts in the
          session scratchpad (s1checks.py, thmC.py, more.py, lemZ2.py, count.py)
RESOURCES: about 5 short single-core runs, each under 30 s CPU, plus one accidental uncapped loop
           (count.py, no Fisher cap) stopped after ~120 s wall; no witness searches
```

## Lemma Z: REFUTED

Counterexample satisfying every hypothesis, checked exactly (integer arithmetic):

- p = 2, q = 6. G^j = G = [[0,1],[-1,0]] (conference, order 2) for all six j; F^i = C for both i, with C the
  symmetric Paley conference matrix of order 6 (from GF(5)). Then W = G ⊗ C (rows (i,e), columns (r,j)),
  whose zeros are exactly the rook pattern. Take Z = [[C - I, I], [-I, C - I]]: supported exactly on the rook
  pattern, ±1 there. W + Z = [[C - I, C + I], [-C - I, C - I]] is Hadamard of order 12 (it is the Paley II
  matrix with column blocks swapped). C is not diagonally equivalent to a skew matrix (D1 C D2 skew forces
  s_i = -s_j for all i ≠ j, s_i = d1_i d2_i, impossible with three indices; also brute-checked over all
  2^12 sign pairs), and q = 6 ≢ 0 mod 4. The symmetric sentence fails the same way at p = 6, q = 2.
- The final sentence "p, q ≥ 3 gives 16 | pq" is also false. General family: S skew Hadamard of order p,
  G = S - I, K = [[0,1],[-1,0]] ⊗ I_{p/2}, T = S K (Hadamard, and S Tᵀ = S Kᵀ Sᵀ is skew), C symmetric
  conference of order q. Then H = S ⊗ C + T ⊗ I_q satisfies H Hᵀ = p(q-1)I + (S Tᵀ + T Sᵀ) ⊗ C + pI = pq I,
  and H - G ⊗ C = I ⊗ C + T ⊗ I is ±1 exactly on the rook pattern. Checked exactly at
  (p,q) = (4,6), (4,14), (12,6) (pq ≡ 8 mod 16) and (8,6), (8,14). So p = 4, q = 6 gives a Hadamard
  W + Z of order 24 with 16 ∤ 24, and F^i = C is symmetric, not skew-equivalent.
- Interpretation risk: if the intended W uses F^i and G^j that vary with i and j, or an extra hypothesis
  not in the packet, the counterexample might fall outside it. As written (constant families are allowed),
  it satisfies every stated hypothesis.

## A0: NOT-BROKEN

Independent argument (not the author's): 2-adically, a normalized H reduces by row/column operations to
1 ⊕ (C - J) = 1 ⊕ (-2 β_c), so the Smith invariants of H are 1 and 2·(those of β_c). From H^{-1} = Hᵀ/N the
invariants pair as d_i d_{N+1-i} = N; d_1 = 1 and d_2 is even (2×2 minors of a ±1 matrix are 0, ±2).
For v₂(N) = 2 every d_2..d_{N-1} has v₂ = 1, so rk₂ β(normalized H) = N - 2. For v₂(N) = 3 they are 2's and 4's
in equal number, so rk₂ = N/2 - 1. Re-signing rows and columns adds r1ᵀ + 1cᵀ, changing rank by at most 2.
Exact checks: Paley I of orders 12, 20, 24, 32, 44; Paley II of orders 12, 28, 36; 2⊗Paley of orders 24, 40;
Sylvester 16, 32. Normalized rk₂ = N - 2 (N ≡ 4 mod 8) and N/2 - 1 (N ≡ 8 mod 16) in every case; 40 random
re-signings each never went below the bound (minimum observed was bound + 2 or + 3). The bound may not be
tight (I did not find a re-signing reaching N - 4); this is not a defect.

## A1, Theorem A: NOT-BROKEN

Independent argument: on block (x,y), β = u_{xy}1ᵀ + 1 v_{xy}ᵀ. Two rows in the same fibre R_x differ by a
vector in span{1_{C_y}}. So the row space lies in span{one row per x} + span{1_{C_y}}, dimension ≤ |X| + |Y|.
Theorem A is A0 + A1; no fibre-size hypothesis is needed. Not computationally tested beyond the argument.

## A2: NOT-BROKEN

β(H) is the sum of the zero-padded β-blocks; rank is subadditive. This holds for any partition into
rectangles, not just a grid.

## A3: NOT-BROKEN

R ∈ {0, ±2} entrywise and β(H) = β(T) + (R/2 mod 2) over 𝔽₂; rk₂(R/2 mod 2) ≤ rank_ℚ(R/2) = rank_ℚ(R)
(rank of the reduction mod p never exceeds the rational rank). A border of width k makes R supported on k rows
∪ k columns, so rank_ℚ(R) ≤ 2k. Both steps check.

## Theorem C: NOT-BROKEN; hypotheses jointly satisfiable

- Self tile: Σ_x diag(M_L[x,x]) = diag(|M_L[x,x]|) = I/(2u), so tile (x,x) = F⁰_x G_x/(2u), ±1 by hypothesis 1.
- Hadamard: writing every tile as Σ_{L ∋ x,y} M_L[x,y] f_{x,L} g_{y,L}ᵀ, the row orthogonality of G_y gives
  block (x,z) of HHᵀ = a Σ_{L ∋ x,z} (M_L M_Lᵀ)[x,z] f_{x,L} f_{z,L}ᵀ = n·a·I·δ_{xz}. Checks.
- Exact constructions with random signed-permutation re-labellings of (F⁰, G) per point and random
  sign/permutation equivalences of each M_L (so Σ_x has many −1 entries: 6–29 per instance):
  K5 (N = 20), AG(2,3) (N = 36), PG(2,3) (N = 52), 5 trials each, all Hadamard; u = 2, a = 16, K17, bent-function
  pair (Sylvester, diag(bent)·Sylvester), N = 272, Hadamard. Negative control: F⁰ diag(±1 mixed) G at a = 4 gives
  entries {−4, 0, 4}, so the Σ_x re-signing is load-bearing.

## Lemma D: NOT-BROKEN

- Row norm of M_L gives |L| − 1 + 1/a = n/a, so all lines have the same size k+1 and n = ak + 1 for every u,
  not only u ≥ 2 (D(i) states it under u ≥ 2; true but the hypothesis is not needed for that part).
- (i) off-diagonal: (KKᵀ)_{ij} + (K_ij d_j + d_i K_ji)/(2u) = 0 with the second term in {0, ±1/u}; for u ≥ 2 it must
  vanish, giving K conference and KD skew; skew conference orders are 2 or ≡ 0 mod 4.
- (ii) u = 1, |L| odd: (KKᵀ)_{ij} is odd, so KD is symmetric and S = KD satisfies S² + S = (|L|−1)I. Integral
  multiplicities force 4|L|−3 = s² with s | 3, so |L| ∈ {1, 3}; |L| = 3 gives M ~ ±(J − (3/2)I). |L| even gives the
  skew-conference type. At a = 4, Fisher (b ≥ v) gives k + 1 ≤ a = 4, so |L| ∈ {2,3,4}: n = 5, 9, 13, N = 20, 36, 52;
  each realized above. List complete.
- (iii) K symmetric with KD skew forces d_j = −d_i for all i ≠ j: impossible for |L| ≥ 3.
- (iv) n = ak + 1 odd, v₂(a) = 2 + 2v₂(u). Checks.

## Theorem C outputs: NOT-BROKEN (conditional)

Enumeration with Fisher (k+1 ≤ a), the line-size rule, and integrality of b: u odd, N ≤ 10⁴ gives exactly
[20, 36, 52, 1332, 3924]. 9108 (u = 3, k+1 = 8) fails because b = 253·36/8 is not an integer. (u even gives
272, 784, 1808, 2832, 3856, 4160; outside the stated u-odd scope.) 1332 and 3924 depend on an unbiased Hadamard
pair of order 36 (unverified) and, for 3924, on S(2,4,109) (109 ≡ 1 mod 12, Hanani). Count bound: pairs (u,k)
with Fisher alone number ≈ √x/3 analytically; observed 329, 3282, 33196 at x = 10⁶, 10⁸, 10¹⁰ against
√x/3 = 333, 3333, 33333. With the line rules, 63, 307, 1368. Bound valid and loose; it relies on Fisher, without
which the count is linear in x.

## Class S1: NOT-BROKEN

The equivalence is immediate for any ±1 matrix: a 2×2 ±1 block is rank one iff d = abc. N ≡ 4 mod 8 is not
needed for it. Untwisted: A ± B block-diagonalize H, (A+B)/2 is W(n, n/2); with N = 4p, n = 2p ≡ 2 mod 4 and
p ≡ 3 mod 4 prime is not a sum of two squares. Depends on the cited W(n,k) theorem. Notation: the packet uses
both N and "order 2n" without saying N = 2n.

## Unchecked

Lemma Z under any reading other than the literal packet; whether the A0 bounds are attained; the two
memory citations (order-36 unbiased pair, W(n,k) sum-of-two-squares theorem); the de Launey–Gordon baseline is
not in the packet.

Redacted 2026-11-24 for privacy (local paths and session identifiers only); the sealed hash refers to the unredacted original.
