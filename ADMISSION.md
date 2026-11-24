# Admission record

**Current state:** DRAFT

**Verdict:** NOT YET ADMITTED

**Version:** 0.1.0 (in preparation)

**Standard:** [A Public Standard for This Work](https://jeff-kline.github.io/posts/research-program/index.html)

Admission is a project release decision. It is not peer review, a correctness
certificate, or proof of global novelty.

**Scope set by the author.** The author chose the title and the repository
name and approved the abstract and the README introduction on 2026-11-24.

## Principal claims

1. Meisner's square (Theorem 1.1): for a fixed Hadamard matrix of order $m$,
   as $m\to\infty$ all but a fraction $o(1)$ of the Bush labellings have
   recoverable fibres and are rigid, and the rigid classes satisfy
   $\log C=N\log N-(2-\log 2)N+O(\sqrt N\log^2 N)$. This is the principal
   result.
2. The four-group construction (Theorem 1.2): the same with linear term
   $-(2+\tfrac18\log 2)N$, and more than $10^{1514}$ rigid regular classes at
   order 1600.
3. Rank-one blocks (Theorem 8.1): $|X|+|Y|\ge N$ for $N\equiv4\pmod 8$ and
   $|X|+|Y|\ge N/2+1$ for $N\equiv8\pmod{16}$, with Proposition 8.2,
   Remark 8.3 and Corollary 8.4 on fibres of size two.

Supporting results: Lemma 3.1 (exact gauge) and Corollary 6.1 (rigid designs).

## Gates

| Gate | Status |
|---|---|
| P1 prior work and credit | Bounded search of 23–24 November 2026: [audit/PRIOR-ART.md](audit/PRIOR-ART.md). Norman 1973 not openly accessible, accepted by the author on 2026-11-23. Not searched: Google Scholar, MathSciNet, zbMATH, the *Handbook of Combinatorial Designs*. GitHub and arXiv rescan done 2026-11-24 ([audit/search-log-github-2026-11-24.txt](audit/search-log-github-2026-11-24.txt)): no overlap found. aiXiv rescan done the same day (page 1 of six queries): no overlap. To repeat within 7 days before tagging. |
| A1 claim consistency | Proof audit of Corollary 8.4 and of the sharp Theorem 8.1: VERIFIED ([audit/reviews/rank-one-blocks/twist-stage2.md](audit/reviews/rank-one-blocks/twist-stage2.md)). Claims-consistency audit: PASS-WITH-FIXES ([audit/reviews/RELEASE-AUDIT-CLAIMS-2026-11-24.md](audit/reviews/RELEASE-AUDIT-CLAIMS-2026-11-24.md)), fixes applied 2026-11-24. End-to-end read of the final manuscript: READY-WITH-FIXES ([audit/reviews/assembled-paper/FINAL-READ-2026-11-24.md](audit/reviews/assembled-paper/FINAL-READ-2026-11-24.md)), one statement error (Theorem 1.1, small orders) and wording fixes, all applied 2026-11-24. |
| R1 release and stewardship | **Pending:** clean-package check, freeze, tag, archive and DOI. |
