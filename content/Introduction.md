---
abstract: |
    In this demo, we demonstrate how Jupyter Book can be used to create and publish a content rich paper that includes 
    interactive elements such as code cells, visualizations, and multimedia. We will walk through the process of setting 
    up a Jupyter Book, adding content, and deploying the final product online.
---

# Introduction

Semi-analytical methods for buckling and post-buckling analysis.

The presence of the bending-twisting coupling terms ($D_{16}$ and $D_{26}$) complicates the analytical resolution of the governing differential equation for the out-of-plane displacement $w$ of a symmetric composite plate subjected to in-plane load resultants ($N_x, N_y, N_{xy}$) [@Kassapoglou2013]:

$$D_{11}\frac{\partial^4 w}{\partial x^4} + 4D_{16}\frac{\partial^4 w}{\partial x^3 \partial y} + 2(D_{12} + 2D_{66})\frac{\partial^4 w}{\partial x^2 \partial y^2} + 4D_{26}\frac{\partial^4 w}{\partial x \partial y^3} + D_{22}\frac{\partial^4 w}{\partial y^4} = N_x\frac{\partial^2 w}{\partial x^2} + N_y\frac{\partial^2 w}{\partial y^2} + 2N_{xy}\frac{\partial^2 w}{\partial x \partial y}$$

When the bending-twisting coupling terms $D_{16}$ and $D_{26}$ are large, or if the boundary conditions are different than simply-supported, or if the load resultants $N_x$, $N_y$ or $N_{xy}$ are non-constant; the buckled mode shape will skew, and exact closed-form solutions using orthogonal Fourier series become intractable, requiring energy methods or finite element discretizations. This section will mainly focus on solutions based on energy methods.

The web version of this chapter is available online at:
[https://saullocastro.github.io/buckling/](https://saullocastro.github.io/buckling/)

+++{"no-pdf":true}
This is a Jupyter Book built using the MyST engine [@Jupyter2025], which allows to export content in multiple output formats including HTML, PDF and docx.
+++

## Background
Some background information about Jupyter Book and its features, like exporting to multiple formats as indicated in {numref}`fig-diagram`.

```{figure} ../figures/diagram.*
:label: fig-diagram
:alt: Some figure

Some figure
```


+++{"no-pdf":true}
```{figure} ../figures/delft.*
:label: fig-delft
:alt: picture of the TUD

A figure that is in the website but not in the PDF version.
```
+++
