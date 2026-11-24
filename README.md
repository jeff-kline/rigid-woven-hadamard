# Rigid woven Hadamard matrices

Jeffery Kline

**Status: admitted, version 0.1.0.** Version DOI
[10.5281/zenodo.24507265](https://doi.org/10.5281/zenodo.24507265); the
concept DOI [10.5281/zenodo.24507264](https://doi.org/10.5281/zenodo.24507264)
always resolves to the latest version. The tag `v0.1.0` was frozen as a
release candidate before the DOI existed, so its README still says so.
Admission under the project's
[public research standard](https://jeff-kline.github.io/posts/research-program/index.html)
is a release decision, not peer review or a correctness certificate; see
[ADMISSION.md](ADMISSION.md).

The paper is [paper/main.pdf](paper/main.pdf); its source is
[paper/main.tex](paper/main.tex).

## Introduction

Meisner (1992) built Hadamard matrices, $\pm1$ matrices with orthogonal rows,
of order $N=m^2$ from one of order $m$: an $m\times m$ array of rank-one sign
blocks whose order and signs can be chosen freely. We prove three results
about these matrices and about a second construction, introduced here, of
order $N=4h^2$, in which a transversal design with four groups lets each local
sign vector serve four blocks.

**First, rigidity.** A typical output reveals which of its rows and columns
came from each block, so every equivalence must respect the blocks. As a
result, all but a fraction $o(1)$ of the outputs are *rigid*: their only
signed row and column symmetries are the identity and the negation of
everything.

**Second, a count.** For each fixed input, up to signed permutations and
transposition, the rigid outputs form $C$ classes with

```math
\log C = N\log N - cN + O\bigl(\sqrt N\log^2 N\bigr),
```

where $c=2-\log 2$ for Meisner's square and $c=2+\tfrac18\log 2$ for four
groups (natural logarithms). At order 1600, one design and one matrix of
order 20 give more than $10^{1514}$ rigid regular classes.

**Third, a limit.** A rank argument shows why such block constructions need
orders divisible by 16. At orders $N\equiv4\pmod 8$, every partition of a
Hadamard matrix into rank-one blocks with no part of size one has all parts
of size two, as in the Paley II matrices. The constructions give no new
orders.

![Three panels of black and white squares. Left: a 144 by 144 matrix divided by thin red lines into a 12 by 12 grid of blocks, with all-white blocks on the diagonal. Middle: the same matrix scrambled, which looks like noise. Right: the scrambled matrix re-sorted, with the 12 by 12 grid of patterned blocks restored.](figures/recovery.png)

*Recovering the blocks of a Meisner square from its entries.* Black is $-1$,
white $+1$. (a) A Bush-type square of order $N=144$ ($m=12$), built from the
Paley-type Hadamard matrix of order 12, with its $12\times12$ grid of rank-one
blocks. (b) The same matrix after a random signed permutation of its rows and
columns. (c) Matrix (b) with its rows and columns re-sorted into the groups
(fibres) found by the divisibility test in the proof of Proposition 4.1, which
reads only the entries of (b). The test finds all 12 row groups and all 12
column groups, so every block is again of rank one. It does not recover the
order of the groups, the order within a group, or the signs. These are exactly
what the disguise changed, and (b) alone cannot reveal them; so (c) is
equivalent to (a) but not equal to it.

Cautions:

- **Asymptotic theorems.** The figure illustrates recovery. It makes no
  rigidity claim for this particular matrix.
- **The paper's test selection goes wrong at this order.** Proposition 4.1
  chooses between two tests. Here some quartets that mix two groups reach
  $N/2$, which selects the large-quartet test, and that test finds 144 column
  groups instead of 12. The figure therefore applies the divisibility test
  directly.
- **Sylvester inputs defeat the divisibility test.** At order 64, where
  Sylvester's matrix is the only possible input, the test relates all 2016
  pairs of rows instead of the 224 true pairs.
- **Cost and evidence.** The test evaluates about $N^4/4$ sums of fourfold
  products, and its success here was checked against the hidden groups for one
  random seed only.

[code/figure_recovery.py](code/figure_recovery.py) draws the figure and checks
each statement above.

## What is new

Meisner (1992) published the square construction, and Craigen (1995)
published the weaving formula that contains it. Kharaghani's construction,
as restated by Bonato, Holzmann and Kharaghani (2001), gives Bush-type
matrices at every order that the two constructions reach. Norman (1973), as Merchant
reports, and Merchant (2006) constructed infinite families of rigid Hadamard designs, and
Merchant's Theorem 5.2 counts them. Lam, Lam and Tonchev (2000) and Orrick
(2008) gave large counts of inequivalent Hadamard matrices, and Spence's
catalogue contains rigid regular matrices of order 36. New here:

1. **Principal result: rigidity and class count for Meisner's square**
   (Theorem 1.1). For a fixed Hadamard matrix of order $m$ and $N=m^2$, as
   $m\to\infty$ all but a fraction $o(1)$ of the choices give rigid
   matrices whose block rows and block columns can be recovered from the
   entries, uniformly in the input. In the Bush-type version the number of
   classes of rigid outputs has logarithm
   $N\log N-(2-\log 2)N+O(\sqrt N\log^2 N)$; the same two terms hold
   without the Bush-type restriction.
2. **The four-group construction** (Theorem 1.2). From a Hadamard matrix of
   order $h$ and a transversal design with four groups and a suitable
   involution of its lines, it gives Hadamard matrices of order $N=4h^2$,
   each with a regular Bush-type form and an associated Menon design.
   Suitable designs exist, for example, when $h=p+1$ for a prime
   $p\equiv7\pmod{12}$, and at $h=20$. All but a fraction $o(1)$ of the
   outputs are rigid, and the number of classes of rigid outputs has
   logarithm $N\log N-(2+\tfrac18\log 2)N+O(\sqrt N\log^2 N)$.
3. **A finite count at order 1600** (Theorem 1.2, finite part). One design
   and the Paley matrix of order 20 give more than $10^{1514}$ inequivalent
   rigid regular matrices.
4. **Exact gauge** (Lemma 3.1). Two choices give the same matrix exactly
   when their port permutations agree and their sign ratios are constant on
   each connected component of the flag graph. This gives the exact number
   of distinct matrices: $2^{m^2}(m!)^{2m}$ for the square,
   $2^{m^2-m}((m-1)!)^{2m}$ for its Bush-type version, and
   $(2^h h!)^{8h}/2^{(h^2+h)/2}$ for four groups before regularizing signs.
5. **Rigid Hadamard designs** (Corollary 6.1). The square's lower bound also
   counts nonisomorphic rigid Hadamard designs on $N-1$ points. Where
   Hadamard matrices of orders $m$ and $m^2/8$ both exist, its leading term
   $N\log N$ is twice that of Merchant's lower bound. This comparison is
   asymptotic only: at order 1600 Merchant's bound exceeds $10^{1962}$ rigid
   designs ([code/arith.py](code/arith.py)), more than the finite count above implies.
6. **Blocks of rank one** (Theorem 8.1). Partition the rows of a Hadamard
   matrix of order $N$ into $|X|$ parts and its columns into $|Y|$ parts so
   that every block has rank one. Then $|X|+|Y|\ge N$ if
   $N\equiv4\pmod 8$, and $|X|+|Y|\ge N/2+1$ if $N\equiv8\pmod{16}$.
   Consequently, at $N\equiv4\pmod 8$ a partition with no part of size one
   has all parts of size two, and any partition with all parts of size at
   least four has $16\mid N$, whatever the blocks are built from. The same
   argument bounds the rank of a repair that would turn such a block
   matrix into a Hadamard matrix.
7. **Fibres of size two** (Proposition 8.2, Remark 8.3, Corollary 8.4). A
   symmetric Hadamard matrix $H$ of order $N>8$ with an involution $\sigma$
   of its indices, $H_{\sigma(i)\sigma(j)}=H_{ij}$, fixing exactly four
   indices gives a pairing into blocks of rank one that is twisted:
   no signing of rows and columns puts it, with those pairs, in the familiar
   doubled form with blocks $A$, $B$ above $B$, $A$. The Paley II matrices of order $2(q+1)$
   supply such pairings for every prime power $q\equiv1\pmod 4$ with
   $q\ge5$, and so attain the bound of Theorem 8.1. At every order
   $N\equiv4\pmod 8$ with $N/4$ not a sum of two squares, including every
   $N\equiv12\pmod{16}$, each partition into blocks of rank one without
   parts of size one is a twisted pairing. The paper does not claim that
   such involutions are the only source of such pairings.

Not new: the square construction and its Hadamard property (Meisner,
Craigen); the orders reached, which already carry Bush-type and regular
witnesses; the dimensions $N-1$ and $N/2$ of the binary code of a normalized
Hadamard matrix, on which Theorem 8.1 rests (Orrick's Theorem 4.3, which
credits Lander, with the Smith-form facts credited to Newman and Wallis);
the Paley II matrices; and the condition that the weight of a weighing
matrix of order $2\pmod 4$ is a sum of two squares, used in Corollary 8.4
(as stated by Christian and Shader). The four-group subarrays are weaves in
Craigen's sense, and its middle factor has the form of Craigen's signed
groups; what is new there is the construction as a whole, its recovery, its
rigidity and its count.

These statements rest on a bounded comparison recorded in
[audit/PRIOR-ART.md](audit/PRIOR-ART.md). In the sources examined we found
no published theorem giving typical recovery, signed rigidity and the
fixed-input class count together for Meisner's square, and no matching
finite rigid-regular lower bound at order 1600, and no statement of the
rank bound of Theorem 8.1, of Proposition 8.2 or of Corollary 8.4. The full text of Norman
(1973) was not openly accessible at the time of writing; Merchant reports
that it gives an infinite family of rigid Hadamard designs from doubled
Paley designs. Google Scholar, MathSciNet, zbMATH and the *Handbook of
Combinatorial Designs* were not searched. This is not a claim of historical
priority.

## Earlier work

- **Paley (1933)**: the Paley matrices, including the order-20 input and
  the symmetric Paley II matrices.
- **Norman (1973)**: rigid Hadamard designs. The full text was not openly
  accessible at the time of writing; Merchant reports that it gives an
  infinite family of rigid Hadamard designs from doubled Paley designs.
- **Meisner (1992)**: the square construction, as the case $v=1$ of a
  construction of regular Hadamard matrices of order $a^2v$.
- **Craigen (1995)**, *weaving*: the general formula; the square is the
  weave with the all-ones pattern. **Craigen (1995)**, *signed groups*: the
  representation machinery behind the four-group middle factor.
- **Lam, Lam and Tonchev (2000)**: counts of designs and matrices,
  including at least $3.66\cdot10^{11}$ inequivalent Hadamard matrices of
  order 40.
- **Bonato, Holzmann and Kharaghani (2001)**, Theorem 1: Kharaghani's
  symmetric Bush-type matrices, which cover the orders reached here.
- **Fon-Der-Flaass (2002)**, **Cameron and Stark (2002)** and
  **Muzychuk (2007)**: many strongly regular graphs from independent local
  assignments of incidence data. Graph isomorphism acts on one point set;
  matrix equivalence acts independently on rows and columns.
- **Christian and Shader (2004)**: nonexistence conditions for weighing
  matrices, used in Corollary 8.4.
- **Merchant (2006)**, Theorem 5.2: from a Hadamard design of order $n>2$,
  at least $(16n-2)!/(2^{10}n^3)$ rigid Hadamard designs of order $8n$,
  with further structural properties.
- **Orrick (2008)**: switching counts of inequivalent matrices, and
  Theorem 4.3 on the binary code of a Hadamard matrix.
- **Crnković and Švob (2022)**: switching of designs and explicit
  Bush-type examples.
- **Spence**: the catalogue of Hadamard matrices of order 36, which
  includes rigid regular matrices.
- **Ferber, Jain and Zhao (2022)** conjectured that the number of labelled
  Hadamard matrices of order $n$ is $2^{O(n\log n)}$; **Stepaniants (2026)**,
  solving problem FR-12 in Townsend's *Open Problems in Numerical Linear
  Algebra*, refuted it along powers of two by iterated doubling. Doubled
  matrices are never rigid, so that count does not bear on the rigid counts
  here.

## Evidence and limits

| Claim | Proved on paper | Certified computation | Computation only |
|---|---|---|---|
| Theorem 1.1 (square: recovery, rigidity, class count) | yes; audited | none | sampled constructions, quartet sums, kernel sizes and exponent diagnostics in [code/meisner-stage2-checks.py](code/meisner-stage2-checks.py); the Stirling terms in [code/arith.py](code/arith.py) |
| Theorem 1.2, asymptotic part (four groups) | yes; audited | none | an order-64 example in [code/gauge_check.py](code/gauge_check.py) |
| Regular Bush-type form of four-group outputs | yes; checked in an end-to-end read of the paper, no separate proof audit | the order-1600 example below | none |
| Exact gauge and distinct-matrix counts (Lemma 3.1) | yes; audited for each construction | fixed lines and $210$ components of the order-1600 geometry in [code/prod_check.py](code/prod_check.py), with [code/geom_check.py](code/geom_check.py) | gauge and regularization at order 64 in [code/gauge_check.py](code/gauge_check.py) and [code/reg_check.py](code/reg_check.py) |
| Order 1600: more than $10^{1514}$ rigid regular classes | yes; audited | exact integer floor, 1515 digits, in [code/count1600.py](code/count1600.py) and [code/arith.py](code/arith.py) | none |
| Bush-type square at order 1600: more than $10^{1268}$ classes, no rigidity claim | yes; audited | exact floors in [code/meisner_equal_terms.py](code/meisner_equal_terms.py) and [code/arith.py](code/arith.py) | none |
| One explicit regular matrix of order 1600 | not applicable | every entry, every row and column sum and every row-pair distance in [code/check1600.py](code/check1600.py) (an independent JavaScript implementation is [code/check1600.mjs](code/check1600.mjs)) | its rigidity is **not** certified |
| Corollary 6.1 (rigid designs, comparison with Merchant) | yes; audited | none | none |
| Theorem 8.1 (blocks of rank one) and its consequences | yes; audited | $\mathrm{rk}_2$ equals $N$ for Paley II at orders 12 to 108 in [code/size_two_fibres_check.py](code/size_two_fibres_check.py) | none |
| Proposition 8.2 and Remark 8.3 (Paley II pairings) | yes; audited | Hadamard property, symmetry, every block, the twist, for $q=5,13,17,29,37,41,53$, with a Sylvester control of order 32, in [code/size_two_fibres_check.py](code/size_two_fibres_check.py) | none |
| Corollary 8.4 (unavoidable twist) | yes; audited | none | the Paley II pairings at $N=12,28,60,76,84,108$ are twisted ([code/size_two_fibres_check.py](code/size_two_fibres_check.py)); all 495 rank-one pairings of two order-12 matrices are twisted ([audit/reviews/rank-one-blocks/twist_stage1_checks.py](audit/reviews/rank-one-blocks/twist_stage1_checks.py)) |
| Lemma 3.2 and Proposition 3.3 (general forms) | yes; checked in an end-to-end read; both specializations audited | none | none |
| Priority | bounded search; see [audit/PRIOR-ART.md](audit/PRIOR-ART.md) | | |

"Audited" means checked by process-separated AI reviews, not human peer
review. The asymptotic theorems give no finite range: for order-4 Sylvester
inputs the square's outputs are not rigid. The order-1600 count is an
existence statement over a fixed ensemble; no individual matrix of order
1600 has a rigidity certificate. The finite square bound counts classes
without a rigidity condition, and the finite bounds do not order the actual
class counts of the two constructions. No proof has been checked by a human
or formalised. The reviews are in [audit/reviews/](audit/reviews/) and the claim ledger is
[audit/CLAIMS.md](audit/CLAIMS.md).

## Reproduce

The checks need Python 3 with NumPy; the paper needs pdfLaTeX.

```sh
make verify PY=/path/to/python   # about 25 seconds on one core
make paper
```

`make verify` runs the ten scripts in `code/` and compares each output with
the pinned copy in `evidence/`. The optional `make node-check` runs the
JavaScript version of the order-1600 check with Node.js.

## Role of AI

AI assisted the derivations, the computer verification, the literature search
and the exposition under the author's direction. Process-separated AI reviews
checked the proofs and certificates; they are not independent expert peer
review, and no independent human expert has examined the proofs. The sources,
the reviews and their dispositions are in [audit/](audit/), and
[audit/ATTRIBUTION.md](audit/ATTRIBUTION.md) records which system found which
result.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
