# 1.8. Numerical Integration

Up to this point only displacement have been discretised. In order to make the formulation fully discrete, numerical integration over volumes and surfaces needs to be applied.

Different integration schemes specify where the intergration points are located and the weight associated with each point. 

The following two schemes arise in Finite Element Analysis: 
- Newton-Cotes
- Gauss Integration

A Newton-Cotes scheme uses equally spaced integration points. In this scheme, (n+1) integration points are needed to integrate a nth- order polynomial. 
Gauss integration is more common in finite element analysis. Gauss integration is also called Gauss Quadrature. Here, the notion of optimal integration scheme needs to be introduced. Optimal in this case, indicates the minimum number of points needed to integrate exactly a polynomial. Gauss integration, or Gauss quadrature is the optimal numerical integration scheme for polynomials in one dimension. For a (2n-1)th-order polynomial, Gauss integration requires n points to integrate the polynomial exactly. However, bear in mind that when considering multiple dimensions, Gaussian integration is not necessarily the most efficient scheme.
