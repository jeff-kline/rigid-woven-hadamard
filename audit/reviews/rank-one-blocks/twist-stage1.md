# Cold exam, Stage 1 (statements only): sharp rank-one blocks bound and unavoidable twist

Date: 2026-11-24. Examiner: Claude (Opus 5.5) subagent. Same model as the author's agents.

```text
STAGE: INITIAL
VERDICT: NOT-BROKEN for Theorem th:tworank (sharp form), for each claim in the
         consequences paragraph after it, and for Corollary cor:twist.
EVIDENCE: twist_stage1_checks.py (this folder; independent implementation,
          runs in 0.7 s on one core) and the independent hand derivation below.
COVERAGE: see "Coverage".
DEPENDENCIES: (D1) Newman/Wallis Smith-form duality d_i d_{N+1-i} = N with
          d_1 = 1 for a Hadamard matrix (standard; not re-derived);
          (D2) weighing matrix W(n,w), n = 2 mod 4 => w a sum of two squares
          (classical; I re-derived it from Hasse-Minkowski, see H3; the cited
          page of Christian-Shader was not opened);
          (D3) uniqueness of the order-12 Hadamard class (standard; used only
          to extend check 3 from two matrices to all of order 12).
EXPOSURE: INTERNAL-NONINDEPENDENT. Read: paper/main.tex lines 1-60, 234-249
          (statement), 255-262 (consequences paragraph, definitions of theta,
          twisted, untwisted), 274-288 (Paley II remark, corollary statement).
          Leaked before sealing: a grep for "twisted|theta" printed main.tex
          lines 264-272 (Proposition prop:sizetwo and its proof) and line 290
          (the full proof of cor:twist). The task brief named the proof step
          "negate the first row and column, rank rk2 B' + 2". I also saw the
          first 30 lines of audit/reviews/rank-one-blocks/CREDIT.md (Lander's
          code dimensions) and the header of sizetwo-stage1.md (an earlier
          examiner called a previous version "correct but weak by 4").
          Not read: proof of th:tworank (lines 250-254), code/, CLAIMS.md,
          the stage-2 files of earlier reviews.
RESOURCES: about 2 CPU seconds total for the checks, one core; no searches.
```

## Hand derivation (independent of the paper's proof, which I did not read)

H1. Upper bound. A real rank-one sign block is `eps f g^T`, so over F_2 its beta is
`e + a_i + b_j`. The vectors a, b depend on the block, not only on the fibre. Still,
for row i in fibre R_x, row i of beta(H) equals `c_x + sum_y a^{(y)}_i 1_{C_y}`, where
c_x collects the b-parts and constants of the blocks in row fibre x. Hence the row
space of beta(H) lies in `span{c_x} + span{1_{C_y}}`, and `rk2 beta(H) <= |X|+|Y|`.
Signing rows and columns keeps every block rank one, so this holds for every signed form.

H2. Lower bound. Normalize H; its core M ((N-1)x(N-1), 0/1) satisfies `H ~ 1 (+) (-2M)`
over Z, so by D1 the 2-rank of M is N-2 when N = 4 mod 8 and N/2-1 when N = 8 mod 16.
Row and column sums of M are N/2, even, so `1^T M = 0 = M 1` mod 2, while `1.1 = N-1` is odd.
So 1 is in neither the row nor the column space of M. Negating the first row and
column gives `beta' = [[0, 1^T],[1, M]]`, whose 2-rank is then `rk2 M + 2`: N, resp.
N/2+1. With H1 this gives both bounds. For N = 4 mod 8 the bound N is met (Paley II
pairings, check 2), so it is sharp there. I did not test sharpness of N/2+1, and the
statement does not claim it.

H3. Corollary. Theta is well defined on rank-one 2x2 blocks: T11 T22 = T12 T21.
Theta = +1 together with rank one forces `[[a,b],[b,a]]`, so an untwisted pairing gives
`[[A,B],[B,A]]` after signing and permuting. Conjugating by `K = [[I,I],[I,-I]]` gives
`(A+B)(A+B)^T = N I`. So `U = (A+B)/2` is a W(N/2, N/4). For N = 12 mod 16, N/2 = 2 mod 4
and N/4 = 3 mod 4. By Hasse-Minkowski and Witt cancellation (w I_4 ~ I_4 always), a
W(n,w) with n = 2 mod 4 forces `w I_2 ~ I_2` over Q, so w is a norm from Q(i). That
means a sum of two squares, which 3 mod 4 is not. Paley II at q = 8t+5 gives
N = 16t+12, and there are infinitely many such primes by Dirichlet.

## Exact checks (twist_stage1_checks.py)

1. rk2 of beta after normalizing and after negating the border. For every N = 4 mod 8
   and N = 8 mod 16 tested, the border-negated value equals the claimed bound and the
   normalized value is 2 less. Matrices: Sylvester 8; Paley I q = 11, 19, 23, 43
   (N = 12, 20, 24, 44); Paley II q = 5, 13, 17 (N = 12, 28, 36); Paley I(11)xH2,
   Paley II(5)xH2 (24); Paley I(19)xH2 (40). Sylvester 16, 32 and Paley I(31) (16 | N)
   were also run, with no claim: their 2-ranks are 6, 7, 17.
2. Paley II involution pairings, q = 5, 13: the largest rk2 over 200 random signings
   is exactly N = |X|+|Y|, consistent with H1 and showing the bound is met.
3. Exhaustive at N = 12, on Paley II(5) and on Paley I(11) separately. There are 10395
   row pairings. For each, I listed all column pairings that make every block rank
   one (same signature of row-pair products). Each matrix has 495 rank-one pairings,
   and **0 are untwisted**. By D3 this covers every Hadamard matrix of order 12.
4. Controls. Sylvester 16, pairing {i, i^1}: rejected (rank-two blocks). Pairing
   {i, i^3}: rank one and detected as untwisted. After signing to theta = +1 and
   permuting, it has the [[A,B],[B,A]] form, and U = (A+B)/2 is a W(8,4). So the
   untwisted detector and the K-step reduction both fire on a real positive case.

## Coverage and gaps

- No counterexample was found to the theorem, the consequences paragraph or the corollary.
- Consequences paragraph, checked by hand: all fibres have size 2 (N = 4 mod 8, no
  singletons); 16 | N when all fibres have size >= 4 (N = 1, 2 cannot occur;
  4 mod 8 gives |X|+|Y| <= N/2 < N; 8 mod 16 gives <= N/2 < N/2+1); repair rank >= N/3
  (fibres >= 3 give |X|,|Y| <= N/3; rational rank of R/2 >= its mod-2 rank); k >= N/6
  (a support in k rows and k columns has rank <= 2k). No defect found.
- Check 3 enumerates only partitions into pairs. Excluding fibres of size >= 3 without
  singletons at N = 12 relies on the theorem itself (H1+H2), not on enumeration.
- N = 4 mod 16 (e.g. 20) is not covered by the corollary. I did not test whether
  untwisted pairings exist there. Scope remark, not a defect: the same proof
  excludes untwisted pairings whenever N = 4 mod 8 and N/4 is not a sum of two
  squares, e.g. N = 84 (N/4 = 21), which is 4 mod 16.
