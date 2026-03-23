---
numbering:
  headings: false
---

```{raw} latex
\setcounter{secnumdepth}{0}
```

# Preface

This book is a successful attempt to organise all material I have concerning semi-analytical modelling, consisting of a self-contained theoretical and practical reference for young and experienced engineers and scienties. It covers topics from linear static analysis using classical formulation to deep post-buckling analysis using third-order shear deformation theory.

You will see that my focus is on displacement-based semi-analytical methods, but some special attention is given to hybrid methods approximating both the displacement and stresses, which clealry show to be advantageous for post-buckling, especially when using perturbation-based methods, such as the Koiter method.

The book is in constant development and the plan is to have one yearly official release.

## Why do you call this semi-analytical instead of numerical?

In a purely numerical approach, such as finite elements (FE) (TODO reference), smoothed particle hydrodynamics (SPH) (TODO reference) and so forth, the domain is approximated using functions of a chosen order that have local support. For instance, a quadrilateral 4-node FE usually approximates the displacements and rotations linearly between nodes. In SPH, usually cubic- or quintic-splines are used to interpolate material-point field variables that are stored in each particle. From ththese interpolation schemes, such as FE or SPH, one can numerically solve for the displacement fields, statically or dynamically.

However, in semi-analytical methods the domain is solved with kinematic equations (strain-displacement relations) that are usually exact for a specific geometry, which is usually a plate or a shell, by means of approximation functions that pertain to the entire domain, hence having global support. This global support means that, if the systems is integrated numerically, every integration point affects all degrees-of-freedom of the corresponding domain. This is contrastingly different than FE or SPH methods, whereby an integration point only affects the corresponding local support. The "semi-" from "semi-analytical" can come from numerically integrating the domain, which is needed in non-linear analysis or on systems with arbitrarily variable stiffness or variable inertia, or it can come from the solution step, which is faster when done numerically than analytically for larger-rank systems.


## Why should you learn about semi-analytical modelling?

The simplest buckling case consists of the classical solution for the deflection $w$ of a plate with length $a$, width $b$ and thickness $h$, under in-plane distributed loads ($N_x$, $N_y$, $N_{xy}$). The governing equation for this problem is given below
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

Even for this simple case, the presence of the bending-twisting coupling terms ($D_{16}$ and $D_{26}$); or the laminate being not symmetric $\boldsymbol{B} \neq 0$; or boundary conditions combining, clamped, simply-supported and free edges; or if the distributed in-plane loads $N_x$, $N_y$ or $N_{xy}$ are non-constant; the buckled mode shape will skew such that the exact closed-form solutions, for instance using orthogonal Fourier series, will become intractable, requiring semi-analytical methods or finite element discretizations. 

## PDF and web version

The web version of the Buckling Handbook is available online at:
[https://saullocastro.github.io/buckling/](https://saullocastro.github.io/buckling/).

The GitHub repository is available online at:
[https://github.com/saullocastro/buckling/](https://github.com/saullocastro/buckling/).

```{raw} latex
\setcounter{secnumdepth}{3}
```