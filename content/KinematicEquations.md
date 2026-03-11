# Strain-displacement (kinematic) equations for plates, cylindrical and spherical shells

Castro [@CastroEMstability2025] compiled the kinematic equations for plates, cylindrical, conical and spherical shells. A general overview from the full elasticity theory to the main equivalent single-layer theories is given. Note that $\gamma_{ij}$ is used here, meaning the engineering shear strains.

## General strain-displacement relations

According to the three-dimensional (3D) elasticity theory, the strain components referred to an arbitrary orthogonal coordinate system $x_1$,$x_2$, $x_3$, illustrated in [](#fig:kestress-3D)

```{figure} Introduction-stress-3D.*
:label: fig:kestress-3D
:width: 50%

Complete stress state of a material point.
```

can be written as [@CastroPhD]: 

\begin{equation*}
\begin{split}
\epsilon_{11} = \frac{1}{2}\left( \left( \frac{e_{13}}{2} - \omega_{2} \right)^{2} + \left( \frac{e_{12}}{2} + \omega_{3} \right)^{2} + e_{11}^{2} \right) + e_{11} \\
\epsilon_{22} = \frac{1}{2}\left( \left( \frac{e_{23}}{2} + \omega_{1} \right)^{2} + \left( \frac{e_{12}}{2} - \omega_{3} \right)^{2} + e_{22}^{2} \right) + e_{22} \\
\epsilon_{33} = \frac{1}{2}\left( \left( \frac{e_{23}}{2} - \omega_{1} \right)^{2} + \left( \frac{e_{13}}{2} + \omega_{2} \right)^{2} + e_{33}^{2} \right) + e_{33} \\
\epsilon_{12} = \left( \frac{e_{23}}{2} + \omega_{1} \right) \left( \frac{e_{13}}{2} - \omega_{2} \right) + e_{11} \left( \frac{e_{12}}{2} - \omega_{3} \right) + e_{22} \left( \frac{e_{12}}{2} + \omega_{3} \right) + e_{12} \\
\epsilon_{13} = e_{33} \left( \frac{e_{13}}{2} - \omega_{2} \right) + e_{11} \left( \frac{e_{13}}{2} + \omega_{2} \right) + \left( \frac{e_{23}}{2} - \omega_{1} \right) \left( \frac{e_{12}}{2} + \omega_{3} \right) + e_{13} \\
\epsilon_{23} = e_{22} \left( \frac{e_{23}}{2} - \omega_{1} \right) + e_{33} \left( \frac{e_{23}}{2} + \omega_{1} \right) + \left( \frac{e_{13}}{2} + \omega_{2} \right) \left( \frac{e_{12}}{2} - \omega_{3} \right) + e_{23}
\end{split}
\end{equation*}

where the parameters $\epsilon_ij$ and $\omega_i$ are (the conventional notation for partial derivatives $\partial/\partial x$ is used here for the sake of clarity) the following (@CastroPhD), with $u$, $v$, $w$ being the displacements along directions $x_1$, $x_2$, $x_3$, respectively: 

\begin{equation*}
\begin{split}
e_{11} = \frac{1}{H_{1}}\frac{\partial u}{\partial x_{1}} + \frac{v}{H_{1}H_{2}} \frac{\partial H_{1}}{\partial x_{2}} + \frac{w}{H_{1}H_{3}} \frac{\partial H_{1}}{\partial x_{3}} \\
e_{22} = \frac{u}{H_{1}H_{2}} \frac{\partial H_{2}}{\partial x_{1}} + \frac{1}{H_{2}}\frac{\partial v}{\partial x_{2}} + \frac{w}{H_{2}H_{3}} \frac{\partial H_{2}}{\partial x_{3}} \\
e_{33} = \frac{u}{H_{1}H_{3}} \frac{\partial H_{3}}{\partial x_{1}} + \frac{v}{H_{2}H_{3}} \frac{\partial H_{3}}{\partial x_{2}} + \frac{1}{H_{3}}\frac{\partial w}{\partial x_{3}} \\
e_{12} = \frac{H_{1}}{H_{2}}\frac{\partial}{\partial x_{2}}\left(\frac{u}{H_{1}}\right) + \frac{H_{2}}{H_{1}}\frac{\partial}{\partial x_{1}}\left(\frac{v}{H_{2}}\right) \\
e_{13} = \frac{H_{1}}{H_{3}} \frac{\partial}{\partial x_{3}}\left(\frac{u}{H_{1}}\right) + \frac{H_{3}}{H_{1}} \frac{\partial}{\partial x_{1}}\left(\frac{w}{H_{3}}\right)\\
e_{23} = \frac{H_{2}}{H_{3}} \frac{\partial}{\partial x_{3}}\left(\frac{v}{H_{2}}\right) + \frac{H_{3}}{H_{2}} \frac{\partial}{\partial x_{2}}\left(\frac{w}{H_{3}}\right) \\
\omega_{1} = \frac{\frac{\partial (H_{3}w)}{\partial x_{2}} - \frac{\partial (H_{2}v)}{\partial x_{3}}}{2(H_{2}H_{3})} \\
\omega_{2} = \frac{\frac{\partial (H_{1}u)}{\partial x_{3}} - \frac{\partial (H_{3}w)}{\partial x_{1}}}{2(H_{1}H_{3})} \\
\omega_{3} = \frac{\frac{\partial (H_{2}v)}{\partial x_{1}} - \frac{\partial (H_{1}u)}{\partial x_{2}}}{2(H_{1}H_{2})} \\
H_{1} = \sqrt{(X_{1,x_{1}})^{2} + (X_{2,x_{1}})^{2} + (X_{3,x_{1}})^{2}} \\
H_{2} = \sqrt{(X_{1,x_{2}})^{2} + (X_{2,x_{2}})^{2} + (X_{3,x_{2}})^{2}} \\
H_{3} = \sqrt{(X_{1,x_{3}})^{2} + (X_{2,x_{3}})^{2} + (X_{3,x_{3}})^{2}}
\end{split}
\end{equation*}

## 3D kinematic equations for plates

Figure [](#fig:keplate-domain) shows the local and global coordinates of a plate.
```{figure} Introduction-plate-domain.*
:label:fig:keplate-domain
:width: 40%

Plate domain.
```

from where the following coordinate relations can be obtained:

\begin{equation*}
\begin{split}
x_{1} = x \quad X_{1} = x \\
x_{2} = y \quad X_{2} = y \\
x_{3} = z \quad X_{3} = z
\end{split}
\end{equation*}

Defining:

\begin{equation*}
\begin{split}
\varepsilon_{xx} = \epsilon_{11} \quad \gamma_{xy} = 2\varepsilon_{xy} = \epsilon_{12} \\
\varepsilon_{yy} = \epsilon_{22} \quad \gamma_{xz} = 2\varepsilon_{xz} = \epsilon_{13} \\
\varepsilon_{zz} = \epsilon_{33} \quad \gamma_{yz} = 2\varepsilon_{yz} = \epsilon_{23}
\end{split}
\end{equation*}


We have that:

\begin{equation*}
\begin{split}
\varepsilon_{xx} = u_{,x} + \frac{1}{2}(u_{,x}^{2} + v_{,x}^{2} + w_{,x}^{2}) \\
\varepsilon_{yy} = v_{,y} + \frac{1}{2}(u_{,y}^{2} + v_{,y}^{2} + w_{,y}^{2}) \\
\varepsilon_{zz} = w_{,z} + \frac{1}{2}(u_{,z}^{2} + v_{,z}^{2} + w_{,z}^{2}) \\
\gamma_{xy} = u_{,y} + v_{,x} + (u_{,x}u_{,y} + v_{,x}v_{,y} + w_{,x}w_{,y}) \\
\gamma_{xz} = u_{,z} + w_{,x} + (u_{,x}u_{,z} + v_{,x}v_{,z} + w_{,x}w_{,z}) \\
\gamma_{yz} = v_{,z} + w_{,y} + (u_{,y}u_{,z} + v_{,y}v_{,z} + w_{,y}w_{,z})
\end{split}
\end{equation*}

## 3D kinematic equations for cylindrical shells

Figure [](#fig:cylinder-domain) shows the local and global coordinates of a cylindrical shell.

```{figure} KinematicEquations-cylinder.*
:label:fig:cylinder-domain
:width: 40%

Cylindrical shell domain.
```

from where the following geometric relations can be derived [@CastroPhD]:

\begin{equation*}
\begin{split}
x_{1} = x \quad X_{1} = R(z) \cos(\theta) \\
x_{2} = \theta \quad X_{2} = R(z) \sin(\theta) \\
x_{3} = z \quad X_{3} = -x
\end{split}
\end{equation*}

Defining:

\begin{equation*}
\begin{split}
\varepsilon_{xx} = \epsilon_{11} \quad \gamma_{x\theta} = 2\varepsilon_{x\theta} = \epsilon_{12} \\
\varepsilon_{\theta\theta} = \epsilon_{22} \quad \gamma_{xz} = 2\varepsilon_{xz} = \epsilon_{13} \\
\varepsilon_{zz} = \epsilon_{33} \quad \gamma_{\theta z} = 2\varepsilon_{\theta z} = \epsilon_{23}
\end{split}
\end{equation*}

we have that, **considering only the linear terms**:

\begin{equation*}
\begin{split}
\varepsilon_{xx} = u_{,x} \\
\varepsilon_{\theta\theta} = \frac{v_{,\theta}}{R(z)} + \frac{w}{R(z)} \\
\varepsilon_{zz} = w_{,z} \\
\gamma_{x\theta} = \frac{u_{,\theta}}{R(z)} + v_{,x} \\
\gamma_{xz} = u_{,z} + w_{,x} \\
\gamma_{\theta z} = v_{,z} + \frac{w_{,\theta}}{R(z)} - \frac{v}{R(z)}
\end{split}
\end{equation*}

These equations represent the linear part of the strain-displacement relations (small strain/small displacement). The terms containing $R(z)$ in the denominators account for the curvature of the coordinate system. Specifically, the $\frac{w}{R(z)}$ term in $\varepsilon_{\theta\theta}$ represents the "hoop strain" contribution from radial displacement. 

## 3D kinematic equations for conical shells

Figure [](#fig:cone-domain) shows the local and global coordinates of a conical shell, adapted from Castro et al. [@Castro2014; @Castro2015; @Castro2015imperfect; @CastroPhD].

```{figure} KinematicEquations-cone.*
:label:fig:cone-domain
:width: 40%

Conical shell domain.
```

from where the following geometric relations can be derived [@CastroPhD]:
\begin{equation*}
\begin{split}
x_{1} = x \quad X_{1} = R(x, z) \cos \theta \\
x_{2} = \theta \quad X_{2} = R(x, z) \sin \theta \\
x_{3} = z \quad X_{3} = z \sin \alpha - x \cos \alpha \\
R(x,z) = R_2 + x \sin \alpha + z \cos \alpha
\end{split}
\end{equation*}

Defining:

\begin{equation*}
\begin{split}
\varepsilon_{xx} = \epsilon_{11} \quad \gamma_{x\theta} = 2\varepsilon_{x\theta} = \epsilon_{12} \\
\varepsilon_{\theta\theta} = \epsilon_{22} \quad \gamma_{xz} = 2\varepsilon_{xz} = \epsilon_{13} \\
\varepsilon_{zz} = \epsilon_{33} \quad \gamma_{\theta z} = 2\varepsilon_{\theta z} = \epsilon_{23}
\end{split}
\end{equation*}

we have that, **considering only the linear terms**:


\begin{equation*}
\begin{split}
\varepsilon_{xx} = u_{,x} \\
\varepsilon_{\theta\theta} = \frac{v_{,\theta}}{R(x, z)} + \frac{u \sin \alpha}{R(x, z)} + \frac{w \cos \alpha}{R(x, z)} \\
\varepsilon_{zz} = w_{,z} \\
\gamma_{x\theta} = \frac{u_{,\theta}}{R(x, z)} + v_{,x} - \frac{v \sin \alpha}{R(x, z)} \\
\gamma_{xz} = w_{,x} + u_{,z} \\
\gamma_{\theta z} = \frac{w_{,\theta}}{R(x, z)} + v_{,z} - \frac{v \cos \alpha}{R(x, z)}
\end{split}
\end{equation*}

The $\sin \alpha$ and $\cos \alpha$ terms represent the coupling between in-plane and out-of-plane displacements caused by the surface curvature and its slope.


## 3D kinematic equations for spherical shells

Figure [](#fig:sphere-domain) shows the local and global coordinates of a spherical shell.

```{figure} KinematicEquations-sphere.*
:label:fig:sphere-domain
:width: 40%

Spherical shell domain.
```

from where the following geometric relations can be derived:

\begin{equation*}
\begin{split}
x_{1} = \phi \quad X_{1} = R(z) \cos \phi \cos \theta \\
x_{2} = \theta \quad X_{2} = R(z) \sin \phi \cos \theta \\
x_{3} = z \quad X_{3} = R(z) \sin \theta \\
R(z) = r + z
\end{split}
\end{equation*}

where $\phi$ is the longitude, $\theta$ the latitude, and the radius $R$ is a function of the third coordinate $z$. Defining:
\begin{equation*}
\begin{split}
\varepsilon_{\phi\phi} = \epsilon_{11} \quad \gamma_{\phi\theta} = 2\varepsilon_{\phi\theta} = \epsilon_{12} \\
\varepsilon_{\theta\theta} = \epsilon_{22} \quad \gamma_{\phi z} = 2\varepsilon_{\phi z} = \epsilon_{13} \\
\varepsilon_{zz} = \epsilon_{33} \quad \gamma_{\theta z} = 2\varepsilon_{\theta z} = \epsilon_{23}
\end{split}
\end{equation*}

we have that, **considering only the linear terms**:
\begin{equation*}
\begin{split}
\varepsilon_{\phi\phi} = \frac{1}{R(z)} \left( \frac{u_{,\phi}}{\cos \theta} + w - v \tan \theta \right) \\
\varepsilon_{\theta\theta} = \frac{1}{R(z)} (v_{,\theta} + w) \\
\varepsilon_{zz} = w_{,z} \\
\gamma_{\phi\theta} = \frac{1}{R(z)} \left( u_{,\theta} + \frac{v_{,\phi}}{\cos \theta} + u \tan \theta \right) \\
\gamma_{\phi z} = \frac{1}{R(z)} \left( \frac{w_{,\phi}}{\cos \theta} - u \right) + u_{,z} \\
\gamma_{\theta z} = \frac{1}{R(z)} (w_{,\theta} - v) + v_{,z}
\end{split}
\end{equation*}

The $1/\cos \theta$ and $\tan \theta$ terms arise from the curvature of the spherical surface, representing how the differential arc length changes with latitude. The presence of $w$ (radial displacement) in both $\varepsilon_{\phi\phi}$ and $\varepsilon_{\theta\theta}$ is characteristic of shell theories where normal expansion or contraction directly contributes to the in-plane strains.

## Equivalent single-layer theories

When analyzing structures, full discretization over the thickness using 3D kinematics presents several significant challenges:

* **Mesh aspect-ratio issues:** 3 to 5 first-order elements are typically needed through the thickness to capture correct bending behavior, leading to heavily distorted elements in thin structures.
* **Poor conditioning of stiffness matrix:** The conditioning scales with $E h^2$ for bending and $E t$ for membrane actions, leading to numerical instabilities.
* **Computational expense:** There is a remarkably high computational cost for laminated composite materials that feature multiple layers.
* **Boundary conditions:** Application of simply supported boundary conditions in analytical or semi-analytical models becomes highly complex.

Consequently, for thin-walled structures, utilizing strictly 3D approaches is inefficient because no prior knowledge about the deformation kinematics is embedded into the strain-displacement relations.

## Typical Kinematic Theories Applied for Composite Plates

Most of the analyses performed on composite plates are based on one of the following approaches [@Reddy2004]:

* **Equivalent single-layer (ESL) theories (2-D)**
* Classical laminated plate theory
* Shear deformation laminated plate theories


* **Three-dimensional elasticity theory (3-D)**
* Traditional 3-D elasticity formulations


* **Layer-wise theories**

Among the ESL theories, the **First-order Shear Deformation Theory (FSDT)**, especially when including transverse extensibility ($\varepsilon_{zz} \neq 0$), provides the best compromise solution between accuracy, economy, and simplicity.

## Equivalent Single-Layer for Shells: Mathematical Illustration

To enable ESL kinematics, the 3D domain integration must be reduced to a 2D domain integration, as illustrated in Figure [](#fig:ESL) [@CastroPhD].

```{figure} KinematicEquations-ESL.*
:label:fig:ESL
:width: 40%

Shallow shell assumption $r>>h$ [@CastroPhD].
```

Given a function $f(x, \theta, z)$, its integral over the 3-D domain $\mathcal{V}$ can be expressed as [@CastroPhD]:

$$\int_{\mathcal{V}} f(x, \theta, z) dV = \int_{r_{int}}^{r_{ext}} \int_{\Omega} f(x, \theta, z) R(x, z) d\Omega dr$$

Using substitutions based on cylindrical shell geometry:

* $d\Omega = d\theta dz$
* $R(x, z) = r + z$
* $dA = r d\Omega$
* $dr = dz$

The integral becomes:

$$\int_{\mathcal{V}} f(x, \theta, z) dV = \int_{-\frac{h}{2}}^{\frac{h}{2}} \int_{\mathcal{A}} f(x, \theta, z) (r + z) \frac{dA}{R(x, z)} dz = \int_{-\frac{h}{2}}^{\frac{h}{2}} \int_{\mathcal{A}} f(x, \theta, z) \left(1 + \frac{z}{r}\right) dA dz \nonumber$$

### Applying the Shallow Shell Assumption

Applying the shallow shell theory assumption, where the radius is much larger than the thickness ($r \gg z$), results in:

$$\left(1 + \frac{z}{r}\right) \approx 1 \nonumber$$

$$(r + z) \approx r \nonumber$$

This simplification reduces the previous integral to:

$$\int_{\mathcal{V}} f(x, \theta, z) dV = \int_{-\frac{h}{2}}^{\frac{h}{2}} \int_{\mathcal{A}} f(x, \theta, z) d\mathcal{A} dz = \int_{z=-\frac{h}{2}}^{\frac{h}{2}} \int_{s=0}^{s=2\pi r} \int_{x=0}^{x=L} f(x, \theta, z) dx ds dz$$

This final equation forms the basis for reducing the 3-D domain to a 2-D domain, paving the way to integrate ESL kinematics efficiently.

## Main Equivalent Single-Layer (ESL) Theories

The main ESL theories make specific assumptions regarding the displacement field $(u, v, w)$ through the thickness coordinate $z$.

### Classical Laminated Plate Theory (CLPT)

An extension of the Classical Plate Theory to composite laminates (Kirchhoff-Love theory).

$$\begin{aligned}
u(x, y, z) &= u_0(x, y) - z\, w_{,x}(x, y) \\
v(x, y, z) &= v_0(x, y) - z\, w_{,y}(x, y) \\
w(x, y, z) &= w_0(x, y)
\end{aligned}$$

* **Assumptions:** Transverse normals remain straight after deformation (rigid cross-section). They do not experience elongation ($\varepsilon_{zz} = 0$) and remain perpendicular to the mid-surface after deformation, meaning no transverse shear strains ($\gamma_{xz} = \gamma_{yz} = 0$).

### First-order Shear Deformation Theory (FSDT)

Also known as Reissner-Mindlin theory.

$$\begin{aligned}
u(x, y, z) &= u_0(x, y) + z\, \phi_x(x, y) \\
v(x, y, z) &= v_0(x, y) + z\, \phi_y(x, y) \\
w(x, y, z) &= w_0(x, y)
\end{aligned}$$

* **Assumptions:** Rotations are disconnected from normal displacements ($\phi_x(x, y) \neq -w_{,x}(x, y)$). Transverse normals do not experience elongation ($\varepsilon_{zz} = 0$). Transverse shear strains $\gamma_{xz}$ and $\gamma_{yz}$ are constant through $z$. Therefore, **shear correction factors are needed**.

### Third-order Shear Deformation Theory (TSDT)

$$\begin{aligned}
u(x, y, z) &= u_0(x, y) + z \phi_x(x, y) + z^2 \psi_x(x, y) + z^3 \lambda_x(x, y) \\
v(x, y, z) &= v_0(x, y) + z \phi_y(x, y) + z^2 \psi_y(x, y) + z^3 \lambda_y(x, y) \\
w(x, y, z) &= w_0(x, y)
\end{aligned}$$

* **Assumptions:** Transverse normals do not experience elongation ($\varepsilon_{zz} = 0$). This kinematics allows for a parabolic distribution of transverse shear strains $\gamma_{xz}(x, y, z)$ and $\gamma_{yz}(x, y, z)$. Consequently, **shear correction factors are NOT needed**.

