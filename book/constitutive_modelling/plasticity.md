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
The Mohr-Coulomb failure criterion is a model used in geotechnical engineering to predict material failure under shear stress. It states that failure occurs when the shear stress ($\tau$) on a plane reaches a critical value defined by {eq}`p-l-taucrit`.

$$
\mbf{\tau_{crit}} = \mbf{- \sigma \ tan(\phi)+c}
$$(p-l-taucrit)

where:
- c is the cohesion of the material (internal strength)
- $\sigma$ is the normal stress acting on the plane
- $\phi$ is the angle of internal friction (resistance to sliding)

This criterion helps engineers assess stability of structures like slopes and foundations. The following figure gives the critical envelope of Mohr-Coulomb.

```{figure} Images/mohr_coulomb_tau_sigma.png
---
---
Mohr-Coulomb
```

Eq. {eq}`p-l-taucrit` ca also be written as Eq. {eq}`p-l-taucrit2`, which will later be used to obtain the Mohr Coulomb yield function.

$$
\mbf{\tau_{crit}+\sigma \ tan(\phi)-c} = 0
$$(p-l-taucrit2)

Using trigonometry the critical envelope for Mohr-Coulomb in terms of principal stresses can be obtained.
```{Note}
It must hold that $\sigma_1 < \sigma_2 < \sigma_3$
``` 

```{figure} Images/mohr_coulomb_circle.png
---
---
Mohr circle
```

Expressions for the shear and normal stress are given in Eq. {eq}`p-l-shearstress` and Eq. {eq}`p-l-normalstress`, respectively.

$$
\mbf{\tau} = \mbf{\frac{1}{2}(\sigma_3 - \sigma_1) cos{\phi}}
$$(p-l-shearstress)

$$
\mbf{\sigma} = \mbf{\frac{1}{2}(\sigma_1 + \sigma_3 ) + \frac{1}{2}(\sigma_3 - \sigma_1) sin{\phi}}
$$(p-l-normalstress)

When substituting Eq. {eq}`p-l-shearstress` and Eq. {eq}`p-l-normalstress` into Eq. {eq}`p-l-taucrit2`, the following equation (Eq. {eq}`p-l-yieldfunction_1`) is derived:

$$
\mbf{\frac{1}{2}(\sigma_3 - \sigma_1) + \frac{1}{2}(\sigma_1 + \sigma_3)sin(\phi)-c \ cos(\phi)} = 0
$$(p-l-yieldfunction_1)

This function written as a function of the stress in Eq. {eq}`p-l-yieldfunction_2`, is know as the $\textcolor{red}{\mbf{Mohr \ Coulomb \ yield \ function}}$.

$$
\textcolor{red}{\mbf{f(\sigma)} = \mbf{\frac{1}{2}(\sigma_3 - \sigma_1) + \frac{1}{2}(\sigma_1 + \sigma_3)sin(\phi)-c \ cos(\phi)}}
$$(p-l-yieldfunction_2)

Using 6 permutations for $\sigma_1$, $\sigma_2$ and $\sigma_3$ Mohr-Coulomb can be defined. By using a state of uniaxial compression, meaning that $\sigma_3 = 0$ and $\sigma_2 = 0$, an equation for $\sigma_1$ can be derived.

$$
\mbf{\sigma_1} = \mbf{-\frac{2c \ cos(\phi)}{1-sin(\phi)}}
$$(p-l-sigma_1)

If the uniaxial compressive strength is defined as $\mbf{\sigma_1} = \mbf{f_c}$, the cohesion parameter can be 'measured' using the expression of {eq}`p-l-cohesion`.

$$
\mbf{c} = \mbf{\frac{1-sin(\phi)}{2 \ cos(\phi)}f_c}
$$(p-l-cohesion)

```{figure} Images/mohr_coulomb_uniaxial_compression.png
---
---
Mohr circle for uniaxial compression
```

### Drucker Prager
The $\textcolor{red}{\mbf{Drucker-Prager \ yield \ function}}$ is a smooth approximation of Mohr-Coulomb, this means there are no corners.

$$
\textcolor{red}{\mbf{f(\sigma)} = \mbf{\sqrt{\frac{1}{2}((\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}) + \frac{1}{3}\alpha(\sigma_1 + \sigma_2 + \sigma_3) - k} = \mbf{\sqrt{J_2} + \alpha p - k}}
$$(p-l-druckerprageryield)

where:
- $\mbf{J_2}$ is the 2nd deviatoric stress invariant
- $\mbf{p}$ is the hydrostatic stress
- $\mbf{\alpha}$ and $\mbf{k}$ material constants

 Drucker-Prager coincides with 3 outer points of Mohr-Coulomb (in π -plane or two-dimensional principal stress space) if the conditions in {eq}`p-l-alpha` and {eq}`p-l-k` are met. This is illustrated in the figure below.

$$
\mbf{\alpha} = \mbf{\frac{6 sin(\phi)}{3 - sin(\phi)}}
$$(p-l-alpha)

$$
\mbf{k} = \mbf{\frac{6 c \ cos(\phi))}{3 - sin(\phi)}}
$$(p-l-k)

```{figure} Images/mohr_coulomb_drucker_prager.png
---
---
Mohr Coulomb and Drucker Prager
```

Both functions contain a point where $\mbf{\sigma_1} = \mbf{\sigma_2} = \mbf{\sigma_3}$, which is called the apex. Substitution of this property in the Mohr-Coulomb function gives $\mbf{\sigma_1} = \mbf{\sigma_2} = \mbf{\sigma_3} = \mbf{\frac{c \ cos(\phi)}{sin(\phi)}} = \mbf{c \ cot(\phi)}$. The apex is defined as $\mbf{(c \ cot(\phi), c \ cot(\phi), c \ cot(\phi))} = \mbf{a}$. The distance to the origin is $\mbf{|a|_2} = \mbf{\sqrt{a^T a}} = \mbf{\sqrt{3} \ c \ cot(\phi)}$.

### Tresca

The Tresca yield criterion, also known as the maximum shear stress criterion, is a material failure theory used in the field of solid mechanics. It predicts the onset of plastic deformation in ductile materials under complex loading conditions. This criterion is named after the French mechanical engineer Henri Tresca.

The Tresca yield criterion states that yielding begins when the maximum shear stress in a material reaches a critical value. This critical value is equivalent to the shear stress at yield in a simple tension test. Mathematically, the Tresca criterion can be expressed as in equation {eq}`p-l-tresca`, which can be rewritten as the Tresca yield function in {eq}`p-l-tresca_yield`.

$$
\mbf{\tau_{crit}} = \mbf{\frac{1}{2}(\sigma_3 - \sigma_1)} = \mbf{c}
$$(p-l-tresca)

$$
\textcolor{red}{\mbf{f(\sigma)} = \mbf{\frac{1}{2}(\sigma_3 - \sigma_1) - c}}
$$(p-l-tresca_yield)

Using 6 permutations for $\sigma_1$, $\sigma_2$ and $\sigma_3$, similar to Mohr-Coulomb, Tresca can be defined. By using a state of uniaxial compression, meaning that $\sigma_3 = 0$ and $\sigma_2 = 0$, an equation for $\sigma_1$ can be derived in {eq}`p-l-sigma_1_tresca`. If the uniaxial compressive strength is defined as $\mbf{\sigma_1} = \mbf{f_c}$, the cohesion parameter can be 'measured' using the expression of {eq}`p-l-cohesion_tresca`.

$$
\mbf{\sigma_1} = \mbf{2c}
$$(p-l-sigma_1_tresca)

$$
\mbf{c} = \mbf{\frac{1}{2}f_c}
$$(p-l-cohesion_tresca)

```{figure} Images/tresca.png
---
---
Tresca yield criterion
```

```{Admonition} Do you see that...
:class: tip
...Mohr-Coulomb with friction angle $\phi = 0$ gives Tresca
```

The Tresca yield criterion is widely used in engineering applications, particularly in designing components subjected to complex loading conditions, such as shafts, pressure vessels, and structural beams.

The Tresca yield criterion provides a straightforward approach to predicting the onset of plastic deformation in ductile materials based on the maximum shear stress. While less accurate than the von Mises criterion, its simplicity makes it a useful tool in many practical engineering scenarios.

### Von Mises
The Tresca criterion is often compared with the von Mises yield criterion, which is another common theory for predicting yielding in ductile materials. While the von Mises criterion assumes that yielding begins when the second deviatoric stress invariant reaches a critical value, the Tresca criterion is based on the maximum shear stress. Generally, the von Mises criterion is considered more accurate for predicting yielding in many materials, but the Tresca criterion is simpler and more conservative. Von Mises is a smooth approximation of Tresca without corners, the yield function is given in equation {eq}`p-l-vonmises_yield` and simplified in equation {eq}`p-l-vonmises_yield_simplified`.

```{figure} Images/tresca_vonmises.png
---
---
Tresca and Von Mises yield criterion
```

$$
\textcolor{red}{\mbf{f(\sigma)} = \mbf{\sqrt{\frac{1}{2}((\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2)} - \sigma_{uni}}}
$$(p-l-vonmises_yield)

$$
\textcolor{red}{\mbf{f(\sigma)} = \mbf{\sqrt{\frac{3}{2}(s_1^2 + s_2^2 + s_3^2)} - \sigma_{uni}} = \mbf{\sqrt{J_2}-\sigma_{uni}}}
$$(p-l-vonmises_yield_simplified)

where:
- $\mbf{J_2}$ is the 2nd deviatoric stress invariant
- $\mbf{\sigma_{uni}}$ is the uniaxial yield strength

```{Note}
Von Mises coincides with 6 outer points of Tresca (in π -plane or two-dimensional principal stress space)
Tresca and Von Mises are independent of p ⇒ pressure-independent
```

### Yield Surface Representation:
Graphical representations in different stress spaces are:
- 3D
- 2D

```{figure} Images/mc_vm_tr_dp.png
---
---
Left: Tresca and Von Mises, tension = compression;  
Right: Mohr-Coulomb and Drucker-Prager, tension $\neq$ compression
```

- Mohr circle
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
```{figure} Images/yield_piplane.png
---
---
Yield functions in π-Plane
```

A good overview of the different yield functions and failure theories, including yield surface representations, is given in the video below.
```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/xkbQnBAOFEg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Hardening/softening Plasticity

Hardening is a phenomenon where a material becomes stronger and more resistant to deformation as it is deformed plastically. Softening, conversely, is the reduction in strength and hardness of a material. In practical applications, materials often experience a combination of hardening and softening mechanisms. For instance, during cyclic loading (as seen in fatigue), a material may initially harden but eventually soften due to damage accumulation and microstructural changes. Understanding the interplay between hardening, softening, and plasticity is crucial for predicting the behavior of materials under various loading conditions, which is essential for designing components that can withstand mechanical stresses in real-world applications.

The simplest extension beyond the model of ideal plasticity as adopted in the previous yield function(s), is to make the yield function also dependent on a scalar measure of the plastic strain tensor:

$$
\mbf{f(\sigma)} = \mbf{f(\sigma, \kappa)}
$$(p-l-yield_depending_strain)

$$
\mbf{\kappa} = \mbf{\int \dot{\kappa} \ dt}
$$(p-l-kappa)

The scalar-valued hardening parameter $\kappa$ is typically dependent on the strain history through invariants of the plastic strain tensor $\varepsilon^p$. Another suitable, frame-invariant choice would be the dissipated plastic work. Although a host of possibilities now emerges, for any function of the invariants of $\varepsilon^p$ and/or the plastic work could serve the purpose, two choices have gained more popularity than most other propostions, namely the work-hardening hypothesis and the strain hardening hypothesis. While the former assumptions sets the rate of the hardening parameter equal to {eq}`p-l-work_hardening`, the latter possibility postulates that {eq}`p-l-strain_hardening`.
 
$$
\mbf{\dot{\kappa}} = \mbf{\sigma^T \dot{\varepsilon^p}}
$$(p-l-work_hardening)

$$
\mbf{\dot{\kappa}} = \mbf{\sqrt{\frac{2}{3}(\dot{\varepsilon^p})^T Q \dot{\varepsilon^p}}}
$$(p-l-strain_hardening)

where $\mbf{Q = diag[1, 1, 1, \frac{1}{2}, \frac{1}{2}, \frac{1}{2}]}$, which takes into account the effect that the shear strains incorporated in the vect0r format of $\varepsilon$ are in fact the double, engineering shear strains.


```{figure} Images/tresca_hardening.png 
---
---
Hardening/softening Tresca
```

```{figure} Images/vonmises_hardening.png
---
---
Hardening/softening Von Mises
```
Isotropic hardening: $\kappa$ is a scalar. The yield surface expands uniformly.  
Kinematic hardening: $\kappa$ is a vector (back stress), e.g. Bauschinger effect in metals. The yield surface translates in stress space.

```{dropdown} Bauschinger effect
The Bauschinger effect is a phenomenon observed in metals and alloys, where the material exhibits a reduction in yield strength when the direction of loading is reversed after plastic deformation. Named after the German engineer Johann Bauschinger, who first reported this effect in the late 19th century, it highlights the anisotropic nature of work hardening in materials.
```

## Continuum tangent matrix
In order to derive the tangent stiffness matrix $\mbf{D_i}$, some steps need to be explained. The first is the principle of additive decomposition of strains, meaning that strains consists out of an $\textbf{elastic}$ and $\textbf{plastic}$ part as in {eq}`p-l-decomposition_strains`.

$$
\mbf{\varepsilon} = \mbf{\varepsilon_e + \varepsilon_p} \rightarrow \mbf{\dot{\varepsilon}} = \mbf{\dot{\varepsilon_e} + \dot{\varepsilon_p}} \rightarrow \mbf{\dot{\varepsilon_e}} = \mbf{\dot{\varepsilon} - \dot{\varepsilon_p}}
$$(p-l-decomposition_strains)

Furthermore, for the elastic part it holds that:

$$
\mbf{\sigma} = \mbf{D_e \varepsilon_e} \rightarrow \mbf{\dot{\sigma}} = \mbf{D_e \dot{\varepsilon_e}}
$$(p-l-elastic_part)

For the plastic part, the flow rule can be used:

$$
\mbf{\dot{\varepsilon_p}} = \mbf{\dot{\lambda} m}
$$(p-l-plastic_part)

where:
- $\mbf{\dot{\lambda}}$ is the plastic multiplier, which gives the magnitude of plastic flow
- $\mbf{m}$ gives the direction of plastic flow

Substitution of {eq}`p-l-plastic_part` into {eq}`p-l-decomposition_strains` and subsequently in {eq}`p-l-elastic_part` gives:

$$
\mbf{\dot{\sigma}} = \mbf{D_e (\dot{\varepsilon} - \dot{\lambda} m)}
$$(p-l-sigma_der)


Using the yield function in {eq}`p-l-yield_depending_strain` and Prager's consistency condition given in {eq}`p-l-prager_condition`

$$
\mbf{\dot{f}(\sigma, \kappa)} = \mbf{0} \rightarrow \mbf{(\frac{\partial f}{\partial \sigma})^T \dot{\sigma} + (\frac{\partial f}{\partial \kappa}) \dot{\kappa}} = \mbf{0}
$$(p-l-prager_condition)

```{dropdown} Prager's consistency condition
Prager's consistency condition is a mathematical condition that ensures the consistency of the plastic state in a material undergoing kinematic hardening. It is derived from the principle that during plastic deformation, the stress state must always remain on the yield surface. This requires that the rate of change of the yield function must be zero during plastic flow.
```

It can be used that the gradient to the yield surface can be expressed as in equation {eq}`p-l-gradient_n`:

$$
\mbf{\frac{\partial f}{\partial \sigma}} = \mbf{n}
$$(p-l-gradient_n)

```{figure} Images/gradient_vector_n.png 
---
---
Orthogonality of gradient vector n to the yield surface $f = 0$
```

```{Admonition} Example gradient vector: Von Mises
:class: tip
$$
\mbf{f(\sigma, \kappa)} = \mbf{\sqrt{\frac{1}{2}((\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2)} - \sigma_{uni}(\kappa)}
$$(p-l-vonmises_gradient)

$$
 \mbf{n} = \mbf{\frac{\partial f}{\partial \sigma}} = \left[\begin{matrix}\frac{\partial f}{\partial \sigma_1} \\ \frac{\partial f}{\partial \sigma_2} \\ \frac{\partial f}{\partial \sigma_3} \end{matrix}\right] = \frac{1}{2 \sqrt{3 J_2}} \left[\begin{matrix}2 \sigma_1 - \sigma_2 - \sigma3 \\ 2 \sigma_2 - \sigma_3 - \sigma1 \\ 2 \sigma_3 - \sigma_1 - \sigma_2 \end{matrix}\right]
$$(p-l-vonmises_example)
```

Using the gradient vector, {eq}`p-l-prager_condition` can be rewritten as {eq}`p-l-prager_rewritten`.

$$
\mbf{n^T \dot{\sigma} - h \dot{\lambda}} = \mbf{0}
$$(p-l-prager_rewritten)

Here the hardening/softening modulus h is defined as in {eq}`h_mod`.

$$
\mbf{h} = \mbf{- \frac{1}{\dot{\lambda}} \frac{\partial f}{\partial \kappa} \dot{\kappa}}
$$(h_mod)

Equation {eq}`p-l-sigma_der` can be rewritten as in {eq}`sigma_der_rewritten`:

$$
\mbf{\dot{\varepsilon}} = \mbf{D_e^{-1} \dot{\sigma} + \dot{\lambda} m} 
$$(sigma_der_rewritten)

By eliminating $\dot{\lambda}$ from {eq}`sigma_der_rewritten`, the compliance form can be derived in {eq}`compliance`:

$$
\dot{\mbf{\varepsilon}} = \left[ \mbf{D}_e^{-1} + \frac{1}{h} \mbf{m} \mbf{n}^\mathrm{T} \right] \dot{\mbf{\sigma}}
$$(compliance)

This can be inverted with the Sherman-Morrison formulae to end up with {eq}`cont_tangent`. Between the brackets [], the final continuum tangent matrix $\mbf{D_i}$ has been obtained.

$$
\dot{\mbf{\sigma}} = \left[ \mbf{D}_e - \frac{\mbf{D}_e \mbf{m} \mbf{n}^\mathrm{T} \mbf{D}_e}{h + \mbf{n}^\mathrm{T} \mbf{D}_e \mbf{m}} \right] \dot{\mbf{\varepsilon}}
$$(cont_tangent)

## Associative Plasticity $\mbf{m = n}$

Associative plasticity in constitutive modeling refers to a type of material behavior where the yield surface evolves based on the stress history and the current stress state of the material. This approach is commonly used to model materials that exhibit complex behaviors under varying loading conditions, such as metals undergoing plastic deformation.

### Key Characteristics:
- Direction of plastic flow is equal to gradient yield surface
- Product $\mbf{n n^T}$ is symmetric $\rightarrow$ tangent stiffness $\mbf{D_i}$ is symmetric.
- Can be derived from Drucker's postulate (normality rule)

### Example:
In finite element simulations of metal forming processes, associative plasticity models like the von Mises yield criterion are often employed. These models accurately capture the material's ability to undergo plastic deformation under different stress states and loading conditions, facilitating the prediction of material flow and strain distribution.

## Non-Associative Plasticity $\mbf{m \neq n}$

Non-associative plasticity in constitutive modeling refers to models where the yield surface does not evolve with plastic deformation. $\mbf{n}$ and $\mbf{m}$ can be described as in {eq}`p-l-gradient_n`, respectively {eq}`p-l-gradient_m`, where g is the plastic potential.

$$
\mbf{\frac{\partial g}{\partial \sigma}} = \mbf{m}
$$(p-l-gradient_m)

### Key Characteristics:
- Direction of plastic flow is unequal to gradient yield surface
- Product $\mbf{m n^T}$ is non-symmetric $\rightarrow$ tangent stiffness $\mbf{D_i}$ is non-symmetric.

### Example:
For certain types of polymers or geological materials, non-associative plasticity models such as the Drucker-Prager model are commonly used. These models assume a fixed yield surface and focus on capturing the material's response to loading conditions without considering the history-dependent effects observed in associative plasticity models.

```{figure} Images/non_associated_flow_rule.png 
---
---
Non-associated flow
```

```{figure} Images/hardening_diagram.png 
---
---
Hardening diagram for metal plasticity
```

## Loading/Unloading Conditions
The Kuhn/Tucker loading conditions, often associated with the Kuhn-Tucker theorem, are used to determine when a material transitions from elastic to plastic behavior and to enforce the constraints of the yield condition during plastic deformation.

For rate independent elasto-plasticity the following equations hold {eq}`rate_indep_plasticity` and {eq}`lambda` :

$$
\mbf{f} \leq \mbf{0}
$$(rate_indep_plasticity)

$$
\mbf{\dot{\lambda}} \geq \mbf{0}
$$(lambda)

For the elastic state equation {eq}`elastic_state` and for the plastic state equation {eq}`plastic_state` hold.

$$
\mbf{f} < \mbf{0} \rightarrow \mbf{\dot{\lambda}} = \mbf{0}
$$(elastic_state)

$$
\mbf{f} = \mbf{0} \rightarrow \mbf{\dot{\lambda}} \neq \mbf{0}
$$(plastic_state)

During plastic flow, Prager's consistency condition gives {eq}`plastic_flow`:

$$
\mbf{\dot{f}} = \mbf{0}
$$(plastic_flow)

## Multi-surface Plasticity

The image below gives a corner in the yield surface and/or plastic potential function g (for multi-surface plasticity)

```{figure} Images/multi_surface_plasticity.png 
---
---
Multi-surface plasticity
```

The starting point for multi-surface plasticity is in equation {eq}`origin`:

$$
\mbf{\dot{\sigma}} = \mbf{D_e (\dot{\varepsilon} - \dot{\varepsilon^p})}
$$(origin)

Now the Koiter assumption {eq}`koiter`, stating that the flow rule is a linear combination ($\rightarrow$ no unique flow direction) comes in handy.

$$
\mbf{\dot{\varepsilon^p}} = \mbf{\dot{\lambda_1} m_1 + \dot{\lambda_2} m_2}
$$(koiter)

After ubstitution of {eq}`koiter` into {eq}`origin`, equation {eq}`substituted` is obtained. Furthermore, also {eq}`yield_zero1` and {eq}`yield_zero2` hold.

$$
\mbf{\dot{\sigma}} = \mbf{D_e (\dot{\varepsilon} - \dot{\lambda_1} m_1 - \dot{\lambda_2} m_2)}
$$(substituted)

$$
\mbf{f_1(\sigma)} = \mbf{0}
$$(yield_zero1)

$$
\mbf{f_2(\sigma)} = \mbf{0}
$$(yield_zero2)

The solution for the plane-stress case consists of 3 equations from {eq}`substituted`, equation {eq}`yield_zero1` and {eq}`yield_zero2`; meaning there are 5 equations in total. The unknowns are also 5 in total; 3 stress componenents ($\sigma_{xx}, \sigma_{yy}, \sigma_{xy}$) and $\mbf{\dot{\lambda_1}}$ and $\mbf{\dot{\lambda_2}}$.

```{Admonition} Remark
The consistency condition is not used!
```

