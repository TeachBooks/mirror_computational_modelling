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

# Computational plasticity

There are multiple stress update algorithms. Those solve nonlinear differential equations at integration point/local level. In this chapter two methods are given. Those are:
- Euler Forward method (explicit)
- Euler Backward method (implicit)

## Euler Forward method

To obtain the strains and stresses in a structure that relate to a generic loading stage, they must be integrated along the loading path. The most straightforward way to integrate is to use one-point Euler forward integration rule. Such a scheme is fully **explicit**: the stresses and the value of the hardening modulus $\mathit{h}$ are known at the beginning of the strain increment so that the tangential stiffness matrix can be evaluated directly. Therefore the equation {eq}`initial_eq` is used.

```{figure} Images/euler_forward.png 
---
align: right
---
```

$$
\Delta \sigma = \mathbf{D}_e \Delta \varepsilon - \frac{\mathbf{D}_e \mathbf{m}_0 \mathbf{n}_0^T \mathbf{D}_e}{h_0 + \mathbf{n}_0^T \mathbf{D}_e \mathbf{m}_0} \Delta \varepsilon \quad 
$$(initial_eq)

Rewrite equation {eq}`initial_eq` as in {eq}`rewritten` where {eq}`delta_lambda` is used.

$$
\sigma_0 + \Delta \sigma = \sigma_0 + \mathbf{D}_e \Delta \varepsilon - \Delta \lambda \mathbf{D}_e \mathbf{m}_0
$$(rewritten)

$$
\Delta \lambda = \frac{\mathbf{n}_0^T \mathbf{D}_e \Delta \varepsilon}{h_0 + \mathbf{n}_0^T \mathbf{D}_e \mathbf{m}_0}
$$(delta_lambda)

A new equation {eq}`sigma_trial` is assumed and substituted into equation {eq}`elastic_plastic_corrector`. Here $\sigma_{trial}$ is the **elastic predictor** and $\Delta \lambda \mathbf{D}_e \mathbf{m}_0$ the **plastic corrector**.

$$
\sigma_{trial} = \sigma_0 + \mathbf{D}_e \Delta \varepsilon
$$(sigma_trial)

$$
\sigma_n = \sigma_{trial} - \Delta \lambda \mathbf{D}_e \mathbf{m}_0
$$(elastic_plastic_corrector)

```{Admonition} Remarks
- Explicit scheme
- Error big when yield contour is very curved
- If initial stress point $\sigma_0$ is inside yield contour, contact stress $\sigma_c$ must be calculated first (alternative: calculate $\mathbf{m}$, $\mathbf{n}$ and $\mathit{h}$ in trial stress state)
```

```{figure} Images/elastic_plastic.png 
---
---
Explicit integration: the total strain is divided into an elastic and a plastic part. The plastic part is integrated with an Euler forward rule.
```

It can be read from the figure above that, while the correction for plastic straining is governed by the direction of the flow vector at $\sigma_c$, the final or new stress point $\sigma_n$
is found at the intersection of the hyperplane that is tangent to the yield surface at $\sigma_c$ and the return direction $\mathbf{m_c}$ (in the absence of hardening). Apparently, the forward Euler method does not guarantee a rigorous return to the yield surface. An error is ocmmitted with a magnitude which depends upon the local curvature of the yield surface. A strongly curved yield surface gives rise to larger errors than an almost flat yield contour. Especially when relatively large loading steps are used, the accumulation of errors may become quite significant, and may even lead to numerical instability of the algorithm. In some situations, the direction of the correction of plastic flow is such that yield surface will never be reached. For the Euler Forward algorithm it can be proven rigorously that stability of the numerical algorithm is only ensured for relatively small loading steps.

The latter property of the Euler Forward method is at variance with the customs of many - especially inexperienced - users of nonlinear finite element programs, who preferably use very large loading steps. Generally, a numerical program should be made as robust as possible, since users of the program will always step beyond the assumptions made - implicitly or explicitly - by its developers. Therefore, the conceptual simplicity of the Euler Forward method should be sacrificed to a more robust algorithm which warrants numerical stability irrespective of the stepsize. A good and still relatively simple algorithm is the fully implicit **Euler backward method**.

## Euler Backward method

```{figure} Images/iterative_method.png 
---
align: right
---
Iterative Method
```

The iterative (implicit) method makes use of the function {eq}`elastic_plastic_corrector`, in which $\mathbf{\Delta \lambda}$ is a function of $\mathbf{m_n}$, $\mathbf{n_n}$ and $\mathit{h_n}$.

$$
\sigma_n = \sigma_{trial} - \Delta \lambda \mathbf{D}_e \mathbf{m}_n
$$(sigma_n)

Taylor series expansion of yield function in current state:

$$
f_C = f_B + \frac{\partial f_B^T}{\partial \sigma} d\sigma + \frac{\partial f_B}{\partial \kappa} d\kappa = f_B + \mathbf{n}_B^T d\sigma + \frac{1}{d\lambda} \frac{\partial f_B}{\partial \kappa} d\kappa d\lambda
$$(taylor_expansion_yield)

Substitute $ d\sigma = -d\lambda \mathbf{D}_e \mathbf{m}_B $ and $ h_B = -\frac{1}{d\lambda} \frac{\partial f_B}{\partial \kappa} d\kappa $ and assume $ f_C = 0 $:

$$
d\lambda = \frac{f_B}{h_B + \mathbf{n}_B^T \mathbf{D}_e \mathbf{m}_B}
$$(delta_lambda)

```{Admonition} Remarks
- Update stress and solve in an iterative way
- Von Mises with linear hardening / softening → 1 iteration ($\mbf{m}$, $\mbf{n}$ and h are exact in trial stress state)
```

```{card}
**Implicit stress update algorithm**
^^^
FOR EACH INTEGRATION POINT:

1. Iteration $k=0$, $\Delta\lambda_{0}=0$, $\kappa_{0}, \ \sigma_{0}, h_{0}$

2. Compute trial stress $\sigma_{trial} = \sigma_0 + D_e \Delta\varepsilon$

3. Plasticity? YES, if $f(\sigma_{trial}, \kappa_0) \geq 0$ ELSE, $\sigma = \sigma_{trial}$ and go to 10.

4. Calculate $m_{k}$ and $n_{k}$ for current stress $\sigma_k$ (= $\sigma_{trial}$ in first iteration)

5. Compute $d\lambda=f(\boldsymbol{\sigma}_{k},\kappa_{k})/[h_{k}+(n_{k})^T\mathbf{D}_e m_{k}]$ and $\Delta\lambda_{k+1}=\Delta\lambda_{k}+d\lambda$

6. Correction of stress: $\boldsymbol{\sigma}_{k+1} = \sigma_{trial} - A_{k+1}\mathbf{D}_e m_k$

7. Calculate $\kappa_{k+1}$ on basis of hardening/softening hypothesis

8. Calculate $h_{k+1}$ and $\overline{\sigma}_{k+1}$ for updated $\kappa_{k+1}$

9. Check convergence: $f(\boldsymbol{\sigma}_{k+1},\kappa_{k+1}) <$ tolerance

    if YES, go to 10.

    if NO, $k=k+1$ go to 4.

10. Next integration point
```

```{Admonition} This is 4 loops deep in the FE code!
:class: Tip
The Full Newton-Raphson loops are:  
1 Load/displacement, time steps  
$\rightarrow$ 2 Per load step iterations  
$\rightarrow  \rightarrow$ 3 For every integration point  
 $\rightarrow \rightarrow \rightarrow$ 4 Iterative return mapping

```
### Consistent tangent operator

Consistent Tangent Operator [Simo and Taylor, 1985]

Tangent operator can be derived **consistently** with implicit stress update algorithm for {eq}`associative_plasticity`:

$$
\sigma_n = \sigma^{\text{trial}} - \Delta \lambda \mathbf{D}_e \mathbf{n}
$$(associative_plasticity)

Linearize this problem and not the continuum problem to optimize convergence rate in {eq}`linearization`:

$$
\dot{\sigma} = \mathbf{D}_e \dot{\varepsilon} - \dot{\lambda} \mathbf{D}_e \mathbf{n} - \Delta \lambda \mathbf{D}_e \frac{\partial^2 f}{\partial \sigma^2} \dot{\sigma}
$$(linearization)

Rewrite to {eq}`rewrite`:

$$
\dot{\sigma} = \mathbf{H} (\dot{\varepsilon} - \dot{\lambda} \mathbf{n}) \quad \text{with} \quad \mathbf{H} = \left( \mathbf{I} + \Delta \lambda \mathbf{D}_e \frac{\partial^2 f}{\partial \sigma^2} \right)^{-1} \mathbf{D}_e
$$(rewrite)

The for ideal plasticity we have {eq}`ideal_plasticity` for the **consistent tangent**:

$$
\dot{\sigma} = \left[ \mathbf{H} - \frac{\mathbf{H} \mathbf{n} \mathbf{n}^T \mathbf{H}}{\mathbf{n}^T \mathbf{H} \mathbf{n}} \right] \dot{\varepsilon}
$$(ideal_plasticity)


In a full Newton-Raphson procedure, a consistent tangent operator warrants for **quadratic convergence**. Convergence behaviour when using a consistent tangent operator in a full Newton-Raphson iteration scheme is shown in the graph below. It can be seen that the consistent tangent converges much faster than the continuum tangent.

```{figure} Images/convergence.png 
---
---
Convergence
```

| Iteration | Continuum tangent $D_i$ | Consistent tangent $D_i$ |
|---|---|---|
| 2 | $\varepsilon_2 \propto 10^{-1}$  | $\varepsilon_2 \propto 10^{-2}$ |
| 3 | $\varepsilon_3 \propto 10^{-2}$ | $\varepsilon_3 \propto 10^{-4}$ |
| 4 | $\varepsilon_4 \propto 10^{-3}$ | $\varepsilon_4 \propto 10^{-16}$ |
| Convergence rate | Linear | Quadratic |

## Locking

An equation for Von Mises associative plasticity can be found in {eq}`associative_plasticity`.

$$
\dot{\varepsilon}^p = \frac{\dot{\lambda}}{2 \bar{\sigma}} \left[\begin{matrix}2 \sigma_1 - \sigma_2 - \sigma3 \\ 2 \sigma_2 - \sigma_3 - \sigma1 \\ 2 \sigma_3 - \sigma_1 - \sigma_2 \end{matrix}\right]
$$(associative_plasticity)

An equation for incompressible material behaviour can be found in {eq}`incompressible_material`.

$$
\dot{\varepsilon}_{vol}^p = \dot{\varepsilon}_1^p + \dot{\varepsilon}_2^p + \dot{\varepsilon}_3^p = 0
$$(incompressible_material)

```{figure} Images/locking.png 
---
---
Locking
```

```{Admonition} Remarks
- Deformation goes into elasticity and not into plasticity ($\dot{\varepsilon}_{vol}^e \neq 0$)
- Overestimation of collapse load (overly stiff behaviour)
- Locking occurs for low-order elements (plane strain, axi-symmetric, 3D stress condition)
```

```{Admonition} Remedies:
:class: tip
- Reduced integration
- Independent interpolation of displacements and pressures
- Enhanced assumed strain (EAS) elements
- Higher-order elements
```


