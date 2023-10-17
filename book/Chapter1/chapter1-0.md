# Introduction to Finite Elements

In this chapter we will introduce all the steps that are usually followed to solve a PDE using the FE method, from the definition of the PDE to the solution of a linear system of equations. To make the learning curve ease, we will exemplify all these steps with a simple linear static problem in 1 dimension (1D).

<!-- For this purpose, both linear and non-linear problems will be demonstrated. The FEM is a broadly used numerical tool that solves PDEs. The areas of application range from solid and structural mechanics to fluid mechanics. In recent years the application of such a method for solving complex physical phenomena end geometries is receiving more attention and is more frequently applied are it is bound with computational power. To be more specific, when a domain is discretised using FEM, a system of linear equations is built. Then, this matrix is solved numerically, using the available computational power. -->


This chapter includes the following sections:

```{tableofcontents}
```

## Problem setting and notation

The general goal of the FE method is to convert PDEs into a form which we, or rather a computer, can solve. The reason for doing this is because it allows a PDE with no analytical solution for the full domain, to be approximated by solving it on smaller 'elements'. This *discretization* into several elements enables us to solve the problems in irregular geometries, different materials, dynamic effects, jumps or complex changes in geometry, ...

The general scheme for FE problems is as follows:
1. From the PDE ([strong form](./chapter1-2_Strong_form_of_the_problem.ipynb)), derive the [weak form](./chapter1-3_Weak_form_of_the_problem.md) of the problem.
2. Discretize the domain and get all elements, nodes, and their properties
3. Make piece-wise functions, typically polynomials, as approximations for the real solution
3. Replace the [discrete functions](./chapter1-4_Discrete_form.ipynb) into the weak form to obtain elemental matrices and vectors
4. Assemble the matrices to obtain the equations for the full solution
5. Solve a system of equations

We will explain this for the case of a prismatic rod that is loaded in its axial direction, $q(x)$. Here prismatic means that there no geometry or property changes along its length. The equation of motion (EOM) that describes this phenomenon is 

$$ 
- EA \frac{\partial^2u(x,t)}{\partial x^2} = q(x) 
$$ (EOM)

With

| | | |
| --- | --- | --- |
| $E$ | stifness of the rod | Pascals |
| $u$ | rod elongation | meters |

Additionally:
- We take the rod fixed at $x=0$, that means that $u(0) = 0 $. 
- A point load $P$ is applied at the far end of the beam at $x=L$.

$$ 
q(x)=\begin{cases}
P\quad\text{if }x=L,\\
0\quad\text{otherwise}.
\end{cases} 
$$ (pointloadapplication)

Let's assume that we want to find an analytical expression of a function that describes the displacement at any point of the rod, denoted as $u(x)$. In general, and mostly depending on the complexity of the forcing term $q(x)$, it is difficult to find an analytical expression that is defined at all points, $u(x)\, ∀ x\in[0,L]$.

```{figure} .././images/Chapter1/1_1_1.png
---
height: 300px
name: 1_1_1
---
Analytical vs approximated functions
```

Instead, we might be interested in knowing the value of the function at specific points, $u(x_0)$, $u(x_1)$, $u(x_2)$,..., $u(x_N)$, (see the red dots in Figure {numref}`1_1_1`). From these set of values, one can reconstruct an approximated function $\tilde{u}(x)$ by, for instance, using a spline interpolation between points (see the green line in Figure {numref}`1_1_1`).

For smooth enough functions, $u(x)$, as we increase the number of evaluation points, $N$, the approximated solution solution $\tilde{u}(x)$ will be closer to $u(x)$.

```{admonition} What's ahead?
In this chapter you will learn how to find approximate solutions like $\tilde{u}_N(x)$ by using the FE method. 
```

## Notation

In this chapter we will use the following notation, see Figure {numref}`1_1_2`: 
* $u_i:=u(x_i)$, the function evaluated at location $x_i$. 
* $\Delta x_i:=x_i-x_{i-1}$, the element size between two points (nodes), $x_{i-1}$ and $x_i$.
When considering constant element size, in a domain of lenght $L$, $x\in[0,L]$ with $N$ elements, the element size will be $\Delta x=L/N$.

```{figure} .././images/Chapter1/1_1_2.png
---
height: 300px
name: 1_1_2
---
Notation
```
