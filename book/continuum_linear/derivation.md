$\newcommand{\beps}{\boldsymbol\varepsilon}$
$\newcommand{\bsig}{\boldsymbol\sigma}$
$\newcommand{\ud}{d}$
$\newcommand{\us}{\mathrm{s}}$
$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bb}{\mathbf{b}}$
$\newcommand{\bc}{\mathbf{c}}$
$\newcommand{\bt}{\mathbf{t}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bw}{\mathbf{w}}$
$\newcommand{\bN}{\mathbf{N}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bD}{\mathbf{D}}$
$\newcommand{\bK}{\mathbf{K}}$
$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\iD}{\boldsymbol{\mathcal{D}}}$
$\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$

# From strong to discrete form

In this chapter, we will introduce finite element formulations for higher order continuum problems. We will focus on solid mechanics problems where the solution is a field in 2D (or 3D) space. This implies the elements and shape functions need to be different (e.g. triangular, quadrilateral, tetrahedral) from what we have seen for 1D problems.

## Preliminaries

We have already shown the finite element derivation for the [Poisson equation in 2D](../introduction/poisson2d.md). The most essential difference between the 2D Poisson equation and 2D continuum elasticity is that in elasticity, the unknown field is a vector field. When solving for displacements in 2D, there are 2 unknowns at every point $(x,y)$ in the domain: $u_x(x,y)$ and $u_y(x,y)$, unlike when solving for instance for temperature with the Poisson equation, where there is only one unknown at every point, i.e. a scalar field. Above, we have used $\bu$ for the degree of freedom vector, distinct from the scalar $u$ that was the unknown field. Now the unknown field is already a vector, so we keep the symbol $\bu$ for the displacement field

$$
\bu \equiv \begin{pmatrix} u_x \\ u_y \end{pmatrix}
$$

After discretization, it would make intuitive sense to have a degree of freedom matrix with the size of number of dimensions by number of nodes. However, it is more convenient to still collect the degrees of freedom in a vector. To avoid a conflict of notation, we will now use a different symbol for this degree of freedom vector, namely $\textbf{a}$. It collects all degrees of freedom as

$$
\ba \equiv \begin{pmatrix} a_{1x} \\ a_{1y} \\ a_{2x} \\ a_{2y} \\ \vdots \\ a_{nx} \\ a_{ny} \end{pmatrix}
$$

where $a_{ij}$ is the displacement at node $i$ in direction $j$. 



## Strong form equation

We have reached a strong form for the equilibrium equation in the {doc}`previous page<continuum_mechanics>`. Here we can briefly reitarate that result: 

$$
\nabla\cdot\bsig + \bb = \boldsymbol{0}
$$(equilibrium-strong)

where $\boldsymbol\sigma$ is the stress tensor, $\mathbf{b}$ is a vector with body forces. Equation {eq}`equilibrium-strong` is a vector equation of which each row stands for balance of linear momentum in one direction. We already make use of symmetry of the stress tensor, which follows from balance of angular momentum (otherwise, we would have had to write $\nabla\cdot\boldsymbol\sigma^T$). 

The equilibrium equation is complemented with a **constitutive relation** between stress and strain:

$$
\bsig = \iD : \beps
$$

Where $\iD$ is a fourth order stiffness tensor and $\boldsymbol\varepsilon$ is the strain tensor. The strain tensor is defined with the **kinematic equation**:

$$
\beps = \nabla^\mathrm{s} \bu
$$

where $\nabla^\us$ is the symmetric gradient operator $\nabla^\us\bu = \frac12(\nabla\bu + (\nabla\bu)^T)$. Substitution of the constitutive and kinematic equations in the equilibrium equation shows that the governing equation has second derivatives of $\bu$ with respect to spatial coordinates and reveals the similarity with the Poisson equation. In our derivation here, we refrain from making these substitutions for some time to keep the formulation general for nonlinear problems as well for some time. 

To formulate a complete problem boundary conditions are defined as:

$$
\bu = \bar{\bu},\quad \text{on} \quad \Gamma_D \\
\bsig\cdot\mathbf{n} = \bt,\quad \text{on} \quad \Gamma_N
$$

where $\bt$ is a boundary traction. In general, it is possible to define a Dirichlet condition on one component and a Neumann condition on another component at the same point on the boundary, so there should be a separate subdivision into $\Gamma_D$ and $\Gamma_N$ for $x$ and $y$ components. Such mixed boundary condition will be ignored for the derivation here and can be reintroduced quite naturally when boundary conditions are applied in the final finite element formulation. 

## Weak form

As Equation {eq}`equilibrium-strong` is a vector equation, we multiply it with a vector of test functions $\bw$ and integrate over the domain in the first step towards a weak form equation:

$$
-\int_\Omega \bw\cdot(\nabla\cdot\bsig)\,d\Omega = \int_\Omega \bw\cdot\bb\,d\Omega
$$

Divergence theorem and substitution of the Neumann boundary conditions gives the weak form equation:

$$
-\int_\Omega \nabla^\us\bw:\bsig\,d\Omega = \int_\Omega \bw\cdot\bb\,d\Omega + \int_{\Gamma_N} \bw\cdot\bt\,d\Gamma
$$

For the case of linear constitutive and kinematic relations, the weak form can be written in terms of $\bu$ as:

$$
-\int_\Omega \nabla^\us\bw:\iD:\nabla^\us\bu\,d\Omega = \int_\Omega \bw\cdot\bb\,d\Omega + \int_{\Gamma_N} \bw\cdot\bt\,d\Gamma
$$


## Discrete form

Instead of finding $\bu$ that satisfies the weak form equation $\forall\ \bw$, we introduce an approximation $\bu^h$ as a component wise interpolation with the shape functions: 

$$
\bu \approx \bu^h \quad\text{with}\quad u^h_x = \sum_j N_j a_{jx} \quad \text{and}\quad  u^h_y = \sum_j N_j a_{jy} 
$$

To compute the $\bu^h$ vector in a single operation, we define the $\bN$ matrix as

$$  
\textbf{N} = \begin{bmatrix}  
N_1  & 0 & N_2 &  0 &... & N_{n} & 0 \\
0 &  N_1 & 0 & N_2 & ...& 0 &  N_{n} \end{bmatrix}
$$

and employ the same approximation for $\bw$, resulting in

$$
\bu^h = \bN\ba \quad \text{and} \quad \bw^h = \bN\bc
$$

where $\ba$ is the vector with nodal degrees of freedom defined above and $\bc$ is a similar vector with nodal coefficients for the test function space. 

At this point, it is convenient to switch to Voigt notation for stresses and strains. The **constitutive equation** can then be recast as a matrix-vector multiplication

$$
\bsig = \bD\beps
$$

The strain is related to the nodal displacements with the $\bB$ matrix

$$ 
\beps = \bB\ba
$$ 

where for two-dimensional problems, the matrix $ \textbf{B} $ has the form:

$$ \textbf{B} = 
\begin{bmatrix} 
\frac{\partial{N_1}}{\partial{x}}  &  0 & \frac{\partial{N_2}}{\partial{x}} &  0 & ... &  \frac{N_{n}}{\partial{x}}& 0 \\
\
0 &   \frac{\partial{N_1}}{\partial{y}}   & 0 &  \frac{\partial{N_2}}{\partial{y}} & ... & 0 & \frac{\partial{N_{n}}}{\partial{y}}  \\
\
\frac{\partial{N_1}}{\partial{y}} &  \frac{\partial{N_1}}{\partial{x}} &\frac{\partial{N_2}}{\partial{y}} & \frac{\partial{N_2}}{\partial{x}}&... & \frac{\partial{N_{n}}}{\partial{y}} & \frac{N_{n}}{\partial{x}} \\
\end{bmatrix}
$$

Substituting $\bB\bc$ for $\nabla^\us\bw$ and $\bB\ba$ for $\nabla^\us\bu$ and adapting the product to Voigt notation ($\beps:\iD:\beps\ \rightarrow\ \beps^T\bD\beps$) gives the following expression for the discrete form: find $\ba$ such that

$$
\int_\Omega (\bB\bc)^T\bD\bB\ba\,\ud\Omega = \int_\Omega (\bN\bc)^T\bb\,\ud\Omega + \int_{\Gamma_N}(\bN\bc)^T\bt\,\ud\Gamma,\quad\forall\bc
$$

The coefficients $\bc$ take the place of the vector $\bw$ from the Poisson derivation and are again eliminated to arrive at a linear system of equations: 

$$
\mathbf{Ka} = \mathbf{f}
$$

with

$$
\bK = \int_\Omega \bB^T\bD\bB\,d\Omega
$$

and

$$
\mathbf{f} = \int_\Omega \bN^T\bb\,\ud\Omega + \int_{\Gamma_N}\bN^T\bt\,\ud\Gamma 
$$


```{admonition} Continuum elasticity in 3D
Again, the derivation in 3D is exactly the same as in 2D. The $\ba$-vector now has the length of three times the number of nodes and $\bN$ changes accordingly:

$$
\ba \equiv \begin{pmatrix} a_{1x} \\ a_{1y} \\ a_{1z} \\ a_{2x} \\ a_{2y} \\ a_{2z} \\ \vdots \\ a_{nx} \\ a_{ny} \\ a_{nz} \end{pmatrix}
\quad
\bN = \myMat{
N_1 & 0   & 0   & N_2 & 0   & 0   & ... & N_n & 0   & 0\\
0   & N_1 & 0   & 0   & N_2 & 0   & ... & 0   & N_n & 0\\
0   & 0   & N_1 & 0   & 0   & N_2 & ... & 0   & 0   & N_n\\
}
$$

The $3\times3$ strain tensor is in Voigt notation made into a vector as

$$
\beps = \begin{pmatrix} \varepsilon_{xx} & \varepsilon_{yy} & \varepsilon_{zz} & \gamma_{xy} & \gamma_{yz} & \gamma_{zx} \end{pmatrix}^T
$$

Consequently, the $\bB$-matrix becomes

$$ \textbf{B} = 
\begin{bmatrix} 
\frac{\partial{N_1}}{\partial{x}}  &  0 & 0 & \frac{\partial{N_2}}{\partial{x}} &  0 & 0 &  ... &  \frac{N_{n}}{\partial{x}}& 0 & 0 \\
0 &   \frac{\partial{N_1}}{\partial{y}}   & 0& 0 &  \frac{\partial{N_2}}{\partial{y}} & 0& ... & 0 & \frac{\partial{N_{n}}}{\partial{y}} & 0  \\
0 & 0 &  \frac{\partial{N_1}}{\partial{z}}   & 0 & 0 &  \frac{\partial{N_2}}{\partial{y}} & ... & 0 & 0 & \frac{\partial{N_{n}}}{\partial{y}} \\
\frac{\partial{N_1}}{\partial{y}} &  \frac{\partial{N_1}}{\partial{x}}  & 0 & \frac{\partial{N_2}}{\partial{y}} & \frac{\partial{N_2}}{\partial{x}} & 0 & ... & \frac{\partial{N_{n}}}{\partial{y}} & \frac{N_{n}}{\partial{x}} & 0  \\
0 & \frac{\partial{N_1}}{\partial{z}} &  \frac{\partial{N_1}}{\partial{y}}  & 0 & \frac{\partial{N_2}}{\partial{z}} & \frac{\partial{N_2}}{\partial{y}} & ... & 0 & \frac{\partial{N_{n}}}{\partial{z}} & \frac{N_{n}}{\partial{y}}  \\
\frac{\partial{N_1}}{\partial{z}} & 0 &  \frac{\partial{N_1}}{\partial{x}}  & \frac{\partial{N_2}}{\partial{z}} & 0 & \frac{\partial{N_2}}{\partial{x}}& ... & \frac{\partial{N_{n}}}{\partial{z}} & 0 & \frac{N_{n}}{\partial{x}}  \\
\end{bmatrix}
$$




```

