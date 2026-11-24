# Final end-to-end read: draft/main.tex

23 November 2026. Cold read of `draft/main.tex` (317 lines; `main.pdf` has 10 pages) against the audited sources. As instructed, OPEN-ITEMS X2 and P01–P05 are out of scope. No existing file was modified.

## VERDICT: READY-WITH-FIXES

Every theorem, lemma and proposition matches its audited source, with no dropped hypothesis and no strengthened conclusion. The conditional criterion (Prop. 3.3) is correct as stated, and both instances satisfy it. Every number recomputed matches. No correctness defect was found.

The fixes below are needed before release:
- one decoder statement in the finite proof;
- one overstated comparison (Stepaniants);
- one citation entry;
- stale PDF metadata;
- several wording and scope repairs.

## Findings

Line numbers refer to `draft/main.tex` as read.

**1. Line 19, wording (metadata).** The `pdftitle` still reads "Rigid woven Hadamard matrices and exact equivalence counts", and `pdfinfo main.pdf` reports that title. The printed title dropped the subtitle, and "exact equivalence counts" overclaims: the class counts carry an O(√N log² N) error term.
Replace `pdftitle={Rigid woven Hadamard matrices and exact equivalence counts}` with
`pdftitle={Rigid woven Hadamard matrices}`.

**2. Line 43, transcription (scope).** "the Sylvester input at m=4 admits nontrivial symmetries" states something trivial: every H(4) has symmetries. The audited fact concerns the *outputs*. Stage 1 (`audit/meisner-stage1-initial.md` l.31–44, l.93) found every sampled output at m = 4 nonrigid (20/20, exact). It also gives an analytic translation family that is present for every labelling at m = 4.
Replace "This theorem gives no finite cutoff; the Sylvester input at \(m=4\) admits nontrivial symmetries." with
"This theorem gives no finite cutoff: at \(m=4\) the outputs from the Sylvester input are not rigid."

**3. Line 117, wording.** "the number of other recoverable distinct outputs in its side-preserving class, including itself" contradicts itself.
Replace with "the number of recoverable distinct outputs in its side-preserving class, itself included, is at most \((b!)^2a^{2b}\)."

**4. Line 220, transcription (decoder).** The finite proof says "Use the divisibility relation from Proposition~\ref{prop:recovery}" but never states its decoder. The decoder cannot be the branch rule of Prop. 4.1. For the Paley H(20), |D| = 12 ≥ h/2 (`meisner-stage2-proof-audit.md`, Sylvester paragraph), so the in-fibre quartet sum is 4h·12 = 960 ≥ N/2 = 800, and the branch rule would select the large-quartet branch. FINITE-1600 and the recovery audit (finite refinement, items 2–4) use the divisibility graph unconditionally and decode by its *unique partition into h-cliques*. Lemma 3.2 needs an explicit equivariant decoder.
After "…so a spanning tree bounds the chance of a given false pair by \(2^{-(h-3)}\)." insert:
"Here the decoder outputs the partition of this divisibility graph into \(h\)-cliques when that partition is unique. It is not the branch rule of Proposition~\ref{prop:recovery}, which would take the large-quartet branch for the Paley matrix (\(|D|=12\)). The rule depends only on the entries and commutes with signed permutations."

**5. Line 262, wording (scope of order coverage).** The row-norm identity and 16 | N are correct; see Coverage. Two sentences overreach.
- "In particular the construction cannot reach…" refers to the general large-fibre framework, not to Theorem 1.2.
- "At any regular order N=(2w)², an ordinary H(2w) already gives a regular witness" is true only as a conditional. Nothing shows that a general large-fibre construction at (2w)² requires H(2w). Coverage is proved only for the two theorems, where H(m) and H(2h) are inputs.

Replace the last two sentences of the paragraph with:
"In particular no such construction with all fibres of size at least four reaches a regular order \(4u^2\) with \(u\) odd. A regular output order is then \((2w)^2\); whenever \(\HH(2w)\) holds, the square construction from that matrix already gives a regular witness at that order. This applies to every order supplied by Theorems~\ref{th:main} and~\ref{th:four}. We do not show that a general construction of this shape needs \(\HH(2w)\)."

**6. Line 267, citation (overstated comparison).** "Counts without rigidity are far larger" compares a *labelled* count with the paper's *class* counts. It is true only asymptotically, and only from about order 2^27:
- Stepaniants' class-level consequence (divide by (2^n n!)²) first exceeds e^{N log N} at k = 27.
- His labelled bound first exceeds the ≈ e^{3N log N} labelled size of the rigid families at k = 27.
- At every order the paper treats concretely (for example 1600), the comparison runs the other way. Recomputed in `nums.py`.

The source states "≥", while the paper says "exceeds". The rest of the sentence checks out against FR-12 `solution.md`:
- the injective doubling H(2m) ≥ (2m−1)!!H(m)² is correct;
- the Lean exports cover m!H(m)² ≤ H(2m) and the stated power-of-two bound;
- FJZ Conjecture 1.3 is the 2^{C n log₂ n} target;
- "doubled matrices are never rigid" holds: swap each matched row pair and negate the second column half.

Replace "Counts without rigidity are far larger: Stepaniants \cite{fr12} iterates an injective doubling to show that the number of labelled Hadamard matrices of order \(2^k\) exceeds \(2^{2^k(k-1)(k-2)/8}\), refuting…" with
"Without rigidity, labelled counts grow faster along powers of two: Stepaniants \cite{fr12} iterates an injective doubling to show that the number of labelled Hadamard matrices of order \(n=2^k\) is at least \(2^{n(k-1)(k-2)/8}\), an exponent of order \(n\log^2 n\), refuting…"
Keep the final sentence ("Doubled matrices are never rigid…").

**7. Line 305, citation.** The repository's own citation block names a single author, "Townsend, Alex", and asks for a commit or access date. The entry has "A. Townsend et al." and no revision. The solution's title is "A matching-indexed doubling counterexample"; "Counting real Hadamard matrices" is the problem's title.
Replace with:
`\bibitem{fr12} G. Stepaniants, A matching-indexed doubling counterexample, solution to problem FR-12 (Counting real Hadamard matrices), 12 September 2026, Lean-verified, in A. Townsend, \emph{Open Problems in Numerical Linear Algebra}, GitHub repository \texttt{ajt60gaibb/OpenProblemsInNLA}, commit \texttt{0212a62}.`
Commit 0212a62c25e02f38a74ce9af5504e37630309a3f is the Lean-verified FR-12 revision. Orrick (l.309) also lacks pages; Crossref gives 31–50 and issue 1.

**8. Lines 204 and 210, citation (fairness of the Merchant comparison).** The comparison is correct and correctly restricted: it needs both H(m) and H(m²/8), N = 32n, a leading term of (N/2) log N, and a doubling of the asymptotic exponent. But 1600 lies in that common range (H(40) and H(200) both exist). There, Merchant's Theorem 5.2 with n = 50 gives (798)!/(2^{10}·50³), a 1963-digit number, so more than 10^{1962} rigid designs. That exceeds the more-than-10^{1514} rigid designs that the paper's finite result implies at that order. Without a sentence saying so, the corollary and l.269 invite a finite reading.
At the end of the paragraph at l.210 add:
"The doubling is asymptotic. At \(N=1600\), where \(\HH(40)\) and \(\HH(200)\) both hold, Merchant's bound with \(n=50\) exceeds \(10^{1962}\) rigid designs, more than the finite count of Theorem~\ref{th:four} implies."

**9. Line 269, wording (process language).** "The finite result strengthens the evidence at a single regular order" does not say what the evidence supports. "The literature comparison is bounded by the sources in the accompanying prior-art record" points the reader to an internal artifact.
Replace these two sentences with:
"The finite result is an existence count at the single order 1600."
and, at the end of the paragraph:
"The comparisons above are limited to the works cited; we make no claim of historical priority."

**10. Line 22 and the `%` comments, wording (release hygiene).**
- `\date{Working draft, November 23, 2026}` must change for release.
- About 17 source comments (`% Source: …`, `% Draft provenance: …stage1-initial.md…`, `% OPEN-ITEMS.md records…` at l.73, 86, 89, 94, 101, 113–114, 119, 125, 134, 143, 170, 195, 206, 216, 252, 257) name internal audit files.
- `\todo` (l.18) is now unused.

Strip them from the released `.tex`, or keep them deliberately as provenance.

**11. Lines 90, 92, 162, wording (notation clashes).**
- `d` is both the local order and the sign vector (−1,1,1,1).
- `K` is both the conference matrix and the exposed integer `K_{cc'}`.
- `D` is both the quartet sum and the output counts D_M, D_B, D_4.

Minimal fix: at l.90 and l.92 rename the vector to `z`: "Let \(z=(-1,1,1,1)^T\), so \((I+K)z=2\one\)", "\(z_i\) times its fixed-line column", "signs \((I+K)\operatorname{diag}(z)\)". At l.162 write `\kappa_{cc'}` for `K_{cc'}`.

**12. Line 129 (Prop. 3.3), wording.** C^rig is not defined in the proposition.
After "If \(D\) is the exact raw output count" insert "and \(C^{\rm rig}\) counts classes, transposes identified, containing an output with properties (i)–(iii)".

**13. Line 34, wording.** "negates everything twice" is opaque.
Replace with "negates all rows and all columns, which leaves the matrix unchanged."

**14. Line 244, wording.** "An explicit labelling independently illustrates the construction" gives no pointer to where the example lives.
Replace with "The release code constructs one explicit labelling at this order:"; the rest is unchanged.

**Not a manuscript defect (ledger).** Theorem 1.2's "Every labelling has a Bush-type regular representative" is F11, which has only a credit-review CONFIRMED and no proof-audit verdict. This read re-derived it; see Coverage. G01, G02 and the criterion (G03 replacement) were also checked here at their stated scope. This is an end-to-end read, not a separate proof audit.

## Coverage

**Transcription against sources.**

*Construction and regularity*
- **Section 2.1** against MEISNER-RIGIDITY "Construction": the Hadamard check for any port signs, and the Bush pinning.
- **Section 2.2** against CONSTRUCTIONS "line involution" and "Regularity":
  - K, W = h(K⊗I + I⊗Π) and WW^T = 4h²I;
  - the fixed-line argument and the count of h fixed lines;
  - (I+K)d = 2·1, checked by hand;
  - field supply: q ≥ 4 even, q ≥ 5 odd;
  - p ≡ 7 mod 12, and √X/(4 log X) recomputed from φ(12) = 4 and h ≤ √X/2.
- **Bush partition** (credit-bush B1), re-derived:
  - (I+K)diag(d) has minus signs at (1,1), (2,4), (3,2), (4,3);
  - pairing rows {1,2}→cols {2,3} and {3,4}→{1,4} gives all-plus diagonal blocks and off-diagonal blocks with zero margins;
  - tiles between distinct fixed lines use nonfixed ports at both ends;
  - Menon parameters (4h², 2h²−h, h²−h).

*Gauge and multiplicity*
- **Lemma 3.1, component count and D_M, D_B, D_4** against RESULT Lemma 1, MEISNER "Gauge" and the stage-2 audits:
  - c = h + (h²−h)/2;
  - Meisner gauge 2^{m²}, or 2^{m²−m} with pins;
  - D formulas re-derived from L/gauge;
  - the raw-versus-regularized scope (F12) is handled correctly at l.112.
- **Lemma 3.2** against RESULT Lemmas 2–3 and E1:
  - the bound counts outputs, (b!)²a^{2b}, equivalent to the source's labellings × 2^c;
  - 2^{2b−1} flips;
  - Bush upper bound D_B.
- **a(d) = (2d)^r**: the collision probability 2^{1−r} is correct; the bound covers the full stabilizer (E1).

*Criterion*
- **Prop. 3.3, correct as stated.**
  - The good set is a union of gauge fibres, because (i)–(iii) are properties of the matrix with the fixed block partition. It therefore holds at least (1−o(1))D outputs.
  - Loss: log 2 + 2 log b! + 2b·r·log(2d) = O(√N log² N) when b, d = O(√N).
  - Upper bound C^rig ≤ D.
  - Both instances satisfy it: Bush (b = d = m, uniform pinned gauge) and four groups (b = 4h, d = h, uniform gauge 2^c); (i) by Prop. 4.1, (ii) and (iii) by Section 5.

*Recovery*
- **Prop. 4.1** against REGULAR-RIGIDITY "Recovery", MEISNER "Fibre recovery" (with D1, E1, E2) and recovery-cold-audit:
  - threshold b|D| ≥ N/2;
  - Hoeffding exponent d/8, recomputed;
  - 2+2 conditioning cost d+1;
  - Bush constants 2e^{−m/8+O(1)} and O(m)e^{−m/8+O(1)};
  - collision probability (d−2)/(2(d−1)); with Bush pinning it is (m/2−1)/(m−1) < 1/2, recomputed;
  - probe counts: h−1 in four groups, m in the square;
  - auxiliary rows from a third row group;
  - Parseval repair: Σ_δ⟨A_a∘A_b∘A_c, A_δ⟩² = d², three zero terms, each remaining term < d²/4, so at least 5 nonzero and one survives the exclusion of y;
  - forest sizes (h−2)/2 and (m−3)/2;
  - **branch rule**: the large-quartet branch whenever any quartet reaches N/2, with the Sylvester remark. It matches stage-1 D1 exactly.

*Rigidity*
- **Section 5** against MEISNER "Rigidity" (E3) and REGULAR-RIGIDITY "Rigidity and class counting":
  - moved-point sum Σ(2b√(a/t))^s, with t = d!, or (m−1)! for Bush; (2b)^s equals (8h)^s and (2m)^s;
  - kernel word set of size ≤ 2d;
  - four-group bound (2h)²/C(h,h/2) by the external three-path;
  - Meisner two-step: δ = 1/4, O(m⁵)2^{(H₂(δ)−1)m}, (2m)^m candidates, (4m(m+1)2^{−m})^{δm} including the Bush factor 2.

*Counts*
- **Section 6 bounds and Stirling**: both constants recomputed. The residual divided by √N log N is bounded:
  - four groups: 1.14 and 1.09 at h = 10³ and 10⁵;
  - Meisner: 0.63 and 0.58;
  - Bush: −0.42 and −0.45 at m = 10³ and 10⁵.
  - The difference is (9 log 2/8)N.
- **Corollary (M5)** against MEISNER M5, E4 and PRIOR-ART item 2:
  - parameters (N−1, N/2−1, N/4−1);
  - the lift of design automorphisms;
  - Merchant N = 32n, input H(N/8), leading term (N/2) log N, the both-H(m)-and-H(m²/8) condition, and the good-block, good-point and tensor-indecomposability remarks.

*Finite count at 1600*
- **Section 7** against FINITE-1600, count-cold-audit and RESULT "Order 1600":
  - pattern counts (h + abcD)/8 re-derived;
  - D ≡ 4 mod 8, exclusion of |D| = h and h ∤ 2D;
  - spanning tree 2^{−(h−3)};
  - two mixed cliques;
  - f_h formula;
  - a_h^proj;
  - kernel ±I via fixed-point-free involution;
  - g_h formula;
  - ratio r²_{h+4}/r²_h, matched symbolically to the exact ratio at h = 20.
- **Section 7 comparisons** against RESULT 1b and X1: B01 and B02 wording, "do not order the actual class counts".

*Order coverage*
- **Section 8.1 from first principles.** The W tile entry is ε√(h_x h_y), because F_x^T f_p = h_x e_p.
  - Row (x,p) of WW^T = NI gives N = h_x Σ_{y faced by p} h_y.
  - Real Hadamard orders ≥ 4 are divisible by 4, so 16 | N, and 4u² with u odd is excluded.
  - Coverage of the two theorems' orders:
    - Meisner: H(m) is the input;
    - four groups: H(2h) by doubling;
    - Meisner with m = 2h gives regular Bush-type of order 4h² (M1);
    - BHK Theorem 1 per involution-audit and credit-bush.
  - The general (2w)² sentence is only conditional (Finding 5).

**Numbers recomputed** (`nums.py`, exact integers and Fractions):

| Quantity | Paper | Recomputed |
|---|---|---|
| a₂₀ | 5 673 369 600 000 | 5 673 369 600 000 |
| f₂₀ | < 0.254 | 0.25378 |
| upper bound on f₂₀ | < 0.258 | 0.25699 |
| r₂₀ | < 1/8 | 0.12217 |
| g₂₀ | < 0.037 | 0.03429 |
| decrease of f-bound and r, and good fraction > 0.70 | for all h ≡ 4 mod 8, h ≥ 20 | confirmed exactly for h = 20…2000 |
| false pairs | — | 1 264 000 |
| 1600 bound (`count1600.py`, rerun) | 1515 digits, leading 587135898904 | 1515 digits, leading 587135898904 |
| D₄ | 3842 digits | 3842 digits (L divisible by the gauge) |
| D_P at m = 40 | 4187 digits | 4187 digits |
| Bush finite class bound at m = 40 | > 10^{1268} | 1269 digits |
| `meisner_equal_terms.py` | — | 1281 / 952 / 10^{4186} / 10^{3841} |
| C(1600,2) | 1 279 200 | 1 279 200 |
| 1600² | 2 560 000 | 2 560 000 |
| Merchant at n = 50 | not stated | 1963 digits |

**Abstract, intro and theorems.** The abstract, introduction and theorem statements agree: N = m², N = 4h², both linear constants, 10^{1514}, transposes identified, and "inequivalent" including transposes as defined at l.34.

**Prior work.**
- Crossref metadata matches the bibliography for Crnković–Švob, Orrick (pages missing), FJZ, LLT, Craigen (two papers) and Merchant.
- FR-12 was read at source (`README.md` and `solution.md` via `gh api`).
- LLT's 3.66·10^{11} rests on the abstract only (PRIOR-ART row; full text unread). Acceptable as stated.
- Spence, Orrick, FdF, Cameron–Stark, Muzychuk and the Craigen weave and signed-group remarks were checked against PRIOR-ART, credit-bush and credit-craigen summaries, not primary texts.
- No "first" or priority claim appears in the paper.

**Not covered.**
- Primary texts of Meisner, BHK, LLT and Spence.
- The F10 example (no rerun).
- The full PDF typesetting, beyond page count and title metadata.

## Resources

- Single core.
- Python 3 in a virtual environment:
  - `count1600.py` and `meisner_equal_terms.py` (< 0.1 CPU-s);
  - scratch scripts `nums.py` and `dbg.py` (session scratchpad; not retained) (0.1 CPU-s).
- No sign-space search.
- Network:
  - `gh api` reads of the public FR-12 entry, its commit history and the repository citation block;
  - seven Crossref metadata lookups.
- Total CPU well under 5 s.
