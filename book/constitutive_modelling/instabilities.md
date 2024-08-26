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
\dot{\epsilon}^T \dot{\sigma} > 0 \quad \text{or} \quad \textcolor{red}{\Delta \epsilon^T \Delta \sigma > 0} \quad \text{(in every integration point)}
$$

2. **Structural (global) stability criterion**

$$
\frac{1}{2} \dot{a}^T \mathbf{K} \dot{a} > 0 \quad \left(\mathbf{K} = \sum_{i=1}^{\text{nelem}} \int_{V_e} \mathbf{B}^T \mathbf{D}_i \mathbf{B} \, dV \right)
$$

Critical state only if one of the eigenvalues becomes zero (K is symmetric)

$$
\Rightarrow \textcolor{red}{\det(\mathbf{K}) = 0} \quad \text{(K loses positive definiteness / becomes singular)}
$$

- $\textcolor{red}{\text{Stiffness matrix - eigenvalues}}$

Derivation of eigenvalues:

Homogeneous equation $(\mathbf{K} - \lambda \mathbf{I}) \mathbf{a} = 0$

Non-trivial solution $(\mathbf{a} \neq 0) \Rightarrow \det(\mathbf{K} - \lambda \mathbf{I}) = 0$

roots $\lambda_1 - \lambda_n$

Determinant is the $n^{th}$-degree polynomial of which $\lambda_1 - \lambda_n$ are solutions

$$
\Rightarrow \det(\mathbf{K} - \lambda \mathbf{I}) = (\lambda_1 - \lambda)(\lambda_2 - \lambda) \dots (\lambda_n - \lambda)
$$

If $\lambda = 0$, $\Rightarrow \det \mathbf{K} = \lambda_1 \lambda_2 \dots \lambda_n$ (Vieta's rule)

If $\mathbf{K}$ is:  
$\Rightarrow$ positive definite, if all eigenvalues positive  
$\Rightarrow$ indefinite, eigenvalues are of different sign  
$\Rightarrow$ singular, if at least one eigenvalue is zero

$\textcolor{red}{\text{Structural stability? det } \mathbf{K}}$  
$\textcolor{red}{\text{> 0 ⇒ stable } (\text{all} \lambda_i > 0)}$  
$\textcolor{red}{\text{= 0 ⇒ critical } (\text{if one or more} \lambda_i = 0)}$  
$\textcolor{red}{\text{< 0 ⇒ unstable } (\text{if one or more} \lambda_i < 0)}$

- $\textcolor{red}{\text{Finite element computations}}$

$\mathbf{K}$ is updated every step (and every iteration in a full Newton-Raphson scheme)

$\Rightarrow$ Eigenvalues or pivots can be monitored during computation  
For symmetric stiffness matrices, the number of positive (or negative) pivots is equal to the number of positive (or negative) eigenvalues (pivots are the diagonal terms that appear during LDU-decomposition)

$\Rightarrow$ Lowest eigenvalue (or pivot) decreases as a consequence of the plastic/damage/fracture process

$\Rightarrow$ Due to a finite step size (load/displacement/time) $\lambda_1$ never becomes exactly zero

$\Rightarrow$ When $\lambda_1 < 0$ (all other $\lambda_i > 0$) a $\textcolor{red}{\text{limit point}}$ (loss of stability) or a $\textcolor{red}{\text{bifurcation point}}$ (loss of uniqueness) is passed

$\Rightarrow$ Plot corresponding eigenvector to show failure mode or bifurcation mode

## Bifurcation - uniqueness

```{figure} Images/bifurcation.png 
---
align: right
---
```

- Assume a structure in an equilibrium state

$$
\mathbf{K} \Delta \mathbf{a} = \mathbf{f}_e^t + \Delta \lambda \mathbf{\hat{f}}_e - \mathbf{f}_i^t
$$

Since $\mathbf{f}_i^t = \mathbf{f}_e^t \Rightarrow \mathbf{K} \Delta \mathbf{a} = \Delta \lambda \mathbf{\hat{f}}_e$


$\textcolor{red}{\Rightarrow 2 \text{ (or more) solutions are possible in a bifurcation point:}}$

$$
\mathbf{K} \Delta \mathbf{a}_1 = \Delta \lambda \mathbf{\hat{f}}_e
$$

$$
\mathbf{K} \Delta \mathbf{a}_2 = \Delta \lambda \mathbf{\hat{f}}_e
$$

$$
\mathbf{K} (\Delta \mathbf{a}_1 - \Delta \mathbf{a}_2) = 0
$$

$$
\Delta \lambda \neq 0, \text{ no limit point (loss of stability)}
$$

Non-trivial solution $\Delta \mathbf{a}_1 \neq \Delta \mathbf{a}_2$ if $\color{red}{\det \mathbf{K} = 0}$

$\Rightarrow$ Necessary condition for loss of uniqueness for symmetric and non-symmetric stiffness matrices

- If $\mathbf{K}$ is symmetric and $\det \mathbf{K} = 0$, the condition for loss of stability and loss of uniqueness coincides ($\det \mathbf{K} = 0 \Rightarrow$ limit or bifurcation point)

- $\textcolor{red}{\text{Finite elements computations}}$ (load/arc-length control)

```{figure} Images/negative_pivots.png 
---
---
```

- First negative pivot belongs to limit point $$\Rightarrow$$ failure mode
- Second negative pivot belongs to bifurcation point $\Rightarrow$ 2 equilibrium branches  
  Plot eigenvectors corresponding to negative pivots. An equilibrium path can be enforced by adding an eigenvector to the incremental displacement field  
  $\Delta \tilde{\mathbf{a}} = \Delta \mathbf{a} + k\mathbf{b}$ ($k$ is scalar, $\mathbf{b}$ is eigenvector)
- Also, $\textcolor{red}{\text{spurious kinematic modes}}$ (zero-energy modes) may give negative pivots  
  $\Rightarrow$ Bifurcation point with equilibrium paths that are very close

```{figure} Images/spurious_kinematic_modes.png 
---
---
Spurious kinematic modes in direct tension test
```

## Localisation

What is $\textcolor{red}{\text{localisation of deformation}}$?

Does a mathematical definition exist ? $\textcolor{red}{\text{NO}}$  
Represents loss of stability (material / structural) ? $\textcolor{red}{\text{NO}}$  
Represents loss of ellipticity (ill-posed boundary-value problem) ? $\textcolor{red}{\text{NO}}$

Experimental / computational observation:  
$\textcolor{red}{\text{Small zones of intense straining occur (while remainder of body is unloading)}}$


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
Experiment with localised deformations (mode-I, mode-II) ⇒ $\textcolor{red}{\text{softening behaviour}}$
```

```{figure} Images/strain_softening_model.png 
---
---
Translation to stress-strain relation (1-D) ⇒ $\textcolor{red}{\text{strain-softening model}}$
```

- However, $\textcolor{red}{\text{serious problems}}$ in case of localised deformations....

```{figure} Images/serious_problems.png 
---
---
```

⇒ Standard homogenization ($\sigma = \frac{F}{A}$ , $\varepsilon = \frac{\delta}{L}$) is wrong !!!
Solutions : 
- Use measurements of strain/deformation field in failure zone
- Failure zone averaging (technique excludes elastic part of response)
- Inverse modelling techniques
Furthermore, there is an influence of boundary conditions, initial conditions and geometry ($\textcolor{red}{\text{size effects}}$) on the measured load-displacement curve (F − $\delta$) 

## Stability - Localisation

- $\textcolor{red}{\text{Load control vs. displacement control}}$

```{figure} Images/load_vs_disp_control.png 
---
---
```

$$
\Delta \sigma = E \Delta \varepsilon_e
$$(a)

$$
\Delta \sigma = h^* \Delta \varepsilon_i
$$(b)

$$
\Delta \varepsilon = \Delta \varepsilon_e \Delta \varepsilon_i
$$(c)

Combining equations {eq}`a`, {eq}`b` and {eq}`c` results in eq. {eq}`combined`:

$$
\sigma = h \Delta \varepsilon \quad \text{in which} \quad h = \frac{h^* E}{E + h^*}
$$(combined)

if $-E < h^* < 0$ ⇒ $h < 0 $ strain-softening behaviour  
if $h^* > 0$ ⇒ $h > 0 $ strain-strain-hardening behaviour  
if $h* > -E$ ⇒ $h > 0 $ local snap-back behaviour

- $\textcolor{red}{\text{Load control vs. displacement control}}$

```{figure} Images/truss_element.png 
---
---
Truss element (A=1)
```

$$
u(x) = \begin{bmatrix} 1 - \frac{x}{k} & \frac{x}{k} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \quad (u(x) = \mathbf{H}\mathbf{a})
$$

$$
\varepsilon(x) = \begin{bmatrix} -\frac{1}{k} & \frac{1}{k} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \quad (\varepsilon(x) = \mathbf{B}\mathbf{a})
$$

Elastic element: $\mathbf{K} = k \mathbf{B}^T E \mathbf{B} = \frac{E}{k} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$

Strain-softening element: $\mathbf{K} = k \mathbf{B}^T h \mathbf{B} = \frac{h}{k} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$

- $\textcolor{red}{\text{Load control vs. displacement control}}$

**Load control**

- **Local instability:**

$$
\Delta \epsilon \Delta \sigma < 0 \quad \text{(in weak element)} \quad \textcolor{red}{\text{YES}}
$$

- **Structural instability:**

$$
\frac{1}{k} \begin{bmatrix} h + E & -E \\ -E & E \end{bmatrix} \begin{bmatrix} \Delta a_1 \\ \Delta a_2 \end{bmatrix} = \begin{bmatrix} 0 \\ f_e \end{bmatrix} - \begin{bmatrix} f_{i1} \\ f_{i2} \end{bmatrix}
$$

$$
\text{det} \mathbf{K} = \frac{Eh}{k^2} < 0 \quad \text{(loss of positive definiteness)} \quad \textcolor{red}{\text{YES}}
$$

**Displacement control**

- **Local instability:**

$$
\Delta \epsilon \Delta \sigma < 0 \quad \text{(in weak element)} \quad \textcolor{red}{\text{YES}}
$$

- **Structural instability:**

$$
\frac{1}{k} (h + E) \Delta a_1 = \frac{E}{k} \Delta a_2 - f_{i1} \quad \frac{E}{k} \Delta a_2 \quad (\text{equivalent nodal force})
$$

$$
\text{det} \mathbf{K}_{ff} = \frac{1}{k} (h + E) > 0 \quad \text{if} \quad h > - E \quad (\mathbf{K} \rightarrow \mathbf{K}_{ff}) \quad \textcolor{red}{\text{NO}}
$$

**Conclusion:**

$$
\Rightarrow \quad \text{Localisation of deformation can occur without loss of stability in displacement control!!}
$$

$$
\Rightarrow \quad \text{The condition } h < - E \text{ leads to global snap-back and structural instability}
$$

- $\textcolor{red}{\text{Load control vs. displacement control}}$

```{figure} Images/weak_element.png 
---
---
```

**Load control**

Structural instability:

$$
\frac{1}{k} \begin{bmatrix} h + E & -E & 0 \\ -E & 2E & -E \\ 0 & -E & E \end{bmatrix} \begin{bmatrix} \Delta a_1 \\ \Delta a_2 \\ \Delta a_3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ f_e \end{bmatrix} - \begin{bmatrix} f_{i1} \\ f_{i2} \\ f_{i3} \end{bmatrix}
$$

$$
\text{det} \mathbf{K} = \frac{E^2 h}{k^3} < 0 \text{loss of positive definiteness}  \quad \textcolor{red}{\text{YES}}
$$

**Displacement control**

Structural instability:

$$
\frac{1}{k} \begin{bmatrix} h + E & -E \\ -E & 2E \end{bmatrix} \begin{bmatrix} \Delta a_1 \\ \Delta a_2 \end{bmatrix} = \begin{bmatrix} 0 \\ \frac{E}{k} \Delta a_3 \end{bmatrix} - \begin{bmatrix} f_{i1} \\ f_{i2} \end{bmatrix}
$$

$$
\text{det} \mathbf{K}_{ff} = \frac{E}{k} (2h + E) > 0 \quad \text{if} \quad h > -\frac{1}{2} E  \quad \textcolor{red}{\text{NO}}
$$

$$
\Rightarrow \quad \text{If} \quad h < -\frac{1}{2} E, \quad \text{global snap-back and structural instability} \quad (h < -\frac{E}{n-1} \quad \text{for} \quad n \quad \text{elements})
$$


## Mesh sensitivity

- $\textcolor{red}{\text{Strain-softening bar}}$

```{figure} Images/strain_softening_bar.png 
---
---
```

After peak load one (weak) element is softening and $m - 1$ elements unload:

$$
u = \frac{L}{m} \varepsilon_1 + \frac{(m - 1) L}{m} \epsilon_{\text{other}} \quad \text{with} \quad \varepsilon_1 = \frac{f_t}{E} + \frac{\sigma - f_t}{h} \quad \text{and} \quad \varepsilon_{\text{other}} = \frac{\sigma}{E}
$$

$$
\Rightarrow \quad u = L \left( \frac{\sigma}{E} + \frac{(E - h)(\sigma - f_t)}{Ehm} \right)
$$

Slope of load-displacement curve \((\sigma - u)\):

$$
\frac{\Delta u}{\Delta \sigma} = L \left( \frac{1}{E} + \frac{E - h}{Ehm} \right)
$$


- $\textcolor{red}{\text{Strain-softening bar}}$

```{figure} Images/n_elements.png 
---
align: right
---
```

m = 1 One element ⇒ homogeneous solution  
m = 2 Localisation in half bar  
m = n Vertical tangent if $n = \frac{\varepsilon_u}{\varepsilon_0}$ ($\frac{\Delta u}{\Delta \sigma} = 0$ or $\frac{\Delta \sigma}{\Delta u} = \infty$)  
m = ∞ Map back on elastic branch (no energy dissipation)

⇒ Loss of material/local stability  
⇒ Loss of structural/global stability (in case of load/arc-length control)  
⇒ Loss of ellipticity (loss of well-posedness)  
⇒ $\textcolor{red}{\text{Mesh dependence}}$

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