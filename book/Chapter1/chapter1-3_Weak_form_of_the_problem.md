# 1.3. Weak form of the Problem

In the finite element method, before the problem is discretized the governing equation is rewritten in the so-called weak form. 

As mentioned in the introduction, the finite element method, in contrast to the the finite difference method, is variational. This becomes more clear in this chapter, as the weak form of the equation is also known as the 'variational form' or 'variational equation'. Hence, the finite element method is a variational method, addressing the weak (variational) form of the corresponding governing equation.

The weak form of the problem is derived by multiplying the strong form by a weight function and then integrate by parts. In this manner, the order of derivatives appearing in the equations is reduced and the resulting equation facilitates a more convenient numerical solution.


The first step is premultiplication of left hand side and right hand side with a weight function $w(x)$ and integrating over the domain:

$$ \int_{0}^{L} wEA \frac{\partial^{2} u}{\partial x^{2}}\,dx = -\int_0^Lwq\,dx,\quad\forall\quad w$$

The $\forall w$ means that the equality has to hold for all possible weight functions $w$. This integral form is only satisfied for all possible weight functions if the original equation is satisfied at every point $x$. Next, integration by parts is used to get rid of the second order derivative in $u$:

$$ \int_{0}^{L} \frac{\partial w}{\partial x}EA \frac{\partial u}{\partial x}\,dx = \int_0^Lwq\,dx,\quad\forall\quad w$$

After integration by parts, a boundary term appears. As long as boundary conditions are Dirichlet boundary conditions (i.e. the primary field $u$ is prescribed), this boundary term drops out. For the point load in the problem sketched above, the values will be added to the right hand side vector of our system of equations. The expression above is called the **weak form** of the PDE.

```{figure} .././images/Chapter1/1_3_1.png
---
height: 300px
name: 1_3_1
---
Strong form to weak form 
```




- Link to virtual displacement
