# 1.7. Isoparametric element in 1D

Considering a mesh using finite elements, each cell can have a unique shape and orientation. However, when performing numerical integration, it is preferable to define the selected integration scheme on a reference element and at the same reference cell, define the shape functions.
Then a special technique is applied in order to bypass the need to prescribe several integration domains. This technique is commonly used in software using FEM and is called isoparametric mapping.

## Why do we need isoparametric mapping?

Let's consider a linear 3-node element with the nodes located in x=2, x=4 and x=6, respectivelly.

In principle shape functions can be defined globally. For example, considering the quadratic line element in 1D, we can state that all shape functions should have the form of a quadratic polynomial, as follows.

$$ N_i(x)= a_ix^2 + b_ix + c_i $$

At node i, the associated shape function must be equal to 1 and zero at the other two nodes.

For an element with three nodes, there are three associated shape functions which can be solved for the coefficients $a_i$, $b_i$, $c_i$

```{figure} .././images/Chapter1/1_7_1.png
---
height: 200px
name: 1_7_1
---
Linear 3-node element.
```


However this is not often the case in the implementation of the FEM method, where the shape functions are defined on a reference element. Then, all the elements of the mesh have the same "reference element". This reference element is defined in an auxiliary coordinate system.

```{figure} .././images/Chapter1/1_7_2.png
---
height: 200px
name: 1_7_2
---
The new reference cordinate system.
```

In this new coordinate system, we redefine the shape functions and the integration points.

```{figure} .././images/Chapter1/1_7_3.png
---
height: 200px
name: 1_7_3
---
Shape functions in the reference coordinate system.
```

The next step is to link this reference element with an actual element in physical space. In order to achieve that, we will use a mapping between the $ξ$ values of the reference coordinate system and the x values of the global coordinate system.

At this point it is useful to recall that we need this mapping in order to define the element's stiffness matrix, which involves integration over the element domain and derivatives of the shape functions in the global coordinate system.

## How to implement isoparametric mapping?

The first step is to construct the relation between x and $ξ$ with the shape functions.

$$ x= \sum_{i=1}^{n-node}\N_i(\xi) x_i $$

In isoparametrix mapping we construct the relation between the two coordinate systems with the shape functions.

We parameterise the mapping of coordinates similarly to the unknown fields {u}.

```{figure} .././images/Chapter1/1_7_4.png
---
height: 200px
name: 1_7_4
---
Mapping process between the two coordinate systems.
```

The next step is to calculate the derivatives of the shape functions w.r.t. x- coordinate without the need to defeine the shape functions in terms of the x- coordinate.

% Add Equation 

Following, we must integrate first on the x- coordinate and then on the coordinates of the reference element.

% Add Equation 
% Add Equation 


Stiffness matrix for the Poisson Equation

% Add Equations 



## Recap

Isoparametric elements are used in finite element software. In this case shape functions are formed in a simple element configuration (unit length side and width sides aligned with the coordinate system). 

The characteristic of an isoparametric element is that both geometry and displacement are interpolated using the same shape functions.

Things to remember about isoparametric mapping:

- In terms of implementation, only one function is enough to evaluate the shape function of each element, irrespective of the exact shape of the element. 
- It allows simple application of numerical integration.
- It allows higher order elements to have curved edges.

In practice, the point (x, y) in the cartesian plane is represented as follows:

$$ x= \sum_{i=1}^{nn}\N_i(\xi,\eta) x_i $$
$$ y= \sum_{i=1}^{nn} \N_i(\xi,\eta) y_i $$

where (ξ,η) are known as the natural coordinates and nn is the number of nodes of an element.

By using isoparametric mapping, shape functions can be defined on simple shapes, such as the bi-unit square. For example, the displacement  in the x direction at a point is given by:

$$ u^h= \sum_{i=1}^{nn}\N_i(ξ,η) α_{ix} $$



