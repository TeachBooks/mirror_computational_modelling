$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\eps}{\varepsilon}$
$\newcommand{\GAs}{GA_s}$

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

where we use a shorthand notation for derivatives with respect to $x$ as $f' = \pder{f}{x}$
