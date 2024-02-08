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
$\newcommand{\dOmega}{\,\mathrm{d}\Omega}$
$\newcommand{\dGamma}{\,\mathrm{d}\Gamma}$
$\newcommand{\us}{\mathrm{s}}$
$\newcommand{\old}{_\mathrm{o}}$
$\newcommand{\new}{_\mathrm{n}}$

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

# Incremental-iterative algorithms

- intro

## Newton-Raphson method revisited

- figure with sketch of Newton's method, with short derivations below --> draw parallel

```{figure} ./figures/newtonraphson.svg
---
height: 200px
name: newtonraphson 
---
The Newton-Raphson method. Left: as a root-finding algorithm for an arbitrary function $f(x)$; Right: recast as a solver for $f_\mrm{int}=f_\mrm{ext}$.
```
$$
\widetilde{f}(x) = f(x\old) + \displaystyle\dder{f}{x}(x\old)\left(x-x\old\right)
$$(sn-sa-flinearization)

$$
x = x\old -\hfrac{f(x\old)}{f'(x\old)}
$$(sn-sa-fnewguess)

## Newton-Raphson for FEM

- recast equations above for FEM
- mention fext - fint sign flipped due to Newton's -f/f' term
- fext is fixed to some arbitrary value for now
- stop at a single update for delta a, leave iterations for force control below
- reminder that this is why we need increments --> initial guess matters, cannot be too far

## Path-following techniques

```{card}
**Load control**
^^^
```

```{figure} ./figures/snapthrough.svg
---
height: 200px
name: snapthrough
---

```

```{card}
**Displacement control**
^^^
```

### Defining convergence

- convergence not guaranteed
- norms on r
- norms on da
- combined norms
- do not give expressions, leave for Bert's course
- comment on quadratic convergence

### Advanced path following

- arclength teaser

```{figure} ./figures/snapback.svg
---
height: 200px
name: snapback
---
```

```{figure} ./figures/arclen.svg
---
height: 200px
name: arclen 
---
```
