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

### Kinematics of a beam

Beam theory is based on the assumption that planes normal to the beam's axis plane remain plane. 

$$
\theta = v_{,x} - \gamma
$$ (beam_kinematics)

### Equilibrium of a beam

The equilibrium of a beam can be developed in two ways: either elaborating on the kinematics of the beam or considering the equilibrium of a beam directly.

The bending moment $m$ in a beam is defined as

$$
m = \int_{-h/2}^{h/2} \sigma_{xx} \: y \: dy
$$ (beam_moment)

and the shear stress $q$ defined by

$$
q = \int_{-h/2}^{h/2} \sigma_{xy} \: dy
$$ (beam_shearstress)

The resultant force $Q$ and moment $M$ can be related to $q$ and $m$ through the equations $Q = q n$ and $M = m n$ where $n$ is the outward unit normal vector of the element.

Considering the vertical equilibrium of a beam element, it follows that

$$
\int_{d\Omega} q \: n \: d\Gamma + \int_{\Omega} f_y \: d\Omega = 0
$$ (beam_tran_eq1)

Following that $\int_{d\Omega} q \: n \: d\Gamma = q|_{x=L_2} - q|_{x=L_1}$, this gives

$$
\int_{\Omega} q_{,x} \: d\Omega + \int_{\Omega} f_y \: d\Omega = 0
$$ (beam_tran_eq2)

Since the equilibrium described by Equation {numref}`beam_eq2` must hold for an infinitely small segment of a beam, it must hold that

$$
q_{,x} + f_y = 0
$$ (beam_tran_eq3)

For rotational equlibrium, it follows that

$$
\int_{d\Omega} m \: n \: d\Gamma - \int_{d\Omega} q \: n \: x \: d\Gamma - \int_{\Omega} f_y \: x \: d\Omega = 0
$$ (beam_rot_eq1)

which can be rearranged such that

$$
\int_{\Omega} m_{,x} \: d\Omega - \int_{\Omega} q \: d\Omega - \int_{\Omega} q_{,x} \: x \: d\Omega - \int_{\Omega} f_y \: x \: d\Omega = 0
$$ (beam_rot_eq2)

Since satisfaction of the translational equilibrium implies that $\int_{\Omega} (q_{,x} + f_y) \: x \: d\Omega = 0$, the rotational equlibrium implies that

$$
m_{,x} - q = 0
$$ (beam_rot_eq3)

...

### Euler-Bernoulli beam

**Strong form equation**

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
- $EI$ is the bending stiffness of the beam.

Taking the derivative of all terms in Equation {numref}`beam_rot_eq3` to $x$ and substituting in {numref}`beam_tran_eq3` yields

$$
\frac{\partial^2 m}{\partial x^2} + f_y = 0
$$ (EB_EOM_eq1)

Assuming $EI$ to be constant and substiuting in {numref}`bending moment` yields

$$
-EI \frac{\partial^4 v}{\partial x^4} + f_y = 0
$$ (EB_EOM_eq2)

which is the strong form equation of equilibrium for an Euler-Bernoulli beam. Being a fourth-order equation, two boundary conditions at both ends of the beam. Dirichlet boundary conditions involved the prescription of the displacement or rotation and Neumann involves either the shear force or moment. With appropriate boundary conditions, the boundary value problem is complete and can be solved.

**Weak form equation**
Following procedures from (REF to weak form eq.), the weak form of equilibrium for a beam can be developed. Multiplying Equation {numref}`EB_EOM_eq1` by a weight function $\overline{v}$, from an appropriately defined space, which is equal to zero where Dirichlet boundary conditions are applied and integration over the beam $\Omega$ yields:

$$
\int_{\Omega} \overline{v} \: m_{,xx} \: d\Omega + \int_{\Omega} \overline{v} f_y \: d\Omega = 0
$$ (EB_WF_eq1)

Integrating by parts the term involving the moment $M$ yields:

$$
- \int_{\Omega} \overline{v}_{,x} \: m_{,x} \: d\Omega + \int_{\Gamma} \overline{v} \: m_{,x} \: n \: d\Gamma + \int_{\Omega} \overline{v} \: f_y \: d\Omega = 0
$$ (EB_WF_eq2)

Applying integration by parts again, this time to the term $\int_{\Omega} \overline{v}_{,x} \: m_{,x} \: d\Omega$, yields

$$
\int_{\Omega} \overline{v}_{,xx} \: m \: d\Omega - \int_{\Gamma} \overline{v}_{,x} \: m \: n \: d\Gamma + \int_{\Gamma} \overline{v} \: m_{,x} \: n \: d\Gamma + \int_{\Omega} \overline{v} \: f_y \: d\Omega = 0
$$ (EB_WF_eq3)

Inserting now the Neumann boundary conditions and the consitutive relation from Equation {numref}`bending moment`, solving the governing weak form equation for a beam involves: find $v \in S$ such that

$$
-\int_{\Omega} \overline{v}_{,xx} \: EI \: v_{,xx} \: d\Omega - \int_{\Gamma_M} \overline{v}_{,x} \: T \: d\Gamma + \int_{\Gamma_Q} \overline{v} \: f_y \: d\Omega = 0
$$ (EB_WF_eq4)



### Timoshenko beam

The Timoshenko beam allows shear deformation and is more suitable for relatively short beams. In Timoshenko beam theory, planes remain plain during deformation but are not needed to remain normal to the longitudinal axis. This assumption allows for shear deformation. The plane is assumed to have a rotation $θ$, where $θ=-γ$, where $γ$ is the rotation due to shear and $θ=dv/dx$.

## 1D elements in 2/3D (space-frame structures)

Here, a one dimensional rod element is considered in two and three dimensions. In the 2D case the nodes of the truss can translate in both x and y dimensions. As a result, a finite element model will require two degrees of freedom at each of the nodes. Typically, the coordinate system  is selected considering that the x-axis is aligned with the axis of a truss element. In the 3D case, every node has three degrees of freedom.


See Garth Wells / Chapter 6.1. Rod in space (Truss) ?

