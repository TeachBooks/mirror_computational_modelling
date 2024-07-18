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

# Continuum damage mechanics

**Foundation theory**:

- Kachanov 1985
- French school in 1980’s (Chaboche, Lemaitre)

**Damage process describes**:

- Initial micro-structure: microcracks, defects, dislocations, cavities
- Micro-structural damage: nucleation, growth, propagation of microcracks, defects, cavities
- Macro-structural damage: formation of macro-cracks, crack coalescence, failure of component / structure


## Damage model

```{figure} Images/damage_unloading.png 
---
align: right
---
```

Principal ingredients of CDM - comparison with elasto-plasticity
- Damage loading function / strain-based (cf. yield function / stress-based)
- Loading / unloading conditions
- Damage evolution law (cf. hardening / softening law)

```{Admonition} Remarks
- Restrict to small strains
- Total strain concept (cf. additive decomposition)
- Secant unloading (cf. elastic unloading)
```

### Damage parameter

```{figure} Images/damage_parameter.png 
---
---
```

The damage parameter $\omega$ is described using equation {eq}`damage_parameter`:

$$
\omega = \frac{A_d}{A}
$$(damage_parameter)

where:
- $A_u$ is the undamaged cross-sectional area
- $ A_d$ is the damaged cross-sectional area

### Effective stress concept

**Nominal stress:**

$$
\sigma = \frac{F}{A}
$$(nominal_stress)

**Effective stress:**

$$
\tilde{\sigma} = \frac{F}{A_u}
$$(effective_stress)

Rewrite:

$$
A_u = A - A_d = A - \frac{A A_d}{A} = (1 - \omega) A
$$(rewrite)

$$
\Rightarrow \quad \tilde{\sigma} = \frac{\sigma}{1 - \omega}
$$(final)


```{figure} Images/secant_unloading.png 
---
align: right
width: 300px
---
Secant unloading
```

### One-dimensional elasticity-based damage model

$$
\sigma = E \varepsilon
$$(sigma)

Actually $\tilde{\sigma} = E \varepsilon \quad \text{(principle of strain equivalence)}$

$$
\frac{\sigma}{1 - \omega} = E \varepsilon \quad \text{or} \quad \sigma = (1 - \omega) E \varepsilon
$$(sigma_rewritten)

$$
0 \leq \omega \leq 1
$$

- $\omega = 0$ implies $\sigma = E \varepsilon$ - fully intact material
- $\omega = 1$ implies $\sigma = 0$ - fully damaged material

Damage reduces elasticity modulus $E$

### Extension to two- and three-dimensional damage model

If $\omega$ works in all directions, we get an isotropic damage model:

$$
\mathbf{\sigma} = (1 - \omega) \mathbf{D_e} \varepsilon
$$(sigma_2d_3d)

```{figure} Images/voids_micro_cracks.png 
---
---
```

For anisotropy the following damage matrix {eq}`damage_matrix` can be obtained, which in tensor notation results in {eq}`tensor_notation`:

$$
\mathbf{\sigma} = \mathbf{(I - \Omega) D_e \varepsilon}
$$(damage_matrix)

$$
\mathbf{\Sigma} = \mathbf{(^4I - ^4W) ^4D:E}
$$(tensor_notation)

- Damage model can also be derived from thermodynamics
- Continuum damage mechanics resembles strain-based plasticity


## Damage loading function

```{figure} Images/strain_space.png 
---
align: right
width: 300px
---
```

$$
f(\tilde{\varepsilon}, \kappa) = \tilde{\varepsilon}(\varepsilon) - \kappa
$$

where:
- $\tilde{\varepsilon}(\varepsilon)$ - scalar-valued strain measure / equivalent strain
- $\kappa$ - damage threshold with initial threshold $\kappa_0$

```{Note}
- Damage loading $f = 0$, unloading $f < 0$
- $\kappa$ always equals maximum of $\tilde{\varepsilon}$ ($\tilde{\varepsilon}$ decreases $\Rightarrow$ $\kappa$ is constant $\Rightarrow f < 0$)
- $\kappa$ grows $\Rightarrow \dot{\kappa} > 0 \Rightarrow$ damage loading surface expands (it cannot shrink!)
- Kuhn-Tucker conditions: $f \le 0$, $f\dot{\kappa} = 0$, $\dot{\kappa} \ge 0$
```

## Equivalent strain measures $\tilde{\varepsilon}$

**Elastic energy:**

$$
\tilde{\varepsilon} = \mathbf{\varepsilon^T D_e \varepsilon} \quad \text{(tension = compression)}
$$(elastic_energy)

**Mazars (concrete):**

$$
\tilde{\varepsilon} = \sqrt{\sum_{i=1}^3 \langle \varepsilon_i \rangle^2} \quad \text{(tension } \neq \text{ compression)}
$$(mazers)

where $\varepsilon_i$ are the principal strains

$$
\langle \varepsilon_i \rangle = 
\begin{cases} 
\varepsilon_i & \text{if } \varepsilon_i > 0 \\
0 & \text{if } \varepsilon_i \leq 0
\end{cases}
$$

## Damage evolution laws

```{figure} Images/lin_exp_softening.png 
---
align: right
width: 400px
---
Top: linear softening; bottom exponential softening
```

**Linear softening**:

$$
\omega = 
\begin{cases} 
\frac{\kappa_u}{\kappa} \frac{\kappa - \kappa_0}{\kappa_u - \kappa_0} & \text{if } \kappa < \kappa_u \\
1 & \text{if } \kappa \geq \kappa_u 
\end{cases}
$$

**Exponential softening**:

$$
\omega = 1 - \frac{\kappa_0}{\kappa} \left(1 - \alpha + \alpha \exp^{-\beta(\kappa - \kappa_0)} \right)
$$

where $\alpha$ and $\beta$ are softening parameters.

\* One-dimensional analysis $\kappa = \varepsilon$

### Damage evolution law $\omega(\kappa)$ from experiments

Derive objective average stress - average strain curve from uniaxial test (difficult!!)

```{figure} Images/damage_evolution_law.png 
---
---
```
Descending branch in {eq}`descending_branch`:

$$
\sigma = f_t(1-\frac{\varepsilon-\kappa_{0}}{\kappa_{u}-\kappa_{0}})
$$(descending_branch)

1D damage model in {eq}`1D_damage_model`:

$$
\sigma=(1-\omega)E\varepsilon
$$(1D_damage_model)

Combining equations {eq}`descending_branch` and {eq}`1D_damage_model` gives {eq}`combined`:

$$
\kappa = \varepsilon \rightarrow \omega (\kappa)
$$(combined)

```{card}
**Stress update algorithm for damage model**
^^^
FOR EACH INTEGRATION POINT:

1. $ \varepsilon $ is given, calculate equivalent strain $ \tilde{\varepsilon} $, for instance via eq. {eq}`elastic_energy` or {eq}`mazers`
2. Evaluate damage loading function: $ f(\tilde{\varepsilon}, \kappa^j) = \tilde{\varepsilon} - \kappa^j $

   ($ \kappa^j $ is the history parameter computed at the end of the previous load increment)
   
3. If $ f > 0 $, update $ \kappa $ such that: $ \kappa^{j+1} = \tilde{\varepsilon} $

   If $ f \leq 0 $, leave $ \kappa $ unchanged: $ \kappa^{j+1} = \kappa^j $

4. Update damage variable: $ \omega^{j+1} = \omega(\kappa^{j+1}) $

5. Compute total stresses: $ \mathbf{\sigma} = (1 - \omega^{j+1}) \mathbf{D_e \varepsilon} $
```

## Tangent operator

Linearize stress - strain law in {eq}'sigma`:

$$
\sigma = (1 - \omega^{j+1}(\kappa)) D_e \epsilon
$$(sigma)

which gives {eq}`linearized_stress_strain`

$$
D_i = \frac{\partial \sigma}{\partial \varepsilon} = (1-\omega) D_e - \frac{\partial \omega}{\partial \kappa} \frac{\partial \kappa}{\partial \tilde{\varepsilon}} D_e \varepsilon \frac{\partial \tilde{\varepsilon}^T}{\partial \varepsilon}
$$(linearized_stress_strain)

```{Admonition} Remark
If in previous step no damage $\frac{\partial \omega}{\partial \kappa} = 0$ and stiffness is the secant stiffness
```

## Mesh sensitivity

```{figure} Images/mesh_sensitivity.png 
---
---
Mesh sensitivity of numerical solution
```

## Damage plasticity models

```{figure} Images/damage_plasticity.png 
---
---
Left: elastic-plastic material (permanent strain); middle: elastic-damageable material (reduction of stiffness); right: elastic-plastic-damageable material (both)
```

```{Admonition} Coupling damage to plasticity
- Via effective stress concept
- Extend damage model with permanent strain
```