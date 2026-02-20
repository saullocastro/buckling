# Static analysis

## Deflection of a plate using 3D elasticity

Using three-dimensional (3D) elasticity, the strain-displacement equations including van Kármán nonlinear terms can be written as:

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

$$\boldsymbol{K} = \iiint_{x,y,z} \boldsymbol{B}^T \boldsymbol{C} \boldsymbol{B} dx dy dz$$

The external force vector in this example includes only a point load $P$ at the center top surface of the plate:

$$\boldsymbol{F}_{ext} = P \boldsymbol{S}^w \Big|_{\substack{x=a/2 \\ y=b/2 \\ z=+h/2}}$$

Solution for the unknown Ritz coefficients:
$$\bar{\boldsymbol{u}} = \boldsymbol{K}^{-1} \boldsymbol{F}_{ext}$$

And the strain recovery becomes:
$$\boldsymbol{\varepsilon} = \boldsymbol{B} \bar{\boldsymbol{u}}$$

+++{"no-pdf":true}
An example of the 3D deflection of a plate can be seen in the following notebook: [](StaticAnalysis-deflection-plate-3D-elasticity.ipynb).
+++

+++{"no-html":true}
An example of the 3D deflection of a plate can be seen in the following notebook: [](https://colab.research.google.com/github/saullocastro/buckling/blob/main/content/StaticAnalysis-deflection-plate-3D-elasticity.ipynb).
+++



## Deflection of a plate using CLPT

Slide 68: Deflection of a plate, CLPT
See: ex/deflection_plate_CLPT.ipynb
Strain-displacement equations (CLPT with nonlinear terms):
$$\varepsilon_{xx} = u_{,x} - z w_{,xx} + \frac{1}{2}w_{,x}^2$$
$$\varepsilon_{yy} = v_{,y} - z w_{,yy} + \frac{1}{2}w_{,y}^2$$
$$\gamma_{xy} = u_{,y} + v_{,x} - 2z w_{,xy} + w_{,x} w_{,y}$$
Displacement field approximation (CLPT kinematics):
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
 
Slide 69: Deflection of a plate, CLPT
See: ex/deflection_plate_CLPT.ipynb
The stiffness matrix becomes, using the laminate constitutive matrices $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{D}$:
$$\boldsymbol{K} = \iint_{x,y} \left( \boldsymbol{B}_m^T \boldsymbol{A} \boldsymbol{B}_m \right) + \left( \boldsymbol{B}_b^T \boldsymbol{D} \boldsymbol{B}_b \right) + \left( \boldsymbol{B}_m^T \boldsymbol{B} \boldsymbol{B}_b \right) + \left( \boldsymbol{B}_b^T \boldsymbol{B} \boldsymbol{B}_m \right) dx dy$$
External force vector (point load $P$ at the midplane):
$$\boldsymbol{F}_{ext} = P \boldsymbol{S}^w \Big|_{\substack{x=a/2 \\ y=b/2}}$$
Solution for unknown coefficients:
$$\bar{\boldsymbol{u}} = \boldsymbol{K}^{-1} \boldsymbol{F}_{ext}$$
 
Would you like to examine the Python implementation of the Ritz method for either the 3D elasticity model or the CLPT model referenced in these slides?

