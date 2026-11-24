# Release audit: claims consistency, privacy, GitHub math (24 November 2026)

Gate A1 of the admit-research-release standard, with the hygiene checks of R1 that concern privacy and
README math. Read-only audit; this file is the only file written.

**Auditor:** Claude (Opus 5.5) subagent, process-separated from the drafting sessions. Not peer review.

**Tree audited** (local, uncommitted; files changed while the audit ran, see note): sha256 prefixes at
09:46 CST

| File | sha256 (first 16) |
|---|---|
| README.md | 617978a854f9c2d1 |
| CITATION.cff | 9ce25ed1ba65c1c4 |
| ADMISSION.md | 4e9af3d9ef23ca24 |
| CORRECTIONS.md | 47fd8ed04d131710 |
| audit/ATTRIBUTION.md | 92b87baef15f11b5 |
| audit/CLAIMS.md | 83f294904406a64e |
| audit/PRIOR-ART.md | 170c1de634cf1878 |
| paper/main.tex | 97d9b4ced1fb9dcd |
| paper/main.aux | 0efe549eab0287ef |

**Concurrent changes.** During this audit ADMISSION.md was edited (P1 rescan recorded) and
`audit/reviews/rank-one-blocks/twist-stage1.md`, `twist-stage1.sha256`, `twist_stage1_checks.py` and
`twist-stage2.md` appeared (09:42–09:44). `twist-stage2.md` gives **VERIFIED** proof audits of the sharp
Theorem 8.1 with its consequences paragraph, and of Corollary 8.4. Findings 5–7 follow from that.

## Verdict: PASS-WITH-FIXES

One claim error (README scope of Proposition 8.2), stale audit statuses after the Corollary 8.4 audit, 1
broken README link, 51 broken links in the audit records, and privacy hits in copied review files (local
username, session ID, a private repository name). All fixes are textual. The README's numbering matches the
compiled paper, and the What-is-new claims otherwise match the paper's statements in scope. The Merchant,
Norman and involution wording is acceptable (small fixes below). GitHub renders all README math.

## Checks that passed

- **Numbering.** `paper/main.aux` (built 09:37:45, after `main.tex` 09:37:43) and `pdftotext` give
  Theorem 1.1, 1.2; Lemma 3.1, 3.2; Proposition 3.3, 4.1; Corollary 6.1; Theorem 8.1; Proposition 8.2;
  Remark 8.3; Corollary 8.4. Every number cited in README.md, ADMISSION.md, CORRECTIONS.md and
  ATTRIBUTION.md matches. `make paper` was not needed.
- **Title, author, version.** "Rigid woven Hadamard matrices", Jeffery Kline, 0.1.0 draft, no DOI and no
  `date-released` on every surface. CITATION abstract = paper abstract plus one sentence ("Novelty is
  bounded to the sources searched."). README Introduction follows the abstract.
- **Scope words.** Abstract, README introduction, CITATION and evidence table say "rigid regular classes".
  Theorem 1.2 and What-is-new item 3 say "inequivalent rigid regular matrices", which means the same under
  the paper's equivalence (transposes identified, main.tex:31). Asymptotic and finite statements are kept
  apart. Bush and unrestricted are distinguished in item 1 and in the 10^1268 row ("no rigidity claim").
- **Merchant figure.** log10 of (16n−2)!/(2^10 n^3) at n=50 is 1962.97 (recomputed here with lgamma), so
  "exceeds 10^1962" holds. PRIOR-ART:38's 10^1956 after dividing by 2·1600² also holds (1956.26).
- **Involutions.** No surface says that involutions are the only source of size-two pairings. README:105–106
  and main.tex:283 say the opposite explicitly.
- **Norman 1973.** README:124–127, README:135–137, main.tex:193, PRIOR-ART:135 and ADMISSION:35 all say
  the full text "was not openly accessible at the time of writing", and the first three quote Merchant's
  report the same way.
- **Process-history phrases.** None in README.md, paper/main.tex or CITATION.cff ("agent", "lane", "pass",
  "session", "handoff", model names, "cold", "draft" except the README status line).
- **Role of AI.** main.tex:301 is the standard text verbatim. The README version is a close paraphrase that
  points to ATTRIBUTION.md.
- **FR-12 citation.** The source README at `ajt60gaibb/OpenProblemsInNLA@0212a62` (owner Alex Townsend)
  states H(2^k) ≥ 2^{2^k(k−1)(k−2)/8} and cites FJZ Conjecture 1.3, printed page 456. This matches
  main.tex:296 and README:163–168.
- **GitHub math (Task 3).** `gh api markdown -f mode=gfm -F text=@README.md`: 67 `js-inline-math`
  elements for 67 source `$…$` spans; 1 `js-display-math` for 1 ```` ```math ```` block; no `<pre
  lang="math">`; no leftover `$` in the rendered text.
- **Emails, tokens, keys.** There are no email addresses, credentials, API keys or machine names anywhere in
  the tree, LICENSE included. `paper/main.log` holds only TeX system paths and is git-ignored.

## Findings

Severities: **claim error** · **consistency** · **link** · **privacy** · **wording**.

### Reader-facing surfaces

1. **README.md:97–99 — claim error.** Item 7 drops the hypothesis \(N>8\) of Proposition 8.2
   (main.tex:264), and "a symmetry of order two" can be read as a *signed* symmetry. The proposition needs
   an index involution with \(H_{\sigma(i)\sigma(j)}=H_{ij}\). Replace
   "A symmetric Hadamard matrix with a symmetry of order two fixing exactly four indices gives"
   with
   "A symmetric Hadamard matrix $H$ of order $N>8$ with an involution $\sigma$ of its indices,
   $H_{\sigma(i)\sigma(j)}=H_{ij}$, fixing exactly four indices gives".
   At README:105–106 replace "symmetries of order two are the only source" with
   "such involutions are the only source".

2. **README.md:194 — link.** `audit/LEDGER.md` does not exist. The checklist also lists an audit ledger as
   a canonical artifact. Either create it, or replace the sentence with
   "The reviews are in audit/reviews/ (`audit/reviews/`, path relative to the repository root) and the claim ledger is
   audit/CLAIMS.md (`audit/CLAIMS.md`, path relative to the repository root)."

3. **README.md:184 — consistency (stale) and evidence label.** `twist-stage2.md` now gives Corollary 8.4 a
   VERIFIED proof audit. The "certified computation" cell overstates the evidence:
   `size_two_fibres_check.py` only prints \(N \bmod 16\) and the twist of the Paley II pairing, and it does
   not test other partitions. Replace the row with
   `| Corollary 8.4 (unavoidable twist) | yes; audited | none | the Paley II pairings at $N=12,28,60,76,108$ are twisted (code/size_two_fibres_check.py (`code/size_two_fibres_check.py`, path relative to the repository root)); all 495 rank-one pairings of two order-12 matrices are twisted (audit/reviews/rank-one-blocks/twist_stage1_checks.py (`audit/reviews/rank-one-blocks/twist_stage1_checks.py`, path relative to the repository root)) |`

4. **README.md:182 — consistency (note).** The "audited" label for the **sharp** Theorem 8.1 rests on
   `twist-stage2.md` §(a). `sizetwo-stage2.md` verified only the weaker \(N-4\), \(N/2-3\) form ("not
   sharp, see O1"), and so did `theoremA-stage2.md`. Before 09:44 this label was unsupported; it is
   correct now. No README change is needed; see finding 6.

5. **ADMISSION.md:36 — consistency (stale).** Replace
   "**Pending:** claims-consistency audit of the README, paper, metadata and records, and a proof audit of
   Corollary 8.4."
   with
   "Proof audit of Corollary 8.4 and of the sharp Theorem 8.1: VERIFIED
   (audit/reviews/rank-one-blocks/twist-stage2.md (`audit/reviews/rank-one-blocks/twist-stage2.md`, path relative to the repository root)).
   Claims-consistency audit: PASS-WITH-FIXES
   (audit/reviews/RELEASE-AUDIT-CLAIMS-2026-11-24.md (`audit/reviews/RELEASE-AUDIT-CLAIMS-2026-11-24.md`, path relative to the repository root));
   **pending** the listed fixes and an end-to-end read of the final manuscript."

6. **audit/ATTRIBUTION.md:14 and :16 — consistency (stale).** In row 14, replace the "Checked by" cell
   "coordinating session, by hand" with
   "coordinating session, by hand; proof audit reviews/rank-one-blocks/twist-stage2.md (a)". In row 16,
   replace "coordinating session, by hand; **no separate proof audit yet**" with
   "coordinating session, by hand; proof audit reviews/rank-one-blocks/twist-stage*.md".

7. **paper/main.tex (whole) — consistency (A1 requirement).** The only end-to-end read,
   `assembled-paper/FINAL-READ-2026-11-23.md`, covers a 317-line draft from 23 November. The current
   350-line manuscript adds §8.1 (from line 244), §8.2, Corollary 8.4, the Stepaniants/FJZ sentences in
   §8.3 and the Norman sentence. The section audits cover line ranges, not the assembly. Run a short
   end-to-end read, or a diff-equivalence check against the audited texts, before freezing.

8. **paper/main.tex:298 — consistency (Merchant wording).** The second mention of the Merchant comparison
   does not say "asymptotic". Replace
   "Its comparison with Merchant concerns rigid \emph{derived designs};"
   with
   "Its comparison with Merchant is asymptotic and concerns rigid \emph{derived designs}; at order 1600
   Merchant's bound, above \(10^{1962}\), is the larger;".
   Optional, Corollary 6.1 statement (main.tex:188): after "twice that of Merchant's Theorem~5.2" add
   "; the comparison is asymptotic". README:82–87 and the proof at main.tex:193 already meet the standard.

9. **README.md:51–53 — consistency (Norman).** "Norman (1973) and Merchant (2006) constructed infinite
   families of rigid Hadamard designs" states Norman's result as checked fact. Replace with
   "Norman (1973), as Merchant reports, and Merchant (2006) constructed infinite families of rigid
   Hadamard designs".

10. **README.md:120–124 — consistency (novelty basis).** The bounded-search sentence covers only the
    square's recovery, rigidity and count and the order-1600 bound. It omits Theorem 8.1, Proposition 8.2
    and Corollary 8.4, which What is new lists as new and PRIOR-ART:141 records as NOT FOUND. After
    "...no matching finite rigid-regular lower bound at order 1600" add
    ", and no statement of the rank bound of Theorem 8.1, of Proposition 8.2 or of Corollary 8.4".
    Apply the same addition to PRIOR-ART:5 ("Finding").

11. **paper/main.tex:40 — wording.** A theorem should not refer to the abstract, and the abstract states an
    asymptotic equality, not a lower bound. Replace
    "In particular the Bush ensemble supplies at least the lower bound stated in the abstract."
    with
    "In particular, at each such order the Bush ensemble gives at least
    \(\exp(N\log N-(2-\log2)N-O(\sqrt N\log^2N))\) rigid classes."

12. **README.md:5–6 — wording.** "The claims are not yet frozen or audited" conflicts with the evidence
    table's "audited" cells. Replace with "The claims are not yet frozen, and the release audit is not
    complete."

13. **README.md:201 vs Makefile:26 — consistency.** The run time is "about 10 seconds" in one and "about
    15 seconds" in the other. Use one figure.

14. **README.md:170–185 — consistency (minor).** The evidence table has no row for the general forms of
    Lemma 3.2 and Proposition 3.3. CLAIMS G02/G03 call them UNAUDITED in general form, while
    FINAL-READ:7 found Proposition 3.3 "correct as stated". Optional row:
    `| Lemma 3.2 and Proposition 3.3 (general forms) | yes; checked in an end-to-end read; both specializations audited | none | none |`

15. **ADMISSION.md:17–29 and CORRECTIONS.md:15 — consistency (minor).** The README lists seven new items
    (Lemma 3.1 and Corollary 6.1 included). ADMISSION lists three principal claims. CORRECTIONS covers
    priority only for Theorems 1.1, 1.2 and 8.1. Suggested additions: in ADMISSION after item 3, add
    "Supporting results: Lemma 3.1 (exact gauge) and Corollary 6.1 (rigid designs)." In CORRECTIONS:15,
    replace "Theorem 1.1, Theorem 1.2 or Theorem 8.1" with
    "Theorem 1.1, Theorem 1.2, Theorem 8.1, Proposition 8.2 or Corollary 8.4". The abstract's "three
    results" (rigidity, count, limit) is a different grouping that the author approved; leave it.

16. **ADMISSION.md:35 — consistency (minor).** README:127–128 also lists the *Handbook of Combinatorial
    Designs* as not searched. Add it: "Not searched: Google Scholar, MathSciNet, zbMATH, the *Handbook of
    Combinatorial Designs*."

17. **audit/ATTRIBUTION.md:3 — wording.** "All work was done by AI agents under the author's direction"
    is broader than the Role of AI text. Replace with "The derivations, computations, literature searches
    and drafting recorded below were done by AI agents under the author's direction; the author set the
    scope and approved the claims."

18. **paper/main.tex:187, :338–339 — wording (optional).** Corollary 6.1 has no `\label`; add
    `\label{cor:designs}`. Norman and FJZ have no links; add
    `\href{https://doi.org/10.1007/BF00147858}{…}` and `\href{https://doi.org/10.1017/S0963548321000377}{…}`
    (DOIs as recorded in PRIOR-ART:39 and in the FR-12 README). Optional per twist-stage2 O1: also credit
    the primary source of the sum-of-two-squares condition (Geramita–Pullman–Wallis) next to Christian and
    Shader at main.tex:290.

19. **No script for the 10^1962 figure — consistency (minor).** README:86 gives the figure, but no script in
    `code/` computes it; it was checked only in FINAL-READ:207. Optionally add one line to
    `code/arith.py` printing the digit count of ⌊798!/(2^10·50^3)⌋ (1963 digits) and repin
    `evidence/arith.txt`.

### Audit records

20. **audit/CLAIMS.md:46, :80–113 — link (35 broken).** All 34 reference definitions point to
    `../four-group-gauge-2026-11-23/`, `../incidence-order-extensions-2026-11-23/` or
    `../paired-hole-repair-2026-11-23/`, which resolve to nonexistent folders at the repository root. The
    35th is `CODE.md` at :46. These targets are now in the repository:
    `[M]: reviews/meisner/MEISNER-RIGIDITY.md` · `[MA]: reviews/meisner/meisner-stage2-proof-audit.md` ·
    `[MI]: reviews/meisner/meisner-stage1-initial.md` · `[A]: reviews/four-group/stage2-proof-audit.md` ·
    `[AI]: reviews/four-group/stage1-initial.md` · `[RC]: ../code/reg_check.py` ·
    `[I]: reviews/four-group/CONSTRUCTIONS.md` · `[IA]: reviews/four-group/involution-audit.md` ·
    `[Q]: reviews/four-group/REGULAR-RIGIDITY.md` · `[Rec]: reviews/four-group/recovery-cold-audit.md` ·
    `[Cnt]: reviews/four-group/count-cold-audit.md` · `[Fin]: reviews/four-group/FINITE-1600.md` ·
    `[Bush]: reviews/four-group/credit-bush.md` · `[Cr]: reviews/four-group/credit-craigen.md` ·
    `[Sample]: ../code/check1600.mjs` · `CODE.md` → `../README.md#reproduce`.
    These targets are not released: [H], [R], [Prior], [IR], [Examples], [PW], [PT], [PWA], [PS], [PTA],
    [Direct], [DirC], [Def], [Quart], [QA], [QAdd], [SkC], [Qc], [Qi]. Turn each into plain text, e.g.
    "RESULT.md (internal working file, 23 November 2026; not in this repository)". Remove the brackets so
    they no longer render as links.

21. **audit/CLAIMS.md (whole) — consistency (stale ledger).** The ledger is dated 23 November. It has no rows
    for Theorem 8.1, Proposition 8.2, Remark 8.3 or Corollary 8.4, and its IDs are not mapped to paper
    numbers. Add a section "Rank-one blocks (24 November 2026)" with four rows: Theorem 8.1 VERIFIED
    (twist-stage2 (a); weak form in theoremA-stage2 and sizetwo-stage2), Proposition 8.2 VERIFIED
    (sizetwo-stage2), Remark 8.3 VERIFIED (sizetwo-stage2; control defect D1 fixed at main.tex:280),
    Corollary 8.4 VERIFIED (twist-stage2). Add a mapping line: G01/F05/M2 → Lemma 3.1; G02 → Lemma 3.2;
    G03 → Proposition 3.3 (checked in FINAL-READ); M1–M4 → Theorem 1.1; M5 → Corollary 6.1;
    F01–F09, F11 → Theorem 1.2 and §§2.2, 7; B01–B02 → §7. Update the header count, now 42 rows with 24
    VERIFIED. Correct the stale placement "body, marked UNAUDITED" for X2 (row 49): X2 is not in the paper.

22. **audit/PRIOR-ART.md:7, :11–14, :74, :118 — link (16 broken).** Remap
    `../incidence-order-extensions-2026-11-23/credit-bush.md` → `reviews/four-group/credit-bush.md`,
    `…/credit-craigen.md` → `reviews/four-group/credit-craigen.md`,
    `…/credit-count.md` → `reviews/four-group/credit-count.md`,
    `../four-group-gauge-2026-11-23/MEISNER-RIGIDITY.md` → `reviews/meisner/MEISNER-RIGIDITY.md`.
    Turn these unreleased targets into plain text marked "not in this repository": NOVELTY-REVIEW.md,
    PRIOR-ART-CONCLUSION.md, HANDOFF-base-inputs.md, RESULT.md, OPEN-ITEMS.md.

23. **audit/PRIOR-ART.md:138–141 — consistency.** Use paper numbering, and point to files that exist.
    Replace "Lemma A0 of the rank-one-blocks theorem" with "the lower bound in the proof of Theorem 8.1".
    Replace 'Corollary "Unavoidable twist"' with "Corollary 8.4". Replace
    "See ../defect-repair-weaving-2026-11-23/CREDIT.md, PRIOR-ART*.md, and the twisted-two-by-two review."
    with "See reviews/rank-one-blocks/CREDIT.md (`reviews/rank-one-blocks/CREDIT.md`, path relative to the repository root)."

24. **audit/PRIOR-ART.md:13 — consistency (minor).** "The four-group proof gives **greater than
    $10^{1514}$** rigid Bush-type classes" → "…rigid regular classes, each with a Bush-type
    representative", to match the paper and README.

25. **audit/PRIOR-ART.md:50, :63 — consistency (minor).** Row 50 cites Crnković–Švob as arXiv only, while
    the paper cites *Des. Codes Cryptogr.* 90 (2022). Row 63 records FJZ as "Abstract. Full text not
    checked", while the paper attributes a specific conjecture to them. Add to row 63: "Conjecture 1.3
    (printed p. 456 of the CPC 2022 version) is cited as quoted in the FR-12 README at commit 0212a62."

26. **audit/reviews/ (copied reviews) — link (plain-text references; minor).** The stage-2 audits audit
    files that are not in the repository: RESULT.md (four-group/stage2-proof-audit.md:1, :141;
    meisner-stage2-proof-audit.md:212, :249), FABLE-REPORT.md (theoremA-stage2.md:6, :177),
    STATEMENTS.md, CODE.md, OPEN-ITEMS.md, audit/sizetwo_stage1_checks.py (sizetwo-stage1.md:88,
    sizetwo-stage2.md:154). These are retained historical records; do not rewrite them. Add
    `audit/reviews/README.md` stating that the audited working files (RESULT.md, FABLE-REPORT.md,
    STATEMENTS.md, CODE.md, OPEN-ITEMS.md, HANDOFF-base-inputs.md, PRIOR-ART-CONCLUSION.md) are not
    released, and that their hashes are recorded inside the reviews where available.

### Privacy (Task 2)

Sealed stage-1 files are hash-pinned by later reviews, so editing them breaks the recorded hash. For those
files (marked **sealed**), redact and add a dated note next to the pin, e.g.
"Redacted 2026-11-24: local paths at lines N; the hash above is of the unredacted original."

27. **audit/reviews/assembled-paper/FINAL-READ-2026-11-23.md:228 — privacy (username + session ID).**
    Replace the path `<scratch>/finalread/` with
    "scratch scripts `nums.py` and `dbg.py` (session scratchpad; not retained)".
    At :226, replace "Python under `~/.venvs/claude/bin/python`" with "Python 3 in a virtual environment".

28. **audit/reviews/meisner/meisner-stage1-initial.md:98, :103 — privacy (username + session ID), sealed**
    (pinned at MEISNER-RIGIDITY.md:4). At :98, replace the text from "~/.venvs/claude/bin/python" through
    "…/dreadnaut" with "Python 3 in a virtual environment, with nauty's dreadnaut from a local SageMath
    installation". At :103, replace with "Script: `meis.py` (session scratchpad; not retained)." Add the
    redaction note at MEISNER-RIGIDITY.md:4.

29. **audit/reviews/meisner/meisner-stage2-proof-audit.md:265, :267 — privacy (username + session ID).**
    Replace the scratchpad path with "`meisner_audit_checks.py` (session scratchpad; not retained;
    sha256 below)". At :267, replace "~/.venvs/claude/bin/python" with "Python 3 in a virtual
    environment".

30. **audit/reviews/meisner/MEISNER-PACKET.md:14, :36, :38 — privacy (absolute home paths).** Replace
    `<workspace>/reviews/incidence-order-extensions-2026-11-23/credit-bush.md` with
    `reviews/four-group/credit-bush.md`; `…/REGULAR-RIGIDITY.md` with
    `reviews/four-group/REGULAR-RIGIDITY.md`; and
    `<workspace>/reviews/four-group-gauge-2026-11-23/PRIOR-ART-CONCLUSION.md` with
    "PRIOR-ART-CONCLUSION.md (internal working file; not released)".

31. **audit/reviews/four-group/STATEMENT-PACKET.md:6, :42, :44 — privacy (absolute home paths).** Replace
    `<workspace>/reviews/incidence-order-extensions-2026-11-23/` with
    "the four-group working folder (its released files are in `audit/reviews/four-group/`)". Replace
    `<workspace>/reviews/four-group-gauge-2026-11-23/` with "the gauge working folder
    (not released)".

32. **audit/reviews/rank-one-blocks/CREDIT.md:4–5 — privacy (username + session ID).** Replace with
    "PRIOR-ART.md was not redone. Downloaded sources were kept in a local scratch folder (not retained)."

33. **audit/reviews/rank-one-blocks/CREDIT.md:170 — privacy (private repository name).** Replace
    "(Includes the user's private repo jeff-kline/hadamard-count-lower-bound; unrelated.)" with
    "(Includes one unrelated private repository of the author.)"

34. **audit/reviews/rank-one-blocks/sizetwo-stage2.md:108, :153–155 — privacy (home directory layout).**
    Replace the reproduction block with
    "From the repository root: `python3 code/size_two_fibres_check.py` (about 0.3 s). The Stage-1 script
    `sizetwo_stage1_checks.py` is not released." At :108, replace "`~/.venvs/claude/bin/python
    code/size_two_fibres_check.py`" with "`python3 code/size_two_fibres_check.py`".

35. **Home-relative interpreter or skill paths, no username — privacy (low).**
    four-group/stage2-proof-audit.md:128 and four-group/stage1-initial.md:66 (`~/.venvs/claude/bin/python`
    → "Python 3 in a virtual environment"); **sealed:** sizetwo-stage1.md:88 (same),
    theoremA-stage1.md:16 (`~/.claude/skills/cold-examiner/SKILL.md` → "the cold-examiner protocol"),
    twist_stage1_checks.py:5 (`Run: ~/.venvs/claude/bin/python twist_stage1_checks.py` → `Run: python3
    twist_stage1_checks.py`; pinned in twist-stage1.sha256 and twist-stage2.md:5). These reveal only a venv
    name. Fixing the sealed files is optional; if you fix them, add the redaction note.

**Not hits.** `audit/search-log-github-2026-11-2{3,4}.txt` list public third-party repositories; the
`scratchpad/` entries there belong to a third-party repo (CIRISAI). PRIOR-ART:113's
`order18-jacobi-triples` is public (checked with `gh repo view`). No email addresses at all,
no tokens, keys, machine names or agent IDs. The session ID `06928e86-…` appears only in findings 27, 28,
29 and 32.

## Method

`grep` over the whole tree (including `audit/`, `code/`, `evidence/`, `build/`, `paper/`) for `/Users/`,
`/private/`, `/tmp/`, `~/`, `<user>`, UUIDs, email patterns, token prefixes (`ghp_`, `github_pat`,
`sk-`), "private repo". A link checker resolved every relative Markdown link and reference definition in
every `.md` file against the repository root. Numbering came from `main.aux` and `pdftotext`. The Merchant
figure was recomputed with `lgamma` in a venv. The README was rendered with the GitHub Markdown API and the
math elements counted against the source spans. No other file was modified.

Redacted 2026-11-24 for privacy (local paths and usernames only).
