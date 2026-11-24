# Cold exam, Stage 1 (statements only): rank-one blocks and fibres of size two

Date: 2026-11-24. Examiner: Claude (Opus 5.5) subagent.

```text
STAGE: INITIAL
VERDICT: NOT-BROKEN for Theorem th:tworank, Proposition prop:sizetwo and the
         Paley II construction claims; REFUTED-AS-WORDED for two prose
         sentences (S1, S2 below); the theorem is correct but weak by 4.
EVIDENCE: audit/sizetwo_stage1_checks.py (independent implementation) and the
          hand arguments below.
COVERAGE: see "Coverage".
DEPENDENCIES: Newman's Smith-form duality for Hadamard matrices
          (d_i d_{N+1-i} = N), a standard fact; nothing else external.
EXPOSURE: draft/main.tex lines 1-92, 129-135 (statements), 157-180, 236-251,
          257-268, 276-291. NOT read: proof of th:tworank (lines 252-256),
          proof of prop:sizetwo (lines 269-275), code/size_two_fibres_check.py,
          CLAIMS.md, prior audits. OPEN-ITEMS.md lines 41-47 and CODE.md
          grep hits seen (they say a same-model examiner VERIFIED Theorem A).
          Same model as the author's agents: INTERNAL-NONINDEPENDENT in the
          sense of the skill (no separate fresh context was spawned).
RESOURCES: one core, ~1.2 s CPU for the script; no searches.
```

## Statements examined

- **th:tworank.** H Hadamard of order N; rows partitioned into fibres R_x (x in X), columns into C_y (y in Y), every block H[R_x, C_y] of rank one. If N = 4 mod 8 then |X|+|Y| >= N-4; if N = 8 mod 16 then |X|+|Y| >= N/2-3.
- **Consequences paragraph.** Fibres >= 3 on both sides excluded for N = 4 mod 8, N > 12; fibres >= 5 excluded for N = 8 mod 16, N > 30; repair rank >= N-4-|X|-|Y| (resp. N/2-3-|X|-|Y|); fibres >= 3 give repair rank >= N/3-4 and border width k >= N/6-2.
- **Definitions.** theta = f1 f2 g1 g2 = T11 T22; untwisted iff some signing makes all theta = +1; then blocks are [[a,b],[b,a]] and H ~ [[A,B],[B,A]]; "Equivalently" Theta has rank one.
- **prop:sizetwo.** Symmetric H, N > 8, involution sigma with H_{sigma i, sigma j} = H_ij fixing exactly four indices; moved indices paired with their images, fixed ones paired by equal diagonal; then the pairing exists, all blocks rank one, pairing twisted.
- **Remark Paley II** and the subsection's framing sentences.

## Findings

### A. The theorem is true, and its bounds are 4 below the sharp value (optional strengthening, not a defect)

Argument (complete, mine; independent of the unseen proof):

1. On a rank-one block, beta_ij = e_xy + phi_xy(i) + gamma_xy(j) mod 2. Split beta = U + V with U_ij = e + phi (depends on i and y(j)) and V_ij = gamma (depends on x(i) and j). U has at most |Y| distinct columns, V at most |X| distinct rows, so rk2 beta(H) <= |X|+|Y|.
2. Signing rows and columns preserves rank-one blocks, so |X|+|Y| >= rk2 beta(DHE) for **every** signing D, E. The bound may use the maximum over signings.
3. Normalize H. Then beta = 0 (+) A with A the (N-1)-square core, and row/column reduction gives Smith(H) = 1 (+) 2 Smith(A). Hence rk2 A = #{i : v2(d_i(H)) = 1}. With d_i d_{N+1-i} = N and rk2 H = 1 (H = J mod 2): rk2 A = N-2 if N = 4 mod 8, and rk2 A = N/2-1 if N = 8 mod 16.
4. Negate the first row and first column of the normalized matrix. Then beta = [[0, 1^T],[1, A]]. Each row of A has weight N/2 (even), so A1 = 0 = A^T 1 mod 2; and 1^T 1 = N-1 is odd. So 1 lies in neither the row nor the column space of A, and this beta has rank rk2 A + 2.
5. Therefore |X|+|Y| >= N when N = 4 mod 8, and |X|+|Y| >= N/2+1 when N = 8 mod 16. In general |X|+|Y| >= 2 + #{i : v2(d_i(H)) = 1}.

Exact checks (script section 2): rk2(core) and the bordered rank for Paley I q = 11, 19, 23, 27, 31, 43, Paley II q = 5, 9, 13, 17, Sylvester 8/16/32 and H2 x {Paley I(11), Paley II(9), Paley I(19)} (orders 8-44). Every case gives core rank N-2 (N = 4 mod 8) or N/2-1 (N = 8 mod 16), bordered rank = core + 2, and random signings never exceed it. Every rank is >= the paper's bound.

Consequences of the sharp form (all optional, but they bear directly on the paper's narrative):
- N = 4 mod 8: if no fibre is a singleton, **every fibre on both sides has size exactly two** (|X|, |Y| <= N/2 and |X|+|Y| >= N). Paley II meets the bound exactly, not "to within four".
- N = 8 mod 16: fibres of size >= 4 on both sides are impossible (|X|+|Y| <= N/2 < N/2+1). With the N = 4 mod 8 case, **any rank-one block partition with all fibres of size at least four forces 16 | N**. This removes the "real local Hadamard bases" hypothesis from the paper's 16 | N statement completely; the current text manages only fibres >= 5 and N > 30.
- Repairs: rank R >= N - |X| - |Y| (sign H and T together); fibres >= 3 give rank R >= N/3 and border width k >= N/6.

### B. Threshold arithmetic (as stated against the stated theorem)

- Fibres >= 3, N = 4 mod 8: max |X|+|Y| = 2 floor(N/3). At N = 12 this is 8 = N-4: not excluded by the theorem as stated. "N > 12" is exact for the stated theorem.
- Fibres >= 5, N = 8 mod 16: at N = 24, 2 floor(24/5) = 8 < 9, so N = 24 is already excluded by integrality. "N > 30" is true but not sharp ("N >= 24" is). Not a defect.
- Repair: N-4-2N/3 = N/3-4 and 2k >= N/3-4 give k >= N/6-2. Correct as arithmetic.

### C. Definitions (theta, twisted/untwisted)

- Swapping both rows and both columns of eps f g^T multiplies it by f1 f2 g1 g2; T11 T22 = f1 f2 g1 g2. Correct, and independent of the order within each pair.
- theta = +1 with rank one forces T22 = T11 and T21 = T12, so blocks are [[a,b],[b,a]]. Ordering first members then second members gives [[A,B],[B,A]]. Signing multiplies Theta by diag(d) Theta diag(e), so all +1 is reachable iff Theta = d e^T, i.e. rank one. Converse: in [[A,B],[B,A]] with pairs {i, i+N/2}, every block [[a,b],[b,a]] has rank one and theta = +1. So untwisted <=> Theta rank one <=> after a signing and row and column permutations taking the pairs to {i, i+N/2}, H = [[A,B],[B,A]]. The chain holds. Wording: "under a permutation" should say rows and columns are permuted separately.

### D. Proposition prop:sizetwo: NOT-BROKEN (true, with a hand argument)

- Moved x moved blocks: H_{sigma i, j} = H_{i, sigma j}, so the block is [[a,b],[b,a]], rank one, theta = +1.
- Moved x fixed pair {u,v}: the block has two equal rows, rank one, theta = H_iu H_iv.
- Orthogonality of rows u, u' in F (the fixed set) gives sum_F H_uk H_u'k = -2 sum_pairs(...), with (N-4)/2 pairs, so the restricted rows have product sum = 0 mod 4. Hence the 4x4 matrix H[F,F] has rows of equal weight parity, and by symmetry the number of -1 diagonal entries is even, so an equal-diagonal pairing exists. The product of row u and row v on {u',v'} equals its product on {u,v}, which is H_uu H_vv = 1. So fixed x fixed off-diagonal blocks have rank one, for every admissible pairing.
- Twist: with Theta symmetric and +1 on all moved x moved entries, rank one would force H_iu H_iv to be constant over the (N-4)/2 moved pairs. Column orthogonality of u, v then gives |N-4| <= 4, i.e. N <= 8. So N > 8 gives twisted. The hypothesis N > 8 is exactly what is used.
- Vacuity: hypotheses realized by Paley II (below).

### E. Paley II remark: NOT-BROKEN, including prime powers

Independent F_q arithmetic (F_9 = F_3[t]/(t^2+1), F_25 = F_5[t]/(t^2-2), F_49 = F_7[t]/(t^2+1), each field checked) for q = 5, 9, 13, 17, 25, 29, 49 (N = 12 to 100). In each case: Hadamard, symmetric, sigma-invariant, exactly 4 fixed indices, equal-diagonal pairing exists ({inf,0} top, {inf,0} bottom), all blocks rank one, Theta not rank one (twisted), |X|+|Y| = N. For any odd q, x = -x iff x = 0, so the fixed-point count holds for prime powers by the same one-line argument. N = 2(q+1) = 4 mod 8 since q = 1 mod 4.

### F. Defects found in the statements (reader-facing, as worded)

- **S1 (sec:sizetwo, paragraph 1): "At an order N = 4 (mod 8), fibres of size three or more on both sides are impossible."** This does not follow from th:tworank as stated at N = 12 (B above), and the paper gives nothing else. The sentence is true (A gives it for every N = 4 mod 8), but as written it cites a theorem that does not imply it. Fix: either restrict to N > 12 or adopt the sharp bound.
- **S2 (same paragraph): "The remaining shape has nearly all fibres of size two, with |X|+|Y| close to N."** False as worded. Singleton fibres on one side make every block rank one whatever the other partition: rows all singletons and columns one fibre gives |X|+|Y| = N+1, with no fibre of size two. The claim needs "if no fibre is a singleton". Under that hypothesis, the stated bound forces sum (size-2) <= 8 on each side; the sharp bound forces all pairs.
- **S3 (Remark Paley II, negative control): "the pairing {2i,2i+1} of the Sylvester matrix of order 32 is untwisted."** For the standard Sylvester matrix (H_ij = (-1)^{popcount(i & j)}), pairing rows and columns as {2i,2i+1} gives blocks +-[[1,1],[1,-1]] of rank two, so it is not a rank-one pairing at all. The claim can hold only for a different indexing, a different column pairing (e.g. {j, j+16}) or a different matrix. To be reconciled with the code in Stage 2.
- **S4 ("met to within four").** True relative to the stated bound; misleading given A, where the bound is attained exactly.

## Coverage

Checked: all statements in scope; the rank-one decomposition bound; core/bordered 2-ranks on 16 matrices of orders 8-44; Paley II for 7 values of q, three of them proper prime powers; threshold arithmetic N <= 120; the definitions chain; the proposition by a hand proof. Not checked: exhaustive search for rank-one partitions with small |X|+|Y| (unnecessary given the rank argument); a counterexample showing N > 8 or symmetry is needed in the proposition.

## Reproduction

`Python 3 in a virtual environment audit/sizetwo_stage1_checks.py` (one core, about 1 s).

Redacted 2026-11-24 for privacy (local paths and session identifiers only); the sealed hash refers to the unredacted original.
