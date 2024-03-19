$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bx}{\mathbf{x}}$
$\newcommand{\bff}{\mathbf{f}}$
$\newcommand{\bN}{\mathbf{N}}$
$\newcommand{\bM}{\mathbf{M}}$
$\newcommand{\bK}{\mathbf{K}}$

# Modal Analysis

Besides solving the dynamic system in the time domain, there is an alternative numerical analysis that is relevant in structural engineering. If we go back to the semi-discrete form of for the undamped system Equation {eq}`dynamics-discrete-short`, we can analyze free vibrations from an eigenvalue problem.

In free vibration analysis, the force vector $\bff$ is set to zero: we are looking for dynamic deformation modes that can exist without external loading. Deformations without external loading can only be sustained if damping is not present. That means the system we are analyzing is:

$$
\bK\ba + \bM\ddot\ba = \mathbf{0}
$$(vibration-semi-discrete)

Any non-trivial motion that can exist for an unloaded system will be harmonic. Therefore, the general solution that we are after can be expressed as:

$$
\ba(t) = \bar\ba\cos(\omega t-\phi)
$$(vibration-solution)

where $\bar\ba$ is an arbitrary vector with nodal displacements, $\omega$ is the frequency of the motion and $\phi$ a phase angle. Note that in combination with the shape functions, a solution $\ba(t)$ describes the time-dependent displacement field as $\bu(\bx,t) = \bN(\bx)\ba(t)$. Similarly $\bar\ba$ describes a time-independent displacement mode $\bar{u}(\bx) = \bN(\bx)\bar\ba$.

Nodal accelerations are given by:

$$
\ddot\ba(t) = -\omega^2\bar\ba\cos(\omega t-\phi)
$$(vibration-accelerations)

Substitution of {eq}`vibration-solution` and {eq}`vibration-accelerations` into {eq}`vibration-semi-discrete` and division by $\cos(\omega t-\phi)$ gives:

$$
\left(\bK-\omega^2\bM\right)\bar\ba = \mathbf{0}
$$(vibration-eigenproblem)

This system has a non-trivial solution ($\bar\ba\neq\mathbf{0}$) for

$$
\det\left(\bK-\omega^2\bM\right) = 0
$$

This is a generalized eigenvalue problem with the stiffness matrix $\bK$ and the mass matrix $\bM$ where the eigenvalues $\omega^2$ correspond to the natural frequencies of the discretized system. There are as many eigenfrequencies as there are degrees of freedom. Generally, only the lowest few of these natural frequencies will be of engineering interest. Each eigenfrequency comes with an eigenvector $\bar\ba$ which is the vibration mode for that frequency.

```{admonition} Analogy between modal analysis and linear buckling analysis
The eigenvalue problem of Eq. {eq}`vibration-eigenproblem` is similar to the eigenvalue problem encountered in linear buckling analysis (see Eq. {eq}`lin-buckling`). These two are fundamentally different from the other finite element analysis types. Linear, non-linear and time-dependent finite element solutions are centered around finding the deformations as a consequence of given loading. By contrast, linear buckling analysis and modal analysis are directed at finding states for the system where deformation can take place without (additional) force. In linear buckling analysis, we are looking for the state of the system where second order changes in internal forces balance the first order changes. In modal analysis, we are looking for a harmonic vibration mode where the internal forces are in balance with the accelerations. 

In both cases we find this special state by solving an eigenvalue problem of the type:

$$
\left(\mathbf{A}-\lambda\mathbf{B}\right)\mathbf{v} = \mathbf{0} \quad \Rightarrow \quad \det(\mathbf{A}-\lambda\mathbf{B}) = 0
$$

Only the contents of $\mathbf{A}$ and $\mathbf{B}$ and the interpretation of physical meaning of the resulting $\lambda$ is different, as summarized in the table below.

|  | Matrix 1 ($\mathbf{A}$) | Matrix 2 ($\mathbf{B}$) | eigenvalue ($\lambda$) | eigenvector ($\mathbf{v}$) |
|---|:---:|:---:|:---:|:---:|
| Linear buckling analysis | $\mathbf{K}_M$ | $-\mathbf{K}_G$ | buckling load | buckling mode |
| Modal analysis  | $\mathbf{K}$ | $\mathbf{M}$ | squared natural frequency | vibration mode |




