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

An example of the TEW method is presented in the following notebook: {doc}`effective-width-composites-TEW`.

+++{"no-pdf":true}
An example of the TEW method is presented in the following notebook: {doc}`effective-width-composites-TEW`.

```An example of the TEW method is presented in the following notebook:

{doc} effective-width-composites-TEW
```
+++

