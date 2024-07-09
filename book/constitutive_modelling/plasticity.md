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
Elasto-plasticity is the study of materials that exhibit both elastic and plastic deformation. This chapter starts with the tangent stiffness matrix for FEM. Then various yield functions for plasticity will be covered, including their application in various materials. Combining hardening/softening plasticity, additive decomposition and the flow rule the continuum tangent is derived. Associative- and non-associative plasticity is also considered, along with loading conditions and multi-surface plasticity.

## Basic Equations for FEM
When using the Finite element method, we often make use of a system of equations. This is fundamental in the iterative process of solving finite element equations, ensuring that the external forces applied to the system are balanced by the internal forces generated due to the deformation induced by the current solution vector a.

$$
K \Delta a = f_e - f_i 
$$(p-l-displacement control)

If a tangent stiffness matrix is used $D_i$ can be determined at integration point level with the following equation:

$$
\Delta \sigma = D_i \Delta \varepsilon
$$(p-l-D_i local)

Using this information, the system can be assembled at a global level: integration point level with the equation **D_i local**.

$$
\mbf{K} = \int \nabla\cdot\mbf{a} \,\ud\Omega = \int_{\Gamma}\mbf{a}\cdot\mbf{n}\
$$(p-c-K_element)


## Yield Functions
Different materials have distinct yield functions:
- **Metals (pressure-independent):** Tresca, Von Mises, Gurson.
- **Soils (pressure-dependent):** Mohr-Coulomb, Drucker-Prager, Cam-clay.
- **Composites/Wood (anisotropic):** Hill, Hoffman, Tsai-Wu.
- **Concrete:** Rankine, Ottosen, Willam/Warnke.

## Yield Surface Representation:
Graphical representations in different stress spaces are:
- 3D
- 2D
- π-plane

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

## Important Concepts
- **Prager’s Consistency Condition:** During plastic flow, \( \dot{f} = 0 \).
- **Hardening Modulus \( h \):**
  \[
  h = -\frac{1}{\lambda} \frac{\partial f}{\partial \kappa} \kappa
  \]


