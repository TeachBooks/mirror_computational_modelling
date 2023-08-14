# 1.6. Special case for linear Langrangian Shape Functions

As mentioned in previous chapters, the weak form is descritised such that it can be solved with a computer. This is done by assuming a certain shape for the displacement $u(x)$ and restricting the set of weight functions $w(x)$ to all functions of that shape.

We introduce a finite set of **shape functions** (or interpolation functions) 

$N_i(x)$ with $i\in[0,n-1]$ 

and say that our approximate solution $u^h(x)$ is a linear combination of these shape functions:

$$ u^h(x) = \sum_{i=0}^{n-1}N_i(x)u_i $$

where $u_i$ is the coefficient with which $N_i$ is multiplied.

Note that $u_i$ is not a function of $x$. In the finite element method, a mesh with nodes and elements is used and the shape functions are defined such that every shape function $N_i$ belongs to a node with coordinates $x_i$ and that that shape function is equal to 1 at its own node and equal to zero at all other nodes:

$$ N_i(x_j) = \left\{ \begin{array}{cl} 1, & i=j \\ 0, & i\neq j\end{array} \right. $$
