# 1.3. Weak form of the Problem


### 1.3.1 Derivation of the weak form
In the FE method, before the problem is discretized, the governing equation is rewritten in the so-called **weak form**. One of the key aspects of the FE method is that we do not seek a nodally exact approximation, but an approximation that minimizes certain energy functional. This is why we aim at finding solutions in a *weak* or *variational* sense, which means that the FE solution might not be nodally exact, but it is the solution that minimizes the global energy of the system.

In practice, the weak form of the problem is derived by multiplying the strong form by a weight function and then integrate by parts. In this manner, the order of derivatives appearing in the equations is reduced and the resulting equation facilitates a more convenient numerical solution.


The first step is premultiplication of left hand side and right hand side with a weight function $w(x)$ and integrating over the domain:

$$ \int_{0}^{L} wEA \frac{\partial^{2} u}{\partial x^{2}}\,dx = -\int_0^Lwq\,dx,\quad\forall\quad w$$

The $\forall w$ means that the equality has to hold for all possible weight functions $w$. This integral form is only satisfied for all possible weight functions if the original equation is satisfied at every point $x$. Next, integration by parts is used to get rid of the second order derivative in $u$:

$$ \int_{0}^{L} \frac{\partial w}{\partial x}EA \frac{\partial u}{\partial x}\,dx = \int_0^Lwq\,dx,\quad\forall\quad w$$

After integration by parts, a boundary term appears. As long as boundary conditions are Dirichlet boundary conditions (i.e. the primary field $u$ is prescribed), this boundary term drops out. For the point load in the problem sketched above, the values will be added to the right hand side vector of our system of equations. The expression above is called the **weak form** of the PDE.

```{figure} .././images/Chapter1/1_3_1.png
---
height: 400px
name: 1_3_1
---
Strong form to weak form 
```
### 1.3.2 Boundary Conditions 

To complete the problem, boundary conditions must be specified. A Dirichlet (essential) boundary condition prescribes the displacement at a point. For example

$$ u=0 at x=0 $$

prescribes the displaecement at left end of the barto be zero.


A Neumann (natural) boundary condition prescribes the applied traction $ σ_n $.

 $ σ_n  = h$, at $ x = L $

 when n is the outward normal to the bar. The above boundary condition sets the applied traction at x=L equal to h.

```{figure} .././images/Chapter1/1_3_2.png
---
height: 400px
name: 1_3_2
---
example rod with distributed load
```

Considering that $ σ= Ε u_x $, applying a force at the end of a bar is equivalent to applying $u_x$.

So finally, we get the following.


$$ -E u_{xx} =f  ,  0<x<L $$
$$ u=0 ,  at  x=0 $$
$$ E u_{xn} =h , at  x=L $$  
 





--------------------------------------------------------------------------------
Back at the linear elastic rod problem of paragraph 1.2. At the fixed degrees of freedom, there is zero displacement  (i.e. homogeneous Dirichlet conditions). In case that non-zero Dirichlet conditions, additional steps need to be taken, as the matrix **K** cannot be simplified and thus cannot be inverted.







- Link to virtual displacement
