# Cold exam, Stage 2 (proof audit): rank-one blocks and fibres of size two

Date: 2026-11-24. Examiner: Claude (Opus 5.5) subagent, the same context that wrote Stage 1.
Scope: draft/main.tex from "The divisibility \(16\mid N\) uses real local Hadamard bases" (line 246) through the end of Remark [Paley II] (line 284). Also code/size_two_fibres_check.py and its CODE.md entry.

```text
STAGE: PROOF-AUDIT
VERDICT: th:tworank VERIFIED (as stated; not sharp, see O1).
         prop:sizetwo VERIFIED.
         Remark [Paley II] construction VERIFIED; its negative-control sentence is FALSE (D1).
         Surrounding prose: three unsupported or false claims (D2-D4).
CLAIM: as in Stage 1 (audit/sizetwo-stage1.md).
EVIDENCE: line-by-line checks below; code/size_two_fibres_check.py run (all asserts
          pass, 0.3 s); independent script audit/sizetwo_stage1_checks.py; control
          probe (scratchpad, reproduced in D1).
COVERAGE: both proofs, every step; the consequences paragraph; the definitions; the
          release script, read line by line; Orrick's Theorem 4.3 read in the arXiv
          version (math/0507515) to check the citation.
DEPENDENCIES: Newman/Wallis Smith-form facts (d_1 = 1, d_i d_{N+1-i} = N). The proof
          derives the second in one line from H^T = N H^{-1}, and the first is
          rk2 H = 1. Discharged. Paley's construction: discharged by computation
          for q = 5, 9, 13, 17, 25, 29, 37, 41, 49, 53 and by the standard
          two-line Gram check.
EXPOSURE: Stage 1 report audit/sizetwo-stage1.md,
          sha256 de563d4d406b6ae9121f5ed84b4a5e25e0d9cd37ad0f1b4c88a1734fff343ed7
          (sealed before the proofs and code were read). main.tex as of 2026-11-24 08:41.
RESOURCES: one core; under 3 s of CPU in total for all scripts.
```

## 1. Theorem th:tworank: proof audit

| Step | Check | Status |
|---|---|---|
| Rank-one sign block = eps f g^T, so beta = eta + phi(e) + gamma(r) on block (x,y) | direct | OK |
| Column (y,r) of beta = c_y + sum_x gamma_xy(r) 1_{R_x}, with c_y independent of r | entries at row (x,e) are eta_xy + phi_xy(e) + gamma_xy(r) | OK |
| Hence rk2 beta <= \|X\|+\|Y\| | columns lie in span{c_y} + span{1_{R_x}} | OK |
| Normalizing changes beta by a 1^T + 1 b^T, rank <= 2 | direct | OK |
| H ~ [1] (+) (-2B') over Z | subtract row 0, then column 0 | OK |
| d_i d_{N+1-i} = N from H^T = N H^{-1} | Smith invariants of N H^{-1}, reversed | OK |
| exactly one odd invariant, since H = J mod 2 | rk2 H = 1 | OK |
| valuations: N = 4 mod 8: 0, (N-2) ones, 2. N = 8 mod 16: 0, (N-2)/2 ones, (N-2)/2 twos, 3 | e_i + e_{N+1-i} = v2(N), monotone, e_1 = 0 is the only zero | OK |
| invariants of B' are d_i/2 (i >= 2), so rk2 B' = N-2, resp. (N-2)/2 | uniqueness of Smith form | OK |
| "Undoing the normalization loses at most two" | correct, but it is where 2 of the slack of 4 enters (O1) | OK |
| Orrick [Thm 4.3] citation | Orrick's code is the span of the 0/1 rows (+1 -> 1) of a column-normalized matrix, with dimensions N-1 and N/2. These are equivalent to, but not equal to, the paper's N-2 and N/2-1. Orrick credits the theorem to Lander and the Smith facts to Wallis and Newman | wording (W4) |

Numerical confirmation (Stage 1 script): rk2 B' = N-2 or N/2-1 on 16 matrices of orders 8-44. The paper's bound holds on every one.

**Verdict: VERIFIED** for the statement as written.

### O1 (optional strengthening, recommended): the bound is attained exactly at N = 4 mod 8

The upper half of the proof holds for every signing of H, since signing preserves rank-one blocks. So the lower half can use the most favourable signing instead of the normalized one. Negate the first row and first column of the normalized matrix. Then beta = [[0, 1^T],[1, B']]. Each row of the normalized H after the first has N/2 minus signs, all in the core, and likewise for columns. So B'1 = B'^T 1 = 0 over F2. Since 1^T 1 = N-1 is odd, 1 is in neither the row space nor the column space of B'. This beta therefore has rank rk2 B' + 2. Hence

- N = 4 mod 8: |X|+|Y| >= N.
- N = 8 mod 16: |X|+|Y| >= N/2+1.

Verified numerically: the bordered rank equals core + 2 on all 16 test matrices, and random signings never exceed it. The release script's own output shows rk2 beta(H) = N for every Paley II matrix, so equality is already visible there.

Consequences, each a one-line deduction:
1. N = 4 mod 8 with no singleton fibre: **every fibre on both sides has size exactly two**, because |X|, |Y| <= N/2. Paley II attains the bound exactly, not "to within four".
2. N = 8 mod 16: fibres of size >= 4 on both sides give |X|+|Y| <= N/2 < N/2+1. So **every rank-one block partition with all fibres of size at least four has 16 | N**. That is precisely the hypothesis-free form of the 16 | N statement in the preceding paragraph. As written, the paragraph claims this (D4) but the stated bounds do not deliver it.
3. Repairs: sign H and T together; then rank R >= N - |X| - |Y|. Fibres >= 3 give rank R >= N/3 and border width k >= N/6.

Exact replacement text, if adopted:

- Theorem statement, last two sentences: "If \(N\equiv4\pmod 8\), then \(|X|+|Y|\ge N\). If \(N\equiv8\pmod{16}\), then \(|X|+|Y|\ge N/2+1\)."
- Proof, replace "Undoing the normalization loses at most two." by: "Signing rows and columns keeps every block of rank one, so the upper bound holds for every signed form of \(H\). Negate the first row and column of the normalized matrix; its \(\beta\) becomes \(\left(\begin{smallmatrix}0&\mathbf 1^T\\ \mathbf 1&B'\end{smallmatrix}\right)\). Every row and column of \(B'\) has weight \(N/2\), which is even, while \(\mathbf 1^T\mathbf 1=N-1\) is odd. So \(\mathbf 1\) lies in neither the row space nor the column space of \(B'\) over \(\mathbb F_2\), and this \(\beta\) has rank \(\operatorname{rk}_2B'+2\)."
- Consequences paragraph, replace from "Otherwise it limits block size." through "needs \(k\ge N/6-2\)." by: "Otherwise it limits block size. If \(N\equiv4\pmod 8\) and no fibre is a singleton, then \(|X|,|Y|\le N/2\) forces every fibre on both sides to have size two. If \(N\equiv8\pmod{16}\) and every fibre has size at least four, then \(|X|+|Y|\le N/2\), which is excluded. Hence any partition of a Hadamard matrix into blocks of rank one with all fibres of size at least four has \(16\mid N\). The same count bounds repairs. If \(H=T+R\), where \(T\) is a sign matrix with such a block partition, then \(R/2\) is an integer matrix with \(\beta(H)\equiv\beta(T)+R/2\pmod 2\), and the same holds after signing \(H\) and \(T\) together. Hence \(\operatorname{rank}R\ge N-|X|-|Y|\), respectively \(N/2+1-|X|-|Y|\). For \(N\equiv4\pmod 8\) and fibres of size at least three, a repair therefore has rank at least \(N/3\). A repair supported on \(k\) rows and \(k\) columns has \(\operatorname{rank}R\le2k\), so it needs \(k\ge N/6\)."
- sec:sizetwo paragraph 1: see D2/D3 (sharp variants) and "met to within four" -> "met exactly".

This is a generalization, not a correctness defect; the author may keep the weaker bound. If it is adopted, the new step needs the same proportional recheck (it is three lines; I checked it above).

## 2. Consequences paragraph (stated bounds)

- 2N/3 < N-4 iff N > 12: exact. 2N/5 < N/2-3 iff N > 30: true. By integrality N = 24 is also excluded (2 floor(24/5) = 8 < 9), so "N > 30" is not sharp (W10).
- Repair: beta(H) = beta(T) + R/2 mod 2 holds entrywise (R in {0, +-2}). rank_Q R >= rk2(R/2). rk2 beta(T) <= |X|+|Y| comes from the first half of the proof, and rk2 beta(H) >= N-4 from the second. Arithmetic N-4-2N/3 = N/3-4 and k >= N/6-2: correct. But the step uses a fact proved inside the proof, not the theorem as stated (W3), and "border" is never defined (W2).

## 3. Proposition prop:sizetwo: proof audit

| Step | Check | Status |
|---|---|---|
| H_{r sigma(c)} = H_{sigma r, sigma c} = H_rc for fixed r | invariance | OK |
| moved columns contribute 2 sum over (N-4)/2 pairs; (N-4)/2 even, so contribution = 0 mod 4 | 4 \| N for a Hadamard matrix with N > 8 | OK |
| fixed rows restricted to fixed columns: inner product = 0 mod 4, so they differ in an even number of places and share the product p | direct | OK |
| symmetric 4x4: product of all entries = product of diagonal = p^4 = 1, so each diagonal sign occurs an even number of times | off-diagonal entries pair up | OK |
| moved x moved block [[a,b],[b,a]], theta = +1 | H_{sigma i, j} = H_{i, sigma j} | OK |
| moved x fixed: equal rows; fixed x moved by symmetry | direct | OK |
| fixed diagonal block: product H_rr H_ss H_rs^2 = 1 (needs H_rs = H_sr and equal diagonal) | direct | OK |
| fixed off-diagonal block: from the equal row products, H_rc H_rd H_sc H_sd = H_rr H_ss = 1 | direct | OK |
| twist: theta_P = H_ic H_id; 0 = 2 sum theta_P + sum_fixed; constant theta gives \|N-4\| <= 4, contradicting N > 8 | column orthogonality, rows sigma(i) and i equal on fixed columns | OK |
| 2x2 minor [[1, theta_P],[1, theta_P']] of Theta is nonzero, so Theta is not rank one | a moved column pair Q exists since N > 8 | OK |

The argument is complete and uses every hypothesis: symmetry (diagonal parity and "by symmetry"), N > 8 (twist and the existence of moved pairs), exactly four fixed points (parity counts). **Verdict: VERIFIED.** Wording: c is reused for a generic column and then for a fixed index (W5).

## 4. Definitions (theta, untwisted, Theta)

Verified in Stage 1 section C; nothing in the proofs changes that. The chain "untwisted <=> Theta rank one <=> (after signing) [[A,B],[B,A]] with the pairs at i, i+N/2" holds. The text states only "=>" for the block form, which is all it uses. W1 tightens "under a permutation".

## 5. Remark [Paley II] and the release script

**Construction.** Hadamard: (C+I)^2 + (C-I)^2 = 2C^2 + 2I = 2(q+1)I, and the cross terms cancel. sigma-invariance by chi(-1) = 1. Exactly four fixed points for every odd q, prime or prime power. The remark is correct for prime powers: Stage 1 checked F_9, F_25 and F_49 independently, and the script covers primes only.

**Script (code/size_two_fibres_check.py), read line by line.**
- paley_ii: chi via Euler's criterion (primes only, matching PRIMES); C[0,1:] = C[1:,0] = 1 is correct since chi(-1) = 1; sigma is correct.
- check(): symmetric and Hadamard assertions; invariance and involution; four fixed points; equal-diagonal pairing; partition completeness; rank one via T00 T11 == T01 T10 (correct for +-1 2x2); theta = T00 T11; twist test theta == theta00 * outer(col0, row0), the correct rank-one test for a sign matrix.
- `r2 <= N` is vacuous (beta is N x N). The comment "rk_2 beta(H) <= |X|+|Y| = N" therefore checks nothing. The printed r2 = N is informative: it attains |X|+|Y| (see O1).
- **Negative control (defect D1):** `S = kron(K, H2)` is the standard Sylvester matrix of order 32 (verified equal to the recursive Sylvester). With pairs {2a, 2a+1}, every block is K_ab * H2, which has **rank two**. The control never checks rank one; it only finds theta = -1 everywhere, which is rank one, and prints "untwisted". So the control certifies a pairing that is not a rank-one pairing, and it would pass even if the twist detector were broken in ways that matter. Probe: pairs {2i,2i+1} give (rank-one blocks, Theta rank one) = (False, True); pairs {i, i XOR 3} give (True, True).
- Run: `python3 code/size_two_fibres_check.py` prints rk2 = N for q = 5..53, twisted = True for all, then the control line and "all checks passed" (0.3 s).

## 6. Defects (correctness of claims)

**D1. Remark [Paley II], last sentence, and the script control. FALSE.**
Current: "As a negative control, the pairing \(\{2i,2i+1\}\) of the Sylvester matrix of order 32 is untwisted."
Replacement: "As a negative control, the pairing \(\{i,i\oplus3\}\) of the Sylvester matrix \(H_{ij}=(-1)^{i\cdot j}\) of order 32 (indices in \(\mathbb F_2^5\)), used on both sides, has blocks of rank one and is untwisted; the pairing \(\{2i,2i+1\}\) is rejected because its blocks have rank two."
Code: use `pairs = [[i, i ^ 3] for i in range(32) if i < i ^ 3]`, assert rank one for every block before the twist test, and assert that {2i,2i+1} fails the rank-one test (a deliberate-error control). Update CODE.md line 275 to match.

**D2. sec:sizetwo paragraph 1: "At an order \(N\equiv4\pmod 8\), fibres of size three or more on both sides are impossible." UNSUPPORTED at N = 12** by the theorem as stated (2 floor(12/3) = 8 = N-4). The claim is true (O1).
Replacement, keeping the stated theorem: "At an order \(N\equiv4\pmod 8\) with \(N>12\), fibres of size three or more on both sides are impossible."
With O1, keep the sentence unchanged.

**D3. Same paragraph: "The remaining shape has nearly all fibres of size two, with \(|X|+|Y|\) close to \(N\)." FALSE as worded.** Singleton fibres on one side make every block rank one: all-singleton rows against a single column fibre give |X|+|Y| = N+1 with no fibre of size two.
Replacement, stated theorem: "If no fibre is a singleton, then \(|X|,|Y|\le N/2\), so the bound leaves fibre sizes exceeding two by at most eight in total over both sides; nearly all fibres have size two and \(|X|+|Y|\) is close to \(N\)."
With O1: "If no fibre is a singleton, then every fibre on both sides has size two and \(|X|+|Y|=N\)."

**D4. Line 246: "A rank argument removes that hypothesis: it applies to any partition into blocks of rank one, whatever the local inputs or their defects." OVERCLAIM.** The hypothesis-free conclusion would be 16 | N for fibres >= 4. The stated theorem does not exclude fibres of size four at N = 8 mod 16 (|X|+|Y| <= N/2 >= N/2-3). It does not exclude them at N = 4 either, though that case is trivial.
Replacement, stated theorem: "A rank argument weakens that hypothesis. It applies to any partition into blocks of rank one, whatever the local inputs or their defects, but at orders \(N\equiv8\pmod{16}\) it excludes only fibres of size at least five."
With O1, the original sentence becomes correct, and the consequences paragraph should then state "\(16\mid N\)" explicitly (text in O1).

## 7. Wording errata (no change to mathematics)

- **W1** (definitions): "so \(H\) becomes a matrix of the form \(\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)\) under a permutation." -> "so after permuting rows and columns, separately, to put each pair at positions \(i\) and \(i+N/2\), \(H\) becomes \(\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)\)."
- **W2** (consequences): "a border of width \(k\), for which \(\operatorname{rank}R\le2k\), needs \(k\ge N/6-2\)." -> "a repair supported on \(k\) rows and \(k\) columns, for which \(\operatorname{rank}R\le2k\), needs \(k\ge N/6-2\)."
- **W3** (consequences): "The same count bounds repairs." -> "The proof also bounds repairs, since it shows \(\operatorname{rk}_2\beta(H)\ge N-4\), respectively \(N/2-3\), for every Hadamard matrix of these orders."
- **W4** (proof of th:tworank, last sentence): "The resulting dimensions of the binary row space of a normalized Hadamard matrix are stated by Orrick \cite[Theorem~4.3]{orrick}, with the Smith form facts credited there to Newman, Wallis and Lander." -> "Orrick \cite[Theorem~4.3]{orrick} states the equivalent dimensions \(N-1\) and \(N/2\) for the binary code spanned by the \(0/1\) rows of a matrix normalized to an all-ones first row. He credits that result to Lander and the Smith form facts to Newman and Wallis."
- **W5** (proof of prop:sizetwo, para 1): "For a fixed index \(r\) and any \(c\), \(H_{r\sigma(c)}=H_{\sigma(r)\sigma(c)}=H_{rc}\). Hence for fixed rows \(r,s\) the moved columns contribute \(2\sum H_{rc}H_{sc}\), a sum over one column \(c\) from each moved pair." -> the same text with \(k\) in place of \(c\) throughout, since \(c\) later names a fixed index.
- **W6** (Remark): "with quadratic character \(\chi\)." -> "with quadratic character \(\chi\), where \(\chi(0)=0\)."
- **W7** (sec:sizetwo para 1): "so those matrices are never rigid" -> "so those matrices are not rigid".
- **W8** (after "Otherwise call the pairing \emph{twisted}."): add "An untwisted pairing is thus the familiar form \(\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)\); the twisted examples below show that pairs of rank-one blocks are not confined to it." Without this the reader is not told why twist matters.
- **W9**: "met to within four" is accurate for the stated bound. With O1, replace with "met exactly".
- **W10** (consequences): "which is excluded for \(N\equiv8\pmod{16}\) and \(N>30\)." -> "which is excluded for \(N\equiv8\pmod{16}\) and \(N\ge24\), since then \(|X|+|Y|\le2\lfloor N/5\rfloor<N/2-3\)." Optional; the current text is true.
- **W11** (CODE.md line 274-275, script docstring item 5): "rk₂ β(H) within the bounds" -> "rk₂ β(H) ≥ N − 4 (the upper bound rk₂ β ≤ N is automatic; the observed value is N = |X| + |Y|)."

## 8. Reader-facing judgment

- **Reconstructible?** Yes. The theorem's proof is short but complete: the decomposition of beta into |X| + |Y| generators, then Smith form. The proposition's proof can be followed line by line. The repair bound relies on an intermediate result of the proof rather than the theorem (W3).
- **Symbols defined before use?** beta, rk2, theta, Theta, eta/phi/gamma, c_y, B', theta_P are all defined. "Core" is used informally but is clear from context. "Border" is undefined (W2). chi(0) is implicit (W6). c is overloaded in the proposition's proof (W5).
- **Connection to the paper's topics.** "The two theorems ... rest on large fibres: recovering them from the entries is what proves rigidity" is accurate (Sections 4-5 recover fibres of size m or h). "Large fibres and the orders N = 4 mod 8 do not mix" is accurate in spirit; precise only for N > 12 under the stated bound (D2). The non-rigidity of the examples is stated plainly and correctly. Why twisted versus untwisted matters is never said (W8).
- **Overclaims:** D1 (false control), D3 (false shape claim), D4 ("removes that hypothesis"), D2 (unsupported at N = 12). Nothing claims novelty.

## Reproduction

From the repository root: `python3 code/size_two_fibres_check.py` (about 0.3 s). The Stage-1 script `sizetwo_stage1_checks.py` is not released.
