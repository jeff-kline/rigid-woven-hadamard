# Cold exam, Stage 2 (proof audit): sharp rank-one blocks bound and unavoidable twist

Date: 2026-11-24. Examiner: Claude (Opus 5.5) subagent, the same agent that wrote the
sealed Stage 1 (twist-stage1.md, sha256 e68b13c1b6e8673cfb6c15334f7e31038dd99273db49f768ecc99907941afec6;
checks script sha256 1360d123069a2f2bfd0dd6367c57e4157160e3e3fde615919fd77bc7d030ce75, in twist-stage1.sha256).

## (a) Theorem th:tworank and the consequences paragraph

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
CLAIM: main.tex lines 246-249. H Hadamard of order N, with rows and columns partitioned
       so that every block has real rank one. Then |X|+|Y| >= N if N = 4 mod 8, and
       |X|+|Y| >= N/2+1 if N = 8 mod 16. Also the consequences paragraph, lines 255-256.
EVIDENCE: line-by-line check below; it agrees with the independent Stage-1 derivation
       (H1, H2) and with exact ranks on 13 matrices (Stage-1 check 1).
COVERAGE: every sentence of the proof (lines 250-254) and of the consequences paragraph.
DEPENDENCIES: all discharged inside the proof. The Smith duality is derived from
       H^T = N H^{-1}. The Orrick/Lander citation is corroborative, not load-bearing.
ERRATA: none required. Optional: one clause justifying "rank rk2 B' + 2" (E1).
EXPOSURE: main.tex lines 1-60, 234-292, 304-346 (bibliography); Christian-Shader PDF.
RESOURCES: hand audit; no extra computation beyond Stage 1.
```

Line-by-line.

1. "A sign block of rank one is eps f g^T": correct. A real rank-one matrix with
   entries +-1 is u v^T, and both u and v can be rescaled to sign vectors.
2. `beta_{(x,e),(y,r)} = eta_xy + phi_xy(e) + gamma_xy(r)` (mod 2): this is the log_{-1}
   of `eps f_e g_r`. Correct.
3. "Column (y,r) of beta is c_y + sum_x gamma_xy(r) 1_{R_x}, with c_y independent of r":
   take `(c_y)_{(x,e)} = eta_xy + phi_xy(e)`. Correct. So the column space lies in
   `span{c_y} + span{1_{R_x}}`, and rk2 beta <= |X|+|Y|. Correct. It is the transpose of
   my Stage-1 H1.
4. Signing preserves rank one, so the upper bound holds for every signed form. Correct.
5. Normalize, then subtract the first row and the first column. With
   `H_core = J - 2B'` this gives `[1] (+) (-2B')` over Z. Correct.
6. Since H^T = N H^{-1}, the invariants of H are the N/d_{N+1-i}. As H^T has the same
   Smith form as H, d_i d_{N+1-i} = N. Correct.
7. "H = J mod 2, so exactly one invariant is odd": the 2-rank of H equals the number of
   odd invariants, and here it is rk2 J = 1. Correct.
8. The valuation patterns are forced by v_i + v_{N+1-i} = v_2(N), v_1 = 0, v_i >= 1 for
   i >= 2, and monotonicity. For N = 4 mod 8: 0, then N-2 ones, then 2. For N = 8 mod 16:
   0, then (N-2)/2 ones, then (N-2)/2 twos, then 3. Correct.
9. "Invariants of B' are d_i/2 for i >= 2": the Smith form of [1] (+) 2D is
   diag(1, 2s_1, ...), already a divisibility chain. Correct. Hence rk2 B' = N-2,
   respectively (N-2)/2. This matches the computed normalized ranks in Stage-1 check 1.
10. Negating the first row and column gives `beta = [[0,1^T],[1,B']]`. The corner entry
    is negated twice and stays +1. Correct.
11. Row weights of B' are N/2, from orthogonality to the all-ones first row. Column
    weights are N/2 by the same argument for columns (H^T H = NI). N/2 is even in both
    cases, and 1^T 1 = N-1 is odd. So 1 is orthogonal to the column space of B' (because
    1^T B' = 0) but not to itself, so it does not lie in that space. The row space is
    the same. Correct.
12. "this beta has rank rk2 B' + 2". (E1) The proof gives no reason, but the step is
    standard and I checked it. Since 1 is not in col(B'), [1 | B'] has rank rk B'+1.
    The top row (0, 1^T) is not in the row space of [1 | B'], because that would need
    c^T B' = 1^T. So the rank is rk B'+2: N, respectively N/2+1. Correct.
    Stage-1 check 1 confirms the +2 exactly on all 13 matrices.
13. Orrick/Lander: the dimensions N-1 and N/2 are "equivalent". The code of the matrix
    normalized only on columns is span(rows of the fully normalized beta) + <1_N>. 1_N
    is not in that span, because every such row has first coordinate 0. So the
    dimension is rk2 B'+1. Correct. CREDIT.md reports Orrick Thm 4.3 read at source; I
    did not reopen Orrick. The claim is not load-bearing.

Consequences paragraph (lines 255-256), every claim checked:
- No constraint when 16 | N: correct as a description of the statement.
- N = 4 mod 8 with no singletons: |X|, |Y| <= N/2, so with sum >= N every fibre has
  size exactly 2. Correct.
- N = 8 mod 16 with fibres >= 4: |X|+|Y| <= N/2 < N/2+1. Correct. "Hence ... 16 | N":
  Hadamard orders are 1, 2 or 0 mod 4; the cases 1, 2, 4 mod 8 and 8 mod 16 are all
  excluded. Correct.
- Repair: R = H - T has entries in {0, +-2}, and `beta(H) = beta(T) + R/2` (mod 2)
  holds entrywise (both cases checked). It survives joint signing because D1 R D2 / 2
  reduces to the same pattern mod 2. The rational rank of R/2 is at least its mod-2
  rank, so rank R >= N - |X| - |Y| (resp. N/2+1-|X|-|Y|). Correct.
- Fibres >= 3 at N = 4 mod 8: |X|, |Y| <= N/3, so rank R >= N/3. Correct.
- "Supported on k rows and k columns" gives rank <= 2k under either reading (a k x k
  submatrix gives <= k; a cross of k rows plus k columns gives <= 2k). So k >= N/6.
  Correct, though conservative under the submatrix reading, where k >= N/3 would follow.

## (b) Corollary cor:twist

```text
STAGE: PROOF-AUDIT
VERDICT: VERIFIED
CLAIM: main.tex lines 285-287. For N = 12 mod 16, every partition of an order-N Hadamard
       matrix into rank-one blocks without singleton fibres is a twisted pairing,
       invariantly under signed permutations. Paley II with q = 5 mod 8 gives
       infinitely many such orders.
EVIDENCE: line-by-line check below; Christian-Shader p. 2 read at source (fetched PDF,
       pdftotext); Stage-1 exhaustive check at N = 12 (495 rank-one pairings on each of
       two order-12 matrices, 0 untwisted) and a positive control for the K-step
       (Sylvester 16, untwisted, yields a W(8,4)).
COVERAGE: lines 261 (definitions) and 289-291 (proof); the cited source sentence.
DEPENDENCIES: Theorem th:tworank (verified in (a)); W(n,w) with n = 2 mod 4 => w a sum of
       two squares (source verified; also re-derived via Hasse-Minkowski in Stage 1 H3);
       Dirichlet's theorem; Paley II is Hadamard for prime q = 1 mod 4 (standard, and
       checked for q = 5, 13, 17 in Stage 1).
ERRATA: none required. Optional notes O1-O3 below.
EXPOSURE: as in (a).
RESOURCES: one PDF fetch (EJC mirror URL from the bibitem), no searches.
```

Line-by-line.

1. "By Theorem th:tworank every fibre has size two": N = 12 mod 16 implies N = 4 mod 8.
   Correct.
2. Untwisted gives [[A,B],[B,A]] (definition paragraph, line 261). theta = T11 T22 is
   well defined on rank-one blocks, since T11 T22 = T12 T21 = f1 f2 g1 g2. Negating a
   row of a pair flips theta along that row pair, so "untwisted" is equivalent to
   Theta = u v^T. Correct. Once theta = +1, rank one gives T22 = T11 and T12 = T21.
   Placing the first member of each pair at i and the second at i+N/2 gives
   [[A,B],[B,A]]. If the order within a pair is swapped, the block becomes [[b,a],[a,b]],
   the same shape, so the order does not matter. Correct.
3. KHK = diag(2(A+B), 2(A-B)): recomputed. KH = [[A+B, A+B],[A-B, B-A]], then times K.
   Correct.
4. `(KHK)(KHK)^T = K H K^2 H^T K = 2N K^2 = 4N I`. Correct, since K is symmetric.
   The (1,1) block gives 4(A+B)(A+B)^T = 4N I, so U U^T = (N/4) I with U = (A+B)/2 in
   {0,+-1}. Correct.
5. Order N/2 = 6 mod 8, hence 2 mod 4; weight N/4 = 3 mod 4. Correct.
6. Citation. Christian-Shader, EJC 11 (2004) #N1, top of p. 2: "If n = 2 mod 4, then
   necessarily w is a sum of two squares ... a number theoretic consequence of applying
   Witt's cancellation to the congruence W W^T = wI." The quoted condition is exact and
   so is the page. Then 3 mod 4 is not a sum of two squares (squares are 0 or 1 mod 4).
   Correct. (O1) Christian-Shader state this as known background, not as their result.
   The primary source is Geramita-Pullman-Wallis / Geramita-Seberry. The citation is
   accurate as a pointer, but crediting the primary source would be better form.
7. Paley II: a prime q = 8t+5 is 1 mod 4, and N = 2(q+1) = 16t+12. Dirichlet gives
   infinitely many such primes. Correct. Non-vacuity: Prop. prop:sizetwo produces
   no-singleton rank-one partitions there (e.g. q = 5, 13), so the corollary has
   instances. Stage 1 check 3 shows that at N = 12 such partitions exist (495) and all
   are twisted.
8. "whatever rows and columns are permuted and signed": twistedness is invariant under
   signing by definition, and permutation only relabels the pairs. Correct.

Optional notes (not correctness defects):
- O1: credit the sum-of-two-squares condition to its primary source as well (see 6).
- O2: the same proof excludes untwisted pairings whenever N = 4 mod 8 and N/4 is not a
  sum of two squares. That adds orders 4 mod 16, e.g. N = 84 (N/4 = 21) and
  N = 132 (N/4 = 33). Possible generalization.
- O3: the corollary also needs the fact that an untwisted pairing can be conjugated by K
  only after both sides use the "first member / second member" split. The proof does
  this implicitly through the definition paragraph. Adequate as written.
