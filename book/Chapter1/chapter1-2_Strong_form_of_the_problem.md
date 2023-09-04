# 1.2. Strong form of the problem

One of the key aspects of the FE method is that we express the set of governing equations in a [*weak form*](./chapter1-3_Weak_form_of_the_problem.md) or also called *variational* form. Before deriving the *weak form* of the problem we need to state the set of governing equations (PDEs) with appropriate boundary and initial conditions that describe the physisc of the solution. This is what we understand as the **strong form**. Solving the strong form of the problem leads to the exact solution of the continuous system. 

At this point, let's take as an example the one dimensional Poisson equation to illustrate at first the so-called strong form of the problem. 

$$ -\frac{\partial}{\partial x} \left(\nu \frac{\partial u}{{\partial x}}\right) = f ,$$

where $\nu$ is a material property, $u$ the solution and $f$ a source, all of which can depend on the coordinate $x$. 

This equation can be used to express various physical phenomena such as steady-state heat conduction, elastic deformation of a rod or flow in permeable media (Darcy’s law).

In a general form, the Poisson equation can be written as follows: 

$$ −(∇ \cdot q) + f = 0 $$

where $(\nabla \cdot )$ is the divergence operator and $q$ is a flux vector whos expresion depends on the problem at hand. In the case of heat conductivity, $q$ is the heat flux vector, while in Darcy’s law, $q$ is the flow rate. The typical constitutive relationship between the flux $q$ and the unkown solution $u$ is given by:

$$ q= - \kappa  ∇ u $$

Note that the solution $u$ can either be a scalar function, for example heat, or a vector function. For example, in linear heat conduction, the scalar $u$ in the above equation is the temperature. In case of structural problems, $u$ can also be the displacement. For Darcy’s law, $u$ is the hydraulic head. Keep also in mind that the constitutive relationship always depends on the problem being solved and $ \kappa $ can take different meanings, for the heat equation $ \kappa $ is the thermal conductivity and for Darcy’s law $ \kappa $ is known as the hydraulic conductivity. In a general form, $ \kappa $ is an anisotropic tensor, therefore, using an index notation the general form of flux is:

$$ q_i= - \kappa_{i,j}  u_{,j}, $$

where the notation $u_{,j}$ denotes the derivative of $u$ along the $j$-th coordinate. For an isotropic medium, 

$$ \kappa = k I .$$

## The strong form of the linear elastic rod
Now, let's consider an example of a one-dimensional bar to apply the Poisson equation. 

```{figure} .././images/Chapter1/1_5_1.png
---
height: 200px
name: 1_5_1
---
One dimensional bar
```

An application of the Poisson equation is the extension of one-dimensional structural elements. Let us consider a horizontal steel bar with a stiffness $EA = 1.0 \cdot 10^3$ kN with a load applied at the right side of $10$ kN and a length of $5$ m and a distributed load along its length $q(x)$. This equilibrium problem can be described with the following differential equation:

$$-EA \frac{\partial^{2} u}{{\partial x}^{2}} = q(x),$$

where $u$ is the displacement of the bar as function of location $x$. As can be seen, the form of this equation is exactly the same as the 1D Poisson equation shown above. The only difference is in the physical interpretation of $u$ and $q$ and that instead of the constant $\nu$ we use the constant $EA$ (Young's modulus $E$ times cross section area $A$) to describe the stiffness. 
