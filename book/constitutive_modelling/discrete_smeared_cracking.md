# Crack models

The main cause of the nonlinearity of concrete is cracking, which is primarily due to the limited capacity of concrete to sustain tensile stresses (or perhaps better, tensile strains). Numerical modelling of cracking concrete started in the late 1960s with the landmark papers of Ngo and Scordelis (1967) and Rashid (1968), in which the discrete and smeared crack models were introduced. Especially the latter approach gained much popularity, and in the 1970s comprehensive efforts were invested in developing constitutive models in a smeared setting which could reproduce the experimentally observed stress-strain characteristics of concrete.

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

```{figure} Images/tension_cut_off_experiments.png 
---
---
Tension cut-off criteria - experimental results
```

```{figure} Images/tension_cut_off_models.png 
---
---
Tension cut-off criteria - models
```