# Post-buckling methods

## Effective width

The effective width method, originating in the 1930s, simplifies the complex,
non-uniform stress distribution in a buckled panel. It replaces it with an
equivalent, uniform stress acting over a reduced "effective width" of the skin
adjacent to the stiffeners. The TEW method extends this concept to curved,
anisotropic, laminated composite panels by reformulating an equivalent column
model to account for the unique bending, torsional, and coupled instability
modes of composite structures.

The analytical process involves:
1.  **First Buckling Calculation:** Determining the initial local buckling of the skin between stringers using semi-empirical or approximate analytical solutions.
2.  **Iterative Convergence of Effective Width:** Once the load exceeds the initial buckling load, an iterative algorithm calculates the effective width of the skin contributing to the load-carrying capacity. This process continues until the stress redistribution between the buckled skin and the stiffener reaches equilibrium.
3.  **Global Stability Analysis:** Evaluating the global column stability based on the flexural, torsional, and warping rigidities of the equivalent skin-stringer cross-section to determine the ultimate collapse load.


### Effective width for metallic structures

### Effective width for composite structures

The Technion Effective Width (TEW) method [@Pevzner2008] is an engineering
approximation for analyzing the postbuckling behavior of curved, laminated
composite structures.

+++{"no-pdf":true}
An example of the TEW method is presented in the following notebook: {doc}`effective-width-composites-TEW`.
```{toc}
- file: effective-width-composites-TEW.ipynb
```
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

