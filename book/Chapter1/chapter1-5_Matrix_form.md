# 1.5. The Matrix form

Because the number of possible functions $w(x)$ is infinite, the expression above represents an infinite number of equations. There is also an infinite number of possible solutions $u(x)$, of which one is the exact solution of our problem. In the next step, we discretize the weak form such that it can be solved with a computer. This is done by assuming a certain shape for $u(x)$ and restricting the set of functions $w(x)$ to all functions of that shape. We introduce a finite set of **shape functions** (or interpolation functions) $N_i(x)$ with $i\in[0,n-1]$ and say that our approximate solution $u^h(x)$ is a linear combination of these shape functions:

$$ u^h(x) = \sum_{i=0}^{n-1}N_i(x)u_i $$

where $u_i$ is the coefficient with which $N_i$ is multiplied. Note that $u_i$ is not a function of $x$. In the finite element method, a mesh with nodes and elements is used and the shape functions are defined such that every shape function $N_i$ belongs to a node with coordinates $x_i$ and that that shape function is equal to 1 at its own node and equal to zero at all other nodes:

$$ N_i(x_j) = \left\{ \begin{array}{cl} 1, & i=j \\ 0, & i\neq j\end{array} \right. $$


This way, the coefficent $u_i$ is equal to the displacement at node $i$: $u^h(x_i) = u_i$. By solving for $u^h$ instead of for $u$ our solution space is no longer infinitely dimensional, but has become $n$-dimensional. If we know the $u_i$ values for all $i$'s from 0 to $n-1$, we know $u^h$ for every $x$ in our domain. We are making an approximation here, it may be impossible to construct the true solution $u(x)$ with the shape functions $N_i(x)$, but it can be shown that if we increase the number of nodes, the true $u(x)$ will be approximated with increased accuracy. 

In the finite element method, we substitute the discretized solution $u^h$ into the weak form equation. We are solving for $n$ values $u_i$. For this, we need to construct $n$ equations. Be reminded that with the "$\forall w$", we had an infinite number of equations. It turns out that it is useful to use the same shape functions $N_i(x)$ to pick $n$ relevant equations from this infinite set. We replace the $w(x)$ with its discretized counterpart $w^h(x)$:

$$ w^h(x) = \sum_{i=0}^{n-1}N_i(x)w_i $$

If the weak form has to hold for all possible functions $w^h$, this is equivalent to say that it has to hold for each of $w^h\in N_i$. So we construct the first equation by replacing $w$ with $N_0$, the second by replacing $w$ with $N_1$ and so until until equation $n$ with $N_{n-1}$. This gives:

$$ \int_{0}^{L} \frac{\partial N_i}{\partial x}EA \frac{\partial \left(\sum N_ju_j\right)}{\partial x}\,dx = \int_0^L N_iq\,dx$$

Because $u_j$ is not a function of $x$, it can be taken out of the integral to give:

$$ \sum_j \left(\left[ \int_{0}^{L} \frac{\partial N_i}{\partial x}EA \frac{\partial N_j}{\partial x}\,dx \right]u_j\right)= \int_0^L N_iq\,dx$$

or 

$$\mathbf{Ku} = \mathbf{f}$$

with 

$$K_{ij} = \int_{0}^{L} \frac{\partial N_i}{\partial x}EA \frac{\partial N_j}{\partial x}\,dx
\quad \text{and} \quad
f_i = \int_0^L N_iq\,dx$$


We still have a global integral and the product of all shape functions $N_i$ with all other shape functions $N_j$. However, we can make use of the fact that every individual shape function (and hence its derivatives) is equal to zero for the largest part of the domain. Moreover, we can split the integral in a sum of integrals over subdomains. Those subdomains are the **elements** of the finite element method. The element is a subdomain over which a fixed set of shape functions is active. For the case with linear shape functions, the element is defined as the domain between two neighboring nodes. We can then define the element stiffness matrix considering only those shape functions that are active in the element. 

```{figure} .././images/Chapter1/1_5_1.png
---
height: 300px
name: 1_5_1
---
Linear two-node element
```


If we introduce the $\mathbf{B}$ matrix (size $1\times 2$) to collect the derivatives of the shape functions in the element, we can write the element stiffness matrix as:

$$ \mathbf{K}_e = \int_{x_1}^{x_2} \mathbf{B}^T EA \mathbf{B} \,dx $$

where $x_1$ and $x_2$ are the $x$-coordinates of the two nodes of the element. For the 1D element with linear shape functions, $\mathbf{B}$ is defined as: 

$$\mathbf{B} = \left[\begin{matrix}\frac{-1}{\Delta x} & \frac{1}{\Delta x}\end{matrix}\right]$$

with $\Delta x = x_2-x_1$ Assuming a constant $EA$, evaluating the integrand over the element domain results in:

$$ \mathbf{K}_e = \frac{EA}{\Delta x}\left[\begin{matrix}1 & -1 \\ -1 & 1\end{matrix}\right]$$
