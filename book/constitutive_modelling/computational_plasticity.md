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
- Euler forward method (explicit)
- Iterative method (implicit)

## Euler forward method

```{figure} Images/euler_forward.png 
---
align: right
---
```

```{figure} Images/elastic_plastic.png 
---
---
Explicit integration: the total strain is divided into an elastic and a plastic part. The plastic part is integrated with an Euler forward rule.
```

## Iterative (implicit) method

```{figure} Images/iterative_method.png 
---
align: right
---
Iterative Method
```

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

### Consistent tangent operator

Convergence behaviour when using a consistent tangent operator in a full Newton-Raphson iteration scheme is shown in the graph below. It can be seen that the consistent tangent converges much faster than the continuum tangent.

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


