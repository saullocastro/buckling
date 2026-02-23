# Buckling of plates with general boundary conditions

## Geometric stiffness

### Geometric stiffness for beams

Using the full nonlinear Green-Lagrange strain relation, the axial strain of a beam can be written as:

$$\varepsilon_{xx} = \frac{\partial u}{\partial x} + \frac{1}{2} \left[ \left(\frac{\partial u}{\partial x}\right)^2 + \left(\frac{\partial v}{\partial x}\right)^2 + \left(\frac{\partial w}{\partial x}\right)^2 \right]$$

The first variation becomes, using $\partial(\cdot)/\partial x = (\cdot)_{,x}$
$$\delta \varepsilon_{xx} = \delta u_{,x} + u_{,x}\delta u_{,x} + v_{,x}\delta v_{,x} + w_{,x}\delta w_{,x}$$

In terms of nodal displacements (or Ritz coefficients) $\boldsymbol{\bar{u}}$:
$$\delta \varepsilon_{xx} = \boldsymbol{\bar{B}} \delta \boldsymbol{\bar{u}} = (\boldsymbol{B}_L + \boldsymbol{B}_{NL}) \delta \boldsymbol{\bar{u}}$$
with:

$$\boldsymbol{B}_L = \frac{\partial \boldsymbol{S}^u}{\partial x} \qquad \boldsymbol{B}_{NL} = \frac{\partial u}{\partial x}\frac{\partial \boldsymbol{S}^u}{\partial x} + \frac{\partial v}{\partial x}\frac{\partial \boldsymbol{S}^v}{\partial x} + \frac{\partial w}{\partial x}\frac{\partial \boldsymbol{S}^w}{\partial x}$$

The second variation becomes:

$$\delta^2 \varepsilon_{xx} = \delta^2 u_{,x} + \delta u_{,x}\delta u_{,x} + u_{,x}\delta^2 u_{,x} + \delta v_{,x}\delta v_{,x} + v_{,x}\delta^2 v_{,x} + \delta w_{,x}\delta w_{,x} + w_{,x}\delta^2 w_{,x}$$

Note that $\delta^2(\cdot)_{,x} \ll \delta(\cdot)_{,x}$, leading to:

$$\delta^2 \varepsilon_{xx} = \delta u_{,x}\delta u_{,x} + \delta v_{,x}\delta v_{,x} + \delta w_{,x}\delta w_{,x}$$

with $\delta^2 \varepsilon_{xx}$ defined as:

$$\delta^2 \varepsilon_{xx} = \delta u_{,x}\delta u_{,x} + \delta v_{,x}\delta v_{,x} + \delta w_{,x}\delta w_{,x}$$

using the finite element (or Ritz method) shape functions:

$$\delta^2 \varepsilon_{xx} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right) + \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right) + \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) \right] \delta \boldsymbol{\bar{u}}$$

Then:

```{math}
\begin{aligned}
\delta \boldsymbol{\bar{u}}^\top \boldsymbol{K}_G \delta \boldsymbol{\bar{u}} &= \int_{\Omega} \hat{\sigma}_{xx}\delta^2 \varepsilon_{xx} \, d\Omega
\\
&= \delta \boldsymbol{\bar{u}}^\top \int_{\Omega} \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right) 
+ \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right) 
+ \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) d\Omega \, \delta \boldsymbol{\bar{u}}
\end{aligned}
```

$\hat{\sigma}_{xx}$ can be given or calculated from an initial nodal displacement state $\boldsymbol{\hat{u}}$ (pre-buckling of fundamental state):

$$\hat{\sigma}_{xx} = E \left( \boldsymbol{B}_L + \frac{1}{2}\boldsymbol{B}_{NL} \right) \boldsymbol{\hat{u}}$$



### Geometric stiffness for plates 

For plates, using the full nonlinear Green-Lagrange strain relation:

$$\varepsilon_{xx} = \frac{\partial u}{\partial x} + \frac{1}{2} \left[ \left(\frac{\partial u}{\partial x}\right)^2 + \left(\frac{\partial v}{\partial x}\right)^2 + \left(\frac{\partial w}{\partial x}\right)^2 \right]$$
$$\varepsilon_{yy} = \frac{\partial v}{\partial y} + \frac{1}{2} \left[ \left(\frac{\partial u}{\partial y}\right)^2 + \left(\frac{\partial v}{\partial y}\right)^2 + \left(\frac{\partial w}{\partial y}\right)^2 \right]$$
$$\gamma_{xy} = \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x} + \left( \frac{\partial u}{\partial x}\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}\frac{\partial v}{\partial y} + \frac{\partial w}{\partial x}\frac{\partial w}{\partial y} \right)$$

The first variation becomes, using $\partial(\cdot)/\partial x = (\cdot)_{,x}$:

```{math}
\begin{aligned}
\delta \varepsilon_{xx} &= \delta u_{,x} + u_{,x}\delta u_{,x} + v_{,x}\delta v_{,x} + w_{,x}\delta w_{,x}
\\
\delta \varepsilon_{yy} &= \delta v_{,y} + u_{,y}\delta u_{,y} + v_{,y}\delta v_{,y} + w_{,y}\delta w_{,y}
\\
\delta \gamma_{xy} &= \delta u_{,y} + \delta v_{,x} + \delta u_{,x}u_{,y} + u_{,x}\delta u_{,y} + \delta v_{,x}v_{,y} + v_{,x}\delta v_{,y} + \delta w_{,x}w_{,y} + w_{,x}\delta w_{,y}
\end{aligned}
```

The second variation becomes:

```{math}
\begin{aligned}
\delta^2 \varepsilon_{xx} &= \delta^2 u_{,x} + \delta u_{,x}\delta u_{,x} + u_{,x}\delta^2 u_{,x} + \delta v_{,x}\delta v_{,x} + v_{,x}\delta^2 v_{,x} + \delta w_{,x}\delta w_{,x} + w_{,x}\delta^2 w_{,x}
\\
\delta^2 \varepsilon_{yy} &= \delta^2 v_{,y} + \delta u_{,y}\delta u_{,y} + u_{,y}\delta^2 u_{,y} + \delta v_{,y}\delta v_{,y} + v_{,y}\delta^2 v_{,y} + \delta w_{,y}\delta w_{,y} + w_{,y}\delta^2 w_{,y}
\\
\delta^2 \gamma_{xy} &= \delta^2 u_{,y} + \delta^2 v_{,x} + \delta^2 u_{,x}u_{,y} + 2\delta u_{,x}\delta u_{,y} + u_{,x}\delta^2 u_{,y} 
\\
&+ \delta^2 v_{,x}v_{,y} + 2\delta v_{,x}\delta v_{,y} + v_{,x}\delta^2 v_{,y} + \delta^2 w_{,x}w_{,y} 
\\
&+ 2\delta w_{,x}\delta w_{,y} + w_{,x}\delta^2 w_{,y}
\end{aligned}
```

Note that $\delta^2(\cdot)_{,x} \ll \delta(\cdot)_{,x}$ and $\delta^2(\cdot)_{,y} \ll \delta(\cdot)_{,y}$, leading to:

$$\delta^2 \varepsilon_{xx} = \delta u_{,x}\delta u_{,x} + \delta v_{,x}\delta v_{,x} + \delta w_{,x}\delta w_{,x}$$
$$\delta^2 \varepsilon_{yy} = \delta u_{,y}\delta u_{,y} + \delta v_{,y}\delta v_{,y} + \delta w_{,y}\delta w_{,y}$$
$$\delta^2 \gamma_{xy} = 2\delta u_{,x}\delta u_{,y} + 2\delta v_{,x}\delta v_{,y} + 2\delta w_{,x}\delta w_{,y}$$

with $\delta^2 \boldsymbol{\varepsilon}$ defined as:
$$\delta^2 \varepsilon_{xx} = \delta u_{,x}\delta u_{,x} + \delta v_{,x}\delta v_{,x} + \delta w_{,x}\delta w_{,x}$$
$$\delta^2 \varepsilon_{yy} = \delta u_{,y}\delta u_{,y} + \delta v_{,y}\delta v_{,y} + \delta w_{,y}\delta w_{,y}$$
$$\delta^2 \gamma_{xy} = 2\delta u_{,x}\delta u_{,y} + 2\delta v_{,x}\delta v_{,y} + 2\delta w_{,x}\delta w_{,y}$$

using finite element or Ritz shape functions:

```{math}
\begin{gather}
\delta^2 \varepsilon_{xx} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right) + \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right) + \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) \right] \delta \boldsymbol{\bar{u}}
\\
\delta^2 \varepsilon_{yy} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right) + \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right) + \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right) \right] \delta \boldsymbol{\bar{u}}
\\
\delta^2 \gamma_{xy} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right) + \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)
\right.
\\
 + \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right) + \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)
 \\
 \left. + \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right) + \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) \right] \delta \boldsymbol{\bar{u}}
 \end{gather}
 ```

Then:

$$\delta \boldsymbol{\bar{u}}^\top \boldsymbol{K}_G \delta \boldsymbol{\bar{u}} = \delta \boldsymbol{\bar{u}}^\top \int_{\Omega} \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right) + \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right) + \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)$$

$$+ \hat{\sigma}_{yy} \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right) + \hat{\sigma}_{yy} \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right) + \hat{\sigma}_{yy} \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)$$

$$+ \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right) + \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^u}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^u}{\partial x}\right)$$
$$+ \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right) + \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^v}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^v}{\partial x}\right)$$
$$+ \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right) + \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) d\Omega \, \delta \boldsymbol{\bar{u}}$$

$\hat{\sigma}_{xx}, \hat{\sigma}_{yy}, \hat{\tau}_{xy}$ can be calculated for plate elements from an initial nodal displacement state $\boldsymbol{\hat{u}}$ (fundamental or pre-buckling state) as:

$$\begin{Bmatrix} \hat{\sigma}_{xx} \\ \hat{\sigma}_{yy} \\ \hat{\tau}_{xy} \end{Bmatrix} = \frac{1}{h} \begin{bmatrix} \boldsymbol{A} & \boldsymbol{B} \\ \boldsymbol{B} & \boldsymbol{D} \end{bmatrix} \left( \boldsymbol{B}_L + \frac{1}{2}\boldsymbol{B}_{NL} \right) \boldsymbol{\hat{u}}$$
 
applying the van K\'arm\'an simplifications, $\delta^2 \boldsymbol{\varepsilon}$ is defined as:

$$\delta^2 \varepsilon_{xx} = \delta w_{,x}\delta w_{,x}$$
$$\delta^2 \varepsilon_{yy} = \delta w_{,y}\delta w_{,y}$$
$$\delta^2 \gamma_{xy} = 2\delta w_{,x}\delta w_{,y}$$

using finite element or Ritz shape functions:

$$\delta^2 \varepsilon_{xx} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) \right] \delta \boldsymbol{\bar{u}}$$
$$\delta^2 \varepsilon_{yy} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right) \right] \delta \boldsymbol{\bar{u}}$$
$$\delta^2 \gamma_{xy} = \delta \boldsymbol{\bar{u}}^\top \left[ \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right) + \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) \right] \delta \boldsymbol{\bar{u}}$$

Then:

$$\delta \boldsymbol{\bar{u}}^\top \boldsymbol{K}_G \delta \boldsymbol{\bar{u}} = \delta \boldsymbol{\bar{u}}^\top \int_{\Omega} \hat{\sigma}_{xx} \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)$$
$$+ \hat{\sigma}_{yy} \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)$$
$$+ \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right) + \hat{\tau}_{xy} \left(\frac{\partial \boldsymbol{S}^w}{\partial y}\right)^\top \left(\frac{\partial \boldsymbol{S}^w}{\partial x}\right) d\Omega \, \delta \boldsymbol{\bar{u}}$$

$\hat{\sigma}_{xx}, \hat{\sigma}_{yy}, \hat{\tau}_{xy}$ can be calculated for plate elements from an initial nodal displacement state $\boldsymbol{\hat{u}}$ (fundamental or pre-buckling state) as:

$$\begin{Bmatrix} \hat{\sigma}_{xx} \\ \hat{\sigma}_{yy} \\ \hat{\tau}_{xy} \end{Bmatrix} = \frac{1}{h} \begin{bmatrix} \boldsymbol{A} & \boldsymbol{B} \\ \boldsymbol{B} & \boldsymbol{D} \end{bmatrix} \left( \boldsymbol{B}_L + \frac{1}{2}\boldsymbol{B}_{NL} \right) \boldsymbol{\hat{u}}$$
 

 

