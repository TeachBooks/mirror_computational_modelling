$\newcommand{\beps}{\boldsymbol\varepsilon}$ $\newcommand{\bsig}{\boldsymbol\sigma}$ $\newcommand{\ud}{\mathrm{d}}$ $\newcommand{\us}{\mathrm{s}}$ $\newcommand{\ba}{\mathbf{a}}$ $\newcommand{\bb}{\mathbf{b}}$ $\newcommand{\bc}{\mathbf{c}}$ $\newcommand{\bt}{\mathbf{t}}$ $\newcommand{\bu}{\mathbf{u}}$ $\newcommand{\bx}{\mathbf{x}}$ $\newcommand{\bw}{\mathbf{w}}$ $\newcommand{\bN}{\mathbf{N}}$ $\newcommand{\bB}{\mathbf{B}}$ $\newcommand{\bD}{\mathbf{D}}$ $\newcommand{\bK}{\mathbf{K}}$ $\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$ $\newcommand{\iD}{\boldsymbol{\mathcal{D}}}$ $\newcommand{\mbf}[1]{\mathbf{#1}}$ $\newcommand{\mrm}[1]{\mathrm{#1}}$ $\newcommand{\bs}[1]{\boldsymbol{#1}}$ $\newcommand{\T}{^\mathrm{T}}$ $\newcommand{\inv}{^{-1}}$ $\newcommand{\myVec}[1]{\left\{ \begin{matrix} #1 \end{matrix} \right\}}$ $\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$ $\newcommand{cA}[1]{\textcolor[RGB]{1,113,136}{#1}}$ $\newcommand{cB}[1]{\textcolor[RGB]{195,49,47}{#1}}$ $\newcommand{cC}[1]{\textcolor[RGB]{0,102,162}{#1}}$ $\newcommand{cD}[1]{\textcolor[RGB]{0,183,211}{#1}}$ $\newcommand{cE}[1]{\textcolor[RGB]{0,163,144}{#1}}$ $\newcommand{cF}[1]{\textcolor[RGB]{97,164,180}{#1}}$ $\newcommand{cG}[1]{\textcolor[RGB]{130,215,198}{#1}}$ $\newcommand{cH}[1]{\textcolor[RGB]{153,210,140}{#1}}$ $\newcommand{cI}[1]{\textcolor[RGB]{235,114,70}{#1}}$ $\newcommand{cJ}[1]{\textcolor[RGB]{241,190,62}{#1}}$ $\newcommand{cK}[1]{\textcolor[RGB]{231,41,138}{#1}}$ 

# Strong form for linear elasticity

In this chapter we treat mechanical equilibrium problems in a more general way. In the {doc}`previous chapter<../introduction/strong>` we have seen how the 1D Poisson equation can be directly used to treat structural bar elements in extension. Here we give the equilibrium problem a more thorough treatment, starting from continuum mechanics and arriving at a strong form PDE we can treat with FEM.

## Kinematic relations

For equilibrium problems, we are concerned with modeling how solids deform as loads are applied. Consider the following domain $\Omega$ of arbitrary shape:

```{figure} ./figures/potato1.svg
---
height: 200px
name: potato1 
---
Deformation of an arbitrary two-dimensional domain $\Omega$. 
```

where the solid is subjected to body loads $\mbf{b}$, prescribed tractions $\mbf{t}$ at surface $\Gamma_N$ and prescribed displacements at surface $\Gamma_D$. Assume the body moves as the loads are applied, and we represent this movement by the displacement vector $\bu$ shown above. In the more general 3D case, we can decompose $\bu$ into three components along our coordinate system axes, and we are therefore interested in solving for a vector field:

$$
\bu(\bx) \equiv \myVec{u_x(x,y,z)\\u_y(x,y,z)\\u_z(x,y,z)}
$$(c-c-dispvectordefinition)

Part of this displacement does not generate deformations, and are therefore called **rigid-body** motions. We are actually more interested in how the body actually deforms. For this we need to adopt a measure of strain. In this chapter we will be confining ourselves to small displacements and small strains. Under these assumptions, we can define strains as a tensor:

$$
\varepsilon_{ij} = \displaystyle\frac{1}{2}\left(u_{i,j}+u_{j,i}\right)
$$(c-c-straindefinition)

where $i,j\in\{1,2,3\}$. In matrix/vector notation this can also be written as:

$$
\beps = \nabla^\mrm{s}\bu = \displaystyle\frac{1}{2}\left(\nabla\bu+\left(\nabla\bu\right)\T\right)
$$(c-c-straindefmatvec)

where $\nabla^\mrm{s}$ is the *symmetric gradient operator*. We can also look at the strain tensor component by component:

$$
\beps = \myMat{
\varepsilon_{xx} & \varepsilon_{xy} & \varepsilon_{xz}\\
\varepsilon_{yx} & \varepsilon_{yy} & \varepsilon_{yz}\\
\varepsilon_{zx} & \varepsilon_{zy} & \varepsilon_{zz}\\
} =
\myMat{
u_{x,x}                      & \frac{1}{2}(u_{x,y}+u_{y,x}) & \frac{1}{2}(u_{x,z}+u_{z,x})\\ 
\frac{1}{2}(u_{y,x}+u_{x,y}) & u_{y,y}                      & \frac{1}{2}(u_{y,z}+u_{z,y})\\
\frac{1}{2}(u_{z,x}+u_{x,z}) & \frac{1}{2}(u_{z,y}+u_{y,z}) & u_{z,z}\\
}
$$(c-c-straintensorallcomps)

from where we can see that $\beps$ is symmetric, as expected. We can also switch to **Voigt notation** and represent strains as a vector instead:

$$
\beps = \myVec{\varepsilon_{xx}\\\varepsilon_{yy}\\\varepsilon_{zz}\\2\varepsilon_{xy}\\2\varepsilon_{yz}\\2\varepsilon_{zx}} = \myVec{\varepsilon_{xx}\\\varepsilon_{yy}\\\varepsilon_{zz}\\\gamma_{xy}\\\gamma_{yz}\\\gamma_{zx}} = \myVec{u_{x,x}\\u_{y,y}\\u_{z,z}\\u_{x,y}+u_{y,x}\\u_{y,z}+u_{z,y}\\u_{z,x}+u_{x,z}}
$$(c-c-strainvectorallcomps)

## Constitutive relations

Stress is a measure of internal forces inside a material, and is intrinsically linked to strains. Stresses are represented by a tensor $\bsig$ and can be related to surface tractions through:

$$
\mbf{t} = \bsig\cdot\mbf{n}
$$(c-c-traction)

which are in turn related related to loads the body $\Omega$ is subjected to. In the expression above, $\mbf{n}$ is the unit normal vector to the surface on which the tractions act. The stress tensor has components:

$$
\bsig = \myMat{
\sigma_{xx} & \sigma_{xy} & \sigma_{xz}\\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz}\\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}\\
}
$$(c-c-stresstensorallcomps)

where the first index of each component associates it to a specific surface in an infinitesimal cubic material volume, and the second index indicates the direction of the stress.

For linear-elastic materials, there is a **constant mapping** between stresses and strains that depends on the Young's modulus $E$ and the Poisson's ratio $\nu$. Working with full strain and stress tensors, this mapping would be a fourth-order tensor:

$$
\bsig = \bs{\mathcal{C}}:\beps
$$(c-c-tensorhooke)

which is known as **Hooke's Law**. The tensor $\bs{\mathcal{C}}$ can be written in index notation as:

$$
\mathcal{C}_{ijkl} = \mu(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}) + \lambda\delta_{ij}\delta_{kl}
$$(c-c-ctensor)

where $\lambda$ and $\mu$ are the so-called *Lamé constants*:

$$
\lambda=\displaystyle\frac{\nu E}{(1+\nu)(1-2\nu)}
\quad\quad
\mu = \displaystyle\frac{E}{2(1+\nu)}
$$(c-c-lameconstants)

Working in Voigt notation and exploiting symmetries in $\bs{\mathcal{C}}$, we can reach a matrix-vector version of Hooke's Law in three dimensions:

$$
\myVec{\sigma_{xx}\\\sigma_{yy}\\\sigma_{zz}\\\sigma_{xy}\\\sigma_{yz}\\\sigma_{zx}}
  =
  \frac{E}{(1+\nu)(1-2\nu)}
  \myMat{1-\nu & \nu   & \nu   & 0 & 0 & 0\\
	   \nu & 1-\nu & \nu   & 0 & 0 & 0\\
	   \nu &   \nu & 1-\nu & 0 & 0 & 0\\
	   0   & 0     & 0     & \frac{1-2\nu}{2} & 0 & 0\\
	   0   & 0     & 0     & 0 & \frac{1-2\nu}{2} & 0\\
	   0   & 0     & 0     & 0 & 0 & \frac{1-2\nu}{2}\\
	}
\myVec{\varepsilon_{xx}\\\varepsilon_{yy}\\\varepsilon_{zz}\\\gamma_{xy}\\\gamma_{yz}\\\gamma_{zx}}
$$(c-c-matrixhooke)

which we can write more compactly as:

$$
\bsig = \mbf{D}\beps
$$(c-c-matrixhookecompact)

When working in two dimensions (i.e. in the $x-y$ plane), we need an extra assumption of how the material behaves out of plane. There are two main possibilities:

```{card} 
**Plane strain assumption**
^^^
Assume that all out-of-plane strain components are zero:

$$
\varepsilon_{zz} = \gamma_{yz} = \gamma_{zx} = 0
$$

Hooke's Law reduces to:

$$
\myVec{\sigma_{xx}\\\sigma_{yy}\\\sigma_{xy}}
=
\frac{E}{(1+\nu)(1-2\nu)}
\myMat{1-\nu & \nu & 0\\ \nu & 1-\nu & 0\\ 0 & 0 & \frac{1-2\nu}{2}}
\myVec{\varepsilon_{xx}\\\varepsilon_{yy}\\\gamma_{xy}}
$$
```

```{card} 
**Plane stress assumption**
^^^
Assume that the all out-of-plane stress components are zero:

$$
\sigma_{zz} = \sigma_{yz} = \sigma_{zx} = 0
$$

Hooke's Law reduces to:

$$
\myVec{\sigma_{xx}\\\sigma_{yy}\\\sigma_{xy}}
=
\frac{E}{1-\nu^2}
\myMat{1 & \nu & 0\\ \nu & 1 & 0\\ 0 & 0 & \frac{1-\nu}{2}}
\myVec{\varepsilon_{xx}\\\varepsilon_{yy}\\\gamma_{xy}}
$$
```

## Equilibrium equations

To get to a final strong-form PDE we need to enforce stress equilibrium over our domain $\Omega$. We can arrive at a result in two ways. First, consider the small volume of material $\Delta\Omega$ shown below:

```{figure} ./figures/potato2.svg
---
height: 250px
name: potato2 
---
Stresses acting on a small piece of continuum $\Omega$.
```

where we use only two dimensions for simplicity. Translational equilibrium in $x$ and $y$ directions within this domain therefore requires:

$$
\displaystyle\frac{\partial\sigma_{xx}}{\partial x} + \frac{\partial\sigma_{xy}}{\partial x} + b_x = 0
\quad\quad
\displaystyle\frac{\partial\sigma_{yy}}{\partial y} + \frac{\partial\sigma_{yx}}{\partial y} + b_y = 0
$$(c-c-transequilibrium2d)

For the rotational equilibrium the easiest is to compute the moments at the center of the volume. This leads to:

$$
\sigma_{xy} = \sigma_{yx}
$$(c-c-rotequilibrium2d)

or, in other words $\bsig=\bsig\T$, which means the stress tensor should be symmetric.

Another way to arrive at the same result is to consider the equilibrium of the whole body $\Omega$ in an integral sense:

$$
\displaystyle\int_\Gamma\bsig\cdot\mbf{n}\,\ud\Gamma + \int_\Omega\mbf{b}\,\ud\Omega = 0
$$(c-c-transequilibrium3d-1)

With the divergence theorem we can turn the integral in $\Gamma$ into an integral in $\Omega$. Then, putting both terms together we have:

$$
\displaystyle\int_\Omega\nabla\cdot\bsig + \mbf{b}\,\ud\Omega = \mbf{0}
$$(c-c-transequilibrium3d-2)

and since this must hold not only in an integral sense but also at any specific point in $\Omega$, we require:

$$
\nabla\cdot\bsig+\mbf{b}=\mbf{0}
\quad\text{in}\,\,\Omega
$$(c-c-transequilibrium3d-3)

Enforcing moment equilibrium is a bit more involved, but results again in the requirement that $\bsig$ is symmetric.

