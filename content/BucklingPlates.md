# Buckling of plates with general boundary conditions

The classical solution for the deflection of a simply-supported plate of length $a$ and width $b$ is:

$$w = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{mn} \sin\left(\frac{m \pi x}{a}\right) \sin\left(\frac{n \pi y}{b}\right)$$

However, when a general set of boundary conditions is needed, a more robust approximation for the displacement field is required. Castro and Donadon [@CastroDonadon2017] present Rodrigues' form of Legendre hierarchic orthogonal polynomials [@Peano1976hierarchies] [@DeChao1986], largely applied by Bardell et al. on the vibration problems [@Bardell1991plate] [@Bardell1997shellfree] [@Bardell1997shell]. In this form the first four terms $i = 1,2,3,4$ consist of Hermite cubic polynomials:

$$s_{i=1}(\xi \text{ or } \eta) = \left(\frac{1}{2} - \frac{3}{4}\xi + \frac{1}{4}\xi^3\right) \delta_{t1}

$$s_{i=2}(\xi \text{ or } \eta) = \left(\frac{1}{8} - \frac{1}{8}\xi - \frac{1}{8}\xi^2 + \frac{1}{8}\xi^3\right) \delta_{r1}$$
$$s_{i=3}(\xi \text{ or } \eta) = \left(\frac{1}{2} + \frac{3}{4}\xi - \frac{1}{4}\xi^3\right) \delta_{t2}$$
$$s_{i=4}(\xi \text{ or } \eta) &= \left(-\frac{1}{8} - \frac{1}{8}\xi + \frac{1}{8}\xi^2 + \frac{1}{8}\xi^3\right) \delta_{r2}$$

where $\delta_{t1}$, $\delta_{r1}$, $\delta_{t2}$ and $\delta_{r2}$ are binary flags equal to $0$ or $1$. Using these flags the first four terms of Rodrigues polynomials can be used to enable/disable the translation and rotation of each domain boundary. Flag $\delta_{t1}$ is used to control the translation at boundary 1 ($\xi = -1$), which is possible because using Rodrigues polynomials this is the only term among all terms in the approximation function that produces $s_i(\xi = -1) = 1$. Similarly, $\delta_{t2}$ is used to control the translation at boundary 2 ($\xi = +1$). The rotation at $\xi = -1$ and $\xi = +1$ is respectively controlled using $\delta_{r1}$ and $\delta_{r2}$, since they are the only terms that produce a non-null rotation $\partial s / \partial \xi$ at each respective domain boundary. 

```{figure} BucklingPlates-Legendre-BC.jpg
:alt: Legendre polynomial boundary functions
:width: 50%

Legendre polynomial boundary functions
```

```{figure} BucklingPlates-Legendre-inner.jpg
:alt: Legendre inner functions
:width: 50%

Legendre polynomial inner functions
```

Vescovini et al. [@Vescovini2018shapefunctions] investigated the sparsity of the systems produced by different shape functions, positively supporting the use of Legendre hierarchical polynomials.