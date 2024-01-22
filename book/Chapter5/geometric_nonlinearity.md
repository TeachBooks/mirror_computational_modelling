$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bN}{\mathbf{N}}$


# Geometrically nonlinear problems

So far in our discussions of the finite element method for applications in solid mechanics, we have dealt with geometrically linear formulation. Deformations, i.e. strain or other strain-like quantities like curvature, have been defined as a linear function of displacements (and, where applicable, rotations). In other words, the kinematic relation was linear. However, this is not always appropriate. Different sources of nonlinearity in kinematic relations can be distinguished. In this introductory section to geometrically nonlinear finite element formulations, the two main ones will be introduced:
- **large strains** as will be illustrated with a 1D rod
- **large displacements** (at small strains) as will be illustrated with a rod in 2D space 

In finite element literature, the word finite is often used instead of large, so **finite strain** and **finite displacement** approaches give rise to geometrically nonlinear finite element formulations. 

### Rod in 1D: finite strain versus small strain

In a 1D rod element, the strain has been defined as 

$$
\eps = \pder{u}{x}
$$(linear-strain)

In a finite element context, where we have $u(x)=\bN(x)\ba$, the linear dependence on $\ba$ is apparent in the linear operation 

$$
\eps = \bB\ba
$$

For a uniform deformation where a rod extends from initial length $L_0$ to current length $L$, Equation {eq}`linear-strain` is equivalent to 

$$
\eps = \frac{L-L_0}{L_0}
$$(engineering-strain)

Again, it is not hard to see that $L$ is linearly dependent on the axial displacements at both ends of the rod. 

However, other strain definitions exist. The strain measure from Equation {eq}`engineering-strain` is generally referred to as the **engineering strain**. An alternative measure is called the **true strain**:

$$
\eps = \ln\left(\frac{L}{L_0}\right)
$$(true-strain)

The engineering strain and true strain measures are in fact equivalent for small deformations: Equation {eq}`engineering-strain` is the first order Taylor approximation of Equation {eq}`true-strain` around $L=L_0$. 

For many engineering applications, deformations remains small, if only because many engineering materials cannot withstand large strains: they break at a strain of a few percent. However, even if the material does not deform much, nonlinear strain definitions can be significant. This is the case when rotations are significant for which we need to turn to higher dimensions. 

### Rod in 2D: finite displacements versus small displacements

Consider the same rod, initially aligned with a global $x$-axis, but now in 2D space. The ends of the rod can deform in $x$ and $y$ directions. Let's assume the rod is fixed at the left end ($u_x(0)=u_y(0)=0$) and there can be a displacement $\left(u_x(L),u_y(L)\right)$ at the right end. 

We assume the strain in the material remains small, so we adopt the engineering strain definition of Equation {eq}`engineering-strain`. As long as $u_y(L)=0$, the engineering strain gives a strain defintion that is linear in $u_x(L)$:

$$
L = L_0 + u_x(L) \quad\Rightarrow\quad \eps = \frac{u_x(L)}{L_0}
$$

However, if $u_x(L)$ and $u_y(L)$ are both allowed to take nonzero values, we get

$$
L = \sqrt{\left(L_0+u_x(L)\right)^2 + \left(u_y(L)\right)^2}
$$

Here, the engineering strain which is linear in $L$ becomes nonlinear in $u$ because of the nonlinear relation between $L$ and $u$. This nonlinearity exists no matter how big or small $\eps$ is. Of course, the resulting relation between the strain and the displacements can be linearized under the assumption that displacements are small, but it should be emphasized that this is an additional assumption on top of the small strain assumption.

## Geometrically nonlinear frame analysis



## Geometrically nonlinear continuum mechanics 

## Linear buckling analysis

## Hyperelasticity 

