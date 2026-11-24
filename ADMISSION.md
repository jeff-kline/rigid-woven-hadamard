# Admission record

**Current state:** ADMITTED

**Current verdict: ADMITTED** on 2026-11-24, with the qualifications and residual risks below

**Version:** 0.1.0 · tag `v0.1.0` at commit `4fe285fa44ab51397247b0dcfe9559f6c7ebf87b` · version DOI [10.5281/zenodo.24507265](https://doi.org/10.5281/zenodo.24507265) · concept DOI [10.5281/zenodo.24507264](https://doi.org/10.5281/zenodo.24507264)

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
| A1 claim consistency | Proof audit of Corollary 8.4 and of the sharp Theorem 8.1: VERIFIED ([audit/reviews/rank-one-blocks/twist-stage2.md](audit/reviews/rank-one-blocks/twist-stage2.md)). Claims-consistency audit: PASS-WITH-FIXES ([audit/reviews/RELEASE-AUDIT-CLAIMS-2026-11-24.md](audit/reviews/RELEASE-AUDIT-CLAIMS-2026-11-24.md)), fixes applied 2026-11-24. End-to-end read of the final manuscript: READY-WITH-FIXES ([audit/reviews/assembled-paper/FINAL-READ-2026-11-24.md](audit/reviews/assembled-paper/FINAL-READ-2026-11-24.md)), one statement error (Theorem 1.1, small orders) and wording fixes, all applied 2026-11-24. Figure 1 was added after that read, at the author's request; every claim in its caption is checked by [code/figure_recovery.py](code/figure_recovery.py), which `make verify` runs. |
| R1 release and stewardship | Candidate frozen 2026-11-24: correction policy ([CORRECTIONS.md](CORRECTIONS.md)), citation metadata without a release date, verification commands with pinned outputs (`make verify`, ten checks), manifest, clean-copy build and verification. Zenodo GitHub integration enabled by the author. Tag `v0.1.0` (annotated, noreply tagger) pushed 2026-11-24; [GitHub Release](https://github.com/jeff-kline/rigid-woven-hadamard/releases/tag/v0.1.0) published. GitHub API zipball for the tag downloaded twice, identical: SHA-256 `788f25e314fdafab6e0ec526b1a2d866e961385a23008fd21b174c7028d38907`, 710529 bytes. Zenodo record 24507265 (open, GPL-3.0, version v0.1.0): its file `jeff-kline/rigid-woven-hadamard-v0.1.0.zip` is byte-identical to that zipball (same SHA-256; `cmp` clean). `git archive v0.1.0`, a secondary check not expected to equal the zipball: SHA-256 `dea0b3177d12168ab160b0fe6de905d688ad8785ba0025fe4c1a41362c05dbcd`. Site listing live at <https://jeff-kline.github.io/> (commit `42c9db5`). |

## Qualifications and residual risks

- Admission is a release decision, not peer review. The proofs were checked by process-separated AI reviews, not by a human expert, and nothing is formalised.
- The theorems are asymptotic; no finite range of rigidity is proved, and no individual matrix of order 1600 has a rigidity certificate.
- Novelty is bounded to the sources searched ([audit/PRIOR-ART.md](audit/PRIOR-ART.md)). Norman (1973) was not openly accessible at the time of writing. Google Scholar, MathSciNet, zbMATH and the *Handbook of Combinatorial Designs* were not searched.
- At order 1600 Merchant's bound for rigid designs (above 10^1962) exceeds the paper's finite count; the comparison with Merchant is asymptotic only.
- Contributions of the two AI systems involved are intermixed ([audit/ATTRIBUTION.md](audit/ATTRIBUTION.md)).
- The tag `v0.1.0` carries the honest release-candidate wording from before the DOI existed; these living records were updated afterwards.
