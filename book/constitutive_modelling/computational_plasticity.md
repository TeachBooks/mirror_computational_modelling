# Computational plasticity

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

```{figure} Images/convergence.png 
---
---
Convergence
```

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


