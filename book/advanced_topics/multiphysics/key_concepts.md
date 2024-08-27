## Key concepts

Many Civil Engineering and Geosciences problems relating to structure or rock deformations and fluid flow can be cast as THMC physical phenomena, Thermo-Hydro-Mechanical-Chemical. Sometimes some of the physical processes can be neglected, for instance when pure mechanical analysis can be performed on structures. In other cases however, multiple physical processes and their interactions need to be accounted for. That is when we speak of multiphysics analysis.

example of pure mech analysis vs heat treatment for metals (https://mooseframework.inl.gov/gallery.html)

### Conservation laws
For those problems, the different existing laws of physics are encompassed into the conservation of three main quantities: momentum, mass and energy.

Conservation of momentum:

$$
\mathrm{\nabla}\cdot\boldsymbol{\sigma}=\boldsymbol{0}
$$

The equation is written in its simplest form of quasi-static equilibrium without considering dynamics (ref book). Here, the displacement variable $\mathbf{u}$ is implicitly the main variable of this system and is linked to the stress with a constitutive model. For example in 1D elasticity, the stress is directly a function of the displacement gradient which simplifies the conservation of momentum to

$$
\mathrm{\Delta \mathbf{u}}=\mathbf{0}
$$

Conservation of mass:

$$
\frac{\partial P}{\partial t}=\mathrm{\nabla}\cdot\left(D\mathrm{\nabla P}\right)+q
$$

Where $P$ is the pressure variable. So this equation corresponds to a transient pressure diffusion. $q$ is a source term indicating injection of production of fluid. $D$ is the diffusion coefficient which for porous materials corresponds to the permeability $k$.

Conservation of energy:

$$
\frac{\partial T}{\partial t}=\alpha\mathrm{\nabla}^2T+\frac{q}{\rho c_p}
$$

Where $T$ is the temperature variable. This is a transient diffusion of temperature. $q$ corresponds to a heat flux or sink. $\alpha$ is the thermal conductivity.

The primary variables are respectively displacement $u$, pressure $P$ and temperature $T$.
However, equations can be rewritten with stress instead of displacement quite commonly or for hydrogeology with hydraulic head instead of pressure.
Note that the governing equations are written in a Lagrangian formulation. In Eulerian formulation, velocity is the primary momentum variable.

### Domain decomposition
Different physical processes may only be applicable to different phases of the domain. Hydraulic flow is necessary in a liquid phase so for example construction materials are not and solid mechanics would rather apply there. In that sense the fluid and solid phase need to be separated and treated differently. On the other hand, rocks are usually porous and allow fluid to flow through, therefore a rock phase can have fluid flow and solid mechanics both at play, described by a system of poromechanics.

### Multiphysics coupling
A multiphysics coupling is represented by a physical phenomenon interacting with another. It is characterized by the presence of at least two physical variables in the governing physical law. One example is thermal advection where heat is transported by the motion of the fluid (in contrast with diffusion), like cooling your room with air conditioning.

$$
\frac{\partial T}{\partial t}+v\cdot\mathrm{\nabla T}=\alpha\mathrm{\nabla}^2T+\frac{q}{\rho c_p}
$$

Here the two variables are $v$ and $T$. Depending on which conservation equation the physical law falls into, the primary variable is distinguished from the secondary variables. In this case, we are dealing with heat transfer corresponding therefore conservation of energy. So the primary variable is $T$ and the secondary variable is $v$.

At a more indirect level, multiphysics couplings can express themselves in the equations of state where physical properties such as material properties can depend on different physical variables. One example is fluid viscosity which is influenced by both temperature and pressure which in turns influences fluid flow, from the Navier-Stokes equations.
