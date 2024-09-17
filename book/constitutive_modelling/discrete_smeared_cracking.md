$\newcommand{\beps}{\boldsymbol\varepsilon}$ $\newcommand{\bsig}{\boldsymbol\sigma}$ $\newcommand{\ud}{\mathrm{d}}$ $\newcommand{\us}{\mathrm{s}}$ $\newcommand{\ba}{\mathbf{a}}$ $\newcommand{\bb}{\mathbf{b}}$ $\newcommand{\bc}{\mathbf{c}}$ $\newcommand{\bt}{\mathbf{t}}$ $\newcommand{\bu}{\mathbf{u}}$ $\newcommand{\bx}{\mathbf{x}}$ $\newcommand{\bw}{\mathbf{w}}$ $\newcommand{\bN}{\mathbf{N}}$ $\newcommand{\bB}{\mathbf{B}}$ $\newcommand{\bD}{\mathbf{D}}$ $\newcommand{\bK}{\mathbf{K}}$ $\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$ $\newcommand{\iD}{\boldsymbol{\mathcal{D}}}$ $\newcommand{\mbf}[1]{\mathbf{#1}}$ $\newcommand{\mrm}[1]{\mathrm{#1}}$ $\newcommand{\bs}[1]{\boldsymbol{#1}}$ $\newcommand{\T}{^\mathrm{T}}$ $\newcommand{\inv}{^{-1}}$ $\newcommand{\myVec}[1]{\left\{ \begin{matrix} #1 \end{matrix} \right\}}$ $\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$ $\newcommand{cA}[1]{\textcolor[RGB]{1,113,136}{#1}}$ $\newcommand{cB}[1]{\textcolor[RGB]{195,49,47}{#1}}$ $\newcommand{cC}[1]{\textcolor[RGB]{0,102,162}{#1}}$ $\newcommand{cD}[1]{\textcolor[RGB]{0,183,211}{#1}}$ $\newcommand{cE}[1]{\textcolor[RGB]{0,163,144}{#1}}$ $\newcommand{cF}[1]{\textcolor[RGB]{97,164,180}{#1}}$ $\newcommand{cG}[1]{\textcolor[RGB]{130,215,198}{#1}}$ $\newcommand{cH}[1]{\textcolor[RGB]{153,210,140}{#1}}$ $\newcommand{cI}[1]{\textcolor[RGB]{235,114,70}{#1}}$ $\newcommand{cJ}[1]{\textcolor[RGB]{241,190,62}{#1}}$ $\newcommand{cK}[1]{\textcolor[RGB]{231,41,138}{#1}}$ 

# Crack models

The main cause of the nonlinearity of concrete is cracking, which is primarily due to the limited capacity of concrete to sustain tensile stresses (or perhaps better, tensile strains). Numerical modelling of cracking concrete started in the late 1960s with the landmark papers of Ngo and Scordelis (1967)[^1] and Rashid (1968)[^2], in which the discrete and smeared crack models were introduced. Especially the latter approach gained much popularity, and in the 1970s comprehensive efforts were invested in developing constitutive models in a smeared setting which could reproduce the experimentally observed stress-strain characteristics of concrete.

```{figure} Images/single_notched_shear.png 
---
---
Single-notched shear beam
```

```{figure} Images/discrete_approach.png
---
---
Discrete approach (interface elements/predefined crack)
```

```{figure} Images/smeared_approach.png 
---
---
Smeared approach (fixed crack model)
```

## Discrete cracking

### Interface elements

```{figure} Images/experiment_interface.png
---
---
Experimental results - masonry wall subjected to a static vertical compression load
```

```{figure} Images/computational_interface.png 
---
---
Computational results - masonry wall subjected to a static vertical compression load. Cracking takes place along a predefined path with 3D interface elements
```

```{figure} Images/biomechanic_interface.png
---
---
Discrete cracking in biomechanics applications (Mota et al., JCM (2003))
```

### Embedded elements

```{figure} Images/strain_field.png
---
align: left
---
Standard strain field and strain field with embedded crack band
```

```{Admonition} Remarks
- Constant strain triangle with embedded crack band
- Discontinuity in strain field or displacement field
- Amplitudes embedded mode are extra d.o.f.’ s
- Extra d.o.f.’ s are solved at integration point or element level
- Discontinuity is smeared over the element
- Versions: weak and strong (symmetric and non-symmetric)
```

```{figure} Images/2d_spec.png
---
---
2D single-notched specimen
```

```{figure} Images/3d_spec.png
---
---
3D specimens with asymmetric nodes
```

### XFEM

```{figure} Images/xfem_disc_medium.png
---
---
eXtended Finite Element Method (XFEM)  
discontinuity in medium
```

A displacement jump can be modelled with the Heaviside function in {eq}`disp_jump`:

$$
\mathbf{u}(\mathbf{x},t) = \mathbf{\hat{u}}(\mathbf{x},t) + \textit{H}_{\Gamma_d}(\mathbf{x})\mathbf{\tilde{u}}(\mathbf{x},t)
$$(disp_jump)

in which:
- $\mathbf{u}(\mathbf{x},t)$ and $\mathbf{\tilde{u}}$ are continuous functions
- $\mathbf{\tilde{u}}(\mathbf{x},t) = [\mathbf{u}(\mathbf{x},t)]$ at $\Gamma_d$
- $\textit{H}_{\Gamma_d}(\mathbf{x})$ is the Heaviside function

```{figure} Images/xfem_disc_discretized.png
---
---
eXtended Finite Element Method (XFEM) - discontinuity in discretized medium
```

FE-formulation displacement jump in equation {eq}`FE_jump`:

$$
\mathbf{u}= \mathbf{Ha} + \textit{H}_{\Gamma_d}\mathbf{Hb}
$$(FE_jump)

in which:
- $\mathbf{a}$ regular d.o.f.'s
- $\mathbf{b}$ enhanced d.o.f.'s
- $\textit{H}_{\Gamma_d}(\mathbf{x})$ is the Heaviside function

```{figure} Images/discontinuity_tip.png
---
---
Propagating discontinuity in discretized medium
```

```{Admonition} Remarks
- Crack path continuity
- Modified integration scheme
- Initiation criter ion
- Orientation of discontinuity (local or nonlocal)
- Discontinuity is continuous over element boundary
```

**Initiation criterion** → if criterion in one or all IP’s of element ahead of discontinuity tip is satisfied  
**Propagation direction** of discontinuity - nonlocal

```{figure} Images/propagation.png
---
---
Propagation direction
```

```{figure} Images/fracture_SEN_beam.png
---
---
Fracture in a SEN-beam - experiment
```

```{figure} Images/SEN_analysis_prop_disc.png
---
---
Fracture in a SEN-beam - analysis with propagating cohesive discontinuities
```

**eXtended Finite Element Method in dynamics** - jump in acceleration field

$$
\ddot{\mathbf{u}}(\mathbf{x}, t) = \ddot{\mathbf{\hat{u}}}(\mathbf{x}, t) + H_{\Gamma_d}(\mathbf{x}) \ddot{\mathbf{u}}(\mathbf{x}, t)
$$

**Discretized jump in acceleration field**

$$
\ddot{\mathbf{u}} = \mathbf{H} \ddot{\mathbf{a}} + H_{\Gamma_d} \ddot{\mathbf{b}}
$$

**Linearized set of equations**

$$
\begin{bmatrix}
\mathbf{M}_{aa} & \mathbf{M}_{ab} \\
\mathbf{M}_{ba} & \mathbf{M}_{bb}
\end{bmatrix}
\begin{bmatrix}
\ddot{\mathbf{a}}^{t + \Delta t} \\
\ddot{\mathbf{b}}^{t + \Delta t}
\end{bmatrix}
+
\begin{bmatrix}
\mathbf{K}_{aa} & \mathbf{K}_{ab} \\
\mathbf{K}_{ba} & \mathbf{K}_{bb}
\end{bmatrix}
\begin{bmatrix}
\Delta \mathbf{a} \\
\Delta \mathbf{b}
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{f}_{e,a}^{t + \Delta t} \\
\mathbf{f}_{e,b}^{t + \Delta t}
\end{bmatrix}
-
\begin{bmatrix}
\mathbf{f}_{i,a}^{t} \\
\mathbf{f}_{i,b}^{t}
\end{bmatrix}
$$

in which:

$$
\mathbf{K} =
\begin{bmatrix}
\int_{\Omega} \mathbf{B}^T \mathbf{D}_e \mathbf{B} d\Omega & \int_{\Omega^+} \mathbf{B}^T \mathbf{D}_e \mathbf{B} d\Omega \\
\int_{\Omega^+} \mathbf{B}^T \mathbf{D}_e \mathbf{B} d\Omega & \int_{\Omega^+} \mathbf{B}^T \mathbf{D}_e \mathbf{B} d\Omega + \int_{\Omega^+} \mathbf{H}^T \mathbf{T} \mathbf{H} d\Gamma
\end{bmatrix}
$$

$$
\mathbf{M} =
\begin{bmatrix}
\int_{\Omega} \rho \mathbf{H}^T \mathbf{H} d\Omega & \int_{\Omega^+} \rho \mathbf{H}^T \mathbf{H} d\Omega \\
\int_{\Omega^+} \rho \mathbf{H}^T \mathbf{H} d\Omega & \int_{\Omega^+} \rho \mathbf{H}^T \mathbf{H} d\Omega
\end{bmatrix}
$$


```{figure} Images/open_hole_laminate.png
---
---
 Open hole laminate [+45/-45] - matrix cracking (ply splitting) modelled with XFEM and delamination modelled with interface elements
```

```{Note}
- Multiple/competing mechanisms, snap-back behaviour, highly nonlinear response
- Algorithmic aspects: implicit, energy-based arc-length, adaptive increment strategy
```

## Smeared Cracking
Within the smeared crack approach distinction can be made between fixed and rotating crack models. In a fixed smeared-crack model the direction of the normal to the crack is fixed upon initiation of the crack. Rotating crack models on the other hand allow the normal to the crack to rotate during the fracture process. In principle the normal of the crack can corotate with the axes of principal strain or with the axes of principal stress. Most fracture models, however, require a relation between the principal tensile strain and the principal tensile stress. This can only be archieved if the axes of principal stress and the axes of principal strain remain aligned during the entire fracture process. In a subsequent section we shall investigate the implications of this so-called requirement of co-axiality of the stress tensor and the strain tensor. First we shall concentrate on fixed smeared-crack models.

Prior to cracking, concrete is, for many purposes, modelled sufficiently accurately as an isotropic, linear-elastic material. For instance, in a two-dimensional state of stress we have {eq}`plane_stress`, which is often referred to as  **plane stress** (see also {doc}`../continuum_linear/continuum_mechanics`):

$$
\myVec{\sigma_{xx}\\\sigma_{yy}\\\sigma_{xy}}
=
\frac{E}{1-\nu^2}
\myMat{1 & \nu & 0\\ \nu & 1 & 0\\ 0 & 0 & \frac{1-\nu}{2}}
\myVec{\varepsilon_{xx}\\\varepsilon_{yy}\\\gamma_{xy}}
$$(plane_stress)

When the major principal tensile stress exceeds the tensile strength or, in more generally when the combination of principal stresses violates the tension-cut-off criterion (e.g. {ref}`tension_exp` or {ref}`tension_mod`), a fixed crack is initiated perpendicular to the direction of the principals stress. In the first so-called elasticity-based crack models, the isotropic stress-strain law is then replaced by an orthotropic law with fixed n, s-axes of orthotropy, where n is the direction normal to the crack (mode-I) and s refers to the direction tangential to the crack (mode-II). In a first attempt the orthotropic relation can be defined as in {eq}`orthotropic_relation` (Rashid 1968 [^2]).

```{figure} Images/tension_cut_off_experiments.png 
---
name: tension_exp
---
Tension cut-off criteria - experimental results
```

```{figure} Images/tension_cut_off_models.png 
---
name: tension_mod
---
Tension cut-off criteria - models
```

$$
\myVec{\sigma_{nn}\\\sigma_{ss}\\\sigma_{ns}}
=
\myMat{0 & 0 & 0\\ 0 & E & 0\\ 0 & 0 & 0}
\myVec{\varepsilon_{nn}\\\varepsilon_{ss}\\\gamma_{ns}}
$$(orthotropic_relation)

Where the orthotropic stress-strain relation has been set up in the coordinate system that aligns with the axes of orthotropy (cracking). Equation {eq}`orthotropic_relation` show that both the normal stiffness and the shear stiffness across the crack are set equal to zero upon cracking. As a consequence all effects of lateral contraction/expansion also disappear. If, for a plane stress situation, $\sigma_{ns} = [\sigma_{nn}, \sigma_{ss}, \sigma_{ns}]^T$ and $\varepsilon_{ns} = [\varepsilon_{nn}, \varepsilon_{ss}, \varepsilon_{ns}]^T$, and the secant siffness matrix $\mathbf{D}_{ns}^s$ is defined as in {eq}`D_ns`, we can write the othrotropic elastics stiffness relation in the n,s-coordinate system as in {eq}`sigma_ns`.

$$
\mathbf{D}_{ns}^s = \myMat{0 & 0 & 0\\ 0 & E & 0\\ 0 & 0 & 0}
$$(D_ns)

$$
\mathbf{\sigma}_{ns} = \mathbf{D}_{ns}^s \varepsilon_{ns}
$$(sigma_ns)

If we introduce $\phi$ as the angle from teh x-axis to the n-axis, we can relate the components of $\varepsilon_{ns}$ and $\sigma_{ns}$ to those in the global x,y-coordinate. Using the standard transformation matrices $\mathbf{T}_\varepsilon$ and $\mathbf{T}_\sigma$ we get {eq}`eps_ns_T` and {eq}`sigma_ns_T`:

$$
\varepsilon_{ns} = \mathbf{T}_\varepsilon(\phi) \varepsilon_{xy}  
$$(eps_ns_T)

$$
\sigma_{ns} = \mathbf{T}_\sigma(\phi) \sigma_{xy}  
$$(sigma_ns_T)

We can transform the local secant stiffness relation in the global x-y, coordinate system in {eq}`transformed_secant`:

$$
\sigma_{xy} = \mathbf{T}_\sigma^{-1}(\phi) \mathbf{D}_{ns}^s \mathbf{T}_\varepsilon(\phi) \varepsilon_{xy}
$$(transformed_secant)

Because of ill-conditioning use of {eq}`plane_stress` may result in premature convergence difficulties. Also, physically unrealistic and distorted crack patterns can be obtained (e.g., Suidean and Schnobrich 1973[^3]). For this reason, a reduced shear modulus $\beta G \ (0 \leq \beta \leq 1)$ was reinserted in the model in {eq}`D_ns_inserted_betag`:

$$
\mathbf{D}_{ns}^s = \myMat{0 & 0 & 0\\ 0 & E & 0\\ 0 & 0 & \beta G}
$$(D_ns_inserted_betag)

The use of this so-called shear retention factor $\beta$ not only reduces the numerical difficulties but it also improves the physical reality of fixed crack models, because it can be thought of as a model representation of aggregate interlock. Most researchers simply adopt a constant shear retention factor ($\beta = 0.2$ is a commenly adopted value) but sometimes a crack-strain dependent factor is employed (Kolmar and Mehlhorn 1984 [^4]). The latter option is more realistic since the capability of a crack to transfer shear stresses in mode-II decreases with increasing crack strain.

The fact that the stiffness normal to the crack in {eq}`D_ns_inserted_betag` is set equal to zero involves a sudden drop of the tensile stress from $f_{ct}$ to zero upon crack initiation. Similar to the use of a zero shear retention factor, this may cause numerical problems. However, careful servocontrolled experiments on plain concrete have shown that concrete is not a perfectly brittle material in the Griffith sense, but that it has some residual load-carrying capacity after reaching the tensile strength. This experimental observation led to the replacement of purely brittle crack models by tension-softening models, in which a descending branch was introduced to model the gradually diminishing tensile strength of concrete upon further crack opening. For discrete crack models, and probably motivated by the cohesisve crack models of Dugdale (1960)[^5] and Blarenblatt (1962)[^6], Hilliborg et al. (1976)[^7] proposed the Fictious Crack model (FCM), which ensured a mesh-independent energy release upon crack propagation. Adaptingthis concept to smeard formulations, Bažant and Oh (1983)[^8] developed the Crack Band Model, in which fracture energy $G_f$ introduced by Hillerborg et al. (1976)[^7] was smeared out over the area in which the crack localizes. In a smeared context, one can model this by inserting a normal reduction factor $\mu$ in the secant stiffness matrix {eq}`D_ns_inserted_mu`:

$$
\mathbf{D}_{ns}^s = \myMat{\mu E & 0 & 0\\ 0 & E & 0\\ 0 & 0 & \beta G}
$$(D_ns_inserted_mu)

where, similar to the shear reduction factor $\beta$, the normal reduction factor $\mu$ can be a function of the strain normal to the crack: $\mu = \mu(\varepsilon_{nn})$. a final refinement is given by the addition of Poisson coupling after crack formation. then, we arrive at the mode-I crack band formulation of Bažant and Oh (1983)[^8] extended with mode-II shear retention {eq}`D_ns_Bazant`:

$$
\mathbf{D}_{ns}^s = \myMat{\frac{\mu E}{1 - \nu^2 \mu} & \frac{\nu \mu E}{1 - \nu^2 \mu} & 0\\ \frac{\nu \mu E}{1 - \nu^2 \mu} & \frac{E}{1 - \nu^2 \mu} & 0\\ 0 & 0 & \beta G}
$$(D_ns_Bazant)

Crack models as discussed in the preceding section are based on total strain concepts. An injective relation is assumed between the stress $\sigma$ and the total strain $\varepsilon$. This approach has two major disadvantages. Firstly, it is impossible to properly combine cracking and other nonlinear phenomena (e.g. plasticity, creep, thermal effects) when a total relation is adopted between stress and strain. Secondly, the fixed-crack model as outlined in the preceding section assumes that, upon violation of the tension cut-off the direction of the crack plane is fixed. During subsequent loading shear strain may then arise along the crack plane, which, in turn, will lead to a build-up of shear stresses over the crack plane. When a softening model is used after cracking the residual normal stress that acts in a crack and the shear stress over the crack can cause principal values of the stress tensor that may exceed the tensile strength in a direction that is different from the normal to the existing crack plane. This rotation of principal stress axes and the subsequent possible violation of the tension cut-off criterion in a new direction can also not be dealt with properly in a total stress-strain relation. If we would transform the total stress-strain relation for the first crack to coordinate system of the second crack and then correct for proper stress-strain situation in the second crack, backtransformation to the coordinate system of the first crack shows that the correct stress-strain relation for the first crack is nog longer complied with.

To overcome these difficulties a  model can be used in which the total strain is additively decomposed into a concrete part $\varepsilon^{co}$ and a cracking part $\varepsilon^{cr}$. In an incremental formulation we can write {eq}`inc_formulation`:

$$
\dot{\varepsilon} = \dot{\varepsilon}^{co} + \dot{\varepsilon}^{cr}
$$(inc_formulation)

As pointed out by de Borst and Nauta (1985)[^9] the crack strain rate $\dot{\varepsilon}^{cr}$ can again be composed of several contributions {eq}`cont_cr_strainrate`:

$$
\dot{\varepsilon}^{cr} = \dot{\varepsilon}_1^{cr} + \dot{\varepsilon}_2^{cr} + ...
$$(cont_cr_strainrate)

where $\dot{\varepsilon}_1^{cr}$ is the strain rate owing to a primary crack, $\dot{\varepsilon}_2^{cr}$ is the strain rate owing to a secondary crack and so on. The relation between the crack strain rate of a particular crack (either primary or secondary) and the stress rate is conveniently defined in the coordinate system which is aligned with the crack. This necessitates a transformation between the crack strain rate $\dot{\varepsilon}_n^{cr}$ of crack n in the global x,y-coordinate system and a crack strain rate \dot{\varepsilon}_n^{cr} which is expressed in local n,s-coordinates. Restricting the treatment to a two-dimensional configuration (which is not essential), we observe that a crack only has a normal strain rate $\dot{\varepsilon}_n^{cr}$ (mode-I) and a shear strain rate $\dot{\gamma}_n^{cr}$ (mode-II), so that {eq}`e_dot_n`:

$$
\mathbf{\dot{e}}_n^{cr} = [\dot{e}_n^{cr}, \dot{\gamma}_n^{cr}]^T
$$(e_dot_n)

The relation between $\dot{\varepsilon}_n^{cr}$ and $\mathbf{\dot{e}}_n^{cr}$ reads {eq}`relation_e_eps_cr`:

$$
\dot{\varepsilon}_n^{cr} = \mathbf{N}_n \mathbf{\dot{e}}_n^{cr}
$$(relation_e_eps_cr)

with $\mathbf{N}_n$ as in {eq}`N_n`:

$$
\mathbf{N}_n = \myMat{cos^2 \phi_n & - sin \phi_n cos \phi_n \\ sin^2 \phi_n & sin \phi_n cos \phi_n \\ 2 sin \phi_n cos \phi_n & cos^2 \phi_n - sin^2 \phi_n}
$$(N_n)

where $phi_n$ is the inclination angle of the normal of crack n with the x-axis. Substitution of eq. {eq}`relation_e_eps_cr` into eq. {eq}`cont_cr_strainrate` gives for multiple cracks eq. {eq}`multiple_cracks`:

$$
\dot{\varepsilon}^{cr} = \mathbf{N}_1 \mathbf{\dot{e}}_1^{cr} + \mathbf{N}_2 \mathbf{\dot{e}}_2^{cr} + ...
$$(multiple_cracks)

For the derivation of the stress-strain law of the system of cracks and concrete, it is convenient to assemble all the crack strain rates that are expressed in their own local coordinate system in a vector $\mathbf{\dot{e}}^{cr}$, as in {eq}`vector_e_cr`:

$$
\mathbf{\dot{e}}^{cr} = [\dot{e}_1^{cr}, \dot{\gamma}_1^{cr}, \dot{e}_2^{cr}, \dot{\gamma}_2^{cr} ...]^T
$$(vector_e_cr)

Introducing the matrix $\mathbf{N}$ in {eq}`N`:

$$
\mathbf{N} = [\mathbf{N}_1, \mathbf{N}_2, ...]
$$(N)

we observe that we can rewrite eq. {eq}`vector_e_cr` as {eq}`e_cr_rewritten`:

$$
\dot{\varepsilon}^{cr} = \mathbf{N} \mathbf{\dot{e}}^{cr}
$$(e_cr_rewritten)

In a similar way, we can define a vector $\mathbf{\dot{s}}_n$ in eq. {eq}`s_n`:

$$
\mathbf{\dot{s}}_n = [\dot{s}_n, \dot{t}_n]^T
$$(s_n)

with $\dot{s}_n$ the normal and $\dot{t}_n$ the shear stress rate in crack n of the integration point. The vector $\mathbf{\dot{s}}$, which assembles all the stress rate with respect to their own local n,s-coordinate system then reads as in eq. {eq}`s_vector`:

$$
\mathbf{\dot{s}} = [\dot{s}_1, \dot{t}_1, \dot{s}_2, \dot{t}_2...]
$$(s_vector)

The relation between the stress rate in the global coordinate system $\dot{\sigma}$ and the stress vector $\mathbf{\dot{s}}$ can subsequently be derived to be eq. {eq}`s_Ns`:

$$
\mathbf{\dot{s}} = \mathbf{N}^T \mathbf{\dot{\sigma}}
$$(s_Ns)

To complete the system of equations, we need a constitutive model for the intact concrete and a stress-strain relation for the smeared cracks. For the concrete between the cracks we assume a relationship of the following structure {eq}`concrete_between_cracks`:

$$
\mathbf{\dot{\sigma}} = \mathbf{D}^{co} \mathbf{\dot{\varepsilon}}^{co}
$$(concrete_between_cracks)

with the matrix $\mathbf{D}^{co}$ containing the instantaneous moduli of the concrete. One of the attractive features of the fixed multiple-crack model with strain-decomposition now becomes apparent, namely that the behaviour of the crack and the behaviour of the intact concrete between the cracks can be treated separately. For most fracture analyses it suffices to use the elasticity matrix for $\mathbf{D}^{co} \ (\mathbf{D}^{co} = \mathbf{D}^e)$, but there is no conceptual limitation to carry out analyses with elastoplastic or visco-elastic concrete properties (De Borst 198[^10]). In a similar way, we can define a relation between the crack strain rate $\mathbf{\dot{e}}^{cr}$ of crack n and the stress rate $\mathbf{\dot{s}}_n$ in the crack. Formally a relation can be assumed that reads {eq}`formal_s_n`:

$$
\mathbf{\dot{s}}_n = \mathbf{D}_n^{cr} \mathbf{\dot{e}}_n^{cr}
$$(formal_s_n)

with $\mathbf{D}_n^{cr}$ a 2x2 matrix. For the derivation of the stress-strain relation of the cracked concrete, it is again convenient to assemble all the matrices $\mathbf{D}_n^{cr}$ in one matrix $\mathbf{D}^{cr}$, which is defined as {eq}`D_cr`:

$$
\mathbf{D}^{cr} = \myMat{\mathbf{D}_1^{cr} & 0 & ... \\ \mathbf{0} & \mathbf{D}_2^{cr} & ... \\ ... & ... & ...}
$$(D_cr)

so that the relation between $\mathbf{\dot{s}}$ and $\mathbf{\dot{e}}_{cr}$ reads {eq}`s_e_cr`:

$$
\mathbf{\dot{s}} = \mathbf{D}^{cr} \mathbf{\dot{e}}^{cr}
$$(s_e_cr)

````{card}
### Additional preliminaries: Sherman-Morrison formula

A useful result on the inversion of a special type of matrices is the **Sherman-Morrison formula**. Let $\mathbf{A}$ be a non-singular $n$ x $4n$ matrix and let $\mathbf{u}$ and $\mathbf{v}$ be two vectors with each $n$ entries. The the following identity holds:

$$
(\mathbf{A} + \mathbf{uv}^T)^{-1} = \mathbf{A}^{-1} - \frac{\mathbf{A}^{-1}\mathbf{uv}^T\mathbf{A}^{-1}}{1+\mathbf{v}^T\mathbf{A}^{-1}\mathbf{u}}
$$(sherman_morrison)

**Exercise**

Prove {eq}`sherman_morrison` indirectly by multiplying $\mathbf{A} + \mathbf{uv}^T$ by the right hand side of {eq}`sherman_morrison`.

```{admonition} Solution
:class: tip, dropdown
Let's denote the right-hand side of the formula as: 

$$
\mathbf{X} = \mathbf{A}^{-1} - \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}}
$$

Then the first step is:

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = (\mathbf{A} + \mathbf{uv}^T) \left( \mathbf{A}^{-1} - \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}} \right)
$$
Distribute $\mathbf{A} + \mathbf{uv}^T$:

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{A} \mathbf{A}^{-1} - \mathbf{A} \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}} + \mathbf{uv}^T \mathbf{A}^{-1} - \mathbf{uv}^T \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}}
$$

Simplify the first two terms to:

1. **First term**: $\mathbf{A} \mathbf{A}^{-1} = \mathbf{I}$, where $\mathbf{I}$ is the identity matrix.

2. **Second term**: $\mathbf{A} \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}} = \frac{\mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}}$

Now, let’s recombine the terms (and shift the 2nd and 3rd term around):

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{I} + \mathbf{uv}^T \mathbf{A}^{-1} - \frac{\mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}} - \mathbf{uv}^T \frac{\mathbf{A}^{-1} \mathbf{u} \mathbf{v}^T \mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}}
$$

Factor out $\mathbf{uv}^T \mathbf{A}^{-1}$ from the last two terms and combine them:

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{I} + \mathbf{uv}^T \mathbf{A}^{-1} - \frac{\mathbf{uv}^T \mathbf{A}^{-1}(1 + \mathbf{uv}^T \mathbf{A}^{-1})}{1 + \mathbf{v}^T \mathbf{A}^{-1} \mathbf{u}}
$$

Rewrite the numerator of the 3rd term:

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{I} + \mathbf{uv}^T \mathbf{A}^{-1} - \frac{\mathbf{u} (1 + \mathbf{v}^T \mathbf{A}^{-1}\mathbf{u})\mathbf{v}^T\mathbf{A}^{-1}}{1 + \mathbf{v}^T \mathbf{A}^{-1}\mathbf{u}}
$$

The 3rd term now has the same nominator and denominator, the fraction can thus be taken out, which results in:

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{I} + (\mathbf{A} + \mathbf{uv}^T) - (\mathbf{A} + \mathbf{uv}^T)
$$

The last two terms cancel out, leaving:

$$
(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{I}
$$

Since $(\mathbf{A} + \mathbf{uv}^T) \mathbf{X} = \mathbf{I}$, this shows that $\mathbf{X} = (\mathbf{A} + \mathbf{uv}^T)^{-1}$, which completes the indirect proof of the Sherman-Morrison formula.
```
````

Using equations {eq}`inc_formulation`, {eq}`e_cr_rewritten`, {eq}`s_Ns`, {eq}`concrete_between_cracks` and {eq}`s_e_cr` we can develop the tangential compliance relation for the cracked concrete {eq}`tang_compliant`:

$$
\mathbf{\dot{\varepsilon}} = [(\mathbf{D}^{co})^{-1} + \mathbf{N}(\mathbf{D}^{cr})^{-1} \mathbf{N}^T] \mathbf{\dot{\sigma}}
$$(tang_compliant)

whereupon use of the extended Sherman-Morrison formula gives for the stiffness relation {eq}`ext_sherman_mor_stiff`:

$$
\mathbf{\dot{\sigma}} = \myVec{\mathbf{D}^{co} - \mathbf{D}^{co} \mathbf{N}[\mathbf{D}^{co} + \mathbf{N}^T \mathbf{D}^{co} \mathbf{N}]^{-1} \mathbf{N}^T \mathbf{D}^{co}} \mathbf{\dot{\varepsilon}}
$$(ext_sherman_mor_stiff)

[^1]: Ngo D. and Scordelis, A.C. (1967), Finite element analysis of reinforced concrete beams, J. Amer. Concrete Inst. 64, 152-163
[^2]: Rashid Y.R. (1968), Analysis of prestressed concrete pressure vessels, Nuclear Eng. Des. 7, 334-344
[^3]: Suidan M. and Schnobrich W.C. (1973), Finite element analysis of reinforced concrete, ASCE J. Struct. Div. 99, 2109-2122
[^4]: Kolmar W. and Mehlhorn G. (1984), Comparison of shear stiffness formulations for cracked Concrete Structures (eds F. Damjanić et al.) Pineridge Press, Swansea, pp. 133-147
[^5]: Dugdale, D.S. (1960), Yielding of steel sheets containing slits, J. Mech. Phys. Solids 8, 100-108
[^6]: Blarenblatt, G.I. (1962), The mathematical theory of equilibrium cracks in brittle fracture, ADv. Appl. Mech. 7, 55-129
[^7]: Hilliborg, A., Modeer, M. and Petersson, P.E. (1976), Analysis of crack formation and crack growth in concrete by means of fracture mechanics and finite elements, Cement Concr. Res. 6, 773-782
[^8]: Bažant Z.P. and Oh B.H. (1983), Crack band theory for fracture of concrete, RILEM Mat. Struct. 16, 155-177
[^9]: De Borst R. and Nauta P. (1985), Non-orthogonal cracks in a smeared finite element model, Eng. Comput. 2, 35-46
[^10]: De Borst R. (1987), Smeared cracking, plasticity, creep and thermal loading - a unified approach, Comp. Meth. Appl. Mech. Eng. 62, 89-110