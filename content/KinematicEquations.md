# Strain-displacement (kinematic) equations for plates, cylindrical and spherical shells

## General strain-displacement relations

According to the three-dimensional (3D) elasticity theory, the strain components referred to an arbitrary orthogonal coordinate system $x_1$,$x_2$, $x_3$, illustrated in [](#fig:kestress-3D)

```{figure} Introduction-stress-3D.*
:label: fig:kestress-3D
:width: 50%

Complete stress state of a material point.
```

can be written as (@CastroPhD): 

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

Three-dimensional plate domain.
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

Three-dimensional cylindrical shell domain.
```

from where the following geometric relations can be derived:

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
\tau_{x\theta} = \frac{u_{,\theta}}{R(z)} + v_{,x} \\
\tau_{xz} = u_{,z} + w_{,x} \\
\tau_{\theta z} = v_{,z} + \frac{w_{,\theta}}{R(z)} - \frac{v}{R(z)}
\end{split}
\end{equation*}


## 3D kinematic equations for conical shells

## 3D kinematic equations for spherical shells