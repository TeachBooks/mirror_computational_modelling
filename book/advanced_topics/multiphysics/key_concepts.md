## Key concepts

Many Civil Engineering and Geosciences problems relating to structure or rock deformations and fluid flow can be cast as THMC physical phenomena, Thermo-Hydro-Mechanical-Chemical. Sometimes some of the physical processes can be neglected, for instance when pure mechanical analysis can be performed on structures (example of mechanical indentation in [Figure 2](#fig-indenter-video)). In other cases however, multiple physical processes and their interactions need to be accounted for (example of thermo-mechanical welding in [Figure 2](#fig-welding-video)). That is when we speak of multiphysics analysis.

<figure id="fig-indenter-video" style="text-align: left; margin: auto;">
  <video width="300" controls autoplay loop muted preload="metadata" poster="thumbnail.jpg">
    <source src="https://mooseframework.inl.gov/large_media/contact/2d_indenter.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <figcaption style="margin-top: 8px; font-size: 14px; color: #555; text-align: left;">
    <strong>Figure 1:</strong> An elastic axisymmetric spherical indenter penetrates into a base material. Sourced from the <a href="https://mooseframework.inl.gov/gallery.html" target="_blank" rel="noopener noreferrer">MOOSE framework simulation gallery</a>.
  </figcaption>
</figure>

<figure id="fig-welding-video" style="text-align: left; margin: auto;">
  <video width="500" controls autoplay loop muted preload="metadata" poster="thumbnail.jpg">
    <source src="https://mooseframework.inl.gov/large_media/gallery/weld.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <figcaption style="margin-top: 8px; font-size: 14px; color: #555; text-align: left;">
    <strong>Figure 2:</strong> Thermo-mechanical simulation of the laser welding process (with a total of 8 weld passes) joining two separate vessel segments. Sourced from the <a href="https://mooseframework.inl.gov/gallery.html" target="_blank" rel="noopener noreferrer">MOOSE framework simulation gallery</a>.
  </figcaption>
</figure>

### Conservation laws
For those problems, the different existing laws of physics are encompassed into the conservation of three main quantities: momentum, mass and energy.

<ins>Conservation of momentum:</ins>

$$
\mathrm{\nabla}\cdot\boldsymbol{\sigma}=\boldsymbol{0}
$$

The equation is written in its simplest form of quasi-static equilibrium without considering dynamics (see [<em>Equilibrium equations</em>](../../introduction/Exercises/supported-rod.ipynb)). Here, the displacement variable $\mathbf{u}$ is implicitly the main variable of this system and is linked to the stress with a constitutive model. For example in 1D elasticity (check example of [<em>Rod with elastic support</em>](../../continuum_linear/continuum_mechanics.md#equilibrium-equations)), the stress is directly a function of the displacement gradient which simplifies the conservation of momentum to

$$
\mathrm{\Delta \mathbf{u}}=\mathbf{0}
$$

<ins>Conservation of mass:</ins>

$$
\frac{\partial P}{\partial t}=\mathrm{\nabla}\cdot\left(D\mathrm{\nabla P}\right)+q
$$

Where $P$ is the pressure variable. So this equation corresponds to a transient pressure diffusion. $q$ is a source term indicating injection of production of fluid. $D$ is the diffusion coefficient which for porous materials corresponds to the permeability $k$.

<ins>Conservation of energy:</ins>

$$
\frac{\partial T}{\partial t}=\alpha\mathrm{\nabla}^2T+\frac{q}{\rho c_p}
$$

Where $T$ is the temperature variable. This is a transient diffusion of temperature. $q$ corresponds to a heat flux or sink. $\alpha$ is the thermal conductivity.

The ***primary variables*** are respectively displacement $\mathbf{u}$, pressure $P$ and temperature $T$.
Still, equations can be rewritten with stress instead of displacement or, in hydrogeology, with hydraulic head instead of pressure.
Note that the governing equations are written in a Lagrangian formulation. In Eulerian formulation, velocity is the primary momentum variable.

### Domain decomposition
Different physical processes may only be applicable to different phases of the domain. For example, hydraulic flow is only applicable for a fluid, in a liquid phase. For the case of simulating the behaviour of construction materials which are solid, solid mechanics would rather apply there. If an external fluid is considered and we are dealing with an interaction fluid-structure, the fluid and solid phases need to be separated and solved differently. On the other hand, rocks are usually porous and allow fluid to flow through, therefore a rock phase can have fluid flow and solid mechanics both at play, described together at the same time by a system of poromechanics.

### Multiphysics coupling
A multiphysics coupling is represented by a physical phenomenon interacting with another. It is characterized by the presence of a physical variable other than the primary one in a governing physical law. One example is thermal advection where heat is transported by the motion of the fluid (in contrast with diffusion), like cooling your room using air conditioning.

$$
\frac{\partial T}{\partial t}+v\cdot\mathrm{\nabla T}=\alpha\mathrm{\nabla}^2T+\frac{q}{\rho c_p}
$$

Here, the two variables are $\mathbf{v}$ and $T$. Depending on which conservation equation the physical law falls into, the primary variable is distinguished from the secondary variables. In this case, we are dealing with heat transfer corresponding therefore to the conservation of energy. So the primary variable is $T$ and the secondary variable is $\mathbf{v}$.

At a more indirect level, multiphysics couplings can express themselves in the equations of state where physical properties such as material properties can depend on different physical variables. One example is fluid viscosity that is influenced by both temperature and pressure which in turns influences fluid flow, in the Navier-Stokes equations.
