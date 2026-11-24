# More than \(10^{662}\) rigid regular Hadamard classes at order 1600

23 November 2026. Fix any admissible four-group geometry and any real local Hadamard matrix \(A\) of order \(h\). Use \(A^T\) on the row side and \(A\) on the column side, with the independently and uniformly signed and permuted ports of the [general theorem](REGULAR-RIGIDITY.md). If \(h\equiv4\pmod8\) and \(h\ge20\), more than 70% of these labellings have recoverable point fibres on both sides and signed side-preserving automorphism group exactly \(\{(I,I),(-I,-I)\}\). Every output has a regular representative. The [product geometry over the fields of orders four and five](CONSTRUCTIONS.md) and an ordinary Hadamard matrix of order 20 therefore yield the class count in the title, even identifying transposes. The count ranges over labellings of these fixed inputs.

## Every four-column correlation supplies a test

Take four distinct columns and multiply rows by the first column to normalize that column to all pluses. Call the other three columns \(u,v,w\), and let \(D=\sum_i u_iv_iw_i\). Each of the eight patterns \((a,b,c)\in\{\pm1\}^3\) occurs \((h+abcD)/8\) times by expanding its indicator and using orthogonality. Thus \(D\equiv h\equiv4\pmod8\). If \(|D|=h\), flip \(w\) if necessary so that \(w=uv\). The four cells specified by \((u,v)\) each have size \(h/4\). Orthogonality of a fifth column to \(1,u,v,uv\) forces its sum in each of those four cells to vanish, impossible because \(h/4\) is odd. This applies equally to rows. Hence

\[
     0<|D|<h,\qquad h\nmid 2D.
\]

Indeed the only possible intermediate magnitude with \(h\mid2D\) is \(h/2\equiv2\pmod4\). At \(h=20\) the correlations are \(\pm4,\pm12\). Whenever two ports \(a,b\) are fixed, every edge on the \(h-2\) remaining ports \(c,d\) therefore has nonzero correlation and distinguishes the two signs of \(D_{abcd}\) modulo \(h\).

## Recovering fibres with occasional false edges

Relate distinct physical rows if every extension by two other distinct rows has four-row sum divisible by \(h\). Within one point fibre each row pair passes. Its product is constant on each column fibre, where the other pair has sum \(0\) or \(\pm h\). For a pair from different fibres choose a column point seeing different ports \(a,b\). Such a point exists in a group external to their points. In a row group different from both original row groups, the \(h\) row points use all \(h\) ports at this column point. For each port \(c\notin\{a,b\}\) choose one row from its corresponding row point. Expose everything except the \(h-2\) column-port signs \(e_c\) there. Extending the false pair by the rows at \(c,d\) gives sum \(K_{cd}+s_{cd}D_{abcd}e_ce_d\), with \(K_{cd}\) and the sign \(s_{cd}\) exposed. Divisibility prescribes at most one value of \(e_ce_d\). Take a spanning tree of the complete graph on the \(h-2\) ports. Its \(h-3\) edge products are independent fair signs, so a fixed false pair passes with probability at most \(2^{-(h-3)}\).

The actual point fibres partition the graph into cliques of size \(h\). Any other such partition must contain at least two cliques meeting more than one actual fibre, since agreement on all but one block forces agreement on the last. Each mixed clique uses at least \(h-1\) cross-fibre edges, attained when its parts in the actual fibres have sizes \(1,h-1\). Two cliques of the partition use disjoint edges. Fewer than \(2(h-1)\) false edges therefore suffice for the actual fibre partition to be unique. Markov's inequality bounds the failure probability by

\[
    f_h=\frac{\binom{4h}{2}h^2}{2(h-1)2^{h-3}}
       \le\frac{4h^4}{(h-1)2^{h-3}}.
\]

At \(h=20\), \(f_{20}=1{,}264{,}000/(38\cdot2^{17})<0.254\). The upper bound on the right is less than \(0.258\) at 20 and decreases thereafter, since each step has ratio less than \((1+1/h)^4/2<1\). The recovered row partition determines the column partition. Two columns belong to the same column point exactly when their product is constant on every row fibre, by the separating-port property and orthogonality. Both tests are invariant under signed row and column permutations.

## The point action and its kernel

For either local basis, bound the number of permutations of the \(h\) projective columns induced by signed row permutations by

\[
     a_h=4(h)_3((h/4)!)^4,\qquad (h)_3=h(h-1)(h-2).
\]

Record columns on three fixed distinct output row coordinates, taking ratios against the first one to eliminate the column sign. The four resulting sign patterns have multiplicities \(h/4\). An inducing signed row operator has at most \((h)_3\) ordered choices of input coordinates and four choices of their relative signs. For each choice the projective column permutation must respect the four matched cells, giving at most \(((h/4)!)^4\) possibilities. This bounds the induced permutations themselves. The scalar pair \(U,-U\) induces the same permutation.

As in the [point-action argument](REGULAR-RIGIDITY.md), a proposed pair of point permutations prescribes its port maps, whenever these exist. For a proposed cycle of length \(j\ge2\) on either side, expose the first port labelling, then the next \(j-1\) in cyclic order. Each successor permits at most \(a_h\) of its \(h!\) independent permutations. Thus support \(s\) on that side costs at most \((a_h/h!)^{s/2}\), since \(j-1\ge j/2\). There are at most \((4h)^s\) point permutations with support \(s\), and none with support one. Both sides have independent labellings. With \(r_h=4h\sqrt{a_h/h!}\), summing over all nonidentity pairs gives the unconditional bound

\[
     g_h\le\left(1+\frac{r_h^2}{1-r_h}\right)^2-1.
\]

Here \(a_{20}=5{,}673{,}369{,}600{,}000\) and \(r_{20}<1/8\). For \(h\ge20\) the square of the ratio \(r_{h+4}/r_h\) equals

\[
  (1+4/h)^2\frac{(h+4)^4}{256(h+1)h(h-1)(h-2)}
  \le (6/5)^2(4/3)^4/256<1.
\]

Consequently \(g_h<(1+1/56)^2-1<0.037\).

If all points are fixed, every local port ray is fixed. For a local basis \(B\), a candidate signed row permutation \(U\) then obeys \(UB=B\operatorname{diag}(e)\). A nonconstant sign word \(e\) would act without a fixed point on the projective rows of \(B\), since every entry of every row is nonzero. The action is an involution, so two disjoint row pairs have the same entrywise product up to sign, yielding a four-row correlation of magnitude \(h\). The first section excludes this. Hence each local operator is scalar, and the nonzero tiles at every ordered point pair force the same scalar on both sides everywhere. The preceding failure probabilities give \(1-f_h-g_h>0.70\), uniformly for the stated orders. Diagonal regularization conjugates the signed automorphism group.

## Finite class count

The number of signed labellings is \((2^h h!)^{8h}\). For any fixed good output, an equivalent good labelled output permits at most \(((4h)!)^2\) choices for its point action. The port maps then have at most \(a_h\) choices of target port permutation per point occurrence relative to the source, and at most \(2^h\) choices of local signs. Thus the factor \(2^{8h^2}\) cancels between total labellings and the upper bound per class. Identifying transposes costs at most another factor two. At \(h=20\), using only that the good proportion exceeds \(1/2\), the number of classes exceeds

\[
      \frac{(20!)^{160}}{4(80!)^2(5{,}673{,}369{,}600{,}000)^{160}}.
\]

The floor of this rational number has 663 decimal digits and 2202 binary digits by integer arithmetic. In particular, there are more than \(10^{662}\) such classes of order 1600.
