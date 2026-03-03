# Post-buckling of perfect shells

## Galerkin method using Airy's stress function

### Core formulation
This part provides comprehensive theoretical overview of the buckling and post-buckling behavior of thin-walled cylindrical shells under single and combined loading conditions, based on the recent work of Lu et al. [@Lu2025ShellPostBuckling]. The formulation follows the Donnell shell theory solved via the Galerkin method. The theoretical framework is established using Donnell shell theory, which is widely adopted for thin shells due to its practical accuracy and relative simplicity. It assumes that in-plane displacements are negligible compared to transverse displacements.

For a cylindrical shell of length $L$, radius $R$, and thickness $h$, the state is defined by the transverse displacement $w(x, y)$ and the Airy stress function $F(x, y)$. The balance of forces in the radial direction, considering geometric nonlinearities (von K\'arm\'an terms), is given by: 

$$D\nabla^4 w - \frac{1}{R}\frac{\partial^2 F}{\partial x^2} = \frac{\partial^2 F}{\partial y^2}\frac{\partial^2 w}{\partial x^2} - 2\frac{\partial^2 F}{\partial x \partial y}\frac{\partial^2 w}{\partial x \partial y} + \frac{\partial^2 F}{\partial x^2}\frac{\partial^2 w}{\partial y^2} \nonumber$$

where $D = \frac{Eh^3}{12(1-\nu^2)}$ is the flexural rigidity. To ensure a continuous displacement field, the stress function must satisfy: 

$$\nabla^4 F + \frac{Eh}{R}\frac{\partial^2 w}{\partial x^2} = Eh \left[ \left(\frac{\partial^2 w}{\partial x \partial y}\right)^2 - \frac{\partial^2 w}{\partial x^2}\frac{\partial^2 w}{\partial y^2} \right] \nonumber$$
 
To solve these nonlinear partial differential equations (PDEs), Lu et al. transformed them into a system of algebraic equations using the Galerkin method. For clamped-clamped (C-C) boundary conditions, the dimensionless transverse displacement $\bar{w}$ is assumed as a double Fourier series: 

$$\bar{w}(\bar{x},\bar{y}) = \sum_{m=1}^{\infty} \sum_{n=0}^{\infty} a_{m,n} (\psi_{m-1,n} + \psi_{m+1,n}) \nonumber$$

where $\psi_{mn}$ are basis functions that inherently satisfy the boundary conditions: 

$$\psi_{mn} = \cos(m\bar{x} + n\bar{y}) + (-1)^m \cos(m\bar{x} - n\bar{y}) \nonumber$$

To derive the stress function, the $\bar{w}$ approximation is inserted into the compatibility equation, allowing the analytical determination of the stress function $F$ in terms of the unknown modal amplitudes $a_{m,n}$. Applying the Galerkin procedure to the equilibrium equation yields a coupled system of cubic algebraic equations: 

$$\int_{0}^{2\pi} \int_{-\pi/2}^{\pi/2} \mathcal{J}(\bar{w}, f) (\psi_{r-1,s} + \psi_{r+1,s}) d\bar{x} d\bar{y} = 0 \nonumber$$
 
### Stability and non-linear path tracking

Tracking the post-buckling equilibrium path requires advanced numerical strategies to handle instabilities and multi-valued solutions. Standard load-controlled solvers fail at limit points where the shell "snaps" to a new state. The arc-length method (Riks method) parameterizes the path by a distance $s$ along the curve, treating the load parameter ($\Sigma$ or $k_s$) as an additional unknown. This allows the solver to trace unstable "snap-back" branches where both load and displacement decrease simultaneously. The stability of a branch is determined by the Jacobian matrix ($\mathbf{J}$) of the residual system, and can be classified within the following criteria:

* Stability criterion: A branch is stable if all eigenvalues of $\mathbf{J}$ have positive real parts.
* Bifurcation/Limit Points: These occur when the minimum real eigenvalue crosses zero ($\lambda_{min} \approx 0$).
* Mode Jumping: Physically, the shell snaps to a lower energy state, often characterized by a decrease in the circumferential wavenumber $N$.

### Non-dimensionalisation scheme

To generalize the computational model across varying geometries, Lu et al. [@Lu2025ShellPostBuckling] proposed a normalisation of the PDEs. The physical domain is mapped into a dimensionless space using the circumferential wavenumber $N$.

Spatial coordinates and field variables:

* Axial Coordinate: $\bar{x} = \frac{\pi x}{L}$ 
* Circumferential Coordinate: $\bar{y} = \frac{N y}{R}$ 
* Transverse Displacement: $\bar{w} = \frac{w}{h}$ 
* Airy's Stress Function: $f = \frac{F}{Eh^3}$ 

The shell's properties are condensed into dimensionless constants:

* Normalized flexural rigidity constant based on Poisson's ratio $\nu$: $c = \frac{1}{12(1-\nu^2)}$
* Geometric scaling factor dependent on the length-to-radius and radius-to-thickness ratios: $\alpha = \frac{L^2}{\pi^2 R h}$
* Dimensionless parameter associated with the circumferential wavenumber $N$: $\beta = \frac{N L}{\pi R}$

The external loads and global deformations are scaled to trace the equilibrium paths:

* Dimensionless Axial Force: $k_x = \frac{P L^2}{2 \pi^3 E R h^3}$
* Dimensionless Torque: $k_s = \frac{T L^2}{2 \pi^3 R^2 D}$
* Dimensionless End Shortening: $\bar{\delta} = \frac{R \Delta}{L h}$
* Dimensionless Twisting Angle: $\bar{\varphi} = \frac{R^2 \varphi}{L h}$

In force-control scenarios, the compressive force $P$ is frequently normalized against the classical critical buckling load $P_{cr0}$ for simply supported shells, denoted as $\Sigma = P/P_{cr0}$. This relates to the core parameter via $P/P_{cr0} = \sqrt{3(1-\nu^2)} \frac{k_x}{\alpha}$.

## Practice, Galerkin method using Airy's stress function

[This notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/PostBucklingShells-Galerkin-Airy.ipynb).
+++{"no-pdf":true}
This example is also available [through this documentation](PostBucklingShells-Galerkin-Airy.ipynb).
+++

# Post-buckling of imperfect cylindrical shells

TODO