# Four-group rigidity and enumeration, initial examination

STAGE: INITIAL  
VERDICT: NOT-BROKEN

I examined the stated conditional claim for a fixed four-group geometry and a fixed ordinary Hadamard of order $h$. The central simultaneous negation supplies the unavoidable signed side-preserving symmetry. Two independent local labellings on opposite sides at each point are important.

* In the kernel of the point action, fixing the column-point names fixes each projective port at each row point, because its four column-point neighbors identify it. The same holds on the other side. On the external entries for one physical line, the bipartite graph on its four flags on each side is $K_{4,4}$ minus a matching, hence connected. All eight local port multipliers on that line coincide. At each point the common multiplier word must therefore belong to **both** independently permuted local sign groups.
* A basis $B$ has at most $2h$ diagonal sign words $s$ for which $B \mathrm{diag}(s)B^T/h$ is a signed permutation. Its first row identifies the word from the signed target row of $B$. Each diagonal entry of this signed permutation equals the mean of the word, so a nonconstant word is balanced. The chance of a common nonconstant word at any point is at most $4h(2h)^2/\binom{h}{h/2}$. If each word is constant, external joins force one global sign.
* For a proposed nonidentity pair of point permutations the port bijections, when they exist, are forced by the neighboring point sets. An independent source-target pair of bases must then implement a prescribed port permutation up to projective basis symmetry. A basis has at most $\exp(O(\log^2 h))$ such symmetries, by choosing $O(\log h)$ row coordinates distinguishing all signed columns and specifying their signed row images. Disjoint moved pairs in the point cycles provide at least a third of the total moved points. This appears sufficient against all pairs of point permutations, stratified by support. The argument uses only universal estimates in $h$.
* Each point sees the same projective basis set in every sample. Equivalences between samples with recovered partitions must therefore act locally through those small basis symmetry groups, up to point permutations. A single labelled output appears to have at most exponentially many parameter preimages in $N$, since each port direction is read directly from its tiles and only signs remain. Both losses and transposition are negligible on the $N\log N$ scale. The fixed-line sign witness in the construction applies to every sampling outcome.

DEPENDENCIES: Intrinsic recovery of both point partitions is assumed. A uniform probability conclusion over geometries needs uniform recovery, or a hypothesis valid along every sequence of admissible inputs. If the requested count includes transposition, the factor of at most two does not establish rigidity against side exchange.

EXPOSURE: Root's isolated claim packet and the four-group section of `CONSTRUCTIONS.md` at file SHA-256 `87e117feb1ff4b201faf58654eabbefce4005f6cfaaa9c9124691019e600e68d`. No proposed rigidity proof or other review was consulted.

RESOURCES: Five minutes wall allocated, zero experimental CPU seconds used. Only analytic counting and file operations were used.
