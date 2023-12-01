# 2D/3D Problems 

## 3.1 Poisson Equation in 2D

The PDE at hand in this chapter is the 2D poisson equation, in a steady state (time-independent solution).

$$-\nu \left(\frac{\partial^{2} u}{{\partial x}^{2}} + \frac{\partial^{2} u}{{\partial y}^{2}}\right) = q$$


There are several applications where this pde can be used to solve problems in sciences and engineering, such as:
-potential flow
-pressure in saturated soil
-temperature distribution


## 3.2 Two dimensional continuum elasticity elements




## 3.3. Governing Equations 


At this point, the discretised filed $u^h$ will be inserted into the weak form of the governing equation. 

The weight functions are discretised similarly to the unknown field $u^h$.

Therefore, for the multi-dimensional case within an element:

$$ 
w^h= \textbf{N} \ \textbf{b}_e  
$$

$$ 
∇^s w^h= \textbf{B} \   \textbf{b}_e  
$$

Now, considering the one-dimensional governing equation for an elastic rod.

Recall 
$$
-\int_{0}^{L} w^h_{,x}E u^h_{,x} \: dx + w^hh|_{x=L} =0 ,  ∀ \ w^h ∈ V^h.
$$


Now, let's consider a single element which extends from x=$l_1$ to x=$l_2$  in the x-axis.

The discretised governing equation for the element is expressed as follows:

$$
\int_{l_1}^{l_2} (\textbf{B b}{_e})^T E \ \textbf{B α}{_e}  \: dΩ  = \int_{Γ{_h,e}} ( \textbf{N b}{_e})^Τ \ h  \: dΓ
$$



where the integral over $Γ_{h,e}$  is only non zero if the boundary of the element coincides with the boundary $Γ_{h}$. The discrete nodal values can be removed from the integrals which after appropriate rearranging leads to: 

$$ 
\textbf{b}_e^T \int_{l_1}^{l_2} \textbf{B}^T E \textbf{B} \: dΩ \ \textbf{α}_e = \textbf{b}_e^T
\int_{Γ{_h,e}} \textbf{N}^T h \: dΓ   $$

and by  eliminating $ \textbf{b}_e $ on both sides, we get

$$ 
\int_{l_1}^{l_2} \textbf{B}^T E  \ \textbf{B} \: dΩ α_e =
\int_{Γ{_h,e}} \textbf{N}^T h \: dΓ   $$


Now the integral on the left hand side of the equation can be recognised as the **element stiffness matrix** **$k_e$**. Once the stiffness matrix has been formed for an element, its contribution is added to the ‘global’ stiffness matrix **K**.

For a continuum elasticity problem, the discretised displacement and strain fields
are inserted into the following equation

$$
-\int_{Ω} ∇^s \textbf{w}^h : \textbf{C} : ε^h \: dΩ +
\int_{Ω} \textbf{w}^h \textbf{b} \: dΩ +
\int_{Γ{_h}} \textbf{w}^h \textbf{b}  \: dΓ = 0  \ \ ∀ \textbf{w}^h ∈ V^h
$$

where $ ε^h = ∇^s \textbf{u}^h $

Note: In a multi dimensional context, the finite dimensional trial and wight functions are denoted $\textbf{u}^h$ and $\textbf{w}^h$, respectivelly.


This yields:

$$
\int_{Ω_e} (\textbf{B b}{_e})^T \textbf{D} \  \textbf{B α}{_e} \: dΩ  =
  \int_{Γ_{h,e}} (\textbf{N b}_e)^T \textbf{h}  \: dΓ +
   \int_{Ω_{e}}  (\textbf{N b}_e)^T \textbf{b} \: dΩ
$$


and following the same steps, the element stiffness matrix can be expressed as follows: 

$$
\int_{Ω_e} \textbf{B}^T \ \textbf{D B} \: dΩ  \ \textbf{α}{_e} =
  \int_{Γ_{h,e}} \textbf{N}^T \textbf{h} \: dΓ +
   \int_{Ω_{e}} \textbf{N}^T \textbf{b} \: dΩ
$$


Once the stiffness matrix has been formed for each element in the problem, it must
be assembled into the global stiffness matrix. This is denoted symbolically by the
operation:

$$
\textbf{K} = A^{ne}_{e=1} \ k_e
$$


$$
\textbf{f} = A^{ne}_{e=1} \ f_e
$$

where A represents the assembly operator and $ne$ the number of elements in the mesh. For an element stiffness materix the term $k_{ij}$ relates the local nodes i and j. The component $k_{ij}$ is added to the location $K_{ij}$. 

Note that the assembly process will be discussed in following chapters.


## Linear elasticity in 3D

## Stokes flow

## Poroelasticity with Darcy flow
