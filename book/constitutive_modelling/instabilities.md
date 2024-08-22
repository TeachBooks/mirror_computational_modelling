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

# Instabilities and localisation

## Stability

1. **Material (local) stability criterion [Hill, 1958]**

$$
\dot{\varepsilon}^T \dot{\sigma} > 0 \ \text{(stable)}
$$

$$
\dot{\varepsilon}^T \dot{\sigma} = 0 \ \text{(critical stable)}
$$

$$
\dot{\varepsilon}^T \dot{\sigma} < 0 \ \text{(unstable)}
$$


```{figure} Images/strain_softening_material.png 
---
---
Strain-softening material (concrete-rock)
```

2. **Structural (global) stability criterion**

$$
\delta^2 W_i = \frac{1}{2} \int_V \dot{\epsilon}^T \dot{\sigma} \ dV > 0 \ \text{(stable)}
$$

$$
\delta^2 W_i = \frac{1}{2} \int_V \dot{\epsilon}^T \dot{\sigma} \ dV = 0 \ \text{(critical stable)}
$$

$$

\delta^2 W_i = \frac{1}{2} \int_V \dot{\epsilon}^T \dot{\sigma} \ dV < 0 \ \text{(unstable)}
$$

$\delta^2 W_i$ - second-order internal work (=second derivative of potential energy)

$\textcolor{red}{\text{Second-order work}}$

$$
\delta^2 W_i = \frac{1}{2} \int_V \delta \epsilon^T \delta \sigma \, dV \quad \text{(second-order internal work)}
$$

$$
\delta^2 W_e = \frac{1}{2} \delta f_e^T \delta a \quad \text{(second-order external work)}
$$

$$
\delta^2 W_e = \delta^2 W_i \quad \text{(conservation of energy)}
$$

```{figure} Images/2nd_order_work.png 
---
---
```

- Material (local) instability ≠ structural (global) instability
- A material instability $\textcolor{red}{\text{preceeds}}$ a structural instability

$\textcolor{red}{\text{Finite elements}}$

$$
\mbf{\dot{\varepsilon} = B \dot{a}} \ \text{or} \ \mbf{\dot{\varepsilon}^T = \dot{a}^T B^T}
$$

$$
\mbf{\dot{\sigma} = D_i B \dot{a}}
$$


```{figure} Images/stability.png 
---
---
```

1. **Material (local) stability criterion**

$$
\dot{\epsilon}^T \dot{\sigma} > 0 \quad \text{or} \quad \Delta \epsilon^T \Delta \sigma > 0 \quad \text{(in every integration point)}
$$

2. **Structural (global) stability criterion**

$$
\frac{1}{2} \dot{a}^T \mathbf{K} \dot{a} > 0 \quad \left(\mathbf{K} = \sum_{i=1}^{\text{nelem}} \int_{V_e} \mathbf{B}^T \mathbf{D}_i \mathbf{B} \, dV \right)
$$

Critical state only if one of the eigenvalues becomes zero (K is symmetric)

$$
\Rightarrow \det(\mathbf{K}) = 0 \quad \text{(K loses positive definiteness / becomes singular)}
$$


## Bifurcation - uniqueness

```{figure} Images/bifurcation.png 
---
---
```

```{figure} Images/negative_pivots.png 
---
---
```

```{figure} Images/spurious_kinematic_modes.png 
---
---
Spurious kinematic modes in direct tension test
```

## Localisation

What is localisation of deformation?

Does a mathematical definition exist ? NO  
Represents loss of stability (material / structural) ? NO  
Represents loss of ellipticity (ill-posed boundary-value problem) ? NO

Experimental / computational observation: Small zones of intense straining occur (while remainder of body is unloading)


```{figure} Images/shear_banding_sands.png 
---
---
Shear banding in sands
```

```{Note}
Shear band thickness is dependent on grain size
```

```{figure} Images/shear_banding_sand_biaxial.png 
---
---
Shear banding in sand in biaxial compression [Desrues] (isocontours of deformation)
```

```{Note}
Shear band thickness has a finite size
```

```{figure} Images/rock_faults.png 
---
---
Low angle normal fault (Death Valley)
```

```{Note}
- Cracks/faults represent zones of strongly localised deformations
- Localisation at large scale ($10^1$ − $10^2$ meter)
```

```{figure} Images/shear_banding_metals.png 
---
---
Shear banding in metals
```

```{figure} Images/more_shear_banding.png 
---
---
More shear banding...
```

```{figure} Images/delamination.png 
---
---
Delamination in a fibre-metal laminate
```

```{Note}
Localisation is a multi-scale phenomenon
```

```{figure} Images/localised_deformations.png 
---
---
Experiment with localised deformations (mode-I, mode-II) ⇒ softening behaviour
```

```{figure} Images/strain_softening_model.png 
---
---
Translation to stress-strain relation (1-D) ⇒ strain-softening model
```

```{figure} Images/serious_problems.png 
---
---
```

## Stability - Localisation

```{figure} Images/load_vs_disp_control.png 
---
---
```

```{figure} Images/truss_element.png 
---
---
Truss element (A=1)
```

```{figure} Images/weak_element.png 
---
---
```

## Mesh sensitivity

```{figure} Images/strain_softening_bar.png 
---
---
```

m = 1 One element ⇒ homogeneous solution
m = 2 Localisation in half bar
m = n Vertical tangent if n = ε u/ε 0 (∆u/∆σ = 0 or ∆σ /∆u = ∞)
m = ∞ Map back on elastic branch (no energy dissipation)

```{figure} Images/n_elements.png 
---
---
```

⇒ Loss of material/local stability
⇒ Loss of structural/global stability (in case of load/arc-length control)
⇒ Loss of ellipticity (loss of well-posedness)
⇒ Mesh dependence

## Localisation - bifurcation

$\textcolor{red}{\text{Strain-softening bar}}$

```{figure} Images/5_elements.png 
---
---
```

⇒ $\textcolor{red}{\text{without imperfections}}$

At peak load : 6 negative pivots / eigenvalues  
1: descending branch homogeneous solution  
5: localised solutions in each of the 5 elements

Limit point = bifurcation point (loss of uniqueness)  
However, localised solution cannot be "entered"

⇒ $\textcolor{red}{\text{Imperfect bar (1 weak element)}}$

At peak load : 1 negative pivot / eigenvalue (= limit point)  
Localised solution is traced, no bifurcation  
(However, an imperfect bar with displacement control ⇒ no negative pivot)


### Mesh sensitivity w.r.t. element size

- $\textcolor{red}{\text{Localisation}}$ - debonding and matrix cracking in a SiC/C composite

```{figure} Images/localisation_debonding.png 
---
---
```

- $\textcolor{red}{\text{Finer mesh results in a more brittle response !!!}}$

### Mesh sensitivity w.r.t. element orientation

- $\textcolor{red}{\text{Localisation}}$ - shear banding in a biaxial test (dynamic loading)  
Plane-strain condition - von Mises plasticity model - imperfection in lower right corner

```{figure} Images/Localisation_shearbanding.png 
---
---
```

- $\textcolor{red}{\text{Failure mode is dominated by mesh bias !!!}}$

- $\textcolor{red}{\text{Dynamic problems}}$

Wave equation (1D):  
$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$

Wave speed:  
$
c = \sqrt{\frac{E}{\rho}} \text{ (elastic)} \quad \text{and} \quad c = \sqrt{\frac{h}{\rho}} \text{ (softening)}
$

Characteristics:  
$
\frac{dx}{dt} = \pm c
$

```{figure} Images/wave_speed.png 
---
---
```

- $\textcolor{red}{\text{Wave speed becomes imaginary}}$ at the onset of strain softening
- $\textcolor{red}{\text{Ill-posed}}$ initial-value problem

```{figure} Images/wave_propagation.png 
---
---
Wave propagation in a strain-softening bar - analytical solution
```


$\textcolor{red}{\text{Wave propagation in a strain-softening bar}}$ - numerical solution

```{figure} Images/n_elements_k.png 
---
---
```

⇒ Width of localisation zone = finite element size
⇒ Analytical solution is approached upon mesh refinement (width localisation zone, energy dissipation, reflected compression wave)

- $\textcolor{red}{\text{Remedies to solve mesh dependency}}$ (introduction of length scale parameter)

- **Fracture energy-type models**  
  Localisation occurs in 1 element ⇒ fracture energy should be dissipated in 1 element  
  Softening modulus $h$ (fracture energy $G_f$) is a function of finite element size

```{figure} Images/fracture_energy.png 
---
---
```

- **Discontinuity models**
  - Interface elements
  - XFEM (eXtended Finite Element Method)
  - Embedded discontinuity elements (weak or strong format)

- **Rate-dependent models** (also effective in statics!)
  - Rate-dependent crack/damage models
  - Visco-plastic models (visco-elastic models do NOT solve mesh dependency)

- **Nonlocal models**
  - Integral models
  - Gradient models (gradient plasticity, explicit/implicit gradient damage)

- **Cosserat models** (micro-polar continua)  
  Modified continuum definition with defined micro-structure

Shear banding in biaxial test of granular material with $\textcolor{red}{\text{visco-plastic model}}$ (Drucker-Prager)

```{figure} Images/shear_banding_viscoplastic.png 
---
---
```

- $\textcolor{red}{\text{Mesh objectivity:}}$ shear band has a finite thickness (set by the visco-plastic length scale)

## Stability

- $\textcolor{red}{\text{Numerical instability}}$

1) **Local (integration point level) numerical instability** of iterative process  
   (e.g. implicit return-mapping scheme)  
   ⇒ Load/time step too large, bad algorithm, highly curved yield surface,...

2) **Global numerical instability** of the Newton-Raphson process  
   ⇒ Poor tangent stiffness matrix  
   ⇒ No equilibrium possible

```{figure} Images/lodi_control.png 
---
---
```

...while arc-length control gives a convergent (stable) process

   ⇒ Around bifurcation and limit points, it is more difficult to obtain proper convergence

⇒ $\textcolor{red}{\text{Numerical instability ≠ mechanical (material/structural) instability}}$  
⇒ In general, unstable material/structural behaviour can be modelled without loss of stability of the numerical scheme