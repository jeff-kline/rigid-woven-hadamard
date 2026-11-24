# Fibre recovery and rigidity for the four-group regular construction

23 November 2026. All asymptotic statements are uniform over the supplied geometry and the chosen local Hadamard matrix.

## Statement

Fix one of the [four-group transversal designs with a common line involution](CONSTRUCTIONS.md) and one real Hadamard \(A\) of order \(h\). On each of the \(4h\) row points take local basis \(A^T\); on each of the \(4h\) column points take \(A\). Independently at each of these \(8h\) point occurrences, permute the basis columns uniformly among its \(h\) flags and give each column an independent fair sign. These signed bases are valid ordinary local Hadamards. Every output has the explicit regular representative from the original construction, with order \(N=4h^2\) and all sums \(2h\).

As \(h\) grows, a proportion \(1-o(1)\) have intrinsically recoverable row and column point fibres and signed side-preserving automorphism group exactly \(\{(I,I),(-I,-I)\}\). The number \(C_h\) of inequivalent rigid outputs from this one geometry and basis satisfies \(\log C_h=N\log N+O(N)\), even identifying transposes. The leading exponent is sharp for the fixed input. Hence every sufficiently large order of the four-group construction carries both conclusions, preserving its \(X^{1/2+o(1)}\) distinct-order exponent.

## Geometry

Each tile at a row point and column point is the signed outer product of one basis column at each end. A port (an incident flag at a point) faces four opposite points, one in each group. Its four tiles are characterized by their common projective column direction at this point. For two distinct opposite points, take a probe group different from both groups. At least \(h-1\) of its \(h\) points see different ports towards them: in external groups the joins use physical lines, two points of different groups have a unique common line, and two distinct points in one group have none. These facts apply on both axes.

Knowing either fibre partition determines the other. Two rows from one point have product constant on every column fibre. Two rows from distinct points see distinct ports at some column point; their restricted product is nonconstant by orthogonality. The same test works on columns. Agreement of product values here is invariant under arbitrary signed equivalence.

## Recovery, uniformly in the local basis

Write \(D\) for the sum of the entrywise product of four vectors. Its absolute value on a row quartet is invariant under signed equivalence. Use the following dichotomy on the columns of \(A\).

**A. Some four distinct columns have \(|D|\ge h/2\).** Their four corresponding local rows in \(A^T\) at each row point form a global quartet with absolute sum at least \(N/2\): every local column contributes its four-row product at \(4h\) coordinates. With probability tending to one, all quartets with this large a sum lie in one fibre. For a mixed quartet of odd multiplicity at some point, expose everything except its independent row-side port signs. Its global correlation has the form \(\sum_{\ell=1}^h e_\ell c_\ell\), with fair independent signs and \(|c_\ell|\le4h\). The sign-sum exponential bound gives probability at most \(2e^{-h/8}\) of reaching \(2h^2\) in magnitude. The other possible mixed pattern is \(2+2\). At the first point the product of its two rows is a uniformly permuted balanced word on the ports, independent of the other point. Again the coefficients have magnitude at most \(4h\). Conditioning fair signs to be balanced costs at most \(h+1\). The resulting failure probability over all mixed quartets is at most \(2N^4(h+1)e^{-h/8}=o(1)\).

Collect the pairs of rows belonging to threshold quartets. Give every physical column the list of those pair products at that coordinate. True column-fibre mates have identical lists if there are no mixed threshold quartets. For two distinct column points, at each of the \(h-1\) or more separating probe points use two specified rows of the predetermined local high quartet. Their uniformly balanced port word has equal values at the two distinct ports with probability \((h-2)/(2(h-1))<1/2\), independently across probe points. The unconditional chance of any missed separation is at most \(\binom{4h}{2}2^{-(h-1)}\). Add the two failure bounds. The lists recover the column fibres and then the row fibres follow by the geometry test above. Row signs change a whole list component simultaneously at every column; column signs cancel.

**B. All distinct local column quartets have \(|D|<h/2\).** Relate two rows if every extension by two other distinct rows has fourth sum divisible by \(h\). A true pair passes: its product is constant on each column fibre, and the sum there of the other two rows' product is \(0\) or \(\pm h\).

For a fixed false pair choose a separating column point \(y\) and denote its two distinct local port labels by \(a,b\). For each other port \(c\), choose one physical row \(w_c\) from its incident point in a row group different from those of the original rows. These points are distinct because the tile joins at \(y\) give a bijection from this group to its ports. Use choices independent of all port signs. On these \(h-2\) ports put an edge \(cd\) if \(D_{abcd}=\sum_i A_{ia}A_{ib}A_{ic}A_{id}\ne0\). The graph has no isolated vertex: the sign vector \(A_aA_bA_c\) is orthogonal to the three indicated columns and has a nonzero coefficient on another basis column. On any edge \(0<|2D_{abcd}|<h\).

Expose everything except the \(h-2\) auxiliary port signs \(e_c\) at \(y\). The fourth sum for the fixed pair extended by \(w_c,w_d\) is \(K_{cd}+s_{cd}D_{abcd}e_ce_d\) with the integer \(K_{cd}\) and sign \(s_{cd}\) already exposed. This uses that signs at \(y\) occur nowhere outside its fibre. Divisibility by \(h\) allows at most one value of \(e_ce_d\) on each edge. A spanning forest has at least \((h-2)/2\) edges, whose products of independent vertex signs are independent. A false pair therefore passes with probability at most \(2^{-(h-2)/2}\). A union bound over \(\binom N2\) pairs recovers the row partition with probability tending to one, and hence the column partition as well. No independence between the false-pair tests is used.

The decoder can even choose its branch from the output alone. If there is a threshold quartet, use its branch-A list procedure with all threshold quartets. Otherwise use the modular test. In case B no true quartet reaches the threshold, and the same bound for mixed quartets makes an erroneous selection have probability \(o(1)\). These tests use ordinary signed equivalence of unmarked matrices; regularizing by diagonal signs preserves recovery. For equivalences allowing transpose it is enough to halve the class bound.

## Rigidity and class counting

The two recovered point partitions reveal every port as a class of four tiles with one projective direction. Thus a proposed pair of point permutations determines its port bijections, if it preserves these classes.

For either local basis \(B\), there are at most \(a=(2h)^r,\ r=\lceil2\log_2 h\rceil+2\), signed row permutations preserving its set of projective columns. Indeed, some \(r\) row coordinates distinguish those columns up to sign: a pair agrees up to sign on a random list with replacement with probability \(2^{1-r}\), and a union bound suffices. Specifying the preimages and signs of these coordinates specifies each transformed column including its sign, then the operator.

For a pair of point permutations moving \(s\) points across the two sides, expose the port labellings in order along each moved cycle. After the first, each successor permits at most \(a\) out of \(h!\) permutations if it is projectively equivalent under the forced port map. Ignoring the last link of each cycle gives at least \(s/2\) such restrictions. Both sides' labellings are independent. Sum over at most \((8h)^s\) assignments of support \(s\). The geometric ratio \(8h\sqrt{a/h!}\) tends to zero. The chance that any lift moves points is \(o(1)\), allowing separately for the probability of failed recovery.

If all points are fixed, all ports are projectively fixed. At each flag the corresponding signed operator has an eigenvalue sign; the two endpoint signs agree on each nonzero flag join. The row and column flags \((i,L)\) have the same sign: follow the three external joins on line \(L\), from row group \(i\) to column \(j\) to row \(k\) to column \(i\), with \(i,j,k\) distinct. Row and column eigenvalue words at the same physical point thus agree flag by flag.

For \(UB=B\,\mathrm{diag}(e)\) with \(U\) a signed permutation, considering one physical row shows that \(e\) is a signed product of that row with one row of \(B\). There are at most \(2h\) candidate words, and every nonconstant candidate is balanced. Local column signs leave the words unchanged. Independent port permutations of the two bases at the point make the chance of any shared nonconstant word at most \((2h)^2/\binom h{h/2}\). Sum over \(4h\) points. The remaining scalar signs must be identical globally, since each ordered point pair has a nonzero tile. This gives the two compulsory automorphisms, also after regularization.

There are \(L=(2^h h!)^{8h}\) equally likely signed labellings. Fix one good output. For a second good labelling yielding an equivalent matrix, the point action admits at most \(((4h)!)^2\) choices and determines the port maps. At each of \(8h\) points there are at most \(a\) resulting choices of target column permutation relative to the fixed source, and at most \(2^h\) choices of port signs. Thus

\[
\frac{(1-o(1))(h!)^{8h}}{2((4h)!)^2 a^{8h}}\le C_h\le (2^h h!)^{8h}.
\]

Now \(8h\log(h!)=N\log N+O(N)\) and \(\log(((4h)!)^2)+8h\log a=o(N)\). This proves the count. Minimal symmetry alone would not prove it; fibre recovery controls multiplicity. This argument supplies existence and many classes without specifying a particular rigid labelling, and asserts no historical priority.

## Effective range

For every supplied \(h\ge512\), more than three quarters of the labellings satisfy the conclusion. To see this, bound the probability of any mixed threshold quartet by \(2(4h^2)^4(h+1)e^{-h/8}\). At 512 this is below 0.20 and its logarithmic derivative is negative thereafter. Each of the false-pair bound \(8h^4\,2^{-(h-2)/2}\), missed-separation bound \(8h^2\,2^{-(h-1)}\), and kernel bound \(16h^3(h+1)2^{-h}\) is below 0.01 at 512 and decreases thereafter. Finally \(r\le h/16\), \(\log(2h)\le2\log(h/2)\), and \(h!\ge(h/2)^{h/2}\) imply \(8h\sqrt{a/h!}\le8h(h/2)^{-3h/16}<1/16\). A point permutation moves at least two points. Its geometric tail is at most \(1/240\). The sum is below \(1/4\).

For \(h=20\), a separate finite argument proves more than \(10^{662}\) equivalence classes of rigid regular matrices of order 1,600 from the one field-product geometry and local Paley basis. The bound concerns the ensemble; the existing explicit regular representative has not been certified rigid here. See [finite proof](FINITE-1600.md), [recovery audit](recovery-cold-audit.md), and [automorphism and counting audit](count-cold-audit.md).
