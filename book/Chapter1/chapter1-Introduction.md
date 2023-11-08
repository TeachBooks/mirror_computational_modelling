# Introduction to Finite Elements

In this chapter we will introduce all the steps that are usually followed to solve a PDE using the FE method, from the definition of the PDE to the solution of a linear system of equations. To make the learning curve ease, we will exemplify all these steps with a simple linear static problem in 1 dimension (1D).

<!-- For this purpose, both linear and non-linear problems will be demonstrated. The FEM is a broadly used numerical tool that solves PDEs. The areas of application range from solid and structural mechanics to fluid mechanics. In recent years the application of such a method for solving complex physical phenomena end geometries is receiving more attention and is more frequently applied are it is bound with computational power. To be more specific, when a domain is discretised using FEM, a system of linear equations is built. Then, this matrix is solved numerically, using the available computational power. -->


This chapter includes the following sections:

```{tableofcontents}
```

The general goal of the FE method is to convert PDEs into a form which we, or rather a computer, can solve. The reason for doing this is because it allows a PDE with no analytical solution for the full domain, to be approximated by solving it on smaller 'elements'. This *discretization* into several elements enables us to solve the problems in irregular geometries, different materials, dynamic effects, jumps or complex changes in geometry, ...

The general scheme for FE problems is as follows:
1. From the PDE ([strong form](./chapter1-1_Strong_form_of_the_problem.md)), derive the [weak form](./chapter1-2_Weak_form_of_the_problem.md) of the problem.
2. Discretize the domain and get all elements, nodes, and their properties
3. Make piece-wise functions, typically polynomials, as approximations for the real solution
4. Substitute the [discrete functions](./chapter1-3_Discrete_form.ipynb) into the weak form
5. Assemble the matrices and vectors element by element to obtain the equations for the full solution in [matrix form](./chapter1-4_Matrix_form.ipynb)
6. Solve the resulting system of equations

We will explain this for the case of a rod that is loaded in its axial direction as an application of the 1-dimensional Poisson equation. Note that the Laplacian operator (i.e. the second derivative) in the Poisson equation appears in many PDEs in various fields of engineering. 

