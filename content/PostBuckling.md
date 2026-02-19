# Post-buckling methods

While historically buckling was seen as failure, modern engineering recognizes the postbuckling reserve of stiffened panels. These panels can withstand loads significantly exceeding their initial buckling threshold by allowing local buckling of the skin while stiffeners maintain global integrity.

## Effective width

The postbuckling behavior and stress/strain distribution
of stiﬀened panels is complex and non-linear. Complicated
non-linear numerical calculation methods that employ sig-
nificant computational resources are laborious and are
required to confidently predict the panels ultimate load
capacity [@Pevzner2008]. To alleviate the calculations, a relatively simplified
model, the so called "eﬀective width" approach, has been proposed
by von K\'arman et al. [@vonKarman1932] and subsequently modified by
Cox [@cox1933] and Sechler [@Sechler1937]. This
approach has provided a good average approximation for
calculation of the eﬀective width, $w_e$, i.e. the portion of
the between adjacent stringers buckled skin, that together
with the stringer constitute the integral skin-stringer combi-
nation that participates in load carrying in postbuckling.
The method works adequately for the case of uniaxial compression, and it is not recommended when there is biaxial loading or compression combined with shear [@Kassapoglou2013].
Based on the average stress $s_{st}$ experienced by the stringers
and the first critical skin stress, $s_{cr}$ between adjacent
stringers of spacing b, the following relation has been pro-
posed by Marguerre for determination of $w_e$:

$$\frac{w_e}{b} = \frac{1}{2}\sqrt[3]{\frac{s_{cr}}{s_{st}}}$$

The above eﬀective width concept is widely and eﬀectively applied as an adequate reliable tool for prediction
of ultimate loads of metal flat stiﬀened panels. When
appropriately modified and adapted it might lend itself as
an appropriate approach for determination of ultimate
load capacities of axially compressed laminated composite
stringer-stiﬀened curved panels as well [@Pevzner2008].

The effective width method simplifies the complex and 
non-uniform stress distribution in a buckled panel, replacing it with an
equivalent and uniform stress acting over a reduced "effective width" of the skin adjacent to the stiffeners. 


### Effective width for metallic structures


### Effective width for composite plates

+++{"no-pdf":true}
An example on how the effective width changes with the loading fraction and material properties can be found here: [](effective-width-composites-Kassapoglou-7.10.ipynb); based on Kassapoglou [@Kassapoglou2013]. An illustration on how the internal load changes over the skin width can be found here: [](effective-width-composites-Kassapoglou-7.12.ipynb); also based on Kassapoglou [@Kassapoglou2013].
+++

### Effective width for composite shells

The Technion Effective Width (TEW) method [@Pevzner2008] is an engineering
approximation for analyzing the postbuckling behavior of curved, laminated
composite structures. The TEW method extends the effective width concept to curved, anisotropic, laminated composite panels by reformulating an equivalent column model to account for the unique bending, torsional, and coupled instability modes of composite structures.

The TEW analysis process is summarized as follows:
1.  **First Buckling Calculation:** Determining the initial local buckling of the skin between stringers using semi-empirical or approximate analytical solutions.
2.  **Iterative Convergence of Effective Width:** Once the load exceeds the initial buckling load, an iterative algorithm calculates the effective width of the skin contributing to the load-carrying capacity. This process continues until the stress redistribution between the buckled skin and the stiffener reaches equilibrium.
3.  **Global Stability Analysis:** Evaluating the global column stability based on the flexural, torsional, and warping rigidities of the equivalent skin-stringer cross-section to determine the ultimate collapse load.


+++{"no-pdf":true}
An example of the TEW method is presented in the following notebook: [](effective-width-composites-TEW.ipynb).
+++

The TEW paper reveals that the predictive fidelity of the TEW method is closely linked to the panel's stiffness.

| Configuration & Geometry             | P_buckling (kN) (Experiment) | P_collapse (kN) (Experiment) | P_collapse (kN) (F.E. Method) | P_collapse (kN) (Proposed TEW Method) |
| :----------------------------------- | :--------------------------: | :--------------------------: | :---------------------------: | :-----------------------------------: |
| **Case I:** 5 T-type, 20 mm web      |      137.3, 147.2, 158.5     |      208.7, 222.7, 224.8     |             204.0             |                 240.5                 |
| **Case II:** 5 T-type, 15 mm web     |      133.4, 110.9, 123.6     |      158.9, 153.3, 147.2     |             135.0             |                 127.4                 |
| **Case III:** 6 T-type, 20 mm web    |      224.2, 237.3, 234.5     |      274.7, 264.9, 274.7     |             290.0             |                 281.7                 |
| **Case IV:** 5 J-form thin stringers |          83.4, 70.6          |         230.5, 226.1         |             215.0             |                 202.6                 |
| **Case V:** 4 J-form thick stringers |          59.8, 90.8          |         289.8, 293.0         |             330.0             |                 354.9                 |

-   **Heavily Stiffened Panels (Cases I, V):** The TEW method tends to overpredict the collapse load. This is likely because the model does not capture localized failure modes like skin-stiffener debonding that can occur before global buckling.
-   **Lightly Stiffened Panels (Cases II, IV):** The TEW method tends to conservatively underpredict the collapse load. The small margin between initial skin buckling and global collapse in these flexible structures may lead the algorithm to predict failure prematurely.
-   **Asymmetric Stiffeners (Cases IV, V):** The use of J-form stringers introduces coupled bending-torsion modes, which significantly complicates the buckling behavior and increases sensitivity to manufacturing imperfections.

