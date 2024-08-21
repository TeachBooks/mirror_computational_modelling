# 6.3. Multiphysics

## Multiphysics in Civil Engineering and Geosciences

Many Civil Engineering and Geosciences problems relating to structures or rock deformations and fluid flow can be cast as THMC physical phenomena, Thermo-Hydro-Mechanical-Chemical. Sometimes some of the physical processes can be neglected, for instance when pure mechanical analysis can be performed on structures. In other cases, however, such as ..., multiple physical processes and their interactions need to be accounted for. That is when we speak of multiphysics analysis.

### Conservation laws
For those problems, the different existing laws of physics are encompassed into the conservation of three main quantities: momentum, mass and energy.

Conservation of momentum:
$$
\mathrm{\nabla}\cdot\sigma=0
$$

The equation is written in its simplest form of quasi-static equilibrium without considering dynamics (ref book). Here, the displacement variable $u$ is implicitly the main variable of this system and is linked to the stress with a constitutive model. For 1D elasticity, the stress is directly a function of the displacement gradient which simplifies the conservation of momentum to

$$
\mathrm{\Delta u}=0
$$

Conservation of mass:

$$
\frac{\partial p}{\partial t}=\mathrm{\nabla}\cdot\left(D\mathrm{\nabla p}\right)+q
$$

Where $P$ is the pressure variable. So this equation corresponds to a transient pressure diffusion. $q$ is a source term indicating injection of production of fluid. $D$ is the diffusion coefficient which for porous materials corresponds to the permeability $k$.

Conservation of energy:

$$
\frac{\partial T}{\partial t}=\alpha\mathrm{\nabla}^2T+\frac{q}{\rho c_p}
$$

Where $T$ is the temperature variable. This is a transient diffusion of temperature. $q$ corresponds to a heat flux or sink. Alpha is the thermal conductivity.

The primary variables are respectively displacement $u$, pressure $P$ and temperature $T$.
Equations can be rewritten with stress instead of displacement quite commonly or for hydrogeology with hydraulic head instead of pressure.
Note that the governing equations are written in a Lagrangian formulation. For Eulerian formulation, velocity is the primary variable.

### Phase decomposition
Different physical processes may only be applicable to different phases of the system such that hydraulic flow is necessary in the fluid phase but construction materials are usually not meant to be flowing and solid mechanics would rather apply there. In that sense the fluid and solid phase need to be separated and treated differently. On the other hand, rocks are usually porous and allow fluid to flow through, therefore rock phase can have fluid flow and solid mechanics both at play, described by a system of poromechanics.

### Multiphysics coupling
A multiphysics coupling is represented by a physical phenomenon interacting with another. It is characterized by the presence of at least two physical variables in the governing physical law. One example is thermal advection where heat is transported by the motion of the fluid (in contrast with diffusion), like cooling your room with air conditioning.

$$
\frac{\partial T}{\partial t}+v\cdot\mathrm{\nabla T}=\alpha\mathrm{\nabla}^2T+\frac{q}{\rho c_p}
$$

Here the two variables are v and T. Depending on which conservation equation the physical law falls into, the primary variable is distinguished from the secondary variables. In this case, we are dealing with heat transfer corresponding therefore conservation of energy. So the primary variable is T and the secondary variable is v.

At a more indirect level, multiphysics couplings can express themselves in the equations of state where physical properties such as material properties can depend on different physical variables. One example is fluid viscosity which is influenced by both temperature and pressure which in turns influences fluid flow, from the Navier-Stokes equations.


## Finite Element implementation of multiphysics couplings

We need to solve for the additional equations brought in by the multiphysics couplings.
After converting the strong form of the equation terms into the weak form, they need to be discretised.
The discrete form will as usual correspond to an equation of the type:

$$
K a = f
$$

Adding other physical variables to solve for through multiphysics processes will increase the number of degrees of freedom of the system, represented by the size of vector a. Because each variable has to be solved for at every node. For a 1D thermo-mechanical problem solved on a mesh of X nodes, the number of degrees of freedom for the system will be 2X.
Since the size of a influences the size of the stiffness matrix we are solving for, multiphysics problems are generally more computationally heavy as they are inverting a larger stiffness matrix.
Note that each variable can be discretised differently so their test/shape functions will be dependent on the primary variable considered. (give example of regularization of Stokes flow with second order velocity and first order pressure? Maybe just orally)

Derivation of the nonlinear term of thermal advection which fall in the discrete form in the off diagonal of the stiffness matrix (more help from Oriol)

### Boundary conditions

Boundary conditions need to apply to each primary variables separately as they are needed to close each governing equation. They are usually captured as constant value or constant flow, described in Finite Element by respectively Dirichlet or Neumann boundary condition. For solid mechanics for example, this is respectively prescribed displacement (Dirichlet BC for u) or prescribed stress (Neumann BC for u).

### Time discretisation

Physical processes have different time scales. Taking examples of chemical reactions vs pressure diffusion vs mechanical shear heating. Solving for multiphysics means accommodating for all those time scales. Most basic solution is to align with the smallest timescale but that can lead in computational heavy simulations if the timescales have orders of magnitude difference. In that case, instead of solving an implicit coupling, the coupling can be explicit where the two different physics are solved separately, and the coupled variable is updated at a different frequency.

### interaction through interface (Oriol)
physics active in different domains
solved differently
interacting at the interface
introduce FSI
