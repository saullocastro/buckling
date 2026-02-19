# Introduction to semi-analytical modelling

The simplest buckling case consists of the classical solution for the deflection $w$ of a plate with length $a$, width $b$ and thickness $h$, under in-plane distributed loads ($N_x$, $N_y$, $N_{xy}$). Even for this simple case, the presence of the bending-twisting coupling terms ($D_{16}$ and $D_{26}$); or the laminate being not symmetric $pmb{B} != 0$; or boundary conditions combining, clamped, simply-supported and free edges; or if the distributed in-plane loads $N_x$, $N_y$ or $N_{xy}$ are non-constant; the buckled mode shape will skew such that the exact closed-form solutions, for instance using orthogonal Fourier series, will become intractable, requiring semi-analytical methods or finite element discretizations. The governing equation for this problem is given below
[@Kassapoglou2013]:

$$\label{eq:diffeqplate} D_{11}\frac{\partial^4 w}{\partial x^4} + 4D_{16}\frac{\partial^4 w}{\partial x^3 \partial y} + 2(D_{12} + 2D_{66})\frac{\partial^4 w}{\partial x^2 \partial y^2} + 4D_{26}\frac{\partial^4 w}{\partial x \partial y^3} + D_{22}\frac{\partial^4 w}{\partial y^4} = N_x\frac{\partial^2 w}{\partial x^2} + N_y\frac{\partial^2 w}{\partial y^2} + 2N_{xy}\frac{\partial^2 w}{\partial x \partial y}$$


# Principle of minimum potential energy

The total potential energy $V$ can be decomposed into elastic energy $U$, and the work due to external forces $W_{ext}$:

$$V = U - W_{ext}$$

This potential becomes stationary when:
$$\delta V = \delta U - \delta W_{ext} = 0$$

## Strain Energy 

The general expression for the strain energy when $pmb{\sigma}$ increases linearly with $pmb{epsilon}$ is:

$$U = \frac{1}{2} \int_{\Omega} \pmb{\sigma}^\top \pmb{\varepsilon} \, d\Omega$$

The variation of this expression, valid also for the case of $\pmb{\sigma}$ being a non-linear function of $\pmb{\varepsilon}$, renders:
$$\delta U = \int_{\Omega} \pmb{\sigma}^\top \delta \pmb{\varepsilon} \, d\Omega$$

To calculate the strain energy in semi-analytical formulations of plates and shells, it is convenient to represent the second-order tensors of strain and stress are represented as vectors, according to Voigt's notation [@Voigt1910]. 
```{figure} Introduction-stress-3D.jpg
:label: fig:stress-3D
:alt: Complete stress state of a material point
:width: 80%

Complete stress state of a material point
```

Given the 3D stress state of a material point illustrated in [](#fig:stress-3D), the components of the stress tensor $\sigma_{ij}$ can be aligned in a vector as in Eq. [](#eq:voigt).

```{math}
:label:eq:voigt
\pmb{\sigma} = \left\{\begin{matrix}
\sigma_{11}\\
\sigma_{22}\\
\sigma_{33}\\
\sigma_{23}\\
\sigma_{13}\\
\sigma_{12}
\end{matrix}\right\}
```

where: 
* $\sigma_{11}$ - Normal in $x_1$
* $\sigma_{22}$ - Normal in $x_2$
* $\sigma_{33}$ - Normal in $x_3$ (thickness direction)
* $\tau_{23}$ - Transverse shear 23
* $\tau_{13}$ - Transverse shear 13
* $\tau_{12}$ - In-plane shear 12


A general constitutive relation for semi-analytical models, which show stresses relate to strains, can be written based on Voigt's notation:

$$\pmb{\sigma} = \pmb{C}\pmb{\varepsilon}$$

where $\pmb{C}$ is the constitutive matrix.

Not all stress components shown in Eq. []($eq:voigt) are relevant when calculating thin-walled structures. For plane stress using the Classical Laminated Plate Theory (CLPT):
$$\varepsilon_{xx}, \varepsilon_{yy}, \gamma_{xy}, \sigma_{xx}, \sigma_{yy}, \tau_{xy}$$
$$\pmb{\varepsilon}^\top = \{ \varepsilon_{xx} \quad \varepsilon_{yy} \quad \gamma_{xy} \} \qquad \pmb{\sigma}^\top = \{ \sigma_{xx} \quad \sigma_{yy} \quad \tau_{xy} \}$$

For plane stress using the First- or Third-order Shear Deformation Theory (FSDT or TSDT):

$$\varepsilon_{xx}, \varepsilon_{yy}, \gamma_{xy}, \gamma_{yz}, \gamma_{xz}$$
$$\sigma_{xx}, \sigma_{yy}, \tau_{xy}, \tau_{yz}, \tau_{xz}$$
$$\pmb{\varepsilon}^\top = \{ \varepsilon_{xx} \quad \varepsilon_{yy} \quad \gamma_{xy} \quad \gamma_{yz} \quad \gamma_{xz} \} \qquad \pmb{\sigma}^\top = \{ \sigma_{xx} \quad \sigma_{yy} \quad \tau_{xy} \quad \tau_{yz} \quad \tau_{xz} \}$$

The strains are usually expressed in terms of displacements in the so called kinematic equations, which can be generally written using Voigt's notation as:

$$\pmb{\varepsilon} = \pmb{B}\pmb{u}$$

where $\pmb{B} \equiv$ differentiation operator matrix, $\pmb{u}(x,y,z) \equiv$ continuous displacement field.

### Finite elements
In finite elemets, interpolation functions are used to approximate the displacement field within each finite element, which can be generally written as:

$$\pmb{u} = \begin{Bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{Bmatrix} = \pmb{S}(x,y,z) \, \pmb{\bar{u}}$$

where $\pmb{\bar{u}} \equiv$ nodal displacements and $\pmb{S}(x,y,z) \equiv$ interpolation (shape) functions valid only within the domain of one finite element.

Example for quadrilateral elements:
$$\pmb{u} = \pmb{S}_1 \pmb{\bar{u}}_1 + \pmb{S}_2 \pmb{\bar{u}}_2 + \pmb{S}_3 \pmb{\bar{u}}_3 + \pmb{S}_4 \pmb{\bar{u}}_4$$

From the kinematic equations: $\pmb{\varepsilon} = \pmb{B}\pmb{u}$, the differentiation operator $\pmb{B}$ will contain the proper derivatives of the interpolation functions corresponding to a given finite element.

The stress strain relation $\pmb{\sigma} = \pmb{C}\pmb{\varepsilon}$ will highly depend on each case. For trusses and beam (uniaxial stress), it can be simply $\sigma_{xx} = E\varepsilon_{xx}$, for plates this becomes more complicated, as covered later.

In finite elements, the strain energy can be thus expressed as:

$$\delta U = \int_{\Omega} \pmb{\sigma}^\top \delta \pmb{\varepsilon} \, d\Omega$$

Replacing $\pmb{\sigma} = \pmb{C}\pmb{\varepsilon}$, for $\pmb{C} = \pmb{C}^\top$:

$$\delta U = \int_{\Omega} \pmb{\varepsilon}^\top \pmb{C} \, \delta \pmb{\varepsilon} \, d\Omega$$

Replacing and $\pmb{\varepsilon} = \pmb{B}\pmb{\bar{u}}$:

$$\delta U = \pmb{\bar{u}}^\top \int_{\Omega} \pmb{B}^\top \pmb{C} \, \pmb{B} \, d\Omega \, \delta \pmb{\bar{u}}$$

$$\delta U = \pmb{\bar{u}}^\top \pmb{K} \, \delta \pmb{\bar{u}}$$

where $\pmb{K}$ is the constitutive stiffness matrix, usually referred to as simply the stiffness matrix:

$$\pmb{K} = \int_{\Omega} \pmb{B}^\top \pmb{C} \, \pmb{B} \, d\Omega$$

For finite elements, the rows and columns of $\pmb{K}$ correspond to the degrees-of-freedom built by the assembly of all finite elements. The integration over the 3-dimensional domain $\Omega$ is performed in a piece-wise manner within the domain of each finite element $\Omega_e$.

$$\pmb{K} = \sum_{e=1}^{n_e} \pmb{K}_e$$

$$\pmb{K}_e = \int_{\Omega_e} \pmb{B}^\top \pmb{C}_e \, \pmb{B} \, d\Omega_e$$

The integration of $\pmb{K}_e$ can be efficiently done numerically due to the local support of the integration points (only affect the stiffness of the corresponding element).

### Energy-based semi-analytical methods

In energy-based methods, such as the well-known Ritz method, the shape functions are expressed in terms of continuous functions instead of nodal degrees-of-freedom:

$$\pmb{u} = \begin{Bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{Bmatrix} = \pmb{S}(x,y,z) \, \pmb{\bar{c}}$$

where $\pmb{\bar{c}} \equiv$ amplitude of each term of the shape functions, $\pmb{S}(x,y,z) \equiv$ shape functions valid within the entire domain of the semi-analytical model, which can be an entire plate, an entire shell, or parts of a structure in the case of multi-domain semi-analytical models.

Example for deflection of simply supported plate $\xi = x/a$, $\eta = y/b$:

$$w(x,y) = \sum_{i=1}^{m} \sum_{j=1}^{n} c_{ij} \sin i\pi\xi \sin j\pi\eta = [\sin i\pi\xi \sin \pi\eta \quad \sin i\pi\xi \sin 2\pi\eta \quad \cdots] \begin{Bmatrix} c_{11} \\ c_{12} \\ \vdots \end{Bmatrix}$$

$$\pmb{\bar{c}} = \begin{Bmatrix} c_{11} \\ c_{12} \\ \vdots \end{Bmatrix}$$

From the kinematic equations: $\pmb{\varepsilon} = \pmb{B}\pmb{u}$, the differentiation operator $\pmb{B}$ will contain the proper derivatives of the shape functions.

The strain energy for the Ritz method can thus be expressed as:

$$\delta U = \int_{\Omega} \pmb{\sigma}^\top \delta \pmb{\varepsilon} \, d\Omega$$

Replacing $\pmb{\sigma} = \pmb{C}\pmb{\varepsilon}$, for $\pmb{C} = \pmb{C}^\top$:

$$\delta U = \int_{\Omega} \pmb{\varepsilon}^\top \pmb{C} \, \delta \pmb{\varepsilon} \, d\Omega$$

Replacing and $\pmb{\varepsilon} = \pmb{B}\pmb{c}$:

$$\delta U = \pmb{c}^\top \int_{\Omega} \pmb{B}^\top \pmb{C} \, \pmb{B} \, d\Omega \, \delta \pmb{c}$$

$$\delta U = \pmb{c}^\top \pmb{K} \, \delta \pmb{c}$$

with the constitutive stiffness matrix defined as:
$$\pmb{K} = \int_{\Omega} \pmb{B}^\top \pmb{C} \, \pmb{B} \, d\Omega$$


In the Ritz Method, the rows and columns of $\pmb{K}$ correspond to the degrees-of-freedom that depend on the number of function terms used in the displacement approximation. In single-domain semi-analytical models, there is only one integration domain $\Omega$, and the integration is usually performed analytically leading to very efficient methods that can analytically calculate the stiffness matrix, even for complex problems such as described by Castro et al. addressing the buckling of conical shells under combined load cases [@Castro2014]. However, when numerical integration is needed, for instance due to variable stiffness or in non-linear analyses [@Castro2015imperfect], the non-local support of the integration can create a large disadvantage of the Ritz method when compared to the finite element. The non-local support comes from the fact that the approximation functions represent the whole domain, and each integration point requires the evaluation of the entire stiffness matrix because all degress-of-freedom are components of continuous functions that affect that integration point. 

Therefore, one must be careful while implementing semi-analytical methods for cases of variable stiffness or non-linear analyses. The use of hierarchical polynomials as approximation functions enable such efficient implementations, because they allow the use of Gauss quadrature rules to efficiently perform the numerical integration. When trigonometric approximation functions are used the stiffness matrix can be integrated using the trapezoidal (piece-wise linear) or Simpson's rule (piece-wise quadratic) [@Castro2015]
 

## Work due to external forces

When considering tranction stresses $\pmb{\bar{\sigma}}$ acting on the boundaries of the domain $\delta\Omega$, and body forces $\pmb{b}$ acting on the entire volume of the domain $\Omega$, the following general expression for the work of external forces can be used:

$$W_{ext} = \int_{\Omega} \pmb{b}^\top \pmb{u} \, d\Omega + \int_{\delta \Omega} (\pmb{\bar{\sigma}}^\top \pmb{u}) d(\delta \Omega)$$

The first variation of work due to external forces becomes:

$$\delta W_{ext} = \int_{\Omega} \pmb{b}^\top \delta \pmb{u} \, d\Omega + \int_{\delta \Omega} (\pmb{\bar{\sigma}}^\top \delta \pmb{u}) d(\delta \Omega)= \pmb{F}^\top \delta \pmb{u}$$

where $\pmb{F} \equiv$ external force vector, including body ($\pmb{b}$) and boundary forces ($\pmb{\bar{\sigma}}$).


## Semi-analytical static solution

Back to the stationary total potential energy functional:

$$\delta V = \delta U - \delta W_{ext} = 0$$

The state of $V$ depends on a nodal displacement vector $\pmb{\bar{u}}$ in the case of displacement-based finite elements. In the Ritz method, we can make $\pmb{\bar{c}} = \pmb{\bar{u}}$ such that $\pmb{\bar{u}}$ represents the Ritz coefficients $\pmb{\bar{c}}$ that contain the amplitude of each term of the shape functions.

We can represent $\delta V$ using Fréchet’s derivatives. In the case of linear analyses:

$$\delta V = {V'}^\top \delta \pmb{\bar{u}} = 0$$

Thus, $V' = \pmb{R}$, or a residual force vector, with $V'$ being the first Fréchet’s derivative of $V$. Using the definition for the total potential energy, the first variation becomes:

$${V'}^\top \delta \pmb{\bar{u}} = \int_{\Omega} \pmb{\sigma}^\top \delta \pmb{\varepsilon} \, d\Omega - \int_{\Omega} (\pmb{b}^\top \delta \pmb{u}) d\Omega - \int_{\delta \Omega} (\pmb{\bar{\sigma}}^\top \delta \pmb{u}) d(\delta \Omega) = 0$$

## Approximation functions

The orthogonal trigonometric series is the simplest solution for Eq. [](#eq:diffeqplate).

$$w = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{mn} \sin\left(\frac{m \pi x}{a}\right) \sin\left(\frac{n \pi y}{b}\right)$$

However, when a general set of boundary conditions is needed, or whenever a skewed buckling mode is possible, a more robust approximation for the displacement field is required. Castro and Donadon [@CastroDonadon2017] present Rodrigues' form of Legendre hierarchic orthogonal polynomials [@Peano1976hierarchies; @DeChao1986], largely applied by Bardell et al. on the vibration problems [@Bardell1991plate; @Bardell1997shellfree; @Bardell1997shell]. In this form the first four terms $i = 1,2,3,4$ consist of Hermite cubic polynomials:

$$P_1(\chi) = \left( \frac{1}{2} - \frac{3}{4}\chi + \frac{1}{4}\chi^3 \right) \delta_{t1}$$
$$P_2(\chi) = \left( \frac{1}{8} - \frac{1}{8}\chi - \frac{1}{8}\chi^2 + \frac{1}{8}\chi^3 \right) \delta_{r1}$$
$$P_3(\chi) = \left( \frac{1}{2} + \frac{3}{4}\chi - \frac{1}{4}\chi^3 \right) \delta_{t2}$$
$$P_4(\chi) = \left( -\frac{1}{8} - \frac{1}{8}\chi + \frac{1}{8}\chi^2 + \frac{1}{8}\chi^3 \right) \delta_{r2}$$
with $\chi \in \{\xi, \eta, \zeta\}$, and for any $i > 4$:
$$P_i(\chi) = \sum_{p=0}^{i/2} \frac{(-1)^p (2i - 2p - 7)!!}{2^p p! (i - 2p - 1)!} \chi^{i-2p-1}$$
where $q!! = q(q - 2) \dots (2 \text{ or } 1)$ such that $0!! = 1$, and $(i/2)$ in the summation is an integer division. The binary flags $\delta_{t1}$, $\delta_{r1}$, $\delta_{t2}$ and $\delta_{r2}$ are equal to $0$ or $1$, and used in the first four terms of Rodrigues polynomials to enable or disable the translation and rotation of each domain boundary. Flag $\delta_{t1}$ is used to control the translation at boundary ($\chi = -1$), which is possible because using Rodrigues polynomials this is the only term among all terms in the approximation function that produces $P_i(\chi = -1) = 1$. Similarly, $\delta_{t2}$ is used to control the translation at boundary 2 ($\chi = +1$). The rotation at $\chi = -1$ and $\chi = +1$ is respectively controlled using $\delta_{r1}$ and $\delta_{r2}$, since they are the only terms that produce a non-null rotation $\partial P / \partial \chi$ at each respective domain boundary. The use of rotation is specially important in FSDT or TSDT formulations.

```{figure} Introduction-Legendre-BC.jpg
:alt: Legendre polynomial boundary functions
:width: 80%

Legendre polynomial boundary functions
```

```{figure} Introduction-Legendre-inner.jpg
:alt: Legendre inner functions
:width: 80%

Legendre polynomial inner functions
```

Vescovini et al. [@Vescovini2018shapefunctions] investigated the sparsity of the systems produced by different shape functions, positively supporting the use of Legendre hierarchical polynomials.


Slide 63: Legendre Polynomials
Shape functions: how displacement field is approximated

A general expression for the 3D displacement field is:

$$\boldsymbol{u} = \begin{Bmatrix} u(x,y,z) \\ v(x,y,z) \\ w(x,y,z) \end{Bmatrix} = \boldsymbol{S}(x,y,z)\bar{\boldsymbol{c}} = \begin{Bmatrix} \boldsymbol{S}^u(x,y,z) \\ \boldsymbol{S}^v(x,y,z) \\ \boldsymbol{S}^w(x,y,z) \end{Bmatrix} \bar{\boldsymbol{c}}$$

using Legendre polynomials (summation convention for repeated indices):

$$u(x,y,z) = c_{ijk}^u P_i(\xi) P_j(\eta) P_k(\zeta)$$
$$v(x,y,z) = c_{ijk}^v P_i(\xi) P_j(\eta) P_k(\zeta)$$
$$w(x,y,z) = c_{ijk}^w P_i(\xi) P_j(\eta) P_k(\zeta)$$

with, for a rectangular plate:
$$\xi = \frac{2x}{a} - 1$$
$$\eta = \frac{2y}{b} - 1$$
$$\zeta = \frac{2z}{h} - 1$$

The slide includes a diagram of a rectangular plate with dimensions $a, b, h$, defining the local coordinate system $x, y, z$ and corresponding displacement components $u, v, w$.

 

References:
•	[1c] Castro S.G.P., Donadon, M.V., "Assembly of Semi-Analytical models to Address Linear Buckling and Vibration of Stiffened Composite Panels with Debonding Defect". Composite Structures, 2017. 10.1016/j.compstruct.2016.10.026
•	[1d] Bardell N.S., "Free vibration analysis of a flat plate using the hierarchical finite element method". Journal of Sound and Vibration, 1991. https://doi.org/10.1016/0022-460X(91)90855-E
 
Would you like me to process any further slides in this deck?

