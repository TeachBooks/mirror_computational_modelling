# 1D Problems

## Poisson 

The poisson equation is often solved using finite elements. The poisson equation can be used to describe a variety of physical phenomena such as steady-state heat conduction and flow in permeable media (Darcy's law). The constitutive relationship depends on the problem being adressed.

The Poisson equation, in its most general form, is defined as follows;

$$
∇² u = -\rho
$$ (generalpoisson)

where

- $∇²u$ represents the Laplacian of a scalar field u, which is the second spatial derivative of $u$
- $\rho$ represents a source or sink term that accounts for the distribution of mass or charge within the system. It can be positive (sources) or negative (sinks) and can vary with spatial coordinates. 

- rod
- soil consolidation

## Beam problems
Typically two types of beams are addressed in literature, the Bernoulli - Euler Beam and the Timoshenko beam. The the Bernoulli - Euler Beam is valid for relatively slender beams, whereas the Timoshenko beam is relevant where shear deformations are present. In order to solve beam elements, a similar process is followed to the one used in continuum elements. Again, since the governing equation is formulated, a weak form of the equation must be developed. At this stage only in-plane, linear beams are considered. All forces and moments are in-plane. 

**Euler-Bernoulli beam**

The Euler-Bernoulli beam does not allow for shear deformation ($\gamma=0$). As a result, the rotation of the beam can be directly related to the displacement $v$:

$$
\theta = \frac{\text{d}v}{\text{d}x}
$$ (euler_rotation)

which means that

$$
\kappa = \frac{\text{d}^2v}{\text{d}x^2}
$$ (euler_kappa)

and the bending moment $m$ in the beam is determined by:

$$
m=-EI \cdot \kappa=-EI \cdot \frac{\text{d}^2v}{\text{d}x^2}
$$ (bending moment)

where 
- $EI$ is the bending stiffness of the beam



**Timoshenko beam**

The Timoshenko beam allows shear deformation and is more suitable for relatively short beams. In Timoshenko beam theory, planes remain plain during deformation but are not needed to remain normal to the longitudinal axis. This assumption allows for shear deformation. The plane is assumed to have a rotation $θ$, where $θ=-γ$, where $γ$ is the rotation due to shear and $θ=dv/dx$.

## 1D elements in 2/3D (space-frame structures)

Here, a one dimensional rod element is considered in two and three dimensions. In the 2D case the nodes of the truss can translate in both x and y dimensions. As a result, a finite element model will require two degrees of freedom at each of the nodes. Typically, the coordinate system  is selected considering that the x-axis is aligned with the axis of a truss element. In the 3D case, every node has three degrees of freedom.


See Garth Wells / Chapter 6.1. Rod in space (Truss) ?

