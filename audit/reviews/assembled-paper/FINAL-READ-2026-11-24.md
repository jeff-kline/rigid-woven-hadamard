# Final end-to-end read: paper/main.tex

24 November 2026. A cold read of `paper/main.tex` (350 lines; `main.pdf` has 13 pages) as a referee would read it. I formed my own view before opening the earlier audits (`FINAL-READ-2026-11-23.md`, `rank-one-blocks/*`, `four-group/*`, `meisner/*`, `RELEASE-AUDIT-CLAIMS-2026-11-24.md`). Line numbers refer to this file:

| File | sha256 (first 16) |
|---|---|
| paper/main.tex | a11a87fb52ec407f |
| README.md | 43ab62dfcfd9c85b |
| paper/main.pdf (after `make paper`) | 979224b1578b2b72 |

**Auditor:** Claude (Opus 5.5) subagent, process-separated from the drafting sessions. This is not peer review. I wrote only this file; `make paper` regenerated `paper/main.{pdf,aux,log,out}` as the task required.

## VERDICT: READY-WITH-FIXES

There is one correctness defect, in a statement rather than a proof. Theorem 1.1 (l.40) now says the lower bound holds "at each such order". The next sentence and the earlier audit both say that at m = 4 the Sylvester outputs are not rigid. There the number of rigid classes is 0, so no bound of the form exp(…) can hold. The fix is "for all sufficiently large such m" (Finding 1).

Every other theorem, lemma, proposition and corollary matches its proof, with no missing hypothesis. That includes the new Section 8, which I re-derived line by line. Every cross-reference resolves to the intended result, and every number I recomputed matches. The other findings concern consistency and wording. Three of them matter for a reader:
- the introduction never announces the third result;
- the section heading files Theorem 8.1 under "earlier work";
- the README evidence table is stale for Corollary 8.4 and for the 10^1268 bound.

Build hygiene passes.

## Findings

Severities: **correctness** · **consistency** · **wording**.

**1. l.40 — correctness (the changed sentence in Theorem 1.1).** "In particular, at each such order the Bush ensemble gives at least \(\exp(\dots-O(\sqrt N\log^2N))\) rigid classes" is false at small orders. The theorem's next sentence says "at m=4 the outputs from the Sylvester input are not rigid", and the 23 November read records that every labelling there has a translation symmetry. So \(C_{\rm B}^{\rm rig}=0\) at m = 4. The O(·) bound is asymptotic only, as Corollary 6.1 (l.188, "every sufficiently large") already says.
Replace
`In particular, at each such order the Bush ensemble gives at least`
with
`In particular, for all sufficiently large such \(m\) the Bush ensemble gives at least`.

**2. l.52 (end of Section 1) — consistency.** The abstract announces three results. Section 1 states only Theorems 1.1 and 1.2, so a reader finds the third result, Theorem 8.1, without introduction in Section 8. After "…uses a stronger arithmetic test at \(h\equiv4\bmod8\)." add:
`The third result, Theorem~\ref{th:tworank}, concerns any partition of a Hadamard matrix of order \(N\) into blocks of rank one: the numbers of row and column parts sum to at least \(N\) when \(N\equiv4\pmod 8\), and to at least \(N/2+1\) when \(N\equiv8\pmod{16}\). Section~\ref{sec:sizetwo} shows that the first bound is attained.`

**3. l.234 and l.293 — consistency (structure).** Theorem 8.1, Proposition 8.2 and Corollary 8.4 sit in a section titled "Order coverage and earlier work". The abstract's third result is thus filed under prior work.
- Replace `\section{Order coverage and earlier work}` with `\section{Order coverage and blocks of rank one}`.
- Replace `\subsection{Comparisons}` with `\section{Comparisons with earlier work}`.

The numbering of Theorem 8.1 to Corollary 8.4 does not change, and the README cites no section numbers.

**4. l.259 — wording (now inaccurate).** "The two theorems of this paper rest on large fibres" is no longer accurate: Theorem 8.1 is also a theorem of the paper.
Replace `The two theorems of this paper rest on large fibres` with `Theorems~\ref{th:main} and~\ref{th:four} rest on large fibres`.

**5. l.290 — wording (notation clash).** In the proof of Corollary 8.4, \(K\) is the 4×4 matrix of Section 2 (l.79). Section 4 already renamed \(K_{cc'}\) to \(\kappa_{cc'}\) to avoid exactly this clash. (\(U\) is also the signed permutation of l.31, but it is local and defined on the spot; renaming it is optional.)
Replace
`With \(K=\left(\begin{smallmatrix}I&I\\I&-I\end{smallmatrix}\right)\), \(KHK\) is block diagonal with blocks \(2(A+B)\) and \(2(A-B)\). Since \(K^2=2I\), \((KHK)(KHK)^T=2N K^2=4NI\).`
with
`With \(S=\left(\begin{smallmatrix}I&I\\I&-I\end{smallmatrix}\right)\), \(SHS\) is block diagonal with blocks \(2(A+B)\) and \(2(A-B)\). Since \(S^2=2I\), \((SHS)(SHS)^T=2N S^2=4NI\).`

**6. l.290 — wording (credit).** Christian and Shader recall the sum-of-two-squares condition as known background; it is not their result (twist-stage2 O1, which I accept). As written, "\cite[p.~2]{christian}" reads as an attribution.
Replace `Such a weight must be a sum of two squares \cite[p.~2]{christian}, which \(N/4\) is not;`
with `By a classical condition, recalled in \cite[p.~2]{christian}, such a weight must be a sum of two squares, which \(N/4\) is not;`.

**7. README.md:187 — consistency (stale after the widened corollary).** Corollary 8.4 now covers every \(N\equiv4\pmod 8\) with \(N/4\) not a sum of two squares. Among the script's Paley II orders, \(N=84\) (\(N/4=21\)) qualifies, and `evidence/size_two_fibres_check.txt` shows it twisted. The row lists only the orders \(\equiv12\pmod{16}\).
Replace `$N=12,28,60,76,108$` with `$N=12,28,60,76,84,108$`.

**8. README.md:182 — consistency (evidence does not match the displayed bound).** The paper (l.229–231) displays \(C_{\rm B}\ge D_{\rm B}/(2N^m(m!)^2(2m\,a_m^{\rm proj})^{2m})>10^{1268}\) with the pinned \(D_{\rm B}=2^{m^2-m}((m-1)!)^{2m}\). The two cited scripts compute a different quantity: the free-tile-sign numerator \(2^{m^2}((m-1)!)^{2m}\), which gives 1281 digits (`evidence/meisner_equal_terms.txt`, `evidence/arith.txt`). I recomputed the displayed floor exactly: 1269 digits, so the claim \(>10^{1268}\) is correct. No released script prints it, however. It appears only in `four-group/stage1-initial.md`, claim 7, and in the 23 November read. Two fixes:
- preferred: add to `code/arith.py`
  `print("Bush pinned-diagonal floor digits:", len(str((2**(m*m-m)*F(m-1)**(2*m)) // (2*N**m*F(m)**2*(2*m*a40)**(2*m)))))`
  then repin `evidence/arith.txt` (expect 1269);
- or replace the cell text with `the free-sign variant (1281 digits) in code/meisner_equal_terms.py (`code/meisner_equal_terms.py`, path relative to the repository root); the displayed pinned-diagonal floor (1269 digits) is recomputed in audit/reviews/four-group/stage1-initial.md (`audit/reviews/four-group/stage1-initial.md`, path relative to the repository root)`.

**9. l.193 — wording (Norman sentence).** The sentence has two problems.
- "its full text" has no antecedent: Norman is a person.
- The Norman remark sits inside the proof of Corollary 6.1, which it does not support. The Merchant sentences justify "twice" and may stay in the proof.

Replace
`Earlier, Norman \cite{norman73} constructed rigid Hadamard designs; its full text was not openly accessible at the time of writing, and Merchant reports that it gives an infinite family of rigid Hadamard designs from doubled Paley designs.
\end{proof}`
with
`\end{proof}
Earlier, Norman \cite{norman73} constructed rigid Hadamard designs. The full text of that paper was not openly accessible at the time of writing; Merchant reports that it gives an infinite family of rigid Hadamard designs from doubled Paley designs.`

**10. l.191 and l.298 — wording (terminology).** "Derived design" already means something standard in design theory: the design induced on a block. Here it names the design read off a normalized matrix.
- At l.191, after "…has parameters \((N-1,N/2-1,N/4-1)\), by row orthogonality." add `Call it the design associated with the distinguished row and column.`
- Then replace `Isomorphic derived designs` with `Isomorphic associated designs`.

**11. l.298 — wording (run-on; unclear last clause).** Replace
`Its comparison with Merchant is asymptotic and concerns rigid \emph{derived designs}; at order 1600 Merchant's bound, above \(10^{1962}\), is the larger; the automorphism group of one normalized design records only the operations fixing that normalization.`
with
`Its comparison with Merchant is asymptotic and concerns rigid associated designs; at order 1600 Merchant's bound, above \(10^{1962}\), is the larger. Rigidity of a design is weaker than rigidity of its matrix: the automorphism group of one normalized design records only the operations that fix that normalization.`

**12. l.256 — wording (two phrases in the consequences paragraph).**
- "supported on \(k\) rows and \(k\) columns" can be read as a \(k\times k\) submatrix, where rank ≤ k and so k ≥ N/3. The stated bound, rank ≤ 2k, fits the cross-shaped reading. Replace with `whose nonzero entries lie in the union of \(k\) rows and \(k\) columns`.
- "Defective local bases with blocks of rank one are covered directly." is cryptic. Replace with `The bound needs no hypothesis on the local vectors: it holds whenever every block has rank one, whether or not the vectors at a point form a Hadamard basis.`

**13. l.261 — wording (repetition).** "An untwisted pairing is thus the familiar form \(\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)\)." repeats the sentence two lines earlier. Delete it, and replace `are not confined to it.` with `are not confined to that form.`

**14. l.223, l.228 — wording (number format).** The paper writes 1600, \(10^{1514}\) and thin-spaced long integers, but also "1,515", "4,187" and "3,842". Replace them with `1515`, `4187` and `3842`, which also matches README:179.

**15. l.337–339 — wording (bibliography order).** The list is alphabetical except that Stepaniants (fr12, now [12]) and Ferber–Jain–Zhao (fjz, [14]) sit between Muzychuk and Orrick. Move `\bibitem{fjz}` to just after `\bibitem{csv}`, and `\bibitem{fr12}` to the end, after `\bibitem{spence}`. The README cites no reference numbers.

**16. Optional — wording.**
- (a) The abstract states the class count without saying "for a fixed input", which the theorems and README item 1 do say. One option is "Second, we count them: for each fixed input, up to signed permutations and transposition, …".
- (b) \(X\) has three meanings: an order bound (l.88), a sign matrix (l.168–177) and a point set (§8). Renaming the l.88 bound to \(x\) or \(T\) would remove one of them.
- (c) `\rank` and `\Stab` are defined but unused, while l.256 writes `\operatorname{rank}`. Either use `\rank` or delete both macros.
- (d) The text layer renders `\tfrac18\log2` as "18 log 2" and \(10^{1514}\) as "101514". This is inherent to pdfTeX and needs no fix, provided the Zenodo and CITATION abstracts are plain-text copies, as they are now.

## Coverage of the new and changed parts

**Abstract (l.24).** Every claim has a theorem with the same scope.
- Rigidity of all but o(1) of the outputs: Theorems 1.1 and 1.2. Gauge fibres have equal size, so a fraction of labellings equals the same fraction of distinct outputs.
- \(\log C=N\log N-cN+O(\sqrt N\log^2N)\) for classes with transposes identified: Theorems 1.1 and 1.2. The upper bound \(C^{\rm rig}\le D\) and the lower bound on good classes also cover all rigid classes, so "the rigid outputs form C classes" is exact in scope.
- "more than \(10^{1514}\) rigid regular classes": Theorem 1.2. Classes there means inequivalent matrices with transposes identified (l.31), and the count includes the transpose factor 2 (l.219–221). Rigidity is a class property, and regularization preserves the class (l.104).
- Third result: the consequences paragraph of Theorem 8.1 (l.256).
- "no new orders": §8.1.

Both constants were re-derived with Stirling:
- \(\log D_{\rm B}=N\log N-(2-\log2)N+O(\sqrt N\log N)\);
- \(\log D_4=N\log N-(2+\tfrac18\log 2)N+O(\sqrt N\log N)\).

**Theorem 1.1 (l.35–41).** Finding 1 only. The rest matches Proposition 3.3 as instantiated in §6.

**Theorem 8.1 (l.246–254), re-derived.**
- *Upper bound.* \(\beta=\eta_{xy}+\varphi_{xy}(e)+\gamma_{xy}(r)\). Each column lies in \({\rm span}\{c_y\}+{\rm span}\{\one_{R_x}\}\), and signing keeps every block of rank one.
- *Normalization.* The reduction gives \(H\sim[1]\oplus(-2B')\): after the row step, the first column of the other rows is already 0.
- *Smith invariants.* Since \(d_id_{N+1-i}=N\) and exactly one invariant is odd (\(H\equiv J\)), the valuation patterns are forced: 0, \(N-2\) ones, 2; and 0, \((N-2)/2\) ones, \((N-2)/2\) twos, 3. Then \(\operatorname{rk}_2B'\) is \(N-2\), respectively \((N-2)/2\).
- *Re-signing.* Negating the first row and column gives \(\beta=\left(\begin{smallmatrix}0&\one^T\\\one&B'\end{smallmatrix}\right)\). Since \(\one^TB'=0\) while \(\one^T\one\) is odd, \(\one\) is not in the column space of \(B'\) or in its row space. The parity argument for "+2" is now written out and is correct.

This proves the sharp form, \(|X|+|Y|\ge N\), respectively \(N/2+1\). Orrick's "\(N-1\) and \(N/2\)" correspond to the convention +1 → 1, giving dimension \(\operatorname{rk}_2B'+1\). The citation is corroborative only.

**Consequences paragraph (l.256).** Every inference holds:
- no singletons at \(N\equiv4\pmod 8\) forces all fibres to size two;
- fibres of size at least four give \(|X|+|Y|\le N/2\);
- hence 16 | N in all cases.

The repair bound also holds: \(\beta(H)\equiv\beta(T)+R/2\), the rank of an integer matrix over \(\mathbb Q\) is at least its rank over \(\mathbb F_2\), and the result survives joint signing. The other two figures check: rank ≥ N/3 for fibres of size at least three, and k ≥ N/6 (Finding 12 concerns wording only).

**Definitions of twist (l.261).**
- \(\theta=f_1f_2g_1g_2=T_{11}T_{22}\) is invariant under the choice of factorization.
- Signing acts on \(\Theta\) by \(a_Pb_Q\), so "untwisted" is equivalent to \(\Theta\) having rank one.

**Proposition 8.2 (l.263–273).** Every step checks.
- \(H_{r\sigma(k)}=H_{rk}\) for fixed \(r\).
- \((N-4)/2\) is even because \(4\mid N\).
- Fixed-column inner products are ≡ 0 mod 4, so the fixed rows have equal products of their fixed entries.
- The diagonal product is \(p^4=1\), so the fixed indices can be paired as stated.
- The moved×moved blocks are \(\left(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\right)\) with \(\theta=+1\). The moved×fixed blocks have equal rows; the fixed×moved blocks follow by symmetry of \(H\).
- The fixed×fixed blocks have entry product 1.
- Twist: if all \(\theta_P\) were equal, \(|2\sum\theta_P|=N-4>4\), which the four fixed rows cannot cancel. This uses \(N>8\).
- The \(2\times2\) minor of \(\Theta\) is \(\theta_P-\theta_{P'}\ne0\).

The proof treats the blocks \(\{c,d\}\times\{c,d\}\) and \(\{c,d\}\times\{r,s\}\) implicitly; they follow by the same diagonal argument and by transposition. This is not a defect.

**Remark 8.3 (l.275–281).** Paley II is symmetric Hadamard, since \((C\pm I)^2\) and the cross terms check out from \(C^2=qI\), with \(N=2(q+1)\equiv4\pmod 8\). Both \(\chi(-1)=1\) and the fixed points \(\{\infty,0\}\times2\) check.
- The listed primes give orders 12, 28, 36, 60, 76, 84, 108, all twisted in the evidence file.
- Sylvester control: \(\{i,i\oplus3\}\) has \(\theta=(-1)^{3\cdot i+3\cdot j}\), which has rank one, so the pairing is untwisted. The pairing \(\{i,i\oplus1\}\) has entry product \((-1)^{1\cdot1}=-1\), so its blocks have rank two.

**Corollary 8.4 (l.285–291), widened form.**
- An untwisted pairing gives \(\left(\begin{smallmatrix}A&B\\B&A\end{smallmatrix}\right)\).
- \(SHS={\rm diag}(2(A+B),2(A-B))\), checked.
- \(U=(A+B)/2\) is a \(W(N/2,N/4)\), with \(N/2\equiv2\pmod 4\).
- The sum-of-two-squares condition gives a contradiction exactly when \(N/4\) is not a sum of two squares.
- \(N\equiv12\pmod{16}\) gives \(N/4\equiv3\pmod 4\).
- There are infinitely many primes \(q\equiv5\pmod 8\), with \(N=16t+12\).

The widening is exactly twist-stage2's O2. The proof needed no other change.

**Corollary 6.1 and the Merchant sentence (l.187–194).**
- \(N=32n\) with input \(\HH(N/8)=\HH(m^2/8)\); Merchant's leading term is \((N/2)\log N\), so the paper's is twice it.
- At \(n=50\), \(\lfloor798!/(2^{10}50^3)\rfloor\) has 1963 digits, recomputed exactly.
- The design parameters, the lift of design automorphisms and the injectivity on classes all check.

**Stepaniants and FJZ (l.296).** The sentence matches the 23 November fix: "is at least", \(n=2^k\), exponent of order \(n\log^2n\). "Doubled matrices are never rigid" was checked there against FR-12.

**Norman (l.193).** The content is accurate to PRIOR-ART:135 (not read; Merchant's report quoted). Finding 9 concerns grammar and placement.

**Unchanged parts (§§2–7).** Re-read at referee level, not re-audited; nothing inconsistent with the 23 November coverage. The following were recomputed:
- \((I+K)z=2\one\);
- the Menon parameters;
- \(\sqrt X/(4\log X)\);
- \(D_{\rm M},D_{\rm B},D_4\) from the labellings and the gauge;
- the collision probability \((d-2)/(2(d-1))\);
- "at least five nonzero" from Parseval;
- the pattern counts \((h+abcD)/8\);
- the exclusion of \(|D|=h\) and \(|D|=h/2\);
- the two-mixed-cliques argument;
- \(r_{h+4}^2/r_h^2\).

**Numbers recomputed** (exact integers, venv Python):

| Quantity | Paper | Recomputed |
|---|---|---|
| \(f_{20}\) | < 0.254 | 0.25378 |
| \(4h^4/((h-1)2^{h-3})\) at 20 | < 0.258 | 0.25699 |
| \(r_{20}\) | < 1/8 | 0.12217 |
| \(g_{20}\) | < 0.037 | 0.03429 |
| good fraction at h = 20, 28, 36 | > 70% | 0.712, 0.9973, 0.99998 |
| \(a_{20}^{\rm proj}\) | 5 673 369 600 000 | same (`evidence/arith.txt`) |
| order-1600 floor | 1515 digits, 587135898904… | same (`evidence/arith.txt`) |
| Bush floor at m = 40 with \(D_{\rm B}\) | > 10^1268 | 1269 digits (not printed by any script; Finding 8) |
| \(D\) at m = 40 with free signs; \(D_4\) | 4187; 3842 digits | 4187; 3842 |
| Merchant at n = 50 | > 10^1962 | 1963 digits |
| N/4 not a sum of two squares among {12,28,36,60,76,84,108} | — | 12, 28, 60, 76, 84, 108 |

**README consistency.**
- The introduction is the abstract verbatim.
- What-is-new items 1–7 match the paper in scope, numbering and hypotheses: N > 8 and the involution condition in item 7, and the widened Corollary 8.4.
- "Not new" and "Earlier work" match the citations.
- The evidence table is stale in two rows (Findings 7, 8).
- Theorem and lemma numbers match `main.aux`: 1.1, 1.2, 3.1, 3.2, 3.3, 4.1, 6.1, 8.1, 8.2, 8.3 (Remark), 8.4.

**Process-history phrases.** None. "release code" and "release script" (l.226, l.280) point to artifacts, which is acceptable.

## Build hygiene

- `make paper`: three pdfLaTeX passes, exit 0. The Makefile's grep for `Warning:|Overfull|undefined references|undefined citations` finds nothing. A wider grep of `main.log` for warning, overfull or underfull matches only the `infwarerr` package banner.
- `pdffonts paper/main.pdf`: 23 fonts, all Type 1, all embedded and subset, all with ToUnicode. No Type 3.
- `pdfinfo`: Title "Rigid woven Hadamard matrices", Author "Jeffery Kline", 13 pages.
- `pdftotext`, raw and `-layout`: the text is readable, there are no `??`, and ligatures resolve. The only artifacts are the usual pdfTeX flattening of superscripts and fractions (Finding 16d).

## Resources

Single core; one `make paper`; one short exact-arithmetic script in the session scratchpad (not retained), under one CPU-second. No network.
