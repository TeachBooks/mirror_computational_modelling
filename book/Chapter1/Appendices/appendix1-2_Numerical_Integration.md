# A1.2. Numerical Integration

At this chapter we will consider integration over a single element.

The following two integration schemes are relevant for Finite Element Analysis: 
- Newton-Cotes
- Gauss Integration

A Newton-Cotes scheme uses equally spaced integration points. In this scheme, (n+1) integration points are needed to integrate a nth- order polynomial. 
Gauss integration is more common in finite element analysis. Gauss integration is also called Gauss Quadrature. Here, the notion of optimal integration scheme needs to be introduced. Optimal in this case, indicates the minimum number of points needed to integrate exactly a polynomial. Gauss integration, or Gauss quadrature is the optimal numerical integration scheme for polynomials in one dimension. For a (2n-1)th-order polynomial, Gauss integration requires n points to integrate the polynomial exactly. However, bear in mind that when considering multiple dimensions, Gaussian integration is not necessarily the most efficient scheme.



### Implementation in the 1D poisson equation
For example in the 1D- Poisson equation it is possible to perform this analytically, as follows.

$$ \mathbf{K}_e = \int_{x_1}^{x_2} \mathbf{B}^T EA \mathbf{B} \,dx $$

$$\mathbf{B} = \left[\begin{matrix}\ B1 & B2\end{matrix}\right]$$

$$ Β1= \frac{1}{x_2-x_1}, Β2= \frac{-1}{x_2-x_1} $$


$$ \mathbf{K}_e = \frac{v}{x_2-x_1}\left[\begin{matrix}1 & -1 \\ -1 & 1\end{matrix}\right] $$


In practice, numerical integration is performed. The idea behind numerical integration is that an integrl can be replaced by a weighted sum, as follows:


$$ \mathbf{K}_e = \int_{Ω^ε}\ f(x,y)dΩ   =  \sum_{i=1}^{n_ip} ω_i f(x,y) $$

The funciton **f** can be evaluated at a selected number of points, with coordinates x, y and multiplied by weights $ ω_i $

```{figure} .././images/Chapter1/1_8_1.png
---
height: 200px
name: 1_8_1
---
Arbitrary discretised shape
``` 

The next step involves considering how to perform efficient and accurate numerical integration.

One first requirement that arises is that the sum of all wights within an element should be equal to the area of the element.

Secondly, the number and location of the integration points must be specified, as well as the individual weights.

It is essential that the number to integration points are the minimum required.


Let's consider a reference element defined from -1 to +1 in the ξ axis. In the gauss integration scheme the position and weights are optimised for exactly integrating polynomials to as high order as possible.Let's now look at an example. 

- For a O-th order polynomial ($ f= c $) the position of the integration point is not important, as long as the weight is equal to the length of the domain, which in this case is 2.
-  For a 1-st order polynomial ($f= b ξ  +  c$), still we can be exact with one integration point if and only is the integrtion point is positioned at the centre of ξ-axis.
- For a 2-nd order polynomial  ($f= aξ^2 + b ξ  +  c$) we will need more than one integration points. In order to use 2 points, one should use a set of points that allow to integrate quadratic funcion exactly, with weights 1 per point. It can be proven that using a specific set of two integration points is still sufficient to integrate 3-rd order polynomials as well.

The following rule applies, regarding the order of the polynomial $p$
and the number of integration points  $ n_{ip} $.

$$ p= 2 n_{ip} -1 $$ 

This information can be summarised in the following manner. 


```{figure} .././images/Chapter1/1_8_2.png
---
height: 300px
name: 1_8_2
---
Gauss Integration points
``` 



| Number of points $n_{ip} $| Position $ξ_i$ | weight | Polynomial order $p$|
| --- | --- | --- | --- |
| 1 | 0 | 2 | 0 or 1|
| 2 |   $-1/\sqrt{3} ,  1/\sqrt{3} $ |  1, 1 | 2 or 3|
| 3 | $-3/\sqrt{5}, 0, 3/\sqrt{5}$ |  5/9, 8/9, 5/9 | 4 or 5|



## Example in 3-node element

By using the information above, on te required integration points for 2nd order polynomials, one can decide the Gauss points needed for a 3-node element with the accompanying shape functions.


```{figure} .././images/Chapter1/1_7_3.png
---
height: 200px
name: 1_8_3
---
3-node element
``` 

### Additinal info on numerical integration



