# 1.7. Isoparametric element in 1D

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



