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
$\newcommand{\mbf}[1]{\mathbf{#1}}$
$\newcommand{\mrm}[1]{\mathrm{#1}}$
$\newcommand{\bs}[1]{\boldsymbol{#1}}$
$\newcommand{\T}{^\mathrm{T}}$
$\newcommand{\inv}{^{-1}}$
$\newcommand{\myVec}[1]{\left\{ \begin{matrix} #1 \end{matrix} \right\}}$
$\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$
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

# Plasticity

## Overview
Elasto-plasticity is the study of materials that exhibit both elastic and plastic deformation. This chapter starts with the tangent stiffness matrix for FEM. Then various yield functions for plasticity will be covered, including their application in various materials. Then other important topics such as hardening/softening plasticity, additive decomposition and the flow rule are explained. Using this information the continuum tangent is derived. Loading conditions and multi-surface plasticity are also considered.

## Basic Equations for FEM
When using the Finite element method, we often make use of a system of equations. This is fundamental in the iterative process of solving finite element equations, ensuring that the external forces applied to the system are balanced by the internal forces generated due to the deformation induced by the current solution vector a.

$$
\mbf{K \Delta a} = \mbf{f_e} - \mbf{f_i} 
$$(p-l-displacement control)


### Tangent stiffnes matrix
If a tangent stiffness matrix is used, $\mbf{D_i}$ can be determined at integration point level with the following equation:

$$
\mbf{\Delta \sigma} = \mbf{D_i \Delta \varepsilon}
$$(p-l-D_i_local)

Using this information, the system can be assembled at a global level.

$$
\mbf{K} = \int_V \mbf{B^T D_i B} \ \ud V
$$(p-l-K)

### Stress update
The stresses can be calculated at integration point (local) level using Eq. {eq}`p-l-D_i_local` and Eq. {eq}`p-l-sigmadt`.

$$
\mbf{\sigma^{t+\Delta t}} = \mbf{\sigma^t + \Delta \sigma}
$$(p-l-sigmadt)

Furthermore, the internal force vector can be assembled at global level using:

$$
\mbf{f_i} = \int_V \mbf{B^T \sigma^{t+\Delta t}} \ \ud V
$$(p-l-forcevector)

The stiffness matrix $\mbf{D}$ is thus of great importance for elasto-plasticity. Further down, the continuum tangent matrix $\mbf{D_i}$ will be derived, but it is important to first tackle some additional theory required. Those ingredients for flow theory of plasticity are:
- Yield functions
- Hardening / softening law
- Flow Rule

```{Admonition} Remarks
Note that this theory is only valid if it satisfies the following conditions:
- Restrict to small strains
- Additive decomposition of strains
- Elastic unloading
```

## Yield Functions
Different materials have distinct yield functions:
- **Metals (pressure-independent, ductile):** Tresca, Von Mises, Gurson.
- **Soils (pressure-dependent, brittle):** Mohr-Coulomb, Drucker-Prager, Cam-clay.
- **Composites/Wood (anisotropic):** Hill, Hoffman, Tsai-Wu.
- **Concrete:** Rankine, Ottosen, Willam/Warnke.

### Mohr-Coulomb

### Tresca

### Von Mises

### Drucker Prager

### Yield Surface Representation:
Graphical representations in different stress spaces are:
- 3D
- 2D
- π-plane

```{dropdown} π-Plane (Deviatoric Plane)
The π-plane is a plane in the three-dimensional deviatoric stress space. It is orthogonal to the hydrostatic axis (the line where the stress states are purely hydrostatic, i.e., no deviatoric stress component). In this plane, the hydrostatic stress component is zero, and only the deviatoric stress components are considered.

#### Visualization

In the π-plane:

- The coordinates are usually the principal deviatoric stresses \((s_1, s_2, s_3)\).
- The condition \(s_1 + s_2 + s_3 = 0\) (because they are purely deviatoric) simplifies the representation to a two-dimensional plane.

#### Yield Surfaces on the π-Plane

Yield functions define surfaces in stress space. When projected onto the π-plane, these yield surfaces help visualize the material's yield behavior under different stress states:

- **Von Mises Yield Criterion**: In the π-plane, this yield surface appears as a circle. This criterion assumes that yielding occurs when the second deviatoric stress invariant reaches a critical value, which corresponds to a circular shape in the π-plane.
- **Tresca Yield Criterion**: This yield surface appears as a hexagon in the π-plane. The Tresca criterion is based on the maximum shear stress theory, leading to a hexagonal shape when represented in the π-plane.
- **Other Criteria**: Different materials and yield criteria will have different shapes in the π-plane, such as ellipses or more complex polygons, depending on the material's specific yield characteristics.

#### Importance of the π-Plane

- **Simplification**: The π-plane provides a simplified, yet insightful view of the yield condition by focusing only on the deviatoric stresses.
- **Material Behavior**: Understanding how different materials yield under deviatoric stresses is crucial for designing components that can withstand specific loading conditions without permanent deformation.
- **Comparison**: It allows for an easier comparison of different yield criteria and their implications on material behavior under multi-axial loading conditions.
```

A good overview of the different yield functions and failure theories, including yield surface representations, is given in the video below.
```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/xkbQnBAOFEg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Hardening/Softening Plasticity
### Hardening
- **Isotropic Hardening:** The yield surface expands uniformly.
- **Kinematic Hardening:** The yield surface translates in stress space.

### Softening
- The yield surface contracts, leading to material degradation.

## Flow Rules
### Associated Flow Rule
- The plastic potential function \( g \) is the same as the yield function \( f \).
- Ensures normality condition: \( \dot{\epsilon}^p = \lambda \frac{\partial f}{\partial \sigma} \).

### Non-associated Flow Rule
- The plastic potential function \( g \) is different from the yield function \( f \).
- Provides better predictions for volume changes in certain materials like soils.

## Tangent Operator
- The consistent tangent operator \( D^t \) is used in numerical implementations to ensure quadratic convergence in Newton-Raphson iterations.

## Loading/Unloading Conditions
- Governed by Kuhn-Tucker conditions:
  \[
  f \leq 0, \quad \lambda \geq 0, \quad \lambda f = 0
  \]

## Multi-surface Plasticity
- Involves multiple yield surfaces or different loading conditions.
- The plastic strain rate is a linear combination of individual strain rates from each yield surface.