# Credit and prior-art check (2026-11-24)

Scope: read-only check of the statements in audit/STATEMENTS.md against the literature. Correctness is not judged.
PRIOR-ART.md was not redone. Downloaded sources were kept in a local scratch folder (not retained).

Read levels: SOURCE = full text read (pdftotext of a PDF fetched today). SECONDARY = a statement quoted from a paper I read at
source, about a paper I did not read. ABSTRACT = search snippet or abstract only. INFERENCE = my own deduction, labelled.

## Q1. Lemma A0 (2-rank of a Hadamard matrix)

Verdict: KNOWN (the code/2-rank statement), with the exact form of A0 a two-step corollary. Smith-form facts are KNOWN (Newman, Wallis 1971).

Exact statements found.
- Orrick, "Switching operations for Hadamard matrices", arXiv math/0507515v4 (SIAM J. Discrete Math. 2008), section 4.2 (SOURCE).
  Code definition: normalise columns so the first row is all 1, change -1 to 0, take the F_p-span of the rows; "The 2-rank of a Hadamard
  matrix is the same as the dimension of its associated binary code." Theorem 4.3, "proved (in greater generality) in many places.
  (For example, see [24], Section 2.3.)", [24] = E. S. Lander, Symmetric designs: an algebraic approach, LMS Lecture Notes 74, 1983:
  H Hadamard of size n, C its binary code. (1) n = 4 mod 8: C = {1_n}^perp, dim C = n-1. (2) n = 0 mod 8: C self-orthogonal, dim C <= n/2.
  (3) n = 8 mod 16: C self-dual, dim C = n/2.
- Same paper, section 4.3 (SOURCE), citing Newman [30] and Wallis [38] (both cited, not read):
  "(1) s1 = 1; s2 = ... = s_{alpha+1} = 2, for some alpha >= floor(log2 n)+1; (2) s_i s_{n+1-i} = n."
  Refs: M. Newman, "Invariant factors of combinatorial matrices", Israel J. Math. 10 (1971) 126-130; W. D. Wallis, "Integral equivalence of
  Hadamard matrices", Israel J. Math. 10 (1971) 349-358.
- Michael and Wallis, "Skew-Hadamard matrices and the Smith normal form", Des. Codes Cryptogr. 13 (1998) 173-176: this is the SKEW case only.
  Greaves-Suda, arXiv 1801.07516 (SOURCE, intro): "The Smith normal form of skew-symmetric Hadamard matrices of order 4t is uniquely
  determined [13, 8]. Theorem 1.1: diag[1, 2^(2t-1), (2t)^(2t-1), 4t]." So Michael-Wallis is NOT the source for general Hadamard matrices.
  The paper itself is INACCESSIBLE (Springer returned an HTML page, not the PDF).
- Assmus-Key, Trans. AMS 330 (1992) 269-293: INACCESSIBLE (AMS PDF returned HTML). Orrick (SOURCE) cites them only for dimensions of the
  five order-16 codes (5,6,7,8,8) and the order-24 codes (all dim 12).

Is the 2-rank bound itself stated? Yes, in code language, for NORMALISED H: dim = N-1 (N = 4 mod 8), = N/2 (N = 8 mod 16) (Orrick Thm 4.3, citing Lander).
The statement "rk2 beta(H) >= N-4 for any H = (-1)^beta" is not stated in this form in anything I read.
INFERENCE (not found in a source): it follows in two steps. (i) For normalised H, beta = J - B, so rk2 beta >= dim C - 1, i.e. >= N-2
and >= N/2-1. (ii) Row and column negations change beta by a rank-one matrix each, so rk2 changes by at most 2. This gives N-4 and N/2-3,
exactly the A0 constants. A0 is therefore a lossy consequence of Orrick Thm 4.3 (and of Lander 1983 Sect. 2.3, not read). The Smith route
is a valid second proof of a weaker statement but is not needed for credit.

## Q2. Theorem A (rank-one tiling and 2-rank obstruction)

Verdict: NOT FOUND IN SEARCHED CORPUS for the obstruction as stated (|X|+|Y| >= N-4 for rank-one tilings). The ingredients are known:
A0 (Q1) and the subadditivity of 2-rank under Kronecker products.
- Abiad-Haemers, arXiv 1412.2945 (ABSTRACT plus search snippet; only the first page read): 2-rank of A_H = (J-H)/2 is subadditive under
  Kronecker products. This is A1-type, not an obstruction to a tiling.
- Counter-check on scope: HKO 2010 Theorem 16 (SOURCE, see Q3) builds K = [r_j^t r_i], a Hadamard matrix of order 4n^2 whose blocks are
  rank-one outer products with 2n row and 2n column fibres. It requires 2n to be a Hadamard order, so 4n^2 = 0 mod 16 and A0 does not apply
  (A0 covers only N = 4 mod 8 and 8 mod 16). No conflict with Theorem A as stated; but it shows rank-one-tiled Hadamard matrices are an
  established family at orders 16k^2.
- Craigen weaving (Q4) produces rank-one-tiled matrices by design (blocks A_i[.,p] B_j[q,.]); Theorem A would apply to woven Hadamard
  matrices at N = 4 mod 8 or 8 mod 16. I found no statement of such a constraint in the weaving literature I read.
- Searched: rank-one blocks, decomposable/Kronecker-structured Hadamard, 2-rank obstruction. Hits were unrelated (3x3 matrix multiplication over F2,
  Z2Z4-linear Hadamard codes, switching of SRGs).
- Not searched (INACCESSIBLE): arXiv listing/search (HTTP 429), Semantic Scholar (not performed).

## Q3. Theorem C (order a(ak+1), a = 4u^2, from unbiased pair, S(2,k+1,ak+1) and skew conference matrix)

Verdict: PARTLY KNOWN. The unbiased-pair facts are KNOWN and read at source. The construction itself, or an equivalent, was NOT FOUND IN SEARCHED CORPUS.

HKO read at source: W. H. Holzmann, H. Kharaghani, W. Orrick, "On the real unbiased Hadamard matrices", in Combinatorics and Graphs,
Contemp. Math. 531, AMS 2010, 243-250. SOURCE = the preprint dated February 8, 2010, at https://www.cs.uleth.ca/~hadi/research/real-mub-12-09.pdf.
It may differ from the published version.
- Definition: H, K of order n unbiased if H K^t = sqrt(n) L, L Hadamard.
- Abstract: "the number of MUH matrices of order 4n^2, n odd is at most 2 and the bound is attained for n = 1, 3. Furthermore, we find a lower
  bound for the number of MUH matrices of order 16n^2, assuming the existence of a Hadamard matrix of order 4n."
- Theorem 5: "There are two regularly unbiased Hadamard matrices of order 36" (explicit matrices in Tables 1, 2; found by searching over 3,000,000
  known order-36 Hadamard matrices). Conjecture 6: m = 2 for RMUH of order 4n^2, n odd.
- Lemma 3 / Corollary 4 are stated for "regularly" unbiased pairs (m <= 2). The abstract's "at most 2" for general MUH is argued, as a
  known easy fact, in Best-Kharaghani below. Theorem 13: m mutually suitable Latin squares of size 2n, 2n a Hadamard order => m mutually
  unbiased Bush-type Hadamard matrices of order 4n^2. Theorem 16: m+1 MUH of order 4n^2.
- Existence for odd n >= 5: HKO attains the bound only for n = 1, 3. Because 2n must be a Hadamard order in Theorems 13 and 16, those theorems give
  nothing for n odd.

Other sources read (SOURCE):
- Best-Kharaghani, "Unbiased complex Hadamard matrices and bases", Cryptogr. Commun. 2 (2010), arXiv 1209.4315: unbiased pairs exist only in square orders;
  "the maximum number of mutually unbiased Hadamard matrices of order 4n^2, n odd, does not exceed 2"; Lemma 13 (weakly unbiased, order 4n, n odd, w(n) <= 2);
  "Until very recently no example for which the upper bound 2 is attained was known besides the trivial ... order 4. The first non-trivial
  example of unbiased Hadamard matrices of order 36 is shown in [4]" ([4] = HKO). They add new order-36 pairs from complex pairs of order 18.
- Kodalen, "Linked systems of symmetric designs", arXiv 1712.02911 (SOURCE, Thm 8.2): optimistic LSSD(v,k,lambda;w) with v-2k = -2 sqrt(k-lambda)
  has v = 4u^2, w <= 2u^2, "if u is odd, then w = 2". Equivalence of regular unbiased Hadamard matrices with LSSDs of Menon parameters.
- Kharaghani-Suda, arXiv 1601.04416 (first page only), unbiased orthogonal designs: no S(2,k,v) content seen.
- Matolcsi-Ruzsa-Weiner, arXiv 1201.0631 (SOURCE, p. 10): "in several dimensions d = 4n^2 pairs (and even larger systems) of real unbiased Hadamard
  matrices are known to exist [4, 11]". Does not list which n.
- Kharaghani-Sasani-Suda Bush-type papers (arXiv 1412.5297, ABSTRACT/first page): no unbiased Bush-type pair for n odd; bound 2n-1 for mutually unbiased Bush-type.
- Araya-Harada-Suda 1504.01236 (quasi-unbiased; SOURCE, Remark 5.5): "f <= 2 if n = 4 alpha^2 and alpha is odd [HKO, Lemma 3.3]"; order-36 pair from [HKO].
  (HKO's preprint numbers this as Lemma 3/Corollary 4. The published numbering may differ.)

Real unbiased pairs of order 4u^2, u odd >= 5: NOT FOUND. No source I read exhibits one, none states it is impossible, and none says it is open
(order 100: no statement). Matolcsi et al.'s "several dimensions" is the only hint and is unspecific. HKO Conjecture 6 concerns the upper bound only.
OpenAlex list of citers of HKO (W4232894208, 41 works, titles only) contains no title that suggests a Steiner-system or conference-matrix
construction; nearest titles: "Balancedly splittable Hadamard matrices" (2018), "Bush-type Butson Hadamard matrices" (2023), "Unbiased weighing matrices of weight 9"
(2025), "On Regular Quaternary Hadamard Matrices" (2026). None of these was read. INFERENCE: "Steiner equiangular tight frames" (Fickus-Mixon-Tremain 2011;
title only) places blocks by Steiner-system incidence, which is structurally related to the Theorem C tile placement, but it builds rectangular frames, not square
Hadamard matrices. Not read.
Ionin-Kharaghani, Kharaghani 1999, Jungnickel-Kharaghani: BGW-based and Bush-type constructions of symmetric designs (ABSTRACT via search; nothing about S(2,k,v)).
Three searches for "Hadamard from Steiner system" returned only Kronecker/Paley/Mathon items and a Cameron encyclopedia entry on Steiner triple systems of order 15 (not read).
Not read, so credit risk remains for: Kharaghani 1985 "Arrays for orthogonal designs" (HKO Theorem 1 source), Ionin-Kharaghani papers.

## Q4. Craigen 1995

Verdict: PARTLY KNOWN. Weaving theorem read at secondary level only. Both Craigen papers INACCESSIBLE at source.
- Title check: J. Combin. Des. 3 (1995) no. 1, 1-13 is "Constructing weighing matrices by the method of weaving" (OpenAlex W2078034177, DOI 10.1002/jcd.3180030103; confirmed
  also by the reference list in arXiv 2309.07522, SOURCE). I found NO paper titled "Weaving rectangular matrices and the existence of orthogonal designs"
  (OpenAlex top results for that title: none; search 86 hits, none match). The title in the task appears to be wrong, or a different version of the paper. The original is closed access (OpenAlex "Closed").
- Signed groups paper: J. Combin. Theory A 71 (1995) 241-?, DOI 10.1016/0097-3165(95)90002-0, OpenAlex marks it "bronze OA", but the ScienceDirect PDF URL returned an HTML page to curl.
  INACCESSIBLE. Not read.
- Exact weaving theorem, SECONDARY, from the full-text survey arXiv 2309.07522 (Section 3.5.3, Theorem 3.17, "cf. [16, Theorem 1]", [16] = the JCD paper; "The version of this next Theorem that appears in
  [16] refers only to real weighing matrices"): let M be an m x n (0,1)-matrix with row sums r_i and column sums c_j. If for fixed a, b there are A_i in CGW(r_i, a; k1) and
  B_j in CGW(c_j, b; k2), then there is a CGW(sigma(M), ab; k), sigma(M) = sum r_i = sum c_j, k = lcm(k1,k2). Construction: if m_ij = 0 the block is 0_{r_i x c_j}; if m_ij = 1 and
  it is the p-th nonzero in row i and q-th nonzero in column j, block W_ij = A_i[.,p] B_j[q,.], "the rank one r_i x c_j matrix". Proof checks W W* = ab I.
  Example 3.18: CGW(15,9;3) from a 5 x 5 circulant M. Application: W(66,36) from W(13,9), W(10,9), W(6,4), W(4,4) and a 6 x 13 matrix M.
- Answer to the question: the blocks are rank one by construction (or zero). The inputs A_i, B_j are full (non-defective) weighing matrices. The survey states no variant allowing non-rank-one blocks
  or defective inputs. For Hadamard output, weight = order forces ab = sigma(M) and every A_i, B_j to be a Hadamard matrix of order r_i, c_j (INFERENCE from the statement).
  Craigen-Kharaghani, "Weaving Hadamard matrices with maximum excess and classes with small excess", JCD 12 (2004) 233-255 (closed, ABSTRACT only via PRIOR-ART): not read.
- Craigen, "The craft of weaving matrices", Congr. Numer. 92 (1993) 9-28 and Craigen's 1991 Waterloo thesis "Constructions for orthogonal matrices": cited in the survey, not read.
- Also read (SOURCE): Craigen-Kharaghani, "A combined approach to the construction of Hadamard matrices" (Australas. J. Combin. 13 (1996) 89-?; title taken from the OCR page): a different method (orthogonal designs and sequences), no weaving statement
  captured. Livinskyi's thesis (Umanitoba) cites Craigen's signed-group bounds; no weaving content.

## Q5. Class S1 (twisted case)

Verdict: NOT FOUND IN SEARCHED CORPUS (the normal form H = [[A,B],[C,A o B o C]], or the pair-swap form). Nothing read contradicts it.
- A 2x2 block of +-1 has rank one iff the product of its four entries is +1, so the normal form is elementary algebra (INFERENCE; not a literature claim).
- Related but different: Orrick (SOURCE) defines switching Hall sets and closed quadruples (Hadamard-product conditions on quadruples of rows); the "H_2-reducible Hadamard matrices of order 6" arXiv
  1003.4133 (search snippet only) uses 2x2 sub-blocks that are themselves Hadamard. Neither is the S1 condition.
- The untwisted case [[A,B],[B,A]] is a two-circulant-type structure. Not searched separately beyond the search log below (the W(n, n/2) / sum of two squares step was not searched).

## Search log (all dated 2026-11-24)

Web search (WebSearch):
1. "Holzmann Kharaghani Orrick On the real unbiased Hadamard matrices ... order 36" -> 1209.4315, Kharaghani et al. 2025; HKO itself not listed. OK.
2. "Smith normal form Hadamard matrices Michael Wallis invariant factors 2-rank" -> DCC 13 page (skew only), Greaves-Suda 1801.07516. OK.
3. 'Craigen "Weaving rectangular matrices and the existence of orthogonal designs"' -> no paper of that title; survey 2309.07522, ajc v13 p89, thesis refs. NOT FOUND as titled.
4. 'unbiased Hadamard real order 4u^2 "Steiner system" OR "unbiased Bush-type"' -> Best-Kharaghani, Bush-type papers, 1601.04416, 1710.07888. OK.
5. "unbiased real Hadamard matrices order 100 OR 196 OR 324 pair existence" -> no order-100 statement. OK.
6. 'Assmus Key "Hadamard matrices and their designs" 2-rank' -> AMS landing page, Norwood-Xiang; no statement. OK (abstract level).
7. "Hadamard matrix blocks rank one 2-rank lower bound ... Kronecker" -> 1412.2945, 1801.01149, 1412.2945; "rank-one blocks" only in a 3x3 matrix multiplication paper. OK.
8. "Hadamard matrices from Steiner systems S(2,k,v) conference matrix tensor construction" -> Kronecker/Paley/Mathon items only. OK.
9. "Kharaghani Suda linked systems ... Steiner conference" -> 1609.05255, 1710.07888, Kodalen 1712.02911. OK.
10. "Ionin Kharaghani BGW Steiner Bush-type" -> EJC 7 (1999), Jungnickel-Kharaghani; nothing on S(2,k,v). OK.
11. "arXiv Hadamard 2-rank lower bound Smith normal form n-4 ... tiling" -> Orrick math/0507515, Greaves 1801.07516, math/0407425. OK.
12. "unbiased Hadamard pair order 100 real open question" (extended) -> found HKO preprint URL at cs.uleth.ca. OK.
13. "Hadamard matrix 2x2 blocks rank one product +1 normal form" -> nothing relevant (1003.4133, Orrick). OK.

OpenAlex (api.openalex.org, no key, no email):
14. search "real unbiased Hadamard matrices Holzmann Kharaghani Orrick" -> returned Best-Kharaghani (W2100535482) but not HKO itself.
15. filter title.search "real unbiased Hadamard" -> HKO found as W4232894208 (2010, 40 cites at that time, DOI 10.1090/conm/531/10471).
16. filter cites:W4232894208 -> 41 works, titles listed in Q3. Titles only.
17. filter cites:W2100535482 (Best-Kharaghani) -> 16 works (subset of 16's overlap).
18. search Craigen weaving title -> no match; 86 hits all unrelated or other titles.
19. search "Signed groups, sequences ..." -> W2030086615 (bronze OA link; fetch failed, see Q4).
20. search "Constructing weighing matrices by the method of weaving" -> W2078034177 closed.
21. search "Hadamard matrices from Steiner systems linear spaces" -> Steiner ETFs (W2072704718), balanced splittable Hadamard; no Steiner-Hadamard construction.
22. search "Hadamard matrix 2-rank block rank one lower bound binary code" -> only rank/kernel of Hadamard codes; none on rank-one blocks.

arXiv: listing/search pages (arxiv.org/search, export.arxiv.org API) returned HTTP 429. INACCESSIBLE: arXiv keyword searches for "Hadamard Steiner system" and "Hadamard rank-one 2-rank".
   arxiv.org/a/kharaghani_h_1(.html): 404. Individual PDFs fetched OK (1209.4315, 1201.0631, 1412.5297, 1504.01236, 1601.04416, 1712.02911, 2309.07522, math/0507515, 1801.07516, 1412.2945, 2109.13052).
aiXiv (aixiv.online):
23. search "Hadamard unbiased" -> listed 22 Hadamard-related papers (MUB dimension six, complex order 6, "Recent progress..." 2610.02075, "Hadamard matrices of orders 668, 716, 892, and others" 2611.02032,
    circulant Hadamard conjecture 2610.00626, Mark 2611.00465...). None about Steiner/weaving/rank-one tilings/2-rank. Page did not show which query produced the list, so treat as weak evidence; titles only.
Semantic Scholar: NOT PERFORMED.
Springer (Michael-Wallis DOI 10.1023/A:1008230429804), AMS (Assmus-Key), ScienceDirect (Craigen JCTA): INACCESSIBLE (HTML bot page, not PDF).
ResearchGate HKO copy: not fetched (HKO read at the uleth.ca preprint).
Google search page: INACCESSIBLE (no results rendered).

GitHub (gh, calls spaced 8 s):
24. code "hadamard unbiased steiner" -> noise only.
25. code "hadamard 2-rank rank-one blocks" -> noise only (unrelated repos).
26. code "hadamard weaving" -> matrix-toolbox/chm CHM/weave.m ("Weaving Hadamard matrices - a construction by Robert Craigen from 1988", code only); AlonSlonimsky/Uniform_Partitions_Hadamard_Matrices tools/hadamard_tools.sage ("basic weaving of the two matrices"). Neither read.
27. code "hadamard unbiased 4u^2" -> Menon-DS-to-Hadamard note (paulklemstine/Lean); OpenAI circulant Hadamard (order 4u^2); no unbiased pairs.
28. code "hadamard smith invariant 2-rank" -> noise only.
29. repos "hadamard" --sort updated -> new repos (vxvware/goethals-seidel-challenge, ardadogan05/hadamard-search, zblore/butson-hadamard-lean, ...). None on Theorem A/C topics. (Includes one unrelated private repository of the author.)
30. repos "unbiased" (match name,description), "weaving", "unbiased-hadamard", "weaving-hadamard" -> no relevant repo, except Diego-Ponterio/Hadamard-matrices (unrelated quantum MUB) and PriyaSound/Unbiased-Matrices (2014; "creates unbiased Hadamard matrices", not read). Note the PRIOR-ART caution: multi-word repo queries can return empty silently.
31. code "hadamard mutually unbiased Steiner system", 'Hadamard "rank-one" "2-rank" Smith', "hadamard skew conference Steiner" -> noise only.

## Summary of verdicts
- A0: KNOWN as code statement (Orrick Thm 4.3, citing Lander 1983); A0 constants N-4, N/2-3 follow by a 2-step de-normalisation (inference). Smith facts: Newman 1971, Wallis 1971 (not read).
- Theorem A: NOT FOUND (ingredients known).
- Theorem C: unbiased-pair framework KNOWN (HKO 2010 read at source; Best-Kharaghani; Kodalen); the order-a(ak+1) Steiner construction NOT FOUND; no real unbiased pair for odd u >= 5 found, none excluded.
- Craigen: weaving theorem known at survey level (rank-one blocks by construction, non-defective inputs); title in the brief not found.
- S1 normal form: NOT FOUND.
