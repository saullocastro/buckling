# Post-buckling of plates

While historically buckling was seen as failure, modern engineering recognizes the postbuckling reserve of stiffened panels. These panels can withstand loads significantly exceeding their initial buckling threshold by allowing local buckling of the skin while stiffeners maintain global integrity.

## Differential quadrature


Methodological Comparison: DQM, iDQM, and MiDQM

When solving high-order boundary value problems such as the coupled Föppl–von Kármán (FvK) equations, the choice of spatial discretization dictates the numerical stability of the solver. We can categorize the Differential Quadrature (DQ) family into three distinct approaches.

### Pure direct Differential Quadrature Method (DQM)

**TODO highlight the strong form**

Pure DQM directly approximates the derivatives of a function at a set of grid points using a weighted linear sum of the function values at all other points. Higher-order derivative matrices are computed by simple matrix multiplication of the first-order weighting matrix ($D^{(m)} = D^{(1)} \dots D^{(1)}$).

Characteristics: Extremely simple to implement.

Drawback: As noted by Raju et al. (2013) [@Raju2013], Pure DQM is notorious for numerical instability in highly nonlinear post-buckling problems. The condition number of $D^{(m)}$ scales exponentially with $m$ and the number of grid points $N$.

### Pure inverse Differential Quadrature Method (iDQM)

Proposed by Ojo et al. (2021) [@Ojo2021], the Pure iDQM inverts the mathematical logic of DQM. Instead of approximating the function and differentiating, it directly approximates the highest-order derivative (e.g., $W_{,xxxx}$) using standard DQ. The lower-order derivatives and the function itself are recovered via integration weighting matrices ($H^{(m)}$), utilizing boundary conditions as constants of integration.

Characteristics: Requires the formulation of inverse boundary value problems to define the integration constants analytically.

Advantage: Integration is inherently a smoothing operation, meaning the condition number of the resulting algebraic system is significantly reduced.

Let's critically evaluate the motivation of Ojo et al. (2021) [@Ojo2021]. Ojo et al. proposed the iDQM fundamentally to bypass the extreme ill-conditioning and round-off error amplification caused by high-order differentiation matrices ($D^{(4)}$) in Pure DQM. When the condition number hits $\mathcal{O}(10^8)$, standard numerical solvers fail to converge. While Ojo's mathematical diagnosis of the matrix condition number is correct, their conclusion that one must switch to integral matrices to achieve stability in high-order PDEs is a misdiagnosis of where the failure actually occurs in nonlinear structural solvers.

Take an analytical Airy stress-based DQM, such as the one implemented in [this practice](PostBuckling-DQM-Analytical-Airy.ipynb), where Ojo's motivation is fundamentally bypassed. The instability in standard Pure DQM for FvK equations is rarely caused by a static matrix-vector multiplication $D^{(4)}W$. The failure actually occurs inside the Newton-Raphson solver during the finite-difference approximation of the Jacobian. When a standard optimizer perturbs the state vector by $\epsilon = 10^{-7}$, the $\mathcal{O}(10^8)$ condition number of $D^{(4)}$ amplifies this perturbation into massive $\mathcal{O}(0.1)$ numeric noise, destroying the descent direction. By deriving the exact analytical Jacobian using Kronecker tensor products, rhe finite-difference noise is entirely eliminated. Consequently, the Pure DQM achieves machine-precision convergence instantly, rendering the heavy machinery of integral $H$-matrices (iDQM) unnecessary.

When using the Ritz-DQM, Ojo's motivation also becomes invalid. Ojo's premise relies on the instability of $4^{\text{th}}$-order derivatives in the strong form. The Ritz method, however, operates on the Total Potential Energy ($\Pi$), which is the weak form.  Furthermore, a lower derivative order is achieved with integration by parts when compared to the strong from, reducing the highest spatial derivative to $m=2$ (the bending curvatures $\kappa_{x,y}$), fundamentally reducing the numerical instability. Finally, the Ritz-DQM does not use dense, global differentiation matrices $D^{(m)}$. Instead, in the practice herein proposed, an analytical, hierarchical Legendre basis functions are proposed, which allow exact analytical derivatives to be calculated at Gauss-Legendre integration points. Because Ritz-DQM relies on exact polynomial derivatives and exact numerical quadrature, it entirely circumvents the round-off amplification issues that Ojo et al. aimed to solve with the inverse quadrature method.

### Mixed iDQM (MiDQM)

**TODO find more about this**

MiDQM is a hybrid approach discussed in contemporary literature (including extensions of Ojo et al.). It uses direct differentiation matrices ($D^{(m)}$) for lower-order derivative terms and integration matrices ($H^{(m)}$) for the highest-order terms.

Characteristics: Balances the smoothing benefits of integral operators with the straightforward boundary condition enforcement of standard differentiation.

## Differential quadrature (OLD)

The Differential Quadrature Method (DQM) is a global numerical technique used to solve partial differential equations (PDEs). Unlike the Finite Element Method (FEM) which relies on localized piecewise interpolation, DQM approximates the derivative of a function at a specific grid point as a weighted linear sum of the function values at all discrete points in the domain.

For a 1D function $f(x)$ discretized over $N$ points, the $n$-th order derivative at point $x_i$ is given by:

$$\left. \frac{d^n f}{dx^n} \right|_{x=x_i} = \sum_{j=1}^{N} W_{ij}^{(n)} f(x_j) \quad \text{for } i = 1, 2, \dots, N \nonumber$$

where $W_{ij}^{(n)}$ are the weighting coefficients. To suppress Runge's phenomenon at higher polynomial orders, the grid points are not distributed uniformly, but rather follow the roots of orthogonal polynomials, such as Chebyshev-Gauss-Lobatto or Gauss-Legendre grids. While traditional DQM solves the strong form of the governing PDEs directly at the collocation points, this approach is mathematically brittle for 2D plate boundaries (specifically corners) due to linearly dependent constraints. 

### The Ritz-DQ Method

To bypass corner singularities and maintain the exponential convergence of spectral methods, it's possible to transition to the **weak form** via the Ritz-DQ method, which hybridises the classical Ritz variational method with DQM's numerical integration rules. Instead of directly evaluating the PDEs, the Ritz-DQ method minimizes the Total Potential Energy ($\Pi$) of the system. The continuous displacement fields $(u, v, w)$ are expanded using a spectral basis (Legendre polynomials). The DQM machinery is then leveraged to evaluate the continuous energy integrals using exact Gauss-Legendre quadrature.

#### Approximation functions
The transverse deflection $w(x,y)$ and in-plane displacements $u(x,y)$, $v(x,y)$ are approximated by expanding unknown Ritz coefficients $\mathbf{C}$ over 1D Legendre polynomials. To explicitly satisfy the simply supported (SSSS) kinematic boundary conditions ($w=0$ at edges), the following modified Legendre basis can be constructued:

$$\phi_m(\xi) = P_{m+2}(\xi) - P_m(\xi) \nonumber$$

Because standard Legendre polynomials $P_m(\pm 1) = (\pm 1)^m$, the difference exactly vanishes at the domain edges. The transverse field is thus:

$$w(\xi, \eta) = \sum_{i=0}^{N_c} \sum_{j=0}^{N_c} C^w_{ij} \phi_i(\xi) \phi_j(\eta) \nonumber$$

#### Strain energy

To capture post-buckling behavior, the strain-displacement relations must account for geometric nonlinearity. The von Karman mid-plane strains isolate the dominant transverse stiffening effects:

\begin{equation*}
\begin{aligned}
\varepsilon_{xx} &= u_{,x} + \frac{1}{2}w_{,x}^2
\\
\varepsilon_{yy} &= v_{,y} + \frac{1}{2}w_{,y}^2
\\
\gamma_{xy} &= u_{,y} + v_{,x} + w_{,x}w_{,y}
\end{aligned}
\end{equation*}

The Total Potential Energy ($\Pi$) is the sum of the membrane ($U_m$) and bending ($U_b$) strain energies. Defining extensional stiffness $C_{ext} = \frac{Eh}{1-\nu^2}$ and bending stiffness $D = \frac{Eh^3}{12(1-\nu^2)}$:

$$
U_m = \frac{C_{ext}}{2} \int_A \left( \varepsilon_{xx}^2 + \varepsilon_{yy}^2 + 2\nu\varepsilon_{xx}\varepsilon_{yy} + \frac{1-\nu}{2}\gamma_{xy}^2 \right) dA
\nonumber $$

$$
U_b = \frac{D}{2} \int_A \left( w_{,xx}^2 + w_{,yy}^2 + 2\nu w_{,xx}w_{,yy} + 2(1-\nu)w_{,xy}^2 \right) dA
\nonumber $$

In the Ritz-DQM, the continuous integral $\int_A (\dots) dA$ is replaced by the 2D Gauss-Legendre quadrature summation $\sum \sum (\dots) W_{ij}$.

An example of the Ritz-DQ method can be seen in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/PostBuckling-Ritz-DQ.ipynb).

+++{"no-pdf":true}
### Practice, Ritz-DQ Methodomputational Workflow
In [the Ritz-DQ practice](PostBuckling-Ritz-DQ.ipynb), the following algorithm is proposed:

1. **Initialization:** Generate the Gauss-Legendre quadrature roots $(\xi_i, \eta_j)$ and weights $W_{ij}$ for polynomial degree $N_c$.
2. **Precomputation:** Evaluate the 1D basis polynomials and their spatial derivatives at the grid points. Form the tensor products.
3. **Displacement Mapping:** Define a loop over incremental edge shortenings $\Delta u$. 
4. **Energy Minimization:** At each load step, project the current coefficient guess $\mathbf{C}$ through the precomputed tensors to obtain physical strains. Calculate $\Pi$ using DQM quadrature. Use an optimizer (e.g., BFGS or SLSQP) to find the coefficient array that minimizes $\Pi$.
5. **Symmetry Breaking:** If the plate is unbuckled ($w \approx 0$), inject an artificial perturbation (e.g., $C^w_{00} = 10^{-3}$) prior to minimization to push the gradient off the unstable saddle point.
6. **Force Recovery:** Post-multiply the converged displacement gradients to extract the boundary membrane stress $N_{xx}$, integrating it via 1D quadrature to output the applied macroscopic load $P$.


#### Boundary Condition Variations: Yamaki I vs. Yamaki III

The post-buckling stiffness of a plate is highly sensitive to the in-plane boundary conditions along the unloaded edges ($y = \pm b/2$). We analyze two foundational cases defined by Yamaki [@Yamaki1959].

##### Yamaki Condition III: Stress-Free (Warping) Edges
* **Physics:** The unloaded edges are completely unrestrained in the $y$-direction. As the plate buckles and deflects in $z$, the edges are physically pulled inward. Because they are unrestrained, they warp and wave, locally relieving membrane tension. 
* **Implementation:** This is a natural boundary condition. The optimizer minimizes the energy unconstrained, inherently finding the stress-free warped state. This results in lower geometric stiffness.

##### Yamaki Condition I: Straight Edges
* **Physics:** The unloaded edges are supported by stiffeners that allow them to slide inward macroscopically (zero average stress, $\int N_{yy} dx = 0$), but force them to remain perfectly straight. This forces the entire edge to displace by the same amount, generating massive transverse membrane tension in the center of the plate.
* **Implementation:** This requires an explicit kinematic equality constraint. The variance of the $v$-displacement along the edges must be zero:
  
  $$
  v(x, \pm b/2) - \bar{v}_{\pm b/2} = 0
  $$
  
In this example this is enforced either via a severe energy penalty factor.
+++

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

An example on how the effective width changes with the loading fraction and material properties can be seen in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/PostBuckling-be-composites-Kassapoglou-7.10.ipynb). An illustration on how the internal load changes over the skin width can be found in [this other notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/PostBuckling-be-composites-Kassapoglou-7.12.ipynb)
+++{"no-pdf":true}
These are also available in this web version of the documentation, see: [Kassapoglou, Fig. 7.10](PostBuckling-be-composites-Kassapoglou-7.10.ipynb) and [Kassapoglou, Fig. 7.12](PostBuckling-be-composites-Kassapoglou-7.12.ipynb).
+++

### Effective width for composite shells

The Technion Effective Width (TEW) method [@Pevzner2008] is an engineering
approximation for analyzing the postbuckling behavior of curved, laminated
composite structures. The TEW method extends the effective width concept to curved, anisotropic, laminated composite panels by reformulating an equivalent column model to account for the unique bending, torsional, and coupled instability modes of composite structures.

The TEW analysis process is summarized as follows:
1.  **First Buckling Calculation:** Determining the initial local buckling of the skin between stringers using semi-empirical or approximate analytical solutions.
2.  **Iterative Convergence of Effective Width:** Once the load exceeds the initial buckling load, an iterative algorithm calculates the effective width of the skin contributing to the load-carrying capacity. This process continues until the stress redistribution between the buckled skin and the stiffener reaches equilibrium.
3.  **Global Stability Analysis:** Evaluating the global column stability based on the flexural, torsional, and warping rigidities of the equivalent skin-stringer cross-section to determine the ultimate collapse load.

An example of the TEW method is presented in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/PostBuckling-be-composites-TEW.ipynb).
+++{"no-pdf":true}
Which is part of this web version of the documentation, see: [TEW method](PostBuckling-be-composites-TEW.ipynb).
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

