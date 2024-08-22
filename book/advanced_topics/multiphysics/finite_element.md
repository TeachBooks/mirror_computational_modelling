## Finite Element implementation

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
