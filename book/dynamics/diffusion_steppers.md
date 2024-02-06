$\newcommand{\E}{\\[3pt]}$
$\newcommand{\DE}{\\[6pt]}$
$\newcommand{\TE}{\\[9pt]}$
$\newcommand{\QE}{\\[12pt]}$
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\beps}{\boldsymbol\eps}$
$\newcommand{\bsig}{\boldsymbol\sigma}$
$\newcommand{\dbdot}{\,\colon\!}$
$\newcommand{\hint}{\displaystyle\int}$
$\newcommand{\hsum}{\displaystyle\sum}$
$\newcommand{\alert}[1]{{\color{pdcolor9}#1}}$
$\newcommand{\gives}{\quad\Rightarrow\quad}$
$\newcommand{\ud}{\mathrm{d}}$
$\newcommand{\uf}{\mathrm{f}}$
$\newcommand{\bff}{\mathbf{f}}$
$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bb}{\mathbf{b}}$
$\newcommand{\bc}{\mathbf{c}}$
$\newcommand{\bh}{\mathbf{h}}$
$\newcommand{\bn}{\mathbf{n}}$
$\newcommand{\bq}{\mathbf{q}}$
$\newcommand{\bt}{\mathbf{t}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bv}{\mathbf{v}}$
$\newcommand{\bw}{\mathbf{w}}$
$\newcommand{\bx}{\mathbf{x}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bD}{\mathbf{D}}$
$\newcommand{\bJ}{\mathbf{J}}$
$\newcommand{\bK}{\mathbf{K}}$
$\newcommand{\bM}{\mathbf{M}}$
$\newcommand{\bN}{\mathbf{N}}$
$\newcommand{\bP}{\mathbf{P}}$
$\newcommand{\bzero}{\mathbf{0}}$
$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\dder}[2]{\frac{\ud #1}{\ud #2}}$
$\newcommand{\pders}[3]{\frac{\partial^2 #1}{\partial #2 \partial #3}}$
$\newcommand{\lder}[2]{{\ud #1}/{\ud #2}}$
$\newcommand{\lpder}[2]{{\partial #1}/{\partial #2}}$
$\newcommand{\lpders}[3]{{\partial^2 #1}/{\partial #2 \partial #3}}$
$\newcommand{\hfrac}[2]{\displaystyle\frac{#1}{#2}}$
$\newcommand{\lfrac}[2]{{#1}/{#2}}$
$\newcommand{\hpder}[2]{\displaystyle\frac{\partial #1}{\partial #2}}$
$\newcommand{\myVec}[1]{\left\{ \begin{matrix} #1 \end{matrix} \right\}}$
$\newcommand{\myMat}[1]{\left[ \begin{matrix} #1 \end{matrix} \right]}$
$\newcommand{\sym}{\ensuremath{_\mathrm{s}}}$
$\newcommand{\dg}{\ensuremath{^\circ}}$
$\newcommand{\mbf}[1]{\mathbf{#1}}$
$\newcommand{\mrm}[1]{\mathrm{#1}}$
$\newcommand{\bs}[1]{\boldsymbol{#1}}$
$\newcommand{\T}{^\mathrm{T}}$

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

# Time stepping algorithms for diffusion

The results from the previous page do not take care of the coupling between field values $\ba$ and it velocities $\dot{\ba}$. In this page we take care of solving the time dimension for this problem by employing a **time stepper**. We will start with two simple Euler time steppers and move on to an efficient trapezoidal rule.

First of all we can draw a parallel between our final system of equations and a general scalar initial-value problem:

$$
\dot{y}(t) = f(y,t) \quad\Rightarrow\quad \dot{\ba}(t) = \mbf{M}^{-1}\left(\bff(t)-\mbf{K}\ba(t)\right)
$$(d-ds-odeparallel1)

and from a Taylor expansion of the time derivative, we can arrive either at a **Forward Euler**:

$$
y_{n+1} = y_n + \Delta t f(y_n,t_n) \quad\Rightarrow\quad \ba_{n+1} = \ba_n + \Delta t\dot{\ba}_n
$$(d-ds-forwardeuler)

or a **Backward Euler** approximation:

$$
y_{n+1} = y_n + \Delta t f(y_{n+1},t_{n+1}) \quad\Rightarrow\quad \ba_{n+1} = \ba_n + \Delta t\dot{\ba}_{n+1}
$$(d-ds-backwardeuler)

for the solution field at time step $n+1$. Note that the forward stepper only needs values from the previous time step $n$ and is therefore **explicit**. In contrast, the backward stepper needs values from the current time step and is therefore **implicit**.

With these starting points, and using the expressions we derived before, we have:

```{card}
**Forward Euler for diffusion**
^^^
Step forward in time with the velocity from the previous time step:

$$
\ba_{n+1} = \ba_n + \Delta t\dot{\ba}_n
$$

Substitute in the discretized form:

$$
\mathbf{M}\dot{\mathbf{a}}_{n+1} + \mathbf{K}\left(\mathbf{a}_n+\Delta t\dot{\mathbf{a}}_n\right) = \mathbf{f}_{n+1}
$$

Solve for the new velocities:

$$
\dot{\mathbf{a}}_{n+1} = \mathbf{M}^{-1}\hat{\mathbf{f}}
  \quad\quad\mathrm{with}\quad\quad
  \hat{\mathbf{f}} = \mathbf{f}_{n+1} - \mathbf{K}\left(\mathbf{a}_n+\Delta t\dot{\mathbf{a}}_n\right)
$$

Store $\dot\ba_{n+1}$ for the next step
```

```{card}
**Backward Euler for diffusion**
^^^

Start from a relation between the current velocity and the solution

$$
  \mathbf{a}_{n+1} = \mathbf{a}_n + \Delta t \dot{\mathbf{a}}_{n+1}
  \quad\Rightarrow\quad
  \dot{\mathbf{a}}_{n+1} = \hfrac{\mathbf{a}_{n+1}-\mathbf{a}_n}{\Delta t}
$$

Substitute in the discretized form to eliminate the current velocity:

$$
  \mathbf{M}\left(\hfrac{\mathbf{a}_{n+1}-\mathbf{a}_n}{\Delta t}\right) + \mathbf{K}\mathbf{a}_{n+1} = \mathbf{f}_{n+1}
$$

Solve for the new solution (and after that the velocity):

$$
  \hat{\mathbf{K}}\mathbf{a}_{n+1} = \hat{\mathbf{f}}
  \quad\quad\mathrm{with}\quad\quad
  \hat{\mathbf{K}} = \mathbf{K} + \hfrac{1}{\Delta t}\mathbf{M} \quad \hat{\mathbf{f}} = \mathbf{f}_{n+1} + \hfrac{1}{\Delta t}\mathbf{M}\mathbf{a}_n
$$

Store $\ba_{n+1}$ and $\dot\ba_{n+1}$ for the next step

```

Note how the Forward Euler solve only involves inverting $\mbf{M}$. A popular strategy to speed up the solver is to **lump** the entries of $\mbf{M}$ by accumulating all entries in a row into the diagonal:

$$
\bar{M}_{ii} = \displaystyle\sum_jM_{ij}
$$(d-ds-lumpedM)

which means $\bar{\mbf{M}}$ is a diagonal matrix and its inverse can be trivially obtained simply by setting its diagonal entries to $1/\bar{M}_{ii}$. The same cannot be done with Backward Euler, which makes each solve considerably more computationally expensive.

The two steppers above can be seen as the bounds of a more general **trapezoidal scheme**:

```{card}
**Trapezoidal stepper for diffusion**
^^^

Step forward in time with a mix of present and past information:

$$
  \mathbf{a}_{n+1} = \mathbf{a}_n + \Delta t\left( (1-\theta)\dot{\mathbf{a}}_n + \theta\dot{\mathbf{a}}_{n+1}\right)
  \quad\Rightarrow\quad
  \dot{\mathbf{a}}_{n+1} = \hfrac{1}{\theta\Delta t}\left(\mathbf{a}_{n+1}-\mathbf{a}_n\right) - \hfrac{(1-\theta)}{\theta}\dot{\mathbf{a}}_n
$$

Substitute in the discretized form:

$$
    \mathbf{M}\left(\hfrac{1}{\theta\Delta t}\left(\mathbf{a}_{n+1}-\mathbf{a}_n\right) - \hfrac{\left(1-\theta\right)}{\theta}\dot{\mathbf{a}}_n\right) + \mathbf{K}\mathbf{a}_{n+1} = \mathbf{f}_{n+1}
$$

Solve for the new solution (and after that the velocity):

$$
    \hat{\mathbf{K}}\mathbf{a}_{n+1} = \hat{\mathbf{f}}
    \quad\quad\mathrm{with}\quad\quad
    \hat{\mathbf{K}} = \hfrac{1}{\theta\Delta t}\mathbf{M} + \mathbf{K}
    \quad
    \hat{\mathbf{f}} = \mathbf{f}_{n+1} + \hfrac{1}{\theta\Delta t}\mathbf{M}\mathbf{a}_n + \hfrac{\left(1-\theta\right)}{\theta}\mathbf{M}\dot{\mathbf{a}}_n
$$

Store $\ba_{n+1}$ and $\dot\ba_{n+1}$ for the next step

```

where we recover Forward Euler for $\theta\rightarrow 0$ and Backward Euler for $\theta=1$. This scheme is by far the most popular of the three we present here. In the following, we go through the reasons for avoiding the other two steppers.

## Accuracy and stability

When choosing a time stepper, two important aspects should be considered;

- **Accuracy**: A time discretization error is always incurred, and it stands to reason that it should go to zero as $\Delta t\rightarrow 0$. However, some steppers improve in accuracy faster than others for the same change in $\Delta t$;
- **Stability**: Some time steppers suffer from numerical instability issues when $\Delta t$ is too large. These usually manifest as the solution exploding to extremely high values or showing spurious oscillations. 

The trapezoidal time stepper is popular for two reasons: it is **unconditionally stable**, i.e. it never loses numerical stability no matter how large $\Delta t$ is; and it is **second-order accurate**, i.e. solution accuracy improves quadratically as $\Delta t$ is reduced. 

On the other hand, although Backward Euler is also unconditionally stable, it is only first-order accurate: $\Delta t$ needs to be halved for a twofold improvement in accuracy. For Forward Euler, although individual solves are computationally efficient, the stepper is highly unstable and therefore requires extremely small time steps to function properly, offsetting any gains in efficiency.


