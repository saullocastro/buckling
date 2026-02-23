# Static analysis

## Deflection of a plate using 3D elasticity


```{figure} StaticAnalysis-plate-point-load.*
:label:fig:plate-point-load
:width: 40%

Plate with a point load at the centre.
```

Using three-dimensional (3D) elasticity, the strain-displacement equations including van Kármán non-linear terms can be written as:

$$\varepsilon_{xx} = u_{,x} + \frac{1}{2}w_{,x}^2$$
$$\varepsilon_{yy} = v_{,y} + \frac{1}{2}w_{,y}^2$$
$$\varepsilon_{zz} = w_{,z} + \frac{1}{2}w_{,z}^2$$
$$\gamma_{xy} = u_{,y} + v_{,x} + w_{,x} w_{,y}$$
$$\gamma_{xz} = u_{,z} + w_{,x} + w_{,x} w_{,z}$$
$$\gamma_{yz} = v_{,z} + w_{,y} + w_{,y} w_{,z}$$

The displacement field consists of:
$$u(x,y,z)$$
$$v(x,y,z)$$
$$w(x,y,z)$$

Using the Ritz method:
$$u(x,y,z) = \boldsymbol{S}^u \bar{\boldsymbol{u}}$$
$$v(x,y,z) = \boldsymbol{S}^v \bar{\boldsymbol{u}}$$
$$w(x,y,z) = \boldsymbol{S}^w \bar{\boldsymbol{u}}$$

The linear strains become:
$$\varepsilon_{xx} = \boldsymbol{S}^u_{,x} \bar{\boldsymbol{u}}$$
$$\varepsilon_{yy} = \boldsymbol{S}^v_{,y} \bar{\boldsymbol{u}}$$
$$\gamma_{xy} = \boldsymbol{S}^u_{,y} + \boldsymbol{S}^v_{,x} \bar{\boldsymbol{u}}$$
$$\boldsymbol{\varepsilon} = \boldsymbol{B} \bar{\boldsymbol{u}}$$
 
The stiffness matrix becomes, using the 3D constitutive matrix $\boldsymbol{C}$:

$$\boldsymbol{K} = \iiint_{x,y,z} \boldsymbol{B}^\top \boldsymbol{C} \boldsymbol{B} dx dy dz$$

The external force vector in this example includes only a point load $P$ at the center top surface of the plate:

$$\boldsymbol{F}_{ext} = P \boldsymbol{S}^w \Big|_{\begin{matrix}x=a/2 \\ y=b/2 \\ z=+h/2\end{matrix}}$$

Solution for the unknown Ritz coefficients:
$$\bar{\boldsymbol{u}} = \boldsymbol{K}^{-1} \boldsymbol{F}_{ext}$$

And the strain recovery becomes:
$$\boldsymbol{\varepsilon} = \boldsymbol{B} \bar{\boldsymbol{u}}$$

An example of the 3D deflection of a plate can be seen in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/StaticAnalysis-deflection-plate-3D-elasticity.ipynb).

+++{"no-pdf":true}
This example is also available [through this documentation](StaticAnalysis-deflection-plate-3D-elasticity.ipynb).
+++

## Deflection of a plate using CLPT

The kinematic (strain-displacement) equations using the clasical laminated plate theory (CLPT), including van Kármán non-linear are:

$$\varepsilon_{xx} = u_{,x} - z w_{,xx} + \frac{1}{2}w_{,x}^2$$
$$\varepsilon_{yy} = v_{,y} - z w_{,yy} + \frac{1}{2}w_{,y}^2$$
$$\gamma_{xy} = u_{,y} + v_{,x} - 2z w_{,xy} + w_{,x} w_{,y}$$

In the CLPT, the rotation of the plate is assumed constant through the thickness and  field approximation (CLPT kinematics):
$$u(x,y,z) = u_0(x,y) - z w_{,x}(x,y)$$
$$v(x,y,z) = v_0(x,y) - z w_{,y}(x,y)$$
$$w(x,y,z) = w_0(x,y)$$

Using the Ritz method:

$$u(x,y,z) = (\boldsymbol{S}^u - z\boldsymbol{S}^w_{,x})\bar{\boldsymbol{u}}$$
$$v(x,y,z) = (\boldsymbol{S}^v - z\boldsymbol{S}^w_{,y})\bar{\boldsymbol{u}}$$
$$w(x,y) = \boldsymbol{S}^w \bar{\boldsymbol{u}}$$

The linear strains then become:
$$\varepsilon_{xx} = (\boldsymbol{S}^u_{,x} - z\boldsymbol{S}^w_{,xx})\bar{\boldsymbol{u}}$$
$$\varepsilon_{yy} = (\boldsymbol{S}^v_{,y} - z\boldsymbol{S}^w_{,yy})\bar{\boldsymbol{u}}$$
$$\gamma_{xy} = (\boldsymbol{S}^u_{,y} + \boldsymbol{S}^v_{,x} - 2z\boldsymbol{S}^w_{,xy})\bar{\boldsymbol{u}}$$

Matrix separation into membrane ($\boldsymbol{B}_m$) and bending ($\boldsymbol{B}_b$) operators:

$$\boldsymbol{\varepsilon} = \begin{Bmatrix} \varepsilon_{xx} \\ \varepsilon_{yy} \\ \gamma_{xy} \end{Bmatrix} = \left( \begin{bmatrix} \boldsymbol{S}^u_{,x} \\ \boldsymbol{S}^v_{,y} \\ \boldsymbol{S}^u_{,y} + \boldsymbol{S}^v_{,x} \end{bmatrix} + z \begin{bmatrix} -\boldsymbol{S}^w_{,xx} \\ -\boldsymbol{S}^w_{,yy} \\ -2\boldsymbol{S}^w_{,xy} \end{bmatrix} \right) \bar{\boldsymbol{u}}$$
$$\boldsymbol{\varepsilon} = (\boldsymbol{B}_m + z\boldsymbol{B}_b)\bar{\boldsymbol{u}}$$
 
The stiffness matrix becomes, using the laminate constitutive matrices $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{D}$:
$$\boldsymbol{K} = \iint_{x,y} \left( \boldsymbol{B}_m^\top \boldsymbol{A} \boldsymbol{B}_m \right) + \left( \boldsymbol{B}_b^\top \boldsymbol{D} \boldsymbol{B}_b \right) + \left( \boldsymbol{B}_m^\top \boldsymbol{B} \boldsymbol{B}_b \right) + \left( \boldsymbol{B}_b^\top \boldsymbol{B} \boldsymbol{B}_m \right) dx dy$$
External force vector (point load $P$ at the midplane):
$$\boldsymbol{F}_{ext} = P \boldsymbol{S}^w \Big|_{\begin{matrix}x=a/2 \\ y=b/2\end{matrix}}$$
Solution for unknown coefficients:
$$\bar{\boldsymbol{u}} = \boldsymbol{K}^{-1} \boldsymbol{F}_{ext}$$
 
An example of the deflection of a plate using the CLPT can be seen in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/StaticAnalysis-deflection-plate-CLPT.ipynb).
+++{"no-pdf":true}
This example is also available [through this documentation](StaticAnalysis-deflection-plate-CLPT.ipynb).
+++

## Deflection of a plate using FSDT

For the first-order shear deformation theory (FSDT), the rotations of the displacement field approximation are decoupled from the gradients of $w$ by creating two independent field variables $\phi_x$ and $\phi_y$:

$$u(x,y,z) = u_0(x,y) + z \phi_x(x,y)$$
$$v(x,y,z) = v_0(x,y) + z \phi_y(x,y)$$
$$w(x,y,z) = w(x,y)$$

Using the Ritz method:
$$u(x,y,z) = (\boldsymbol{S}^u + z\boldsymbol{S}^{\phi_x})\bar{\boldsymbol{u}}$$
$$v(x,y,z) = (\boldsymbol{S}^v + z\boldsymbol{S}^{\phi_y})\bar{\boldsymbol{u}}$$
$$w(x,y) = \boldsymbol{S}^w \bar{\boldsymbol{u}}$$

The kinematic (strain-displacement) equations for the FSDT, including van Kármán non-linear are:

$$\varepsilon_{xx} = u_{,x} + z \phi_{x,x} + \frac{1}{2}w_{,x}^2$$
$$\varepsilon_{yy} = v_{,y} + z \phi_{y,y} + \frac{1}{2}w_{,y}^2$$
$$\gamma_{xy} = u_{,y} + v_{,x} + z\phi_{x,y} + z\phi_{y,x} + w_{,x} w_{,y}$$
$$\gamma_{xz} = \phi_x + w_{,x}$$
$$\gamma_{yz} = \phi_y + w_{,y}$$

The linear strains terms are:
$$\varepsilon_{xx} = (\boldsymbol{S}^u_{,x} + z\boldsymbol{S}^{\phi_x}_{,x})\bar{\boldsymbol{u}}$$
$$\varepsilon_{yy} = (\boldsymbol{S}^v_{,y} + z\boldsymbol{S}^{\phi_y}_{,y})\bar{\boldsymbol{u}}$$
$$\gamma_{xy} = (\boldsymbol{S}^u_{,y} + \boldsymbol{S}^v_{,x} + z\boldsymbol{S}^{\phi_x}_{,y} + z\boldsymbol{S}^{\phi_y}_{,x})\bar{\boldsymbol{u}}$$
$$\gamma_{yz} = (\boldsymbol{S}^{\phi_y} + \boldsymbol{S}^w_{,y})\bar{\boldsymbol{u}}$$
$$\gamma_{xz} = (\boldsymbol{S}^{\phi_x} + \boldsymbol{S}^w_{,x})\bar{\boldsymbol{u}}$$
 
Stress resultant operator definitions:

$$\boldsymbol{B}^N = \boldsymbol{A} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + \boldsymbol{B} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix}$$

$$\boldsymbol{B}^M = \boldsymbol{B} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + \boldsymbol{D} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix}$$

$$\boldsymbol{B}^Q = \boldsymbol{A} \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(0)}} \end{Bmatrix}$$

For the FSDT, the variation of the strain energy is:

$$\delta U = \iint_{xy} \left( \boldsymbol{N}^\top \begin{Bmatrix} \delta \varepsilon_{xx}^{(0)} \\ \delta \varepsilon_{yy}^{(0)} \\ \delta \gamma_{xy}^{(0)} \end{Bmatrix} + \boldsymbol{M}^\top \begin{Bmatrix} \delta \varepsilon_{xx}^{(1)} \\ \delta \varepsilon_{yy}^{(1)} \\ \delta \gamma_{xy}^{(1)} \end{Bmatrix} + \boldsymbol{Q}^\top \begin{Bmatrix} \delta \gamma_{yz}^{(0)} \\ \delta \gamma_{xz}^{(0)} \end{Bmatrix} \right) dx dy$$

Such that the stiffness matrix becomes, using the laminate constitutive matrices $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{D}$:
$$\boldsymbol{K} = \iint_{xy} \left( {\boldsymbol{B}^N}^\top \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + {\boldsymbol{B}^M}^\top \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix} + {\boldsymbol{B}^Q}^\top \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(0)}} \end{Bmatrix} \right) dx dy$$

The external force vector is then defined as:
$$\boldsymbol{F}_{ext} = P \boldsymbol{S}^w \Big|_{\begin{matrix}x=a/2 \\ y=b/2\end{matrix}}$$

Which can be solved for the Ritz coefficients with:

$$\bar{\boldsymbol{u}} = \boldsymbol{K}^{-1} \boldsymbol{F}_{ext}$$

An example of the deflection of a plate using the FSDT can be seen in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/StaticAnalysis-deflection-plate-FSDT.ipynb).
+++{"no-pdf":true}
This example is also available [through this documentation](StaticAnalysis-deflection-plate-FSDT.ipynb).
+++

## Deflection of a plate using the TSDT

The third-order shear deformation theory enforces zero transverse shear stresses and strains at the plate faces, $z = -h/2$ and $z = +h/2$, leading to additional 4 equations that enable a third-order interpolation of displacements througth the thickness that results in a consistent second-order interpolation of transverse strains and stresses [@Reddy2003]. The following displacement field representation was proposed by Reddy:

$$u(x,y,z) = u_0(x,y) + z \phi_x(x,y) - \frac{4}{3h^2}z^3 \left( \phi_x(x,y) + w_{,x}(x,y) \right)$$
$$v(x,y,z) = v_0(x,y) + z \phi_y(x,y) - \frac{4}{3h^2}z^3 \left( \phi_y(x,y) + w_{,y}(x,y) \right)$$
$$w(x,y,z) = w(x,y)$$

Using the Ritz method:

$$u(x,y,z) = \left( \boldsymbol{S}^u + z\boldsymbol{S}^{\phi_x} + z^3\left(-\frac{4}{3h^2}\right) (\boldsymbol{S}^{\phi_x} + \boldsymbol{S}^w_{,x}) \right)\bar{\boldsymbol{u}}$$
$$v(x,y,z) = \left( \boldsymbol{S}^v + z\boldsymbol{S}^{\phi_y} + z^3\left(-\frac{4}{3h^2}\right) (\boldsymbol{S}^{\phi_y} + \boldsymbol{S}^w_{,y}) \right)\bar{\boldsymbol{u}}$$
$$w(x,y) = \boldsymbol{S}^w \bar{\boldsymbol{u}}$$

Strain-displacement equations, including van K\'arm\an non-linear terms:

$$\varepsilon_{xx} = u_{,x} + \frac{1}{2}w_{,x}^2 + z\phi_{x,x} + z^3\left(-\frac{4}{3h^2}\right) (\phi_{x,x} + w_{,xx})$$
$$\varepsilon_{yy} = v_{,y} + \frac{1}{2}w_{,y}^2 + z\phi_{y,y} + z^3\left(-\frac{4}{3h^2}\right) (\phi_{y,y} + w_{,yy})$$
$$\gamma_{xy} = u_{,y} + v_{,x} + w_{,x} w_{,y} + z\phi_{x,y} + z\phi_{y,x} + z^3\left(-\frac{4}{3h^2}\right) (\phi_{x,y} + \phi_{y,x} + 2w_{,xy})$$
$$\gamma_{xz} = \phi_x + w_{,x} + z^2\left(-\frac{4}{h^2}\right) (\phi_x + w_{,x})$$
$$\gamma_{yz} = \phi_y + w_{,y} + z^2\left(-\frac{4}{h^2}\right) (\phi_y + w_{,y})$$

The linear strains then become:
$$\varepsilon_{xx} = \left( \boldsymbol{S}^u_{,x} + z\boldsymbol{S}^{\phi_x}_{,x} + z^3\left(-\frac{4}{3h^2}\right) (\boldsymbol{S}^{\phi_x}_{,x} + \boldsymbol{S}^w_{,xx}) \right)\bar{\boldsymbol{u}}$$
$$\varepsilon_{yy} = \left( \boldsymbol{S}^v_{,y} + z\boldsymbol{S}^{\phi_y}_{,y} + z^3\left(-\frac{4}{3h^2}\right) (\boldsymbol{S}^{\phi_y}_{,y} + \boldsymbol{S}^w_{,yy}) \right)\bar{\boldsymbol{u}}$$
$$\gamma_{xy} = \left( \boldsymbol{S}^u_{,y} + \boldsymbol{S}^v_{,x} + z\boldsymbol{S}^{\phi_x}_{,y} + z\boldsymbol{S}^{\phi_y}_{,x} + z^3\left(-\frac{4}{3h^2}\right) (\boldsymbol{S}^{\phi_x}_{,y} + \boldsymbol{S}^{\phi_y}_{,x} + 2\boldsymbol{S}^w_{,xy}) \right)\bar{\boldsymbol{u}}$$
$$\gamma_{yz} = \left( \boldsymbol{S}^{\phi_y} + \boldsymbol{S}^w_{,y} + z^2\left(-\frac{4}{h^2}\right) (\boldsymbol{S}^{\phi_y} + \boldsymbol{S}^w_{,y}) \right)\bar{\boldsymbol{u}}$$
$$\gamma_{xz} = \left( \boldsymbol{S}^{\phi_x} + \boldsymbol{S}^w_{,x} + z^2\left(-\frac{4}{h^2}\right) (\boldsymbol{S}^{\phi_x} + \boldsymbol{S}^w_{,x}) \right)\bar{\boldsymbol{u}}$$
 
Stress resultant operator definitions:

$$\boldsymbol{B}^N = \boldsymbol{A} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + \boldsymbol{B} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix} + \boldsymbol{E} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(3)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(3)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(3)}} \end{Bmatrix}$$
$$\boldsymbol{B}^M = \boldsymbol{B} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + \boldsymbol{D} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix} + \boldsymbol{F} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(3)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(3)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(3)}} \end{Bmatrix}$$
$$\boldsymbol{B}^P = \boldsymbol{E} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + \boldsymbol{F} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix} + \boldsymbol{H} \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(3)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(3)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(3)}} \end{Bmatrix}$$
$$\boldsymbol{B}^Q = \boldsymbol{A} \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(0)}} \end{Bmatrix} + \boldsymbol{D} \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(2)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(2)}} \end{Bmatrix}$$
$$\boldsymbol{B}^R = \boldsymbol{D} \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(0)}} \end{Bmatrix} + \boldsymbol{F} \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(2)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(2)}} \end{Bmatrix}$$

For the TSDT, the variation of the strain energy is:
$$\delta U = \iint_{xy} \left( \boldsymbol{N}^\top \begin{Bmatrix} \delta\varepsilon_{xx}^{(0)} \\ \delta\varepsilon_{yy}^{(0)} \\ \delta\gamma_{xy}^{(0)} \end{Bmatrix} + \boldsymbol{M}^\top \begin{Bmatrix} \delta\varepsilon_{xx}^{(1)} \\ \delta\varepsilon_{yy}^{(1)} \\ \delta\gamma_{xy}^{(1)} \end{Bmatrix} + \boldsymbol{P}^\top \begin{Bmatrix} \delta\varepsilon_{xx}^{(3)} \\ \delta\varepsilon_{yy}^{(3)} \\ \delta\gamma_{xy}^{(3)} \end{Bmatrix} + \boldsymbol{Q}^\top \begin{Bmatrix} \delta\gamma_{yz}^{(0)} \\ \delta\gamma_{xz}^{(0)} \end{Bmatrix} + \boldsymbol{R}^\top \begin{Bmatrix} \delta\gamma_{yz}^{(2)} \\ \delta\gamma_{xz}^{(2)} \end{Bmatrix} \right) dx dy$$

Such that the stiffness matrix becomes, using the laminate constitutive matrices $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{D}, \boldsymbol{E}, \boldsymbol{F}, \boldsymbol{G}$:
$$\boldsymbol{K} = \iint_{xy} \left( {\boldsymbol{B}^N}^\top \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(0)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(0)}} \end{Bmatrix} + {\boldsymbol{B}^M}^\top \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(1)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(1)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(1)}} \end{Bmatrix} + {\boldsymbol{B}^P}^\top \begin{Bmatrix} \boldsymbol{B}^{\varepsilon_{xx}^{(3)}} \\ \boldsymbol{B}^{\varepsilon_{yy}^{(3)}} \\ \boldsymbol{B}^{\gamma_{xy}^{(3)}} \end{Bmatrix} + {\boldsymbol{B}^Q}^\top \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(0)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(0)}} \end{Bmatrix} + {\boldsymbol{B}^R}^\top \begin{Bmatrix} \boldsymbol{B}^{\gamma_{yz}^{(2)}} \\ \boldsymbol{B}^{\gamma_{xz}^{(2)}} \end{Bmatrix} \right) dx dy$$

External force vector:
$$\boldsymbol{F}_{ext} = P \boldsymbol{S}^w \Big|_{\substack{x=a/2 \\ y=b/2}}$$

Which can be solved for the Ritz coefficients:
$$\bar{\boldsymbol{u}} = \boldsymbol{K}^{-1} \boldsymbol{F}_{ext}$$

An example of the deflection of a plate using the TSDT can be seen in [this notebook](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/StaticAnalysis-deflection-plate-TSDT.ipynb).
+++{"no-pdf":true}
This example is also available [through this documentation](StaticAnalysis-deflection-plate-TSDT.ipynb).
+++