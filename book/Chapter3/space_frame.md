$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\beps}{\boldsymbol\varepsilon}$
$\newcommand{\bsig}{\boldsymbol\sigma}$
$\newcommand{\GAs}{GA_s}$
$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bff}{\mathbf{f}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bD}{\mathbf{D}}$
$\newcommand{\bK}{\mathbf{K}}$
$\newcommand{\xloc}{{\bar{x}}}$
$\newcommand{\yloc}{{\bar{y}}}$

# 2D frame analysis

Frame structures are structures made of one-dimensional structural elements that are loaded axially as well as in bending. These structural elements can be considered a combination of the rod and the beam. One more conceptual ingredient needs to be added and that is that the structure is defined in two-dimensional space (or three-dimensional, but we limit the discussion to 2D here). This is different from rods and beams, which are 1D objects in 1D space. In a frame, different members are present that have different orientations, therefore a global coordinate frame is needed. In this chapter, we start with  the formulation of an extensible beam element that is aligned with global coordinates. After that, we define the element for arbitrary orientation. 
 
## Extensible beam element

### Governing equations 
The extensible beam element is a combination of the rod element with a beam element. Here, we use a Timoshenko beam element. We take a linear 2-node element, initially one that is aligned with the global $x$-axis. Notably, the same linear hat functions can be used as shape functions for rod elements as well as for Timoshenko beam elements, so in terms of shape functions, we need only one set. The same shape functions are used to interpolate three different fields (displacement-like quantities): 
- the displacement in $x$-direction, $u_x$, this is the $u$ from rod analysis  
- the displacement in $y$-direction, $u_y$, this is the $v$ from beam analysis
- and the rotation $\theta$, also known from beam analysis

There are three deformations (strain-like  quantities) that are related to these displacements with kinematic relations: 
- axial strain $\eps =  \pder{u_x}{x}$
- shear strain $\gamma = \pder{u_y}{x}-\theta$
- curvature $\kappa = \pder{\theta}{x}$ 

Then there are three section forces (stress-like quantities) that are related to the strains through constitutive relations:
- axial force $N = EA\eps$
- shear force $V = \GAs\gamma$
- moment $M = EI\kappa$

Where $E$ is the Young's modulus, $A$ the cross-sectional area, $I$ the second moment of inertia and $\GAs$ the shear stifness (shear modulus times area, corrected with cross-section dependent shear factor). For non-homogeneous cross section, $EA$, $EI$ and $\GAs$ should be obtained through integration over the cross section and are not a simple product anymore. 

Finally there are equilibrium relations that give the strong form equations for the extensible beam element, one for extension and two for the Timoshenko beam formulation. For the element that is aligned with the global $x$-axis, the rod action is uncoupled from the Timoshenko beam action so the resulting element formulation is really just a straightforward combination of rod and Timoshenko elements. 


### Element formulation 
Using the same set of shape functions $N_1$, $N_2$ to interpolate the three fields over the element domain, the strain-displacement relation for a single element is given as: 

$$
\begin{pmatrix}
\eps \\ \gamma \\ \kappa
\end{pmatrix} 
= 
\begin{bmatrix}
N_1' & 0 & 0 & N_2' & 0 & 0 \\
0 & N_1' & -N_1 & 0 & N_2' & -N_2 \\
0 & 0 & N_1' & 0 & 0 & N_2' \\
\end{bmatrix}
\begin{pmatrix}
u_{x1} \\
u_{y1} \\
\theta_{1} \\
u_{x2} \\
u_{y2} \\
\theta_{2}
\end{pmatrix}
$$
where we use a shorthand notation for derivatives with respect to $x$ as $f' = \pder{f}{x}$. This is a linear relation which can be written as 

$$
\beps = \bB\ba^e
$$

where $\bB$ is the 3 by 6 matrix that defines the relation between the deformations $\beps=\left[ \eps, \gamma, \kappa\right]^T$ and $\ba^e= \left[u_{x1}, u_{y1}, \theta_1, u_{x2}, u_{y2}, \theta_2\right]^T$. Note that the $bB$-matrix contains shape function derivatives, but also shape functions themselves, which comes from the fact that shear strain depends on $\theta$ directly rather than on $\theta'$. 

We can then also introduce a stress vector $\bsig$, which is related to the deformations as:

$$
\bsig = \bD\beps
$$

with

$$
\bD = \begin{pmatrix} EA & 0  & 0 \\ 0 & \GAs & 0 \\ 0 & 0 & EI \end{pmatrix}
$$


which allows for writing the element stiffness matrix in the familiar form 

$$
\bK^e = \int_{\Omega^e} \bB^T\bD\bB \,d\Omega
$$

Note that we can define an element force vector, defined as 

$$ 
\bff^e = \bK^e\ba^e
$$

where the element force vector has length six and the physical interpretation of its components mirrors that of the degree of freedom vector:

$$
\bff^e = \begin{pmatrix} F_{x1} \\ F_{y1} \\ M_{1} \\ F_{x2} \\ F_{y2} \\ M_{2} \end{pmatrix}
$$

where $F_{xi}$ and $F_{yi}$ are the two components of a force vector on node $i$ and $M_i$ is a moment on node $i$. 


:::{card} Exercise
Write out the product $\bB^T\bD\bB$ and show that this element works like a combination of a bar element and a Timoshenko beam element. 

<!-- TODO: add solution -->
:::


## Rotated extensible beam element 

A 2D frame can be described by connecting different extensible beam domains with different orientations to one another. In the element formulation given above, the beam was aligned with the global $x$-axis. In a 2D domain, that is not necessarily the case. Relation between forces and displacements does not fundamentally change, but to connect different elements with possibly different orientations we need to define the degrees of freedom in terms of displacements in global coordinate frame. To evaluate the deformations of the element, a transformation then needs to be applied to the displacements. Note that the rotational degree of freedom $\theta$ is independent of the choice of coordinate frame. 

We can define a local coordinate frame $(\xloc,\yloc)$ that is aligned with the frame. Then we have 

$$
\eps &= \pder{u_\xloc}{\xloc} \\
\gamma &= \pder{u_\yloc}{\xloc}-\theta \\
\kappa &= \pder{\theta}{\xloc} \\
$$

The following transformation applies to the displacement vector (and likewise to the force vector): 

$$
\begin{pmatrix} u_\xloc \\ u_\yloc \end{pmatrix} = \begin{pmatrix} \cos{\phi} & \sin{\phi} \\ -\sin{\phi} & \cos{\phi} \end{pmatrix}
\begin{pmatrix} u_x \\ u_y \end{pmatrix} 
$$

As a consequence, we can write

$$
\eps &= \cos{\phi}\pder{u_x}{\xloc}  + \sin{\phi}\pder{u_y}{\xloc} \\
\gamma &= -\sin{\phi}\pder{u_x}{\xloc}  + \cos{\phi}\pder{u_y}{\xloc} - \theta \\
$$

This means that with the same definition of $\ba^e$ as above (in terms of degrees of freedom in global coordinates $x$ and $y$), the strain-displacement matrix becomes:

$$
\bB = 
\begin{bmatrix}
\cos{\phi}N_1' & \sin{\phi}N_1' & 0 & \cos{\phi}N_2' & \sin{\phi}N_2' & 0 \\
-\sin{\phi}N_1' & \cos{\phi}N_1' & -N_1 &  -\sin{\phi}N_2' & \cos{\phi}N_2' & -N_2 \\
0 & 0 & N_1' & 0 & 0 & N_2' \\
\end{bmatrix}
$$

where $N_i'$ is the derivative of the shape function along the local coordinate $\xloc$. 

