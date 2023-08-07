# 1.4. The Galerkin method

The Galerking method is an approximative method. This means, that instead of solving the strong form of a problem, which leads to the exact solution, an estimate of the exact solution is derived at specific predeterminted points of the system. This process of reducing the full problem to a reduced, descrete counterpart is called discretisation. 

The Galerkin method is a weighted residual method, which has a close relationship with the Rayleigh-Ritz method (Variational Method). It has been shown that the Galerkin method minimises the error in terms of energy, which is the principle behind the Rayleigh-Ritz method. It is worth mentioning that these two methods for several problems in solid mechanics are equivalent.

A weighted residual method starts with an estimate of the solution and demand that its weighted average error is minimised. The Boris- Galerkin method is one type of weighted residual methods.


- Using arbitrary FE spaces
