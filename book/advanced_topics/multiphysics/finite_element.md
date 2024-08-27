## Finite Element implementation

### Discrete form

We need to solve for the additional equations brought in by the multiphysics couplings.
After deriving the strong form of the equation terms into their weak form, they need to be discretised.
The discrete form will as usual correspond to an equation of the type:

$$
\mathbf{K} \mathbf{a} = \mathbf{f}
$$

With $\mathbf{K}$ the stiffness matrix, $\mathbf{a}$ the solution vector and $\mathbf{f}$ the force vector.

Adding other physical variables to solve for through multiphysics processes will increase the number of degrees of freedom of the system, represented by the size of vector $\mathbf{a}$. Because each variable has to be solved for at every node. For a 1D thermo-mechanical problem solved on a mesh of X nodes, the number of degrees of freedom for the system will be 2X.
Since the size of $\mathbf{a}$ directly correlates to the size of the stiffness matrix we are solving for, multiphysics problems are generally more computationally heavy as they are trying to invert a larger stiffness matrix.

Multiphysics coupling terms, as shown for example in .., contribute in the off-diagonal part of the stiffness matrix. Let's see it for an example by deriving the discrete form of the Stokes flow equations. In its strong form, it is expressed as:

$$
\mu \nabla^2 \mathbf{v} -\nabla P = \mathbf{0} \\
\nabla \cdot \mathbf{v} = 0
$$

with the first equation being the conservation of momentum with the fluid velocity $\mathbf{v}$ as the primary variable and the second equation being the conservation of mass with the fluid pressure $P$ being the primary variable.

After introducing $\mathbf{w^v}$ and $\mathbf{w^p}$ are the test functions respectively for $\mathbf{v}$ and $P$, we can derive the weak form as:

$$
\int_\Omega \mu \nabla \mathbf{v} : \nabla \mathbf{w^v} \, d\Omega - \int_\Omega P \, (\nabla \cdot \mathbf{w^v}) \, d\Omega &= 0 \\
\int_\Omega \mathbf{w^p} \, (\nabla \cdot \mathbf{v}) \, d\Omega &= 0
$$

After discretising $\mathbf{v}$ and $P$ as

$$
\mathbf{v} \approx \sum_{i=1}^{n}N^v_{i}v_i \\
\mathbf{p} \approx \sum_{i=1}^{m}N^p_{i}P_i
$$

where $n$ are the number of degrees of freedom for $\mathbf{v}$ and $m$ for $P$, the discrete form can be derived as:

$$
\mathbf{A} \mathbf{v} - \mathbf{B}^T \mathbf{p} &= \mathbf{0} \\
\mathbf{B} \mathbf{v} &= \mathbf{0}
$$

where

$$
A_{ij} = \int_\Omega \mu \nabla \mathbf{N^v}_i : \nabla \mathbf{N^v}_j \, d\Omega \\
B_{ij} = \int_\Omega N^p_i \, (\nabla \cdot \mathbf{N^v}_j) \, d\Omega
$$

The system of equation can be rewritten in a matrix form, to make the stiffness matrix of the system appear

$$
\begin{bmatrix}
\mathbf{A} & \textcolor{red}{-\mathbf{B}^T} \\
\textcolor{red}{\mathbf{B}} & \mathbf{0}
\end{bmatrix}
\begin{bmatrix}
\mathbf{v} \\
\mathbf{p}
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{0} \\
\mathbf{0}
\end{bmatrix}
$$

In this form, we can observe that the term $\nabla P$ present as a multiphyics coupling in the conservation of momentum ends up in the off-diagonal of the stiffness matrix. Similarly for the $\nabla \cdot \mathbf{v}$ term in the conservation of mass.

Note in Eq(ref) that each variable can be discretised differently so their test/shape functions will be dependent on the primary variable considered. Below, we explain how the regularisation for the finite element solution of Stokes flow can be implemented using that particular aspect of the multiphysics coupling. Let's explain first what is the problem.

The number of velocity unknowns is determined by the discretisation of the velocity variable. But the number of equations to solve for the velocity unknowns is mostly dependent on the discretisation of the pressure variable because of the $\nabla \cdot \mathbf{v}$ term in the conservation of mass.
If the number of pressure unknowns is greater than the number of velocity unknowns, we have either a dependent or inconsistent system of equations. This is called the Ladyzhenskaya-Babuška-Brezzi (LBB) condition. To regularise the problem we need to increase the number of pressure unknowns so that it never exceeds the  number of velocity unknowns. To enforce it, we can increase the order of interpolation of the variable $\mathbf{v}$, while keeping a lower interpolation order for $P$.
To this end, a special class of elements can be used, the Taylor hood elements, which are illustrated in Fig. for a triangular mesh.
This trick is only possible because the discretisation between different variables can be independent.

```{figure} ./figures/taylor-hood_element.png
---
height: 200px
name: taylor-hood
---
Triangular Taylor-Hood element. Figure from https://homepage.tudelft.nl/d2b4e/burgers/fem_notes.pdf
```

### Boundary conditions

Boundary conditions need to apply to each primary variables separately as they are needed to close each governing equation. They are usually captured as constant value or constant flow, described in Finite Element by respectively Dirichlet or Neumann boundary condition. For solid mechanics for example, this is respectively prescribed displacement (Dirichlet BC for u) or prescribed stress (Neumann BC for u).

### Time discretisation

Physical processes have different time scales. Taking examples of chemical reactions vs pressure diffusion vs mechanical shear heating. Solving for multiphysics means accommodating for all those time scales. Most basic solution is to align with the smallest timescale but that can lead in computational heavy simulations if the timescales have orders of magnitude difference. In that case, instead of solving an implicit coupling, the coupling can be explicit where the two different physics are solved separately, and the coupled variable is updated at a different frequency.

```{figure} ./figures/timescales.png
---
height: 200px
name: timescales
---
Schematic time scale of some physical processes contributing to the occurrence of a geological instability . Figure from https://www.taylorfrancis.com/chapters/edit/10.1201/9780203885284-279/global-monitoring-strategy-applied-ground-failure-hazards
```
