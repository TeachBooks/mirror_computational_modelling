$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bb}{\mathbf{b}}$
$\newcommand{\bc}{\mathbf{c}}$
$\newcommand{\bff}{\mathbf{f}}$
$\newcommand{\bt}{\mathbf{t}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bw}{\mathbf{w}}$
$\newcommand{\bx}{\mathbf{x}}$
$\newcommand{\bN}{\mathbf{N}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bC}{\mathbf{C}}$
$\newcommand{\bD}{\mathbf{D}}$
$\newcommand{\bM}{\mathbf{M}}$
$\newcommand{\bK}{\mathbf{K}}$

# Time stepping schemes for elasto-dynamics

On the previous page, we have derived the semi-discrete finite element equations for continuum dynamics. Discretization in space was applied, but derivatives with respect to time were maintained. In order to arrive at an algorithm that can be implemented, time discretization should also be applied. It is possible to perform time-discretization with shape functions to arrive at the *space-time finite element method*. However, this is not the most common choice. The finite element discretization approach with nodes, elements and shape functions is convenient for discretization in space, but less so for discretization in time. Therefore, in finite element solvers for time-dependent problems, the finite element discretization in space is usually combined with some type of finite difference discretization in time. To solve th governing equations over a certain time interval, finite time increments $\Delta t$ are introduced and the solution $\ba$ is computed for a finite number of time steps to solve the governing equations over a certain time interval.

In this page different algorithms are introduced for the temporal discretization. In every case, the objective is to find the solution vector $\ba_{n+1}=\ba(t_{n+1})$ and if necessary its time derivatives $\dot\ba_{n+1} = \dot\ba(t_{n+1})$ and $\ddot\ba_{n+1}=\ddot\ba(t_{n+1})$ with the previous solution $\ba_{n}=\ba(t_{n})$, $\dot\ba_{n}=\dot\ba(t_{n})$ known. This implies that for the first time step, initial conditions $\ba_0$ and $\dot\ba_0$ need to be given. 

Starting point is the semi-discrete form, for generality with damping included:

$$
\bM\ddot\ba + \bC\dot\ba + \bK\ba = \bff
$$(steppers-semi-discrete)

We aim to find $\ba(t)$ for given $\bK$, $\bC$, $\bM$ and $\bff(t)$. On the previous page, we have shown how to derive $\bM$ and $\bK$ for continuum dynamics. Note that similar matrices can also be derived for other mechanical systems such as beams, frames, plates or shells. The contents of the matrices will vary, but the semi-discrete equations for dynamics problems can always be expressed as Eq. {eq}`steppers-semi-discrete`.

```{card}
**Main algorithm for dynamic analysis**
^^^
**Require** Stiffness matrix $\bK$; mass matrix $\bM$; external force vector $\bff(t)$; time step size $\Delta t$

**Optional** Damping matrix $\bC$

**Initialize** $n=0$, initial conditions $\ba_0, \dot\ba_0$

- **while** $n<\text{number of time steps}$
    - Compute solution $\ba_{n+1}$ with selected **time stepping scheme**
    - Update velocity $\dot\ba_{n+1}$ and acceleration $\ddot\ba_{n+1}$
    - Go to the next time step $n=n+1$

**Return** Nodal displacements for every time step $[\ba_1, \ba_2, \ldots, \ba_n]$ (and velocities, accelerations)
```

This page is about the different options that exist for the time stepping scheme in the algorithm above. The solution is computed with a linear system of equations and involves evaluation of the force vector, either at $t=n\Delta t$ or at $t=(n+1)\Delta t$. 

## Central difference scheme

For the first algorithm, we make use of central difference approximations for the first and second order time derivatives at $t_n$. These are: 

$$
\dot\ba_n \approx \frac{\ba_{n+1}-\ba_{n-1}}{2\Delta t}
$$

and 

$$
\ddot\ba_n \approx \frac{\ba_{n+1}-2\ba_n+\ba_{n-1}}{\Delta t^2}
$$

Substituting these expression into Eq. {eq}`steppers-semi-discrete` at $t=t_n$ gives:

$$
\bM\frac{\ba_{n-1}-2\ba_n+\ba_{n+1}}{\Delta t^2} + \bC\frac{\ba_{n+1}-\ba_{n-1}}{2\Delta t} + \bK\ba_n = \bff_n
$$

With previous solutions known, this equation can be reordered, such that only terms associated with the unknown $\ba_{n+1}$ remain on the left hand side:

$$
\left(\frac{1}{\Delta t^2}\bM + \frac{1}{2\Delta t}\bC\right)\ba_{n+1} = \frac{1}{\Delta t^2}\bM \left(2\ba_n-\ba_{n-1}\right) + \frac{1}{2\Delta t}\bC\ba_{n-1} - \bK\ba_n + \bff_n
$$

Now we arrive at a linear system of equations

$$
\hat\bM\ba_{n+1} = \hat\bff_n
$$(central-difference-system)

with

$$
\hat\bM = \left(\frac{1}{\Delta t^2}\bM + \frac{1}{2\Delta t}\bC\right) \\
$$

and

$$
\hat\bff_n = \frac{1}{\Delta t^2}\bM \left(2\ba_n-\ba_{n-1}\right) + \frac{1}{2\Delta t}\bC\ba_{n-1} - \bK\ba_n + \bff_n
$$

This linear system of equations can be solved in a loop over time steps. This time stepping scheme is referred to as the **central difference scheme**. It counts as an explicit time integration scheme and is very popular. The central difference scheme is particularly powerful in combination with **mass lumping**. The matrix $\hat\bM$ can be made diagonal without too much loss of accuracy. Then the system of equations {eq}`central-difference-system` can be solved at much lower cost, becuase the equations are uncoupled. 

A downside of the central difference scheme is that it is only conditionally stable. Time steps need to be chosen sufficiently small to avoid instability in the time integration. This makes the central difference scheme particularly well-suited for fast dynamics problems like impact simulations where the time window of interest is relatively short. 

Because of their robustness, explicit dynamics solvers are also used for solving quasi-static nonlinear equilibrium problems. The critical time step size is then increased by artificially scaling the mass matrix to contain higher values, which is conceptually allowed because in the end the static solution should be independent of the mass. One should remain careful when using explicit solvers for equilibrium problems. Equilibrium is by definition violated in the dynamic solver and the influence of this on the results cannot be assessed with certainty, although it is possible to get some insight by monitoring the energy balance. 

## Newmark scheme

For slower dynamics problems, the stability requirement from the critical time step can make the central difference scheme impractical. Then implicit time integration schemes are to be preferred. One family of time integration schemes is the Newmark schame. 

Starting point of the Newmark scheme are expressions for $\ba_{n+1}$ and $\dot\ba_{n+1}$ in terms of quantities from the previous time step and $\ddot\ba_{n+1}$: 

$$
\dot\ba_{n+1} &= \dot\ba_n + \Delta t \left((1-\gamma)\ddot\ba_n + \gamma\ddot\ba_{n+1}\right) \\
\ba_{n+1} &= \ba_n + \Delta t\dot\ba_n + \frac{\Delta t^2}{2}\left((1-2\beta)\ddot\ba_n + 2\beta\ddot\ba_{n+1}\right)
$$(newmark-integration)

of which the first can be recognized as a generalized trapozoidal time-integration scheme with parameter $\gamma$, and the second is a similar kind of time-integration rule with parameter $\beta$. 

For defining an implicit time stepping scheme from the Newmark family, we rearrange the expressions in {eq}`newmark-integration` to express $\ddot\ba_{n+1}$ and $\dot\ba_{n+1}$ in terms of $\ba_{n+1}$ as:

$$
\ddot\ba_{n+1} &= \frac{1}{\beta\Delta t^2}\left(\ba_{n+1}-\ba_n\right) - \frac{1}{\beta\Delta t}\dot\ba_n + \left(1-\frac{1}{2\beta}\right)\ddot\ba_n   \\
\dot\ba_{n+1} &= \dot\ba_n + \Delta t\left((1-\gamma)\ddot\ba_n + \gamma\left( \frac{1}{\beta\Delta t^2}\left(\ba_{n+1}-\ba_n\right) - \frac{1}{\beta\Delta t}\dot\ba_n + \left(1-\frac{1}{2\beta}\right)\ddot\ba_n\right)\right)
$$(newmark-derivs)

Setting $\bC$ to zero, substitution into the semi-discrete form at $t=t_{n+1}$ gives:

$$
\bM\left(\frac{1}{\beta\Delta t^2}\left(\ba_{n+1}-\ba_n\right) - \frac{1}{\beta\Delta t}\dot\ba_n + \left(1-\frac{1}{2\beta}\right)\ddot\ba_n\right) + \bK\ba_{n+1} = \bff_{n+1}
$$

which can be rearranged to 

$$
\hat\bK\ba_{n+1} = \hat\bff_{n+1}
$$(newmark-system)

with

$$
\hat\bK = \bK + \frac{1}{\beta\Delta t^2}\bM
$$

and

$$
\hat\bff_{n+1}  =  \bff_{n+1} + \bM\left(\frac{1}{\beta\Delta t^2}\ba_n + \frac{1}{\beta\Delta t}\dot\ba_n + \left(\frac{1}{2\beta}-1\right) \ddot\ba_n\right)
$$

With damping included, the first expression of Eq. {eq}`newmark-derivs` is also used. Still the resulting system of equations can be written as {eq}`newmark-system`, but the expressions for $\hat\bK$ and $\hat\bff$ get additional terms that are associated with $\bC$.



:::{card} Exercise
Derive the expression for $\hat{\bK}$ and $\hat{\bff}_{n+1}$ when damping is not neglected
```{admonition} Solution
:class: tip, dropdown

$$\hat\bK = \bK + \frac{1}{\beta\Delta t^2}\bM + \frac{\gamma}{\beta\Delta t}\bC$$ 

$$
\hat\bff_{n+1} = \bff_{n+1} + \bM\left(\frac{1}{\beta\Delta t^2}\ba_n + \frac{1}{\beta\Delta t}\dot\ba_n + \left(\frac{1}{2\beta}-1\right) \ddot\ba_n\right) \\ 
+ \bC\left(\frac{\gamma}{\beta\Delta t}\ba_n + \frac{\gamma}{\beta}\dot\ba_n + \left(\frac{\gamma}{2\beta}-1\right)\Delta t\ddot\ba_n\right)
$$
```
:::



The Newmark method is unconditionally stable for:

$$
2\beta \geq \gamma \geq \frac12
$$

For $\beta=0$, and $\gamma=\frac12$, the central difference approximations are recovered. 

## HHT scheme


