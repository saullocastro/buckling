# Introduction to semi-analytical modelling

The simplest buckling case consists of the classical solution for the deflection $w$ of a plate with length $a$, width $b$ and thickness $h$, under in-plane distributed loads ($N_x$, $N_y$, $N_{xy}$). Even for this simple case, the presence of the bending-twisting coupling terms ($D_{16}$ and $D_{26}$); or the laminate being not symmetric $\boldsymbol{B} \neq 0$; or boundary conditions combining, clamped, simply-supported and free edges; or if the distributed in-plane loads $N_x$, $N_y$ or $N_{xy}$ are non-constant; the buckled mode shape will skew such that the exact closed-form solutions, for instance using orthogonal Fourier series, will become intractable, requiring semi-analytical methods or finite element discretizations. The governing equation for this problem is given below
[@Kassapoglou2013]:

\begin{equation}
\label{eq:diffeqplate}
\begin{aligned}
D_{11}\frac{\partial^4 w}{\partial x^4} + 4D_{16}\frac{\partial^4 w}{\partial x^3 \partial y} \\
+ 2(D_{12} + 2D_{66})\frac{\partial^4 w}{\partial x^2 \partial y^2} \\
+ 4D_{26}\frac{\partial^4 w}{\partial x \partial y^3} + D_{22}\frac{\partial^4 w}{\partial y^4} \\
= N_x\frac{\partial^2 w}{\partial x^2} + N_y\frac{\partial^2 w}{\partial y^2} + 2N_{xy}\frac{\partial^2 w}{\partial x \partial y}
\end{aligned}
\end{equation}

## Principle of minimum potential energy

The total potential energy $V$ can be decomposed into elastic energy $U$, and the work due to external forces $W_{ext}$:

$$V = U - W_{ext} \nonumber$$

This potential becomes stationary when:
$$\delta V = \delta U - \delta W_{ext} = 0 \nonumber$$

### Strain Energy 

The general expression for the strain energy when $\boldsymbol{\sigma}$ increases linearly with $\boldsymbol{epsilon}$ is:

$$U = \frac{1}{2} \int_{\Omega} \boldsymbol{\sigma}^\top \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

The variation of this expression, valid also for the case of $\boldsymbol{\sigma}$ being a non-linear function of $\boldsymbol{\varepsilon}$, renders:

$$\delta U = \int_{\Omega} \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega  \nonumber$$

To calculate the strain energy in semi-analytical formulations of plates and shells, it is convenient to represent the second-order tensors of strain and stress are represented as vectors, according to Voigt's notation [@Voigt1910]. 
```{figure} Introduction-stress-3D.*
:label: fig:stress-3D
:width: 50%

Complete stress state of a material point.
```

Given the 3D stress state of a material point illustrated in [](#fig:stress-3D), the components of the stress tensor $\sigma_{ij}$ can be aligned in a vector as in Eq. [](#eq:voigt).

\begin{equation}
\label{eq:voigt}
\boldsymbol{\sigma} = \left\{
\begin{matrix}
\sigma_{11}\\
\sigma_{22}\\
\sigma_{33}\\
\sigma_{23}\\
\sigma_{13}\\
\sigma_{12}
\end{matrix}
\right\}
\end{equation}

where: 
* $\sigma_{11}$ - Normal in $x_1$
* $\sigma_{22}$ - Normal in $x_2$
* $\sigma_{33}$ - Normal in $x_3$ (thickness direction)
* $\tau_{23}$ - Transverse shear 23
* $\tau_{13}$ - Transverse shear 13
* $\tau_{12}$ - In-plane shear 12


A general constitutive relation for semi-analytical models, which show stresses relate to strains, can be written based on Voigt's notation:

$$\boldsymbol{\sigma} = \boldsymbol{C}\boldsymbol{\varepsilon}$$

where $\boldsymbol{C}$ is the constitutive matrix.

Not all stress components shown in Eq. []($eq:voigt) are relevant when calculating thin-walled structures. For plane stress using the Classical Laminated Plate Theory (CLPT):

$$\varepsilon_{xx}, \varepsilon_{yy}, \gamma_{xy}, \sigma_{xx}, \sigma_{yy}, \tau_{xy} \nonumber$$
$$\boldsymbol{\varepsilon}^\top = \{ \varepsilon_{xx} \quad \varepsilon_{yy} \quad \gamma_{xy} \} \qquad \boldsymbol{\sigma}^\top = \{ \sigma_{xx} \quad \sigma_{yy} \quad \tau_{xy} \} \nonumber$$

For plane stress using the First- or Third-order Shear Deformation Theory (FSDT or TSDT):

$$\varepsilon_{xx}, \varepsilon_{yy}, \gamma_{xy}, \gamma_{yz}, \gamma_{xz} \nonumber$$
$$\sigma_{xx}, \sigma_{yy}, \tau_{xy}, \tau_{yz}, \tau_{xz} \nonumber$$
$$\boldsymbol{\varepsilon}^\top = \{ \varepsilon_{xx} \quad \varepsilon_{yy} \quad \gamma_{xy} \quad \gamma_{yz} \quad \gamma_{xz} \} \qquad \boldsymbol{\sigma}^\top = \{ \sigma_{xx} \quad \sigma_{yy} \quad \tau_{xy} \quad \tau_{yz} \quad \tau_{xz} \} \nonumber$$

The strains are usually expressed in terms of displacements in the so called kinematic equations, which can be generally written using Voigt's notation as:

$$\boldsymbol{\varepsilon} = \boldsymbol{B}\boldsymbol{u} \nonumber$$

where $\boldsymbol{B} \equiv$ differentiation operator matrix, $\boldsymbol{u}(x,y,z) \equiv$ continuous displacement field.

#### Finite elements
In finite elemets, interpolation functions are used to approximate the displacement field within each finite element, which can be generally written as:

$$\boldsymbol{u} = \begin{Bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{Bmatrix} = \boldsymbol{S}(x,y,z) \, \boldsymbol{\bar{u}} \nonumber$$

where $\boldsymbol{\bar{u}} \equiv$ nodal displacements and $\boldsymbol{S}(x,y,z) \equiv$ interpolation (shape) functions valid only within the domain of one finite element.

Example for quadrilateral elements:
$$\boldsymbol{u} = \boldsymbol{S}_1 \boldsymbol{\bar{u}}_1 + \boldsymbol{S}_2 \boldsymbol{\bar{u}}_2 + \boldsymbol{S}_3 \boldsymbol{\bar{u}}_3 + \boldsymbol{S}_4 \boldsymbol{\bar{u}}_4 \nonumber$$

From the kinematic equations: $\boldsymbol{\varepsilon} = \boldsymbol{B}\boldsymbol{u}$, the differentiation operator $\boldsymbol{B}$ will contain the proper derivatives of the interpolation functions corresponding to a given finite element.

The stress strain relation $\boldsymbol{\sigma} = \boldsymbol{C}\boldsymbol{\varepsilon}$ will highly depend on each case. For trusses and beam (uniaxial stress), it can be simply $\sigma_{xx} = E\varepsilon_{xx}$, for plates this becomes more complicated, as covered later.

In finite elements, the strain energy can be thus expressed as:

$$\delta U = \int_{\Omega} \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

Replacing $\boldsymbol{\sigma} = \boldsymbol{C}\boldsymbol{\varepsilon}$, for $\boldsymbol{C} = \boldsymbol{C}^\top$:

$$\delta U = \int_{\Omega} \boldsymbol{\varepsilon}^\top \boldsymbol{C} \, \delta \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

Replacing and $\boldsymbol{\varepsilon} = \boldsymbol{B}\boldsymbol{\bar{u}}$:

$$\delta U = \boldsymbol{\bar{u}}^\top \int_{\Omega} \boldsymbol{B}^\top \boldsymbol{C} \, \boldsymbol{B} \, d\Omega \, \delta \boldsymbol{\bar{u}} \nonumber$$

$$\delta U = \boldsymbol{\bar{u}}^\top \boldsymbol{K} \, \delta \boldsymbol{\bar{u}} \nonumber$$

where $\boldsymbol{K}$ is the constitutive stiffness matrix, usually referred to as simply the stiffness matrix:

$$\boldsymbol{K} = \int_{\Omega} \boldsymbol{B}^\top \boldsymbol{C} \, \boldsymbol{B} \, d\Omega \nonumber$$

For finite elements, the rows and columns of $\boldsymbol{K}$ correspond to the degrees-of-freedom built by the assembly of all finite elements. The integration over the 3-dimensional domain $\Omega$ is performed in a piece-wise manner within the domain of each finite element $\Omega_e$.

$$\boldsymbol{K} = \sum_{e=1}^{n_e} \boldsymbol{K}_e \nonumber$$

$$\boldsymbol{K}_e = \int_{\Omega_e} \boldsymbol{B}^\top \boldsymbol{C}_e \, \boldsymbol{B} \, d\Omega_e \nonumber$$

The integration of $\boldsymbol{K}_e$ can be efficiently done numerically due to the local support of the integration points (only affect the stiffness of the corresponding element).

#### Energy-based semi-analytical methods

In energy-based methods, such as the well-known Ritz method, the shape functions are expressed in terms of continuous functions instead of nodal degrees-of-freedom:

$$\boldsymbol{u} = \begin{Bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{Bmatrix} = \boldsymbol{S}(x,y,z) \, \boldsymbol{\bar{c}} \nonumber$$

where $\boldsymbol{\bar{c}} \equiv$ amplitude of each term of the shape functions, $\boldsymbol{S}(x,y,z) \equiv$ shape functions valid within the entire domain of the semi-analytical model, which can be an entire plate, an entire shell, or parts of a structure in the case of multi-domain semi-analytical models.

Example for deflection of simply supported plate $\xi = x/a$, $\eta = y/b$:

$$w(x,y) = \sum_{i=1}^{m} \sum_{j=1}^{n} c_{ij} \sin i\pi\xi \sin j\pi\eta = [\sin i\pi\xi \sin \pi\eta \quad \sin i\pi\xi \sin 2\pi\eta \quad \cdots] \begin{Bmatrix} c_{11} \\ c_{12} \\ \vdots \end{Bmatrix} \nonumber$$

$$\boldsymbol{\bar{c}} = \begin{Bmatrix} c_{11} \\ c_{12} \\ \vdots \end{Bmatrix} \nonumber$$

From the kinematic equations: $\boldsymbol{\varepsilon} = \boldsymbol{B}\boldsymbol{u}$, the differentiation operator $\boldsymbol{B}$ will contain the proper derivatives of the shape functions.

The strain energy for the Ritz method can thus be expressed as:

$$\delta U = \int_{\Omega} \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

Replacing $\boldsymbol{\sigma} = \boldsymbol{C}\boldsymbol{\varepsilon}$, for $\boldsymbol{C} = \boldsymbol{C}^\top$:

$$\delta U = \int_{\Omega} \boldsymbol{\varepsilon}^\top \boldsymbol{C} \, \delta \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

Replacing and $\boldsymbol{\varepsilon} = \boldsymbol{B}\boldsymbol{c}$:

$$\delta U = \boldsymbol{c}^\top \int_{\Omega} \boldsymbol{B}^\top \boldsymbol{C} \, \boldsymbol{B} \, d\Omega \, \delta \boldsymbol{c} \nonumber$$

$$\delta U = \boldsymbol{c}^\top \boldsymbol{K} \, \delta \boldsymbol{c} \nonumber$$

with the constitutive stiffness matrix defined as:

$$\boldsymbol{K} = \int_{\Omega} \boldsymbol{B}^\top \boldsymbol{C} \, \boldsymbol{B} \, d\Omega \nonumber$$


In the Ritz Method, the rows and columns of $\boldsymbol{K}$ correspond to the degrees-of-freedom that depend on the number of function terms used in the displacement approximation. In single-domain semi-analytical models, there is only one integration domain $\Omega$, and the integration is usually performed analytically leading to very efficient methods that can analytically calculate the stiffness matrix, even for complex problems such as described by Castro et al. addressing the buckling of conical shells under combined load cases [@Castro2014]. However, when numerical integration is needed, for instance due to variable stiffness or in non-linear analyses [@Castro2015imperfect], the non-local support of the integration can create a large disadvantage of the Ritz method when compared to the finite element. The non-local support comes from the fact that the approximation functions represent the whole domain, and each integration point requires the evaluation of the entire stiffness matrix because all degress-of-freedom are components of continuous functions that affect that integration point. 

Therefore, one must be careful while implementing semi-analytical methods for cases of variable stiffness or non-linear analyses. The use of hierarchical polynomials as approximation functions enable such efficient implementations, because they allow the use of Gauss quadrature rules to efficiently perform the numerical integration. When trigonometric approximation functions are used the stiffness matrix can be integrated using the trapezoidal (piece-wise linear) or Simpson's rule (piece-wise quadratic) [@Castro2015]
 

### Work due to external forces

When considering tranction stresses $\boldsymbol{\bar{\sigma}}$ acting on the boundaries of the domain $\delta\Omega$, and body forces $\boldsymbol{b}$ acting on the entire volume of the domain $\Omega$, the following general expression for the work of external forces can be used:

$$W_{ext} = \int_{\Omega} \boldsymbol{b}^\top \boldsymbol{u} \, d\Omega + \int_{\delta \Omega} (\boldsymbol{\bar{\sigma}}^\top \boldsymbol{u}) d(\delta \Omega) \nonumber$$

The first variation of work due to external forces becomes:

$$\delta W_{ext} = \int_{\Omega} \boldsymbol{b}^\top \delta \boldsymbol{u} \, d\Omega + \int_{\delta \Omega} (\boldsymbol{\bar{\sigma}}^\top \delta \boldsymbol{u}) d(\delta \Omega)= \boldsymbol{F}^\top \delta \boldsymbol{u} \nonumber$$

where $\boldsymbol{F} \equiv$ external force vector, including body ($\boldsymbol{b}$) and boundary forces ($\boldsymbol{\bar{\sigma}}$).


### Semi-analytical static solution

Back to the stationary total potential energy functional:

$$\delta V = \delta U - \delta W_{ext} = 0 \nonumber$$

The state of $V$ depends on a nodal displacement vector $\boldsymbol{\bar{u}}$ in the case of displacement-based finite elements. In the Ritz method, we can make $\boldsymbol{\bar{c}} = \boldsymbol{\bar{u}}$ such that $\boldsymbol{\bar{u}}$ represents the Ritz coefficients $\boldsymbol{\bar{c}}$ that contain the amplitude of each term of the shape functions.

We can represent $\delta V$ using Fréchet’s derivatives. In the case of linear analyses:

$$\delta V = {V'}^\top \delta \boldsymbol{\bar{u}} = 0 \nonumber$$

Thus, $V' = \boldsymbol{R}$, or a residual force vector, with $V'$ being the first Fréchet’s derivative of $V$. Using the definition for the total potential energy, the first variation becomes:

$${V'}^\top \delta \boldsymbol{\bar{u}} = \int_{\Omega} \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega - \int_{\Omega} (\boldsymbol{b}^\top \delta \boldsymbol{u}) d\Omega - \int_{\delta \Omega} (\boldsymbol{\bar{\sigma}}^\top \delta \boldsymbol{u}) d(\delta \Omega) = 0 \nonumber$$

## Approximation functions

The orthogonal trigonometric series is the simplest solution for Eq. [](#eq:diffeqplate).

$$w = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{mn} \sin\left(\frac{m \pi x}{a}\right) \sin\left(\frac{n \pi y}{b}\right) \nonumber$$

However, when a general set of boundary conditions is needed, or whenever a skewed buckling mode is possible, a more robust approximation for the displacement field is required. Castro and Donadon [@CastroDonadon2017] present Rodrigues' form of Legendre hierarchic orthogonal polynomials [@Peano1976hierarchies; @DeChao1986], largely applied by Bardell et al. on the vibration problems [@Bardell1991plate; @Bardell1997shellfree; @Bardell1997shell]. In this form the first four terms $i = 1,2,3,4$ consist of Hermite cubic polynomials:

\begin{equation*}
\begin{aligned}
P_1(\chi) &= \left( \frac{1}{2} - \frac{3}{4}\chi + \frac{1}{4}\chi^3 \right) \delta_{t1}
\\
P_2(\chi) &= \left( \frac{1}{8} - \frac{1}{8}\chi - \frac{1}{8}\chi^2 + \frac{1}{8}\chi^3 \right) \delta_{r1}
\\
P_3(\chi) &= \left( \frac{1}{2} + \frac{3}{4}\chi - \frac{1}{4}\chi^3 \right) \delta_{t2}
\\
P_4(\chi) &= \left( -\frac{1}{8} - \frac{1}{8}\chi + \frac{1}{8}\chi^2 + \frac{1}{8}\chi^3 \right) \delta_{r2}
\end{aligned}
\end{equation*}

with $\chi \in \{\xi, \eta, \zeta\}$, and for any $i > 4$:

$$P_i(\chi) = \sum_{p=0}^{i/2} \frac{(-1)^p (2i - 2p - 7)!!}{2^p p! (i - 2p - 1)!} \chi^{i-2p-1} \nonumber$$

where $q!! = q(q - 2) \dots (2 \text{ or } 1)$ such that $0!! = 1$, and $(i/2)$ in the summation is an integer division. The binary flags $\delta_{t1}$, $\delta_{r1}$, $\delta_{t2}$ and $\delta_{r2}$ are equal to $0$ or $1$, and used in the first four terms of Rodrigues polynomials to enable or disable the translation and rotation of each domain boundary, as illustrated in [](#fig:legendre-bc). From the fifth term onwards, the translation and rotation at the boundaries are always zero, such that they are use to increase the interpolation order in the inner part of the domain, as illustrated in [](#fig:legendre-inner). Flag $\delta_{t1}$ is used to control the translation at boundary ($\chi = -1$), which is possible because using Rodrigues polynomials this is the only term among all terms in the approximation function that produces $P_i(\chi = -1) = 1$. Similarly, $\delta_{t2}$ is used to control the translation at boundary 2 ($\chi = +1$). The rotation at $\chi = -1$ and $\chi = +1$ is respectively controlled using $\delta_{r1}$ and $\delta_{r2}$, since they are the only terms that produce a non-null rotation $\partial P / \partial \chi$ at each respective domain boundary. The use of rotation is specially important in FSDT or TSDT formulations. Vescovini et al. [@Vescovini2018shapefunctions] investigated the sparsity of the systems produced by different shape functions, positively supporting the use of these Legendre hierarchical polynomials.

```{figure} Introduction-Legendre-BC.*
:label:fig:legendre-bc
:width: 80%

Legendre polynomial boundary functions.
```

```{figure} Introduction-Legendre-inner.*
:label:fig:legendre-inner
:width: 80%

Legendre polynomial inner functions.
```

Take the plate-like domain shown in [](#fig:plate-domain). A general expression for the 3D displacement field is:

$$\boldsymbol{u} = \begin{Bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{Bmatrix} = \boldsymbol{S}(x,y,z)\bar{\boldsymbol{c}} = \begin{Bmatrix} \boldsymbol{S}^u(x,y,z) \\ \boldsymbol{S}^v(x,y,z) \\ \boldsymbol{S}^w(x,y,z) \end{Bmatrix} \bar{\boldsymbol{c}} \nonumber$$

using Legendre polynomials (summation convention for repeated indices):

$$u(x,y,z) = c_{ijk}^u P_i(\xi) P_j(\eta) P_k(\zeta) \nonumber$$
$$v(x,y,z) = c_{ijk}^v P_i(\xi) P_j(\eta) P_k(\zeta) \nonumber$$
$$w(x,y,z) = c_{ijk}^w P_i(\xi) P_j(\eta) P_k(\zeta) \nonumber$$

which, for a plate:

$$\xi = \frac{2x}{a} - 1 \nonumber$$
$$\eta = \frac{2y}{b} - 1 \nonumber$$
$$\zeta = \frac{2z}{h} - 1 \nonumber$$

```{figure} Introduction-plate-domain.*
:label:fig:plate-domain
:width: 40%

Three-dimensional plate domain.
```


## Neutral Equilibrium Criterion

The neutral equilibrium of a vertical slender beam is illustrated in [](#fig:neutral-equilibrium)

```{figure} Introduction-Neutral-Equilibrium.*
:label:fig:neutral-equilibrium
:width: 100%

Neutral Equilibrium of a vertical slender beam.
```
Given the expression for $V'$:
$${V'}^\top \delta \boldsymbol{\bar{u}} = \int_{\Omega} \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega - \int_{\Omega} (\boldsymbol{\hat{b}}^\top \delta \boldsymbol{u}) d\Omega - \int_{\delta \Omega} (\boldsymbol{\hat{\sigma}}^\top \delta \boldsymbol{u}) d(\delta \Omega) \nonumber$$

The second variation of $V$ becomes:
$$\delta^2 V = V'' \delta \boldsymbol{\bar{u}} \delta \boldsymbol{\bar{u}} = \nonumber$$

$$= \int_{\Omega} \delta \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega + \int_{\Omega} \boldsymbol{\sigma}^\top \delta^2 \boldsymbol{\varepsilon} \, d\Omega - \int_{\Omega} (\delta \boldsymbol{\hat{b}}^\top \delta \boldsymbol{u}) d\Omega - \int_{\Omega} (\boldsymbol{\hat{b}}^\top \delta^2 \boldsymbol{u}) d\Omega - \int_{\delta \Omega} (\delta \boldsymbol{\hat{\sigma}}^\top \delta \boldsymbol{u}) d(\delta \Omega) - \int_{\delta \Omega} (\boldsymbol{\hat{\sigma}}^\top \delta^2 \boldsymbol{u}) d(\delta \Omega) \nonumber$$

In a system without follower forces $\delta \boldsymbol{\hat{\sigma}} = \delta \boldsymbol{\hat{b}} = \boldsymbol{0}$, and we can consider $\delta^2 \boldsymbol{u} \ll \delta \boldsymbol{u}$:

$$V'' \delta \boldsymbol{\bar{u}} \delta \boldsymbol{\bar{u}} = \int_{\Omega} \delta \boldsymbol{\sigma}^\top \delta \boldsymbol{\varepsilon} \, d\Omega + \int_{\Omega} \boldsymbol{\sigma}^\top \delta^2 \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

The first integral represents the nonlinear constitutive stiffness, whereas the second integral represents the geometric stiffness matrix. If the strains can be represented as:

$$\boldsymbol{\varepsilon} = \left( \boldsymbol{B}_L + \frac{1}{2}\boldsymbol{B}_{NL} \right) \boldsymbol{\bar{u}} \qquad \text{and} \qquad \delta \boldsymbol{\varepsilon} = (\boldsymbol{B}_L + \boldsymbol{B}_{NL}) \delta \boldsymbol{\bar{u}} \nonumber$$

And the stresses as:

$$\boldsymbol{\sigma} = \boldsymbol{C}\boldsymbol{\varepsilon} \nonumber$$

Then:

$$V'' \delta \boldsymbol{\bar{u}} \delta \boldsymbol{\bar{u}} = \delta \boldsymbol{\bar{u}}^\top \int_{\Omega} (\boldsymbol{B}_L + \boldsymbol{B}_{NL})^\top \boldsymbol{C} (\boldsymbol{B}_L + \boldsymbol{B}_{NL}) d\Omega \, \delta \boldsymbol{\bar{u}} + \int_{\Omega} \boldsymbol{\sigma}^\top \delta^2 \boldsymbol{\varepsilon} \, d\Omega \nonumber$$

The neutral equilibrium criterion states that:

$$\delta^2 V = 0 \nonumber$$
$$\delta^2 V = V'' \delta \boldsymbol{\bar{u}} \delta \boldsymbol{\bar{u}} = \delta \boldsymbol{\bar{u}}^\top \int_{\Omega} (\boldsymbol{B}_L + \boldsymbol{B}_{NL})^\top \boldsymbol{C} (\boldsymbol{B}_L + \boldsymbol{B}_{NL}) d\Omega \, \delta \boldsymbol{\bar{u}} + \delta \boldsymbol{\bar{u}}^\top \boldsymbol{K}_G \delta \boldsymbol{\bar{u}} = 0 \nonumber$$

This term represents the constitutive stiffness matrix:

$$\boldsymbol{K}_C = \int_{\Omega} (\boldsymbol{B}_L + \boldsymbol{B}_{NL})^\top \boldsymbol{C} (\boldsymbol{B}_L + \boldsymbol{B}_{NL}) d\Omega \nonumber$$

From a linear fundamental (pre-buckling) state we have that $\boldsymbol{B}_{NL} = \boldsymbol{0}$:
$$\boldsymbol{K}_C = \boldsymbol{K}_0 = \int_{\Omega} \boldsymbol{B}_L^\top \boldsymbol{C} \boldsymbol{B}_L d\Omega \nonumber$$

such that:

$$\delta^2 V = \delta \boldsymbol{\bar{u}}^\top \boldsymbol{K}_0 \delta \boldsymbol{\bar{u}} + \delta \boldsymbol{\bar{u}}^\top \boldsymbol{K}_G \delta \boldsymbol{\bar{u}} = 0 \nonumber$$

where $\boldsymbol{K}_G$ represents the geometric stiffness matrix. Note that this expression must be true for any variation $\delta \boldsymbol{\bar{u}}$, such that $\boldsymbol{K}_0 + \lambda\boldsymbol{K}_G$ must be singular for the expression to be generaly true, hence:

$$\det(\boldsymbol{K}_0 + \lambda\boldsymbol{K}_G) = 0 \nonumber$$

where $\lambda$ is a load multiplier applied to the initial stress state defining $\boldsymbol{K}_G$. This is the well-known eigenvalue problem for buckling, also referred to as linear buckling equation.

 