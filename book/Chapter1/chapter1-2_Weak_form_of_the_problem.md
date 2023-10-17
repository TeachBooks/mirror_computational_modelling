# Weak form of the Problem

In the FE method, before the problem is discretized, the governing equation is rewritten in the so-called **weak form**. One of the key aspects of the FE method is that we do not seek a nodally exact approximation, but an approximation that minimizes certain energy functional. This is why we aim at finding solutions in a *weak* or *variational* sense, which means that the FE solution might not be nodally exact, but it is the solution that minimizes the global energy of the system.

```{figure} .././images/Chapter1/1_3_1.png
---
height: 400px

name: 1_3_1
---
Strong form to weak form 
```

## Derivation of the weak form

In practice, the weak form of the problem is derived by multiplying the strong form by a test function and then integrate by parts the terms containing derivatives[^integration_by_parts]. In this manner, the order of derivatives appearing in the equations is reduced and the resulting form is symmetric (in general), facilitating a more efficient numerical solution. 

Let's put this in practice for the rod equation {eq}`1drod`. The first step is premultiplication of left hand side and right hand side with a test function $w(x)$ and integrating over the domain:

$$ -\int_{0}^{L} wEA \frac{\partial^{2} u}{\partial x^{2}}\,dx = \int_0^Lwq\,dx,\quad\forall\quad w$$

The $\forall w$ means that the equality has to hold for all possible test functions $w$. Note that a solution of the *strong form* also satisfies this equation. 

Next, integration by parts is used to get rid of the second order derivative in $u$:

$$ \int_{0}^{L} \frac{\partial w}{\partial x}EA \frac{\partial u}{\partial x}\,dx -w EA \left.\frac{\partial u}{\partial x}\right|_0^L = \int_0^Lwq\,dx,\quad\forall\quad w$$ (1drod_weak)

Note that after integrating by parts, a boundary term appears. This term is often used to enforce the boundary conditions, see next subsection.

## Boundary Conditions 

We typically distinguish between two[^BC_types] type of boundary conditions:

- **Dirichlet** (or *essential*) boundary conditions, where we enforce the value of the solution. In that case $u=u_0$ at $x=0$, with $u_0=0$.
- **Neumann** (or *natural*) boundary conditions, where we enforce the flux (or force). In that case $EA \frac{\partial u}{\partial x}=F$ at $x=L$, with $F=10$.

To enforce Dirichlet boundary conditions we strongly[^weak_bc] prescribe the value of the solution and set the test function to zero at that boundary. This effectively means that the boundart term coming from the integration by parts evaluated at the Dirichlet boundary goes to zero.

$$
{\color{red}w} EA \left.\frac{\partial u}{\partial x}\right|_{x=0} = {\color{red}0} EA \left.\frac{\partial u}{\partial x}\right|_{x=0} = 0
$$ (1drodDirichlet)

To enforce the Neumann boundary condition we just need to replace the value of the prescribed flux (or force) in the boundary term apearing after the integration by parts. This type of boundary condition is often called *natural* as it naturally appears when deriving the weak form.

$$
w {\color{red}EA \left.\frac{\partial u}{\partial x}\right|_{x=L}} = w(L){\color{red}F}.
$$ (1drodNeumann)

Now we can replace equations {eq}`1drodDirichlet` and {eq}`1drodNeumann` into the weak form {eq}`1drod_weak`, and send to the righ-hand site the terms that do not depend on the unknown $u$. This leads us to the final weak form:

$$ \int_{0}^{L} \frac{\partial w}{\partial x}EA \frac{\partial u}{\partial x}\,dx = \int_0^Lwq\,dx + w(L)F,\quad\forall\quad w$$ (1drod_weak_final)

<!-- - Link to virtual displacement -->

[^integration_by_parts]: Note that this is not a general rule. There are cases of terms containing derivatives that might not be integrated by parts, typically non-symmetric terms.

[^BC_types]: We can also find Robin type of boundary conditions, which are a mix between Dirichlet and Neumann type, for example: $\alpha u + EA \frac{\partial u}{\partial x}=f$.

[^weak_bc]: We can also enforce Dirichlet boundary conditions in a *weak* sense, by introducing additional terms on the weak form that penalize the difference between the solution and the prescribed value at the boundary. This will not be covered in this chapter.
