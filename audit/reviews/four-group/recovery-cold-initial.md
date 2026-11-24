# Initial cold examination of point-fibre recovery

**Stage** INITIAL. **Verdict** NOT-BROKEN. The probability claim remains unverified at this stage.

I tested whether a high-symmetry local input makes the partitions ambiguous. For a Sylvester input, every four-column product of a local basis has sum zero or ±h. Consequently every four-row correlation in the assembled matrix is divisible by h, including correlations of rows from four unrelated points. Divisibility by h alone cannot recognize the true fibres uniformly. Independent local column permutations preserve this obstruction. This supplies no alternative global fibre partition and does not refute recovery.

For two distinct rows at one physical point, their entrywise product is constant on every physical column fibre. For rows at distinct points of the same group, the two column ports at any target point are distinct, so the product on that target fibre is balanced. For two points in different groups, some targets can give the same port. Thus a proof based on local balance must allow such coincidences. A recovery test also needs to identify both partitions when supplied only the matrix up to signs and permutations. The literal labels of the recovered parts have no intrinsic meaning.

The hypotheses are nonvacuous along the unbounded dyadic field family with Sylvester bases. I saw no construction of inequivalent competing partitions inside the same realization. Unresolved issues include a uniform probability bound over all Hadamard inputs and the effect of port dependence within permutations.

**Exposure and resources.** Parent's statement packet, local cold-examiner instructions, and `CONSTRUCTIONS.md` (SHA-256 `87e117feb1ff4b201faf58654eabbefce4005f6cfaaa9c9124691019e600e68d`). No recovery proof, other review, external source, or experimental run. Work used symbolic reasoning within the approximately five-minute wall allocation and zero experimental CPU seconds.
