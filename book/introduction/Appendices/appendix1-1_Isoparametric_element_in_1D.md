# A1.1. Isoparametric element in 1D

Considering a mesh using finite elements, each cell can have a unique shape and orientation. However, when performing numerical integration, it is preferable to define the selected integration scheme on a reference element and at the same reference cell, define the shape functions.
Then a special technique is applied in order to bypass the need to prescribe several integration domains. This technique is commonly used in software using FEM and is called isoparametric mapping.

### Why do we need isoparametric mapping?

Let's consider a linear 3-node element with the nodes located in x=2, x=4 and x=6, respectivelly.

In principle shape functions can be defined globally. For example, considering the quadratic line element in 1D, we can state that all shape functions should have the form of a quadratic polynomial, as follows.

$$ N_i(x)= a_ix^2 + b_ix + c_i $$

At node i, the associated shape function must be equal to 1 and zero at the other two nodes.

For an element with three nodes, there are three associated shape functions which can be solved for the coefficients $a_i$, $b_i$, $c_i$

```{figure} ../.././images/Chapter1/1_7_1.png
---
height: 300px
name: 1_7_1
---
Linear 3-node element.
```


However this is not often the case in the implementation of the FEM method, where the shape functions are defined on a reference element. Then, all the elements of the mesh have the same "reference element". This reference element is defined in an auxiliary coordinate system.

```{figure} ../.././images/Chapter1/1_7_2.png
---
height: 200px
name: 1_7_2
---
The new reference cordinate system.
```

In this new coordinate system, we redefine the shape functions and the integration points.

```{figure} ../.././images/Chapter1/1_7_3.png
---
height: 200px
name: 1_7_3
---
Shape functions in the reference coordinate system.
```

The next step is to link this reference element with an actual element in physical space. In order to achieve that, we will use a mapping between the $ξ$ values of the reference coordinate system and the x values of the global coordinate system.

At this point it is useful to recall that we need this mapping in order to define the element's stiffness matrix, which involves integration over the element domain and derivatives of the shape functions in the global coordinate system.

### How to implement isoparametric mapping?

The first step is to construct the relation between x and $ξ$ with the shape functions.

$$ x= \sum_{i=1}^{n-node}N_i(\xi) x_i $$

In isoparametrix mapping we construct the relation between the two coordinate systems with the shape functions.

We parameterise the mapping of coordinates similarly to the unknown fields {u}.

```{figure} ../.././images/Chapter1/1_7_4.png
---
height: 350px
name: 1_7_4
---
Mapping process between the two coordinate systems.
```

The next step is to calculate the derivatives of the shape functions w.r.t. x- coordinate. Here, the shape functions themselves do not need to be defined in terms of x, as the chain rule is used.

$$ \frac{\partial N_i}{\partial x} = \frac {1}{J} \, \frac {\partial N_i}{\partial x} $$


where  J is the Jacobian:
$$ J = \frac {\partial x} {\partial ξ}  = \sum_{i=1}^{n-node}  \frac {\partial N_i} {\partial ξ}  x_i $$

Following, we integrate first on the x- coordinate and then on the coordinates of the reference element.

At the transformation of the integral, the same Jacobian appears, in absolute value.

Integraton is performed as follows

$$ \int_{x_1}^{x_3} f \, dx = \int_{-1}^{1} f |J| \, dξ$$

Then numerical integration is performed using $ξ_i$ and $w_i$ as they were defined on the integration scheme of the reference element.

$$ \int_{-1}^{1} f |J| \, dξ \approx \sum_{i=1}^{n- ip} f(ξ_i)  |J(ξ_i)| w_i $$



### Example 

```{figure} ../.././images/Chapter1/1_7_5.png
---
height: 300px
name: 1_7_5
---
Mapping process between the two coordinate systems.
```


| | | 
| --- | --- |
|$  N_1= \frac{1 }{2} ξ^2 - \frac{1 }{2} ξ  $| $x_1=2$|
|$  N_2= 1 - ξ^2$ | $x_2=4$|
|$  N_3=\frac{1 }{2} ξ^2 + \frac{1 }{2} ξ $ | $x_3=6$|

- Mapping 
  
$$ x= N_1 x_1 + N_2 x_2 +N_3 x_3 = 4+2ξ $$

- Derivatives
  
$$  J= \frac{\partial N_1}{\partial ξ}   x_1 +  \frac{\partial N_2}{\partial ξ}   x_2    + \frac{\partial N_3}{\partial ξ}   x_3  = 2    $$


$$  \frac{\partial N_1}{\partial x} = \frac{1}{2} \frac{\partial N_1}{\partial ξ} $$

### Stiffness matrix of a 3-node element

$$ \mathbf{K}^e = \int_{Ω^e} \mathbf{B}^T ν \mathbf{B} dΩ   $$

$$ \mathbf{B} = \left[  \frac {\partial N_1}{\partial x}, \frac {\partial N_2}{\partial x}, \frac {\partial N_3}{\partial x} \right] $$ 

Every entry can be integrated separately 

$$ \mathbf{K_{ij} ^e} = \int_{x_1}^{x_3} \frac{\partial N_i}{\partial x} ν  \frac{\partial N_j}{\partial x} dx $$

with isoparametric mapping 

$$ \frac{\partial N_i}{\partial x} = \frac {1}{J} \frac{\partial N_i}{\partial ξ} $$

$$ \int_{x_1}^{x_3} f \, dx = \int_{-1}^{1} f |J| \, dξ$$

Substitution gives 


$$ \mathbf{K_{ij} ^e} = \int_{-1}^{1} \frac {1}{J} \frac{\partial N_i}{\partial ξ} ν \frac {1}{J} \frac{\partial N_j}{\partial ξ} |J| dξ =  \int_{-1}^{1} \frac {1}{|J|} \frac{\partial N_i}{\partial ξ} ν  \frac{\partial N_j}{\partial ξ} dξ $$


Note that at the left hand side of the equation J appears three times. For the 1D case, this is simplified as you can see, and J appears only once at the right-hand side of the equation. 

J is a measure of the element length, so we see that the stiffness matrix is inversely proportional to the element's length.

In the 2D case a similar operation exists, however in that case J is a matrix.

### Recap

Isoparametric elements are used in finite element software. In this case shape functions are formed in a simple element configuration (unit length side and width sides aligned with the coordinate system). 

The characteristic of an isoparametric element is that both geometry and displacement are interpolated using the same shape functions.

Things to remember about isoparametric mapping:

- In terms of implementation, only one function is enough to evaluate the shape function of each element, irrespective of the exact shape of the element. 
- It allows simple application of numerical integration.
- It allows higher order elements to have curved edges.

In practice, the point (x, y) in the cartesian plane is represented as follows:

$$ x= \sum_{i=1}^{nn}N_i(\xi,\eta) x_i $$
$$ y= \sum_{i=1}^{nn} N_i(\xi,\eta) y_i $$

where (ξ,η) are known as the natural coordinates and nn is the number of nodes of an element.

By using isoparametric mapping, shape functions can be defined on simple shapes, such as the bi-unit square. For example, the displacement  in the x direction at a point is given by:

$$ u^h= \sum_{i=1}^{nn}N_i(ξ,η) α_{ix} $$



