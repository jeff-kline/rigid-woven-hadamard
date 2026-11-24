# Isolated assessment of the line involution

STAGE: INITIAL  
VERDICT: NOT-BROKEN for the conditional construction and its stated supply. The order-image comparison is unresolved from the statement packet.

The packet specifies a TD(4,h), an involution on its lines, and a bijection from lines to ordered sheet pairs in each group. These hypotheses pass a fixed-point check. For any sheet a in any group, the unique line mapping to (a,a) must be fixed, since its partner maps to the same pair. Thus the involution fixes exactly h lines, and these meet every sheet once in every group.

An independent derivation uses group-by-line flags. Take a skew conference matrix C of order four, with first row (0,1,1,1) and remaining rows (-1,0,1,-1), (-1,-1,0,1), (-1,1,-1,0). On flags put Q = C tensor I + I tensor P, where P is the line involution. Symmetry and orthogonality of P give QQ^T = 4I. Let R be a block-diagonal matrix on flags, whose blocks are order-h Hadamards on the h flags at each point. Then RQR^T has Gram 4h²I. For endpoints in distinct groups the point pair determines one line and hence one summand; for endpoints in the same group the sheet-pair bijection determines one line and hence one summand. All entries are signs, with no cross-basis condition.

To build h=20·2^m, use fields F_q with q=2^(m+2) and F_5. In both factors the lines are pairs (x,y). In even characteristic use four distinct sheet labels x+ay and the involution (x,y) -> (x+y,y). For any slope the original and transformed forms differ by y, so their pair determines the line. Over F_5 use the four nonzero slopes and the involution (x,y) -> (-x,y). For a fixed slope the determinant of the two forms is 2a, nonzero. Distinct slopes are independent in both factors. Taking coordinatewise products preserves all bijections, and H_20 from the ordinary Paley construction over F_19, tensored with the order-two Sylvester matrix m times, supplies H_h. The characterization of diagonal pairs holds in both factors. There are consequently examples for every stated m. Also H_4 tensor H_h tensor H_h already realizes each ordinary order 4h² from H_h alone. Any new result at these orders must concern the imposed structure or a comparison of specified scheme images.

COVERAGE: fixed points, sign entries, Gram, even and odd factors, product at m=0 and higher, and independent known ordinary orders. Image definitions for the earlier paired and dyadic schemes were absent; no disjointness result was inferred.

DEPENDENCIES: finite fields of prime-power order, the standard Paley H_20, and Sylvester doubling. No published-source comparison was attempted in this stage.

EXPOSURE: coordinator's statement-only message and installed cold-examiner skill. No author proof, other review, or repository research file read. Tools used for directory existence, skill text, UTC clock, report writing, and hashing.

RESOURCES: allocation six wall minutes and under five local CPU seconds. Symbolic argument only, without sign search, data enumeration, or Python. Report sealed on creation; its SHA-256 is recorded by the coordinator.
