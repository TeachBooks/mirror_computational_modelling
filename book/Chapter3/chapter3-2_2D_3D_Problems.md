# 2D/3D Problems 

In this chapter, we will introduce finite element formulations for higher order problems. You have already seen 2D frame formulations, but there still the elements themselves were one-dimensional in nature. Now, we will focus on problems where the solution is a field in 2D (or 3D) space. This implies the elements and shape functions need to be different (e.g. triangular, quadrilateral, tetrahedral). We will start with the 2D Poisson equation and then move to 2D elasticity. Interestingly, both of these are generalizations of the 1D Poisson equation you have seen in Chapter 1. Of these, the 2D Poisson equation is the simplest one, so that will be our starting point. 

## Poisson Equation in 2D

### Strong form equation 

The PDE at hand in this chapter is the 2D Poisson equation. It describes the steady state (time-independent solution) of a diffusion problem.

$$-\nu \left(\frac{\partial^{2} u}{{\partial x}^{2}} + \frac{\partial^{2} u}{{\partial y}^{2}}\right) = q$$ (poisson2d)

Where $u$ is the unknown field, $\nu$ is the diffusivity parameter and $q$ is a source term. At least $u$ and possibly also $\nu$ and $q$ are a function of $x$ and $y$. 

There are several applications where this PDE can be used to solve problems in sciences and engineering, such as:
- potential flow
- pressure in saturated soil
- temperature distribution in solids

Equation {eq}`poisson2d` can be written with the Laplacian operator $\Delta = \nabla\cdot\nabla$ as 

$$ -\nu\Delta u = q $$

To formulate a problem the strong form governing equation is combined with boundary conditions

$$
u = \bar{u},\quad \text{on} \quad \Gamma_D \\
\nu\nabla u\cdot\mathbf{n} = h,\quad \text{on} \Gamma_N
$$

where $\bar{u}$ stands for prescribed values for the unknown field on the part of the boundary where Dirichlet boundary conditions are applied ($\Gamma_D$) and $h$ for a flux on the part of the boundary where Neumann boundary conditions are applied ($\Gamma_N$). 

### Weak form

As usual, we start with multiplying the strong form equation with a (for now arbirtary) test function and integrating over the domain

$$
-\int_\Omega w\nabla\cdot\nabla u\,d\Omega = \int_\Omega wq\,d\Omega
$$

Integration by parts in combination with Divergence theorem gives:

$$
\int_\Omega \nabla w\nabla u\,d\Omega  - \int_{\Gamma} w\nabla u\cdot\mathbf{n}\,d\Gamma = \int_\Omega wq\,d\Omega
$$

Substitution of the Neumann boundary in combination with the condition that $w=0$ on $\Gamma_D$ eliminates the unknown $u$ from the boundary term, after which it is moved to the right hand side to arrive at the weak form equation:

$$
\int_\Omega \nabla w\nabla u\,d\Omega = \int_\Omega wq\,d\Omega + \int_{\Gamma_N} wh\,d\Gamma 
$$(poisson2d-weak)

### Discrete form

Discretization of the solution is done with 2D shape functions

$$
u \approx u^h = \sum_j N_j(x,y) u_j = \mathbf{Nu}
$$

where $\textbf{u}$ contains the degrees of freedom of the discretized field and $\mathbf{N}$ is a row vector with all shape functions:

$$  \textbf{N} = \begin{bmatrix}  N_1  & N_2 &... & N_{n} \end{bmatrix}$$

in which $n$ is the number of degrees of freedom, which is for conventional shape functions equal to the number of nodes in the mesh. 

Following the Bubnov-Galerkin method, the same discretization is introduced for $w$:

$$
w \approx w^h = \mathbf{Nw}
$$

The gradients of $u$ and $w$ are defined with the $\mathbf{B}$-matrix as:

$$
\nabla{u} = \mathbf{Bu} \qquad \text{and} \qquad \nabla{w} = \mathbf{Bw} 
$$

with

$$
\mathbf{B} = \begin{bmatrix} \frac{\partial N_1}{\partial x}, \frac{\partial N_2}{\partial x}, \ldots, \frac{\partial N_{n}}{\partial x} \\ \frac{\partial N_1}{\partial y}, \frac{\partial N_2}{\partial y}, \ldots, \frac{\partial N_{n}}{\partial y} \end{bmatrix}
$$

Substitution into the {eq}`poisson2d-weak` gives

$$
\int_\Omega \mathbf{Bw}\nu \mathbf{Bu}\,d\Omega = \int_\Omega \mathbf{Nw}q\,d\Omega + \int_{\Gamma_N} \mathbf{Nw}h\,d\Gamma
$$

As for the 1D problem, eliminating $\mathbf{w}$ involves transposing $\mathbf{N}$ and $\mathbf{B}$ matrices where they are multiplied with $\mathbf{w}$. Finally, we arrive at a linear system of equations written as:

$$
\mathbf{Ku} = \mathbf{f}
$$

with

$$
\mathbf{K} = \int_\Omega \mathbf{B}^T\nu \mathbf{B}\,d\Omega \qquad \text{and} \qquad \mathbf{f} = \int_\Omega \mathbf{N}^Tq\,d\Omega + \int_{\Gamma_N} \mathbf{N}^Th\,d\Gamma
$$



## Two dimensional continuum elasticity elements

In two or more dimensions, each unknown field (such as displacement in each directions) in interpolated using polynomial shape functions. The displacement field for an element is given by: 

$$ 
u^h= \textbf{N} \ \textbf{α}_e  
$$

and the strain field is given by: 

$$ 
ε^h= \textbf{Β} \ \textbf{α}_e  
$$

The matrix $\mathbf{N}$ contains the element shape functions. In two dimensions it has the form : 


$$  \textbf{N} = \begin{bmatrix}  
N_1  & 0 & N_2 &  0 &... & N_{nn} & 0 \\
0 &  N_1 & 0 & N_2 & ...& 0 &  N_{nn} \end{bmatrix}$$

where $nn$ is the numbers of nodes of the element. 

For two-dimensional problems, the matrix $ \textbf{B} $ has the form:

$$ \textbf{B} = 
\begin{bmatrix} 
\frac{\partial{N_1}}{\partial{x}}  &  0 & \frac{\partial{N_2}}{\partial{x}} &  0 & ... &  \frac{N_{nn}}{\partial{x}}& 0 \\
\
\
0 &   \frac{\partial{N_1}}{\partial{y}}   & 0 &  \frac{\partial{N_2}}{\partial{y}} & ... & 0 & \frac{\partial{N_{nn}}}{\partial{y}}  \\
\
\
\
\frac{\partial{N_1}}{\partial{y}} &  \frac{\partial{N_1}}{\partial{x}} &\frac{\partial{N_2}}{\partial{y}} & \frac{\partial{N_2}}{\partial{x}}&... & \frac{\partial{N_{nn}}}{\partial{y}} & \frac{N_{nn}}{\partial{x}} \\
\end{bmatrix}
$$

The nodal degrees of freedom (normally one for each spatial dimension at each node for elasticity problems) are stores in a vector $ \alpha$

For a two dimensional problem 

$$ \textbf{α}_e=
\begin{equation*}
\begin{Bmatrix} α_{1 \ x} \\ α_{1 \ y} \\ α_{2 \ x} \\ α_{2 \ y} \\ . \\ . \\. \\ α_{nn \ x} \\α_{nn \ y}
\end{Bmatrix}
\end{equation*}
$$

At this point, the discretised filed $u^h$ will be inserted into the weak form of the governing equation. 

The weight functions are discretised similarly to the unknown field $u^h$.

Therefore, for the multi-dimensional case within an element:

$$ 
w^h= \textbf{N} \ \textbf{b}_e  
$$

$$ 
∇^s w^h= \textbf{B} \   \textbf{b}_e  
$$

Now, considering the one-dimensional governing equation for an elastic rod.

Recall 
$$
-\int_{0}^{L} w^h_{,x}E u^h_{,x} \: dx + w^hh|_{x=L} =0 ,  ∀ \ w^h ∈ V^h.
$$


Now, let's consider a single element which extends from x=$l_1$ to x=$l_2$  in the x-axis.

The discretised governing equation for the element is expressed as follows:

$$
\int_{l_1}^{l_2} (\textbf{B b}{_e})^T E \ \textbf{B α}{_e}  \: dΩ  = \int_{Γ{_h,e}} ( \textbf{N b}{_e})^Τ \ h  \: dΓ
$$



where the integral over $Γ_{h,e}$  is only non zero if the boundary of the element coincides with the boundary $Γ_{h}$. The discrete nodal values can be removed from the integrals which after appropriate rearranging leads to: 

$$ 
\textbf{b}_e^T \int_{l_1}^{l_2} \textbf{B}^T E \textbf{B} \: dΩ \ \textbf{α}_e = \textbf{b}_e^T
\int_{Γ{_h,e}} \textbf{N}^T h \: dΓ   $$

and by  eliminating $ \textbf{b}_e $ on both sides, we get

$$ 
\int_{l_1}^{l_2} \textbf{B}^T E  \ \textbf{B} \: dΩ α_e =
\int_{Γ{_h,e}} \textbf{N}^T h \: dΓ   $$


Now the integral on the left hand side of the equation can be recognised as the **element stiffness matrix** **$k_e$**. Once the stiffness matrix has been formed for an element, its contribution is added to the ‘global’ stiffness matrix **K**.

For a continuum elasticity problem, the discretised displacement and strain fields
are inserted into the following equation

$$
-\int_{Ω} ∇^s \textbf{w}^h : \textbf{C} : ε^h \: dΩ +
\int_{Ω} \textbf{w}^h \textbf{b} \: dΩ +
\int_{Γ{_h}} \textbf{w}^h \textbf{b}  \: dΓ = 0  \ \ ∀ \textbf{w}^h ∈ V^h
$$

where $ ε^h = ∇^s \textbf{u}^h $

Note: In a multi dimensional context, the finite dimensional trial and wight functions are denoted $\textbf{u}^h$ and $\textbf{w}^h$, respectivelly.


This yields:

$$
\int_{Ω_e} (\textbf{B b}{_e})^T \textbf{D} \  \textbf{B α}{_e} \: dΩ  =
  \int_{Γ_{h,e}} (\textbf{N b}_e)^T \textbf{h}  \: dΓ +
   \int_{Ω_{e}}  (\textbf{N b}_e)^T \textbf{b} \: dΩ
$$


and following the same steps, the element stiffness matrix can be expressed as follows: 

$$
\int_{Ω_e} \textbf{B}^T \ \textbf{D B} \: dΩ  \ \textbf{α}{_e} =
  \int_{Γ_{h,e}} \textbf{N}^T \textbf{h} \: dΓ +
   \int_{Ω_{e}} \textbf{N}^T \textbf{b} \: dΩ
$$


Once the stiffness matrix has been formed for each element in the problem, it must
be assembled into the global stiffness matrix. This is denoted symbolically by the
operation:

$$
\textbf{K} = A^{ne}_{e=1} \ k_e
$$


$$
\textbf{f} = A^{ne}_{e=1} \ f_e
$$

where A represents the assembly operator and $ne$ the number of elements in the mesh. For an element stiffness materix the term $k_{ij}$ relates the local nodes i and j. The component $k_{ij}$ is added to the location $K_{ij}$. 

Note that the assembly process will be discussed in following chapters.


## Linear elasticity in 3D

## Stokes flow

## Poroelasticity with Darcy flow
