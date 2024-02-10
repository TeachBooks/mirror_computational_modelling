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
$\newcommand{\hpders}[2]{\displaystyle\frac{\partial^2 #1}{\partial #2^2}}$
$\newcommand{\myVec}[1]{\left\{ \begin{matrix} #1 \end{matrix} \right\}}$
$\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$
$\newcommand{\sym}{\ensuremath{_\mathrm{s}}}$
$\newcommand{\dg}{\ensuremath{^\circ}}$
$\newcommand{\mbf}[1]{\mathbf{#1}}$
$\newcommand{\mrm}[1]{\mathrm{#1}}$
$\newcommand{\bs}[1]{\boldsymbol{#1}}$
$\newcommand{\T}{^\mathrm{T}}$
$\newcommand{\dOmega}{\,\mathrm{d}\Omega}$
$\newcommand{\dGamma}{\,\mathrm{d}\Gamma}$
$\newcommand{\us}{\mathrm{s}}$
$\newcommand{\old}{_\mathrm{o}}$
$\newcommand{\new}{_\mathrm{n}}$
$\newcommand{\balpha}{\boldsymbol{\alpha}}$
$\newcommand{\fext}{\bff_\mathrm{ext}}$
$\newcommand{\fint}{\bff_\mathrm{int}}$

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

# Material non-linearity

In this page we give a brief overview of different types of material model, with focus on models for which the mapping between stresses $\bsig$ and strains $\beps$ is nonlinear. For several of the models we will see below, nonlinear behavior arises from an intrinsic dependency on **strain history**. For such models, it is therefore possible to deform the material up to the same value of $\beps$ but depending on the path we take we will end up with distinct values of $\bsig$ once we get there.

A common trait for this type of model is the definition of **internal variables** $\balpha$. These variables store the current state of the material, and effectively remove the non-uniqueness we mention above: **given** $\balpha$, the mapping between $\bsig$ and $\beps$ becomes unique:

$$
\bsig=\mathcal{M}\left(\beps,\balpha\right)
$$(sn-mn-general1)

where $\mathcal{M}$ represents a function or algorithm that computes material behavior. These state variables usually arise from robust thermodynamics principles and model phenomena that lead to energy dissipation and irreversible changes to material composition. Further details on the nature of these variables and how to arrive at a consistent thermodynamic treatment of material models will be left out of scope for this book. 

For our discussion here, it suffices to assume that if we know the current value of $\balpha$ we can compute $\bsig$ for any value $\beps$ **without the need to store the complete history of $\beps$** since the beginning of the simulation. It is also important to mention that since these internal variables evolve as the result of irreversible phenomena, we should only update $\balpha$ once equilibrium is reached. In other words, intermediate values we obtain during Newton-Raphson iterations should be discarded.

Taking all the aforementioned points into consideration, here is an algorithm for a FEM simulation in displacement control considering a nonlinear and history-dependent material model:

```{card}
**Displacement control with material history**
^^^

**Require**: Nonlinear relation $\bff_\mrm{int}(\ba)$ with $\bK(\ba) = \pder{\bff_\mrm{int}}{\ba}$

**Initialize**: $n=0$, $\ba^0=\mbf{0}$, $\balpha\old=\mbf{0}$ partition DOFs into *free* ($f$) and *constrained* ($c$)

- **while** $n<\text{number of time steps}$:
    - Get new external force vector: $\bff_\mrm{ext}^{n+1}$
    - Initialize new solution at old one: $\ba^{n+1} = \ba^n$
    - Update material model: $\bsig^{n+1},\bD^{n+1},\balpha\new = \mathcal{M}\left(\beps^{n+1},\balpha\old\right)$
    - Compute internal force and stiffness: $\fint^{n+1} = \hint_\Omega\bB^\mathrm{T}\bsig^{n+1}\ud\Omega$, $\bK^{n+1} = \hint_\Omega\bB^\mathrm{T}\bD^{n+1}\bB\ud\Omega$
    - Constrain $\bK^{n+1}$ so that $\Delta\ba_c=\bar{\ba}^{n+1}-\bar{\ba}^{n}$
    - Evaluate residual at free DOFs: $\mbf{r} = - \bff_{\mrm{int},f}^{n+1}$
    - **while** $|\mbf{r}| < \text{tolerance}$:
        - Solve linear system of equations: $\bK^{n+1} \Delta\ba = \mbf{r}$
        - Update solution: $\ba^{n+1} = \ba^{n+1} + \Delta\ba$
        - Update material model: $\bsig^{n+1},\bD^{n+1},\balpha\new = \mathcal{M}\left(\beps^{n+1},\balpha\old\right)$
        - Compute internal force and stiffness: $\fint^{n+1} = \hint_\Omega\bB^\mathrm{T}\bsig^{n+1}\ud\Omega$, $\bK^{n+1} = \hint_\Omega\bB^\mathrm{T}\bD^{n+1}\bB\ud\Omega$
        - Evaluate residual at free DOFs: $\mbf{r} = - \bff_{\mrm{int},f}^{n+1}$
        - Constrain $\bK^{n+1}$ so that $\Delta\ba_c=0$
    - Commit material history: $\balpha\old = \balpha\new$
    - Go to the next time step: $n=n+1$

**Return**: Set of internal forces and displacements (equilibrium path)
```

Since the integrals we use to compute $\bff_\mrm{int}$ and $\bK$ are {doc}`performed numerically<introduction/numerical_integration>` we need to store a unique $\balpha$ for every integration point in the mesh. Note also that since $\balpha$ should only be updated upon equilibrium, we keep using its old values $\balpha\old$ for every solver iteration of a given time step, and only overwrite it with new values at the end of the step (the values will therefore be the latest ones, from the final iteration before convergence). Finally, note that we need $\bK$ to be a consistent linearization of $\bff_\mrm{int}$, {doc}`as previously discussed<linearization>`. This means that we need to compute $\bD$ as:

$$
\bD = \hpder{\bsig}{\beps}
$$(sn-mn-general2)

## Elasticity

We briefly recap linear elasticity here to contrast it with other models. Under the assumption of linearity, stresses are simply:

$$
\bsig=\bD\beps
$$(sn-mn-hyperelasticity)

where $\bD$ is a **constant** stiffness matrix. For the actual matrices, refer back to our discussion on the {doc}`strong form for linear elasticity<continuum_linear/continuum_mechanics>`. Looking at a one-dimensional version of this model we would see: 

```{figure} ./figures/matelastic.svg
---
height: 200px
name: matelastic 
---
Stress-strain behavior arising from a linear-elastic model.
```

where the behavior is linear, as expected. We also see that loading and unloading (represented by the arrows) always happens through the same path, as the mapping between $\bsig$ and $\beps$ is unique. Since deformation is fully reversible in this case, we have no need for internal variables.

Most materials behave elastically for small amounts of deformation, and for some materials (e.g. glass) linear elasticity can be a good approximation of material behavior up until failure. It is therefore widely adopted by the solid mechanics community.

## Hyperelasticity

In hyperelasticity we also assume full reversibility of deformations, but now the mapping between strains and stresses is nonlinear:

```{figure} ./figures/mathyperelastic.svg
---
height: 200px
name: mathyperelastic 
---
Stress-strain behavior arising from a hyperelastic model.
```

In hyperelasticity, this nonlinearity is explained by a complex (though still unique) mapping between strains and an energy potential $W$ from which stresses and stiffness can be obtained through differentiation:

$$
W(\beps) \gives \bsig=\hpder{W}{\beps} \gives \hpder{\bsig}{\beps} = \hpders{W}{\beps}
$$(sn-mn-hyperelasticity)

A classic example of material that deforms hyperelastically is rubber. Certain polymers can also be well described by the theory, as are some other materials of interest such as carbon fibers. A wide range of hyperelastic models is available in literature, and new models specially tuned for specific materials or discovered through machine learning are active fields of research.

## Viscoelasticity

Viscoelastic material models attempt to combine a solid-like (time-independent) contribution to stresses with a fluid-like response which evolves in time even when holding the material at a constant stress or a constant strain. This time dependency makes the instantaneous response of the material nonlinear and dependent not only on the strain path but also on the rate of the application of strains. The viscous contributions introduce a time-dependent stiffness contribution that makes the material unload through a different path that gives rise to **hysteresis**:

```{figure} ./figures/matviscoelastic.svg
---
height: 200px
name: matviscoelastic
---
Stress-strain behavior arising from a viscoelastic model.
```

The stress response can be written as a combination of long-term and viscous contributions:

$$
\bsig = \bD_\infty\beps + \hint_0^t\bD_\mathrm{ve}\left(t-\tilde{t}\right)\hpder{\beps}{\tilde{t}}\ud\tilde{t}
$$(sn-mn-viscoelasticity)

with the viscous contribution involving an integral in time which can be cumbersome to compute. In practice it is handled using discrete time steppers that allow for updating material state step by step without having to store the full strain history. The internal variables here are usually the viscoelastic stresses $\bsig_\mrm{ve}$.

Many materials can be well described by viscoelastic models, an important one being asphalt binders. Models are usually constructed with a set of long-term (springs) and viscous (dashpots) elements arranged in series and/or parallel.

## Elasto-plasticity

The goal of elastoplasticity is to describe the occurrence of permanent deformations in materials. This is usually done by assuming an additive split of strains into **elastic** and **plastic** parts, and further assuming that only elastic strains produce stresses:

$$
\beps=\beps^\mathrm{e}+\beps^\mathrm{p}
\quad\Rightarrow\quad
\bsig = \bD\left(\beps-\beps^\mathrm{p}\right)
$$(sn-mn-plasticity1)

with $\bD$ being the same stiffness matrix adopted for elasticity. A key assumption in plasticity is that plastic strains are **irreversible**. This implied that if the material is unloaded back to zero stress, it will not unload back to zero strains:

```{figure} ./figures/matplastic.svg
---
height: 200px
name: matplastic
---
Stress-strain behavior arising from an elastoplastic model.
```

The evolution of plastic strains $\beps^\mathrm{p}$ is dictated by a **yield surface** $f(\bsig)$. We assume that stresses can increase only up until the yield surface is reached, after which point all extra deformation will be plastic and therefore generate no stresses:

$$
f\left(\bsig\right) = \tilde{\bsig} - \sigma_y\left(\kappa\right)
$$(sn-mn-plasticity2)

where $\tilde{\bsig}$ is an equivalent stress measure. Note that since plastic strains do not generate stresses, $f(\bsig)\leq 0$. The **yield stress** $\sigma_y$ represents the stress level after which plastic strains evolve, and can be made to evolve during loading based on an internal variable $\kappa$ that quantifies the accumulated plastic strain. If $\sigma_y$ increases with $\kappa$ we say the material is **hardening**; if it decreases we speak of **softening**.

Internal variables $\balpha$ for plasticity models usually include at least $\kappa$ and the current plastic strain $\beps^\mathrm{p}$. A wide range of materials can be modeled as elastoplastic, from metals to polymers. It is one of the most widely employed material models in solid mechanics.

## Damage

Damage models describe material failure through a distributed fracture process that effectively amounts to a **loss of load-bearing area**. Numerically, this is modeled as a loss of stiffness, usually described by a single damage indicator $d$ satisfying $0\leq d\leq 1$:

$$
\bsig=\left(1-d\right)\bD\beps
$$(sn-mn-damage1)

Loading the material causes damage to evolve, resulting in nonlinear stress-strain behavior. The loss of stiffness that drives this nonlinearity becomes evident when the material is unloaded:

```{figure} ./figures/matdamage.svg
---
height: 200px
name: matdamage
---
Stress-strain behavior arising from a damage model.
```

and we see that the unloading branch has lower stiffness than the loading one. Also note how this model does not assume the existence of permanent strains, and therefore unloads back to zero strain at zero stress.

Damage evolution is dictated by a fracture surface that can be formulated in a similar way as an yield surface for plasticity:

$$
f\left(\tilde{\beps},\kappa\right) = \tilde{\beps} - \kappa, \quad f\leq 0, \dot{\kappa}\geq 0, f\dot{\kappa}=0
$$(sn-mn-damage2)

with $\tilde{\beps}$ being an equivalent strain measure and $\kappa$ being an internal variable that evolves in order to guarantee that $f$ is never positive. The evolution of the damage variable $d$ can then be posed in terms of $\kappa$:

$$
d = d\left(\kappa\right)
$$(sn-mn-damage3)

completing the formulation of the model. Since Eq. {eq}`sn-mn-damage3` represents a unique mapping, it suffices to store only $\kappa$ as internal variable in $\balpha$. Damage model are used to describe failure of a wide range of materials.
