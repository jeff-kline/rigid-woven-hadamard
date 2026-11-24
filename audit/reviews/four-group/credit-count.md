# Counts and symmetry under signed matrix equivalence

## Scope and verdict

The defensible claim is the joint theorem for the stated random labellings of **one fixed geometry and one fixed basis**, including intrinsic recovery, asymptotically typical minimal side-preserving signed automorphism group, and the sharp class exponent for those inputs. Searches of the sources below found no theorem supplying this conjunction or its finite rigid-regular bound at 1600. There are prior rigid regular matrices, prior factorial counts of Hadamard classes, and larger bounds at 1600 when a hypothesis is dropped. Priority for the conjunction remains open.

## Which equivalence is counted

Normalize one chosen row and column to all plus and delete them. For a matrix of size M the resulting ordinary Hadamard design has parameters (M−1,M/2−1,M/4−1). Each signed equivalence class has at most M² descendant isomorphism classes, since the chosen row and column determine the normalization up to permutations. Thus D nonisomorphic such designs give at least D/M² signed matrix classes and D/(2M²) classes allowing transpose. The design automorphism group is the stabilizer of the chosen pair in the effective side-preserving matrix group. It can be trivial when the matrix group moves the pair.

For Menon designs of size M the normalization argument changes. A regular signing of H with positive sums √M is determined by its right sign vector b with |Hb|=√M coordinatewise. Its left sign vector is Hb/√M. Vectors b and −b give identical regular matrices. Permutations only relabel the incidence design, so one signed matrix class covers at most 2^(M−1) such Menon isomorphism classes for the fixed choice of block size. Divide by a further two if transpose is allowed. Design rigidity again constrains only the stabilizer. Conversely rigid matrices give rigid Menon designs. Transpose identification halves a lower bound but side-preserving rigidity leaves possible dualities open.

## Primary-source comparisons

* Kantor's 1994 Theorem 1.1 prescribes the automorphism group of classical-parameter projective and affine designs for q>3 and large dimension. Section 6 studies typical automorphism groups under random gluing, and §9 discusses recovery from good blocks and the small-field cases. These are incidence automorphisms. Norman's 1973 paper already treats asymmetric ordinary Hadamard designs. [Kantor, original paper](https://darkwing.uoregon.edu/~kantor/PAPERS/AutoIsos.pdf) · [Norman](https://doi.org/10.1007/BF00147858) · [Merchant §1](https://emis.de/ft/43704)
* Lam, Lam and Tonchev (2000) explicitly counted inequivalent matrices, including at least 3.66×10¹¹ of order 40. Their follow-up on even design orders, Theorem 3.10, gives at least (4n−1)!/[f²(4n−1)²(2n−1)²] ordinary Hadamard designs on 8n−1 points for odd n with 4n−1=p^f>11. Theorem 3.11 gives (8n−1)!/[(8n−1)²(4n−1)²] on 16n−1 points for prime 8n−1>7. Either gives signed matrix classes of log size at least (M/2)log M−O(M) along its range after the preceding conversion. The proofs count extensions over a recognizable design substructure. [2000 author repository](https://digitalcommons.mtu.edu/math-fp/140/) · [even orders, §§2–3](https://www.academia.edu/20829682/Bounds_on_the_number_of_Hadamard_designs_of_even_order)
* Merchant (2006), Theorem 5.2, starts with an ordinary Hadamard design of order n>2 and produces at least (16n−2)!/(2¹⁰n³) nonisomorphic rigid ordinary designs of order 8n, equivalent to a matrix size M=32n. They have a good block and arise by doubling. The doubled matrix with row blocks (A,A) and (B,−B) admits the involution exchanging its column halves and negating the bottom rows, even when B has a relative permutation. Thus this is a particularly sharp example of the difference between the stabilizers. At n=50 the input exists by the Paley matrix of order 200 (q=199). After division by 2·1600², the log base ten of the bound is 1956.2649675. Theorem 1.1 also prescribes arbitrary finite design automorphism groups. [Merchant, §§3,5,7](https://emis.de/ft/43704)
* Meisner (1992) constructs regular matrices of order a²v from a Hadamard of size a and a regular Hadamard of size v. His Theorem 3 gives s+t−1 inequivalent regular matrices of size 4^t v, given s inputs of size v with distinct characteristic numbers. His equivalence allows independent sign changes. The Bush-type study at orders 64 and 144 also uses rank-one blocks and Latin squares and reports 390 Menon (144,66,30) designs with trivial incidence automorphism groups. [Meisner, Theorem 3](https://www.bdim.eu/item?fmt=pdf&id=RLIN_1992_9_3_4_233_0) · [Bush-type study](https://www.sciencedirect.com/science/article/abs/pii/S0378375801003184)
* Spence's order-36 catalogue gives actual **rigid regular** precedents. Its first five classes each have effective matrix group order 1 and 1296 different descendants. A regular representative exists for each catalogue class. Indeed every one of the 227 underlying two-graph switching classes has a strongly regular graph with parameters (36,15,6,6), and its adjacency matrix A gives the regular Hadamard J−2A, whose row sums equal 6. Switching amounts to conjugating by a sign diagonal. Kimura had also obtained trivial effective matrix groups at nonsquare order 28 and employed invariants from four rows. [Spence catalogue description](https://www.maths.gla.ac.uk/~es/hadamard/hadamard.php) · [Spence group orders and descendants](https://www.maths.gla.ac.uk/~es/hadamard/hadamard.36) · [McKay's switching-class data](https://users.cecs.anu.edu.au/~bdm/data/graphs.html) · [Kimura, §§1–2](https://www.math.sci.hokudai.ac.jp/hmj/page/17-1/pdf/HMJ_17_1_1988_139-146.pdf)
* Orrick's switching paper gives millions of signed matrix classes of orders 32 and 36. Its doubling family and the permutation-based doubling literature are relevant precedents for counting from a fixed seed. Counting labelled matrices merely from permutation freedom addresses a different quantity. [Orrick](https://arxiv.org/abs/math/0507515) · [Permutation-based doubling](https://combinatorialpress.com/jcmcc-articles/volume-063/inequivalent-hadamard-matrices-of-order-2n-constructed-from-hadamard-matrices-of-order-n/)

## Separate elementary comparison for regular matrices

The following is a deduction for this audit, without historical priority or attribution of the bound to a published theorem. Let F(m) count regularizable Hadamard classes up to signed side-preserving equivalence. For four ordered representatives B_j of such classes with positive regular sums, four permutations π_j, and S=J₄−2I₄, put

    H[(i,x),(j,y)] = S[i,j] B_j[π_j(x),y].

For x≠x′ each block contributes zero to the row inner product. For x=x′ use the orthogonality of S. Every row and column sums to 2√m.

Mark the four ordered column blocks. Inside any block its projective row directions identify the m quadruples indexed by x. The four sets of projective rows recover the ordered input classes up to signed equivalence. Once a common ordering of quadruples is chosen (at most m! options), each block permits at most a_m=(2m)^(ceil(2 log₂m)+2) bijections to the rows of the chosen representative. Indeed a signed column operator inducing such a bijection preserves the projective row set relative to a fixed first solution. Some r=ceil(2 log₂m)+2 coordinates distinguish the m projective rows, because for a distinct pair the failure probability at r uniform coordinates is 2^(1−r). The images and signs of these coordinates determine the operator. Thus each marked class can account for at most m! a_m⁴ parameter choices, and one unmarked class has at most 4^(4m) ordered markings. It follows that

    F(4m) ≥ F(m)^4 (m!)³ / [4^(4m) a_m⁴].

At m=400 a regular input exists by Meisner with a=20,v=1. Even with just that input and allowing transpose, the right side divided by 2 has log base ten 1410.5750275. All outputs have a nonscalar signed symmetry. For example interchange the first two and last two sheets via (12)(34), multiply rows of sheets 3,4 by −1 and columns in blocks 1,2 by −1. This fixes H. This construction therefore cannot refute the 1600 rigid-regular statement.

For fixed m₀ with regular input, iteration at m=m₀4^t gives log F(m)=Ω(m(log m)²): divide the logarithmic recurrence by 4m and sum the increments (3/4)log m−O(1). Even among regular matrices the global class growth can exceed the fixed-input exponent on a subsequence. This argument proves a comparison for all regular classes only.

## Coverage

| ID | Comparison | Outcome |
|---|---|---|
| C1 | Rigid regular matrices as an existence claim | Prior order-36 examples verified |
| C2 | Ordinary design counts under signed/transpose equivalence | Polynomial loss verified |
| C3 | Menon incidence rigidity implies signed rigidity | Fails as an inference |
| C4 | A global count record at 1600 without rigidity | Ruled out by the regular block count |
| C5 | A global sharp exponent N log N for regular classes | Ruled out on a subsequence |
| C6 | Combined fixed-input theorem and the finite rigid-regular bound | No matching prior theorem located in bounded search |

Coverage 6/6 comparisons. The search does not establish historical priority or independently reprove the target theorem. The original 2000 Lam–Lam–Tonchev paper was checked against the author-repository abstract and the explicit comparison in their full follow-up. Norman's publisher supplied bibliographic metadata only. No sign search was performed.

**Verdict: QUALIFY.**
