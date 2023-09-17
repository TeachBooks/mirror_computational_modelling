# 1.2. Strong form of the problem

One of the key aspects of the FE method is that we express the set of governing equations in a [*weak form*](./chapter1-3_Weak_form_of_the_problem.md), also known as the *variational* form. Before deriving the *weak form* of the problem we need to state the set of governing equations (PDEs) with appropriate boundary and initial conditions that describe the physics of the solution. This is what we understand as the *strong form*. Solving the strong form of the problem leads to the exact solution of the continuous system.

At this point, let's take as an example the one dimensional Poisson equation to illustrate at first the so-called strong form of the problem:

$$
-\frac{\partial}{\partial x} \left(\nu \frac{\partial u}{{\partial x}}\right) = f
$$ (1Dpoissonequation)

where $\nu$ is a material property, $u$ the solution and $f$ a source, all of which can depend on the coordinate $x$. 

This equation can be used to express various physical phenomena such as steady-state heat conduction, elastic deformation of a rod or flow in a permeable media (such as Darcy’s law).

In a general form, the Poisson equation can be written as follows: 

$$ 
−(∇ \cdot q) + f = 0 
$$ (generalpoisson)

where $(\nabla \cdot )$ is the divergence operator and $q$ is a flux vector, of which the definition depends on the problem at hand. In the case of heat conductivity, $q$ is the heat flux vector, while in Darcy’s law, $q$ is the flow rate. The typical constitutive relationship between the flux $q$ and the unkown solution $u$ is given by:

$$ 
q= - \kappa  ∇ u 
$$ (consitutive)

Note that the solution $u$ can either be a scalar function, such as heat, or a vector function. In the case of linear heat conduction, for instance, the scalar $u$ in the above equation is the temperature. In the case of a structural problem, $u$ can also be the displacement. For Darcy’s law, $u$ is the hydraulic head. 

Keep in mind that the constitutive relationship always depends on the problem being solved and $ \kappa $ can take different meanings. for the heat equation, $\kappa$ is the thermal conductivity while for Darcy’s law $ \kappa $ is known as the hydraulic conductivity. In a general form, $ \kappa $ is an anisotropic tensor, therefore, using an index notation the general form of flux is:

$$
q_i= - \kappa_{i,j}  u_{,j}
$$ (flux)

where the notation $u_{,j}$ denotes the derivative of $u$ along the $j$-th coordinate. For an isotropic medium,

$$
\kappa = k I
$$ (kappaforisotropy)

## The strong form of the linear elastic rod
Now, let's consider an example of a one-dimensional bar to apply the Poisson equation. 

```{figure} .././images/Chapter1/1_5_1.png
---
height: 200px
name: 1_5_1
---
One dimensional bar
```

An application of the Poisson equation is the extension of one-dimensional structural elements. Let us consider a horizontal steel bar with a stiffness $EA = 1.0 \cdot 10^3$ kN with a load applied at the right side of $10$ kN and a length of $5$ m and a distributed load along its length $q(x)$. This equilibrium problem can be described with the following differential equation:


$$
-EA \frac{\partial^{2} u}{{\partial x}^{2}} = q(x)
$$ (1dpoisson)

where $u$ is the displacement of the bar as function of location $x$. 

As can be seen, the form of this equation is exactly the same as the 1D Poisson equation shown above. The only difference is in the physical interpretation of $u$ and $q$ and that instead of the constant $\nu$ we use the constant $EA$ (Young's modulus $E$ times cross section area $A$) to describe the stiffness.  

### Implementation 

After working with individual elements with respect to the displacement of their nodes, the next step is to assemble a global matrix from contributions of every element. For this example the problem above is divided into three equal elements of $1$ meter. To stay organized we give each element and node a number. As you can see in the figure below, there are 4 nodes, numbered $n_0$ to $n_3$ and 3 elements numbered $e_0$ to $e_2$.

```{figure} .././images/Chapter1/1_2_2.png
---
height: 200px
name: 1_2_2
---
One dimensional multielement bar
```

In the physical interpretation of solving mechanical equilibrium in a bar, we can interpret the result of the product $\mathbf{K}_e\mathbf{u}$ as forces coming from the element. Using the "local" stiffness formulation as shown above we can acquire the forces exerted on a node by an element as a function of the displacement. We will in this example have four nodes and therefore four unknowns. Let us consider the forces excerted by the second element ($e2$):

$$
\left[\begin{matrix}f_1^{e2} \\ f_2^{e2} \\ f_3^{e2} \\ f_4^{e2}\end{matrix}\right] = \frac{EA}{\Delta x}\left[\begin{matrix}0 & 0 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{matrix}\right] \left[\begin{matrix}u_1 \\ u_2 \\ u_3 \\ u_4\end{matrix}\right]
$$ (element2)

It follows logically that the other elements also excert forces on our nodes. By a simple addition of the influences of each element we can find the total stiffness matrix of our problem:


$$
\left[\begin{matrix}f_1 \\ f_2 \\ f_3 \\ f_4\end{matrix}\right] = \left[\begin{matrix}f_1^{e1} \\ f_2^{e1} \\ f_3^{e1} \\ f_4^{e1}\end{matrix}\right] + \left[\begin{matrix}f_1^{e2} \\ f_2^{e2} \\ f_3^{e2} \\ f_4^{e2}\end{matrix}\right] + \left[\begin{matrix}f_1^{e3} \\ f_2^{e3} \\ f_3^{e3} \\ f_4^{e3}\end{matrix}\right] = \frac{EA}{\Delta x} \left(\left[\begin{matrix}1 & -1 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{matrix}\right] + \left[\begin{matrix}0 & 0 & 0 & 0 \\ 0 & 1 & -1 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{matrix}\right] + \left[\begin{matrix}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & -1 & 1 \end{matrix}\right] \right) \left[\begin{matrix}u_1 \\ u_2 \\ u_3 \\ u_4\end{matrix}\right]
$$ (assembly)

Collection of the matrices gives:

$$
\left[\begin{matrix}f_1 \\ f_2 \\ f_3 \\ f_4\end{matrix}\right] = \frac{EA}{\Delta x}\left[\begin{matrix}1 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 1 \end{matrix}\right] \left[\begin{matrix}u_1 \\ u_2 \\ u_3 \\ u_4\end{matrix}\right]
$$ (sumofmatrixes)

To solve for global equilibrium, we need to equate the product $\mathbf{Ku}$ to a vector with external forces. Point loads on a node can directly be inserted on the right hand side vector of the equation $\mathbf{Ku}=\mathbf{f}$, while a distributed load $q$ is translated to a load vector with the expression from the derivation:

$$\mathbf{f}=\int_0^L\mathbf{N}^Tq\,dx$$ 




### Boundary conditions

We derived a way to express the relation between $\mathbf{u}$ and $\mathbf{f}$ through a matrix $\mathbf{K}$. However, when we try to solve the equation $\mathbf{K u} = \mathbf{f}$, we will run into a problem. On the left hand side one of the values for $u$ is already known, the displacement of the left node ($n_0$) will be zero. The corresponding force $f_1$ is as of yet unknown. Since there is unknowns on either side of the equation we cannot solve it by inverting K and bringing it to the other side.

$$
\frac{EA}{\Delta x}\left[\begin{matrix}1 & -1 & 0 & 0 \\ -1 & 2 & -1 & 0 \\ 0 & -1 & 2 & -1 \\ 0 & 0 & -1 & 1 \end{matrix}\right] \left[\begin{matrix}0 \\ u_2? \\ u_3? \\ u_4?\end{matrix}\right] = \left[\begin{matrix}f_1? \\ 0 \\ 0 \\ 10\end{matrix}\right]
$$

A way to overcome this problem is to leave out equations belonging to nodes for which the solution is known. As long as the fixed degrees of freedom are prescribed at a value of 0 (i.e. homogeneous Dirichlet conditions), we can do this by simply removing the corresponding columns and rows out of our system. Doing that for node 0 in our example, we get:

$$
\frac{EA}{\Delta x}\left[\begin{matrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{matrix}\right] \left[\begin{matrix}u_2? \\ u_3? \\ u_4?\end{matrix}\right] = \left[\begin{matrix}0 \\ 0 \\ 10\end{matrix}\right]
$$

This system can solved, by inverting $\mathbf{K}$, or more efficiently by using an appropriate linear solver. It is important to note that for nonzero Dirichlet conditions, additional steps need to be taken.

Solving the system of equations above will finally result in a vector with values for the nodal displacements $\mathbf{u}$. Note that with the shape functions, we also have an interpolation between the nodes, so a continuous approximate solution $u^h(x)$ can be obtained with:

$$
u^h(x) = \mathbf{N}\mathbf{u}
$$

Moreover, the reaction force $f_1$ can be computed by multiplying the complete $4\times4$-matrix with the nodal displacement vector.

$$
-EA \frac{\partial^{2} u}{{\partial x}^{2}} = q(x)
$$

where $u$ is the displacement of the bar as function of location $x$. As can be seen, the form of this equation is exactly the same as the 1D Poisson equation shown above. The only difference is in the physical interpretation of $u$ and $q$ and that instead of the constant $\nu$ we use the constant $EA$ (Young's modulus $E$ times cross section area $A$) to describe the stiffness. 

