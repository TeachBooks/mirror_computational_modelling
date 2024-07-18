# Continuum damage mechanics

## Damage model

```{figure} Images/damage_unloading.png 
---
---
```

### Damage parameter

```{figure} Images/damage_parameter.png 
---
---
```

### Effective stress concept

```{figure} Images/secant_unloading.png 
---
---
```

```{figure} Images/voids_micro_cracks.png 
---
---
```

## Damage loading function

```{figure} Images/strain_space.png 
---
---
```

## Equivalent strain measures $\tilde{\varepsilon}$

**Elastic energy:**

$$
\tilde{\varepsilon} = \mathbf{\varepsilon^T D_e \varepsilon} \quad \text{(tension = compression)}
$$

**Mazars (concrete):**

$$
\tilde{\varepsilon} = \sqrt{\sum_{i=1}^3 \langle \varepsilon_i \rangle^2} \quad \text{(tension } \neq \text{ compression)}
$$

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

```{figure} Images/damage_evolution_law.png 
---
---
```

## Mesh sensitivity

```{figure} Images/mesh_sensitivity.png 
---
---
```

## Damage plasticity models

```{figure} Images/damage_plasticity.png 
---
---
```