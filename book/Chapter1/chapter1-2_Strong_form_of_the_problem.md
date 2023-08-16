# 1.2. Strong form of the problem

Let's consider we need to describe a problem mathematically, meaning express the process taking place using symbols and equations. 
In order to have a complete descreption of the problem, one needs to formulate a well-posed set of the underlying differential equations with boundary conditions and in some cases also initial conditions. Solving the strong form of the problem leads to the exact solution of the continuous system. 

At this point, let's take as an example the one dimensional poisson equation to illustrate at first the so-called strong form of the problem. 


$$ -\nu \frac{\partial^{2} u}{{\partial x}^{2}} = f $$

The poisson equation is often solved by using the finite element method. This equation can be used to express various physical phenomena such as steady-state heat conduction and flow in permeable media (Darcy’s law).


In a general form, the poisson equation can be written as follows: 

$$ −∇· q + f = 0 $$

where q is a flux vector and f is a source term. 

In the case of heat conductivity, q is
the heat flux vector. 
In Darcy’s law, q is the flow rate. 

The constitutive relationship is given by:

$$ q= - \kappa  ∇ u $$

where $$ q_i=-\kappa_{ij} u_j $$

and u is a potential 

Keep in mind that the constitutive relationship always depends on the problem being solved. 

For example, in linear heat conduction, the scalar u in the above equation is the temperature. In case of structural problems, u can also be the displacement. For Darcy’s law, u is the hydraulic head.

For an isotropic medium, $$ \kappa = k I $$

where k is the thermal conductivity

For Darcy’s law, u is the hydraulic head and κ is known as the hydraulic conductivity.
