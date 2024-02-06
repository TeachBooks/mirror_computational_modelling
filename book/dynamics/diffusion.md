$\newcommand{\E}{\\[3pt]}$
$\newcommand{\DE}{\\[6pt]}$
$\newcommand{\TE}{\\[9pt]}$
$\newcommand{\QE}{\\[12pt]}$
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\beps}{\boldsymbol\eps}$
$\newcommand{\bsig}{\boldsymbol\sigma}$
$\newcommand{\dbdot}{\,\colon\!}$
$\newcommand{\hint}{\displaystyle\int}$
$\newcommand{\hsum}{\displaystyle\sum}$
$\newcommand{\alert}[1]{{\color{pdcolor9}#1}}$
$\newcommand{\gives}{\quad\Rightarrow\quad}$
$\newcommand{\ud}{\mathrm{d}}$
$\newcommand{\uf}{\mathrm{f}}$
$\newcommand{\bff}{\mathbf{f}}$
$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bb}{\mathbf{b}}$
$\newcommand{\bc}{\mathbf{c}}$
$\newcommand{\bh}{\mathbf{h}}$
$\newcommand{\bn}{\mathbf{n}}$
$\newcommand{\bq}{\mathbf{q}}$
$\newcommand{\bt}{\mathbf{t}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bv}{\mathbf{v}}$
$\newcommand{\bw}{\mathbf{w}}$
$\newcommand{\bx}{\mathbf{x}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bD}{\mathbf{D}}$
$\newcommand{\bJ}{\mathbf{J}}$
$\newcommand{\bK}{\mathbf{K}}$
$\newcommand{\bM}{\mathbf{M}}$
$\newcommand{\bN}{\mathbf{N}}$
$\newcommand{\bP}{\mathbf{P}}$
$\newcommand{\bzero}{\mathbf{0}}$
$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\dder}[2]{\frac{\ud #1}{\ud #2}}$
$\newcommand{\pders}[3]{\frac{\partial^2 #1}{\partial #2 \partial #3}}$
$\newcommand{\lder}[2]{{\ud #1}/{\ud #2}}$
$\newcommand{\lpder}[2]{{\partial #1}/{\partial #2}}$
$\newcommand{\lpders}[3]{{\partial^2 #1}/{\partial #2 \partial #3}}$
$\newcommand{\hfrac}[2]{\displaystyle\frac{#1}{#2}}$
$\newcommand{\lfrac}[2]{{#1}/{#2}}$
$\newcommand{\hpder}[2]{\displaystyle\frac{\partial #1}{\partial #2}}$
$\newcommand{\myVec}[1]{\left\{ \begin{matrix} #1 \end{matrix} \right\}}$
$\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$
$\newcommand{\sym}{\ensuremath{_\mathrm{s}}}$
$\newcommand{\dg}{\ensuremath{^\circ}}$
$\newcommand{\mbf}[1]{\mathbf{#1}}$
$\newcommand{\mrm}[1]{\mathrm{#1}}$
$\newcommand{\bs}[1]{\boldsymbol{#1}}$
$\newcommand{\T}{^\mathrm{T}}$

$\newcommand{cA}[1]{\textcolor[RGB]{1,113,136}{#1}}$
$\newcommand{cB}[1]{\textcolor[RGB]{195,49,47}{#1}}$
$\newcommand{cC}[1]{\textcolor[RGB]{0,102,162}{#1}}$
$\newcommand{cD}[1]{\textcolor[RGB]{0,183,211}{#1}}$
$\newcommand{cE}[1]{\textcolor[RGB]{0,163,144}{#1}}$
$\newcommand{cF}[1]{\textcolor[RGB]{97,164,180}{#1}}$
$\newcommand{cG}[1]{\textcolor[RGB]{130,215,198}{#1}}$
$\newcommand{cH}[1]{\textcolor[RGB]{153,210,140}{#1}}$
$\newcommand{cI}[1]{\textcolor[RGB]{235,114,70}{#1}}$
$\newcommand{cJ}[1]{\textcolor[RGB]{241,190,62}{#1}}$
$\newcommand{cK}[1]{\textcolor[RGB]{231,41,138}{#1}}$

# Semi-discrete form for diffusion 

In this section we go back to the Poisson equation one last time. We have seen this PDE before in {doc}`1D<../../introduction/strong>` and {doc}`2D<../../introduction/poisson2d>`, but only for steady-state (time-independent) problems. Here we make one more extension by allowing time-dependent behavior to arise. We will see one common way to treat time in FEM problems, by arriving at a **semi-discrete** system of equations we can solve numerically.

This page also allows you to switch between tensor notation and index notation. Try it out and see how different parts of the formulation become easier to write in one or the other notation.

## Strong form equation

````{tab-set}
```{tab-item} Tensor notation
:sync: tensor

As always, we start the formulation with the PDE in its strong form:

$$
-\nabla\cdot\mathbf{q} - {\rho c\dot{u}} + f = 0,\quad\text{with}\quad\mathbf{q} = -\boldsymbol{\kappa}\cdot\nabla u
$$(d-d-tstrongform1)

where $u$ is our solution field of interest: in heat conduction problems it would represent temperature; in mass diffusion it would be a concentration; in Darcy flow it would be the hydraulic head. Furthermore, $\mathbf{q}$ is a gradient-driven flux vector that depends on a diffusivity matrix $\bs\kappa$. The new term here is $\rho c\dot{u}$, with $\rho c$ being a capacity parameter and $\dot{u}$ the first time derivative of our solution, i.e. a velocity field.

The problem is completed by Dirichlet, Neumann and **initial** boundary conditions:

$$
\begin{aligned}
u=g \quad&\text{on}\quad\Gamma_D\\
-\mathbf{q}\cdot\mathbf{n}=h \quad&\text{on}\quad\Gamma_N\\
u = u_0\quad&\text{at}\quad t=0 
\end{aligned}
$$(d-d-tstrongform2)

where $g$ is a prescribed value for the solution field and $\mbf{n}$ is the normal to the surface where Neumann boundary conditions are applied. Since we are solving a time-dependent problem, the third condition fixes an initial field $u_0$ from which we will predict into the future.
```

```{tab-item} Index notation
:sync: index
As always, we start the formulation with the PDE in its strong form:

$$
-q_{i,i} + f = 0,\quad\text{with}\quad q_i = -\kappa_{ij}u_{,j}
$$(d-d-istrongform1)

where $u$ is our solution field of interest: in heat conduction problems it would represent temperature; in mass diffusion it would be a concentration; in Darcy flow it would be the hydraulic head. Furthermore, $q_i$ is a gradient-driven flux vector that depends on a diffusivity matrix $\kappa_{ij}$. The new term here is $\rho c\dot{u}$, with $\rho c$ being a capacity parameter and $\dot{u}$ the first time derivative of our solution, i.e. a velocity field.

The problem is completed by Dirichlet, Neumann and **initial** boundary conditions:

$$
\begin{aligned}
u=g \quad&\text{on}\quad\Gamma_D\\
-q_in_i = h \quad&\text{on}\quad\Gamma_N\\
u = u_0\quad&\text{at}\quad t=0 
\end{aligned}
$$(d-d-istrongform2)

where $g$ is a prescribed value for the solution field and $n_i$ is the normal to the surface where Neumann boundary conditions are applied. Since we are solving a time-dependent problem, the third condition fixes an initial field $u_0$ from which we will predict into the future.

```
````

## Weak form

````{tab-set}
```{tab-item} Tensor notation
:sync: tensor

To get to the weak form we first multiply the PDE by a weight function $w$ and integrate over the domain $\Omega$:

$$
 -\hint_\Omega w\left(\nabla\cdot\mathbf{q}\right)\ud\Omega - \hint_\Omega w\rho c\dot{u}\ud\Omega + \hint_\Omega wf\ud\Omega = 0
$$(d-d-tweakform1)

where $w$ for this problem is always a scalar field, irrespective of the dimensionality of $\Omega$. The next step is to eliminate the derivative $\nabla\cdot\mbf{q}$ using the divergence theorem and integration by parts. Here we can directly use the result we already derived in Eq. {eq}`p-c-divtheoremvecfinal`:

$$
\hint_\Omega\nabla w\cdot\mathbf{q}\ud\Omega - \hint_\Omega w\rho c\dot{u}\ud\Omega + \hint_\Omega wf\ud\Omega - \hint_{\Gamma_N} w\mathbf{q}\cdot\mathbf{n}\ud\Gamma = 0
$$(d-d-tweakform2)

and we see that the derivative has now been transferred to $w$. This also causes an integral over $\Gamma$ to appear. From the requirement that $w=0$ at $\Gamma_D$, only the integral over $\Gamma_N$ remains. Finally, note that we did not touch the time derivative $\dot{u}$, which means we are effectively treating $u$ and $\dot{u}$ as two independent fields.

As a final step, we substitute the Neumann boundary condition of Eq. {eq}`d-d-tstrongform2` and the constitutive relation $\mbf{q}=-\bs{\kappa}\cdot\nabla u$ to get to the final weak form:

$$
{-\hint_\Omega\nabla w\cdot\boldsymbol{\kappa}\nabla u\ud\Omega - \hint_\Omega w\rho c\dot{u}\ud\Omega + \hint_\Omega wf\ud\Omega +\hint_{\Gamma_h} wh\ud\Gamma = 0}
$$(d-d-tweakform3)

which is valid for any $w\in\mathcal{V}$, an infinite-dimensional function space. Weak solutions to the PDE are equally valid and exact as solutions to the strong form. The only limitation is that they only obey the original PDE in a *distribution* sense. This is a sensible tradeoff, in exchange we get a whole new set of solutions that do not need to be twice differentiable.
```

```{tab-item} Index notation
:sync: index
To get to the weak form we first multiply the PDE by a weight function $w$ and integrate over the domain $\Omega$:

$$
 -\hint_\Omega wq_{i,i}\ud\Omega - \hint_\Omega w\rho c\dot{u}\ud\Omega + \hint_\Omega wf\ud\Omega = 0
$$(d-d-iweakform1)

where $w$ for this problem is always a scalar field, irrespective of the dimensionality of $\Omega$. The next step is to eliminate the derivative $q_{i,i}$ using the divergence theorem and integration by parts. Here we can directly use the result we already derived in Eq. {eq}`p-c-divtheoremvecfinal`:

$$
\hint_\Omega w_{,i}q_i\ud\Omega - \hint_\Omega w\rho c\dot{u}\ud\Omega + \hint_\Omega wf\ud\Omega - {\hint_{\Gamma_h} wq_in_i\ud\Gamma} = 0
$$(d-d-iweakform2)

and we see that the derivative has now been transferred to $w$. This also causes an integral over $\Gamma$ to appear. From the requirement that $w=0$ at $\Gamma_D$, only the integral over $\Gamma_N$ remains. Finally, note that we did not touch the time derivative $\dot{u}$, which means we are effectively treating $u$ and $\dot{u}$ as two independent fields.

As a final step, we substitute the Neumann boundary condition of Eq. {eq}`d-d-istrongform2` and the constitutive relation $q_i = -\kappa_{ij}u_{,j}$ to get to the final weak form:

$$
-\hint_\Omega w_{,i}\kappa_{ij}u_{,j}\ud\Omega - \hint_\Omega w\rho c\dot{u}\ud\Omega + \hint_\Omega wf\ud\Omega +\hint_{\Gamma_h} wh\ud\Gamma = 0
$$(d-d-iweakform3)

which is valid for any $w\in\mathcal{V}$, an infinite-dimensional function space. Weak solutions to the PDE are equally valid and exact as solutions to the strong form. The only limitation is that they only obey the original PDE in a *distribution* sense. This is a sensible tradeoff, in exchange we get a whole new set of solutions that do not need to be twice differentiable.
```
````

## Semi-discrete form

````{tab-set}
```{tab-item} Tensor notation
:sync: tensor

To get to a tractable FEM problem we need to restrict the space $\mathcal{V}$. We do this through the Galerkin method, by defining shape function-based approximations to all of our fields:

$$
u^h = \mathbf{N}\mathbf{a},\quad\quad \dot{u}^h = \mathbf{N}\dot{\mathbf{a}}, \quad\quad w^h = \mathbf{N}\mathbf{c}
$$(d-d-tdiscreteform1)

where the shape function matrices and DOF vectors take the shape:

$$
\mathbf{N} = \displaystyle\myMat{N_1 & N_2 & \cdots & N_{nn}}\quad\quad\mathbf{a}=\myVec{a_1\\a_2\\\vdots\\a_{nn}}
\quad\quad\dot{\mathbf{a}}=\myVec{\dot{a}_1\\\dot{a}_2\\\vdots\\\dot{a}_{nn}}
\quad\quad\mathbf{c}=\myVec{c_1\\c_2\\\vdots\\c_{nn}}
$$(d-d-tdiscreteform2)

with $nn$ being the number of nodes in our finite element mesh. Now the problem has two DOFs per node, namely a solution value $a_n$ and a velocity $\dot{a}_n$. We will also need gradients of $u^h$ and $w^h$:

$$
\nabla u^h = \mathbf{B}\mathbf{a},\quad\quad \nabla w^h = \mathbf{B}\mathbf{c}
$$(d-d-tdiscreteform3)

with:

$$
\mathbf{B} = \displaystyle\myMat{N_{1,x} & N_{2,x} & \cdots & N_{nn,x}\\N_{1,y} & N_{2,y} & \cdots & N_{nn,y}}
$$(d-d-tdiscreteform4)

We now substitute the approximations above into the weak form. The goal is to reach a so-called **semi-discrete** form, indicating that only spatial derivatives are discretized while time derivatives remain untouched and are treated as additional DOFs.

Substitution yields:

$$
-\hint_\Omega\left(\mathbf{B}\mathbf{c}\right)^\mathrm{T}\boldsymbol{\kappa}\mathbf{B}\mathbf{a}\ud\Omega -
\hint_\Omega\left(\mathbf{N}\mathbf{c}\right)^\mathrm{T}\rho c \mathbf{N}\dot{\mathbf{a}}\ud\Omega +
\hint_\Omega\left(\mathbf{N}\mathbf{c}\right)^\mathrm{T}f\ud\Omega + 
\hint_{\Gamma_h}\left(\mathbf{N}\mathbf{c}\right)^\mathrm{T}h\ud\Gamma = 0
$$(d-d-tdiscreteform5)

Making use of Eq. {eq}`p-l-transprod` we can remove $\mbf{c}$, $\mbf{a}$ and $\dot{\mbf{a}}$ from the integrals:

$$
-{\mathbf{c}^\mathrm{T}}\left(\hint_\Omega\mathbf{B}^\mathrm{T}\boldsymbol{\kappa}\mathbf{B}\ud\Omega\right){\mathbf{a}} -
{\mathbf{c}^\mathrm{T}}\left(\hint_\Omega\mathbf{N}^\mathrm{T}\rho c\mathbf{N}\ud\Omega\right){\dot{\mathbf{a}}} +
{\mathbf{c}^\mathrm{T}}\left(\hint_\Omega\mathbf{N}^\mathrm{T}f\ud\Omega\right) +
{\mathbf{c}^\mathrm{T}}\left(\hint_{\Gamma_h}\mathbf{N}^\mathrm{T}h\ud\Gamma\right) = 0
$$(d-d-tdiscreteform6)

and cancel out $\mbf{c}$ from all terms. We then gather the expressions into the more compact form:

$$
\mathbf{K}\mathbf{a} + \mathbf{M}\dot{\mathbf{a}}=\mathbf{f}
$$(d-d-tdiscreteform7)

where the time derivative makes the new term $\mbf{M}\dot{\mbf{a}}$ appear. We have then reached the final discretized form and can write down the terms one more time for completeness:

$$
\mathbf{K}=\hint_\Omega\mathbf{B}^\mathrm{T}\boldsymbol{\kappa}\mathbf{B}\ud\Omega
$$(d-d-tdiscreteform8)

$$
\mathbf{M}=\hint_\Omega\mathbf{N}^\mathrm{T}\rho c\mathbf{N}\ud\Omega
$$(d-d-tdiscreteform9)

$$
\mathbf{f}=\hint_\Omega\mathbf{N}^\mathrm{T}f\ud\Omega + \hint_{\Gamma_h}\mathbf{N}^\mathrm{T}h\ud\Gamma
$$(d-d-tdiscreteform10)

```

```{tab-item} Index notation
:sync: index

To get to a tractable FEM problem we need to restrict the space $\mathcal{V}$. We do this through the Galerkin method, by defining shape function-based approximations to all of our fields:

$$
u^h = N_na_n,\quad \dot{u}^h = N_n\dot{a}_n, \quad w^h = N_mc_m
$$(d-d-idiscreteform1)

where the shape function matrices and DOF vectors take the shape:

$$
N_n = \displaystyle\myMat{N_1 & N_2 & \cdots & N_{nn}}\quad\quad {a_n}=\myVec{a_1\\a_2\\\vdots\\a_{nn}}
\quad\quad\dot{a}_n=\myVec{\dot{a}_1\\\dot{a}_2\\\vdots\\\dot{a}_{nn}}
\quad\quad c_m=\myVec{c_1\\c_2\\\vdots\\c_{nn}}
$$(d-d-idiscreteform2)

with $nn$ being the number of nodes in our finite element mesh. Now the problem has two DOFs per node, namely a solution value $a_n$ and a velocity $\dot{a}_n$. We will also need gradients of $u^h$ and $w^h$:

$$
u^h_{,j} = N_{n,j}a_n,\quad\quad w^h_{,i} = N_{m,i}c_m
$$(d-d-idiscreteform3)

with:

$$
N_{n,j} = \displaystyle\myMat{N_{1,x} & N_{2,x} & \cdots & N_{nn,x}\\N_{1,y} & N_{2,y} & \cdots & N_{nn,y}}
$$(d-d-idiscreteform4)

We now substitute the approximations above into the weak form. The goal is to reach a so-called **semi-discrete** form, indicating that only spatial derivatives are discretized while time derivatives remain untouched and are treated as additional DOFs.

Substitution yields:

$$
-\hint_\Omega N_{m,i}c_m\kappa_{ij}N_{n,j}a_n\ud\Omega - 
\hint_\Omega N_mc_m\rho cN_n\dot{a}_n\ud\Omega +
\hint_\Omega N_mc_mf\ud\Omega +
\hint_{\Gamma_h}N_mc_m h\ud\Gamma = 0
$$(d-d-idiscreteform5)

Making use of Eq. {eq}`p-l-transprod` we can remove $c_m$, $a_n$ and $\dot{a}_n$ from the integrals:

$$
-{c_m}\left(\hint_\Omega N_{m,i}{\kappa}_{ij}N_{n,j}\ud\Omega\right){a_n} -
  {c_m}\left(\hint_\Omega N_m\rho c N_n\ud\Omega\right){\dot{a}_n} +
{c_m}\left(\hint_\Omega N_m f\ud\Omega\right) +
{c_m}\left(\hint_{\Gamma_h}N_m h\ud\Gamma\right) = 0
$$(d-d-idiscreteform6)

and cancel out $c_m$ from all terms. We then gather the expressions into the more compact form:

$$
K_{mn}a_n + M_{mn}\dot{a}_n = f_m
$$(d-d-idiscreteform7)

where the time derivative makes the new term $M_{mn}\dot{a}_n$ appear. We have then reached the final discretized form and can write down the terms one more time for completeness:

$$
K_{mn} = \hint_\Omega N_{m,i}\kappa_{ij}N_{n,j}\ud\Omega
$$(d-d-idiscreteform8)

$$
M_{mn} = \hint_\Omega N_{m}\rho c N_n\ud\Omega
$$(d-d-idiscreteform9)

$$
f_m = \hint_\Omega N_m f\ud\Omega + \hint_{\Gamma_h} N_m h\ud\Gamma
$$(d-d-idiscreteform10)
```
````

## Solving the semi-discrete system

We have reached a semi-discrete system with $nn$ equations, the number of nodes in the FE mesh. However, we now have **twice** as many DOFs: solution values $\mbf{a}$ and velocities $\dot{\mbf{a}}$. The problem seems under-determined, but that is only because we still did not take into account that $\mbf{a}$ and $\dot{\mbf{a}}$ are of course coupled in time and for now the FEM discretization is only taking care of spatial derivatives. We will address this on the next page.
