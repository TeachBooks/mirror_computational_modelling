## FE$^2$
In some instances, standalone upscaling as described above is not possible. It is the case when the process to upscale is path- or history-dependent (such as irreversible processes like plasticity). The micro-scale system requires therefore information from the macro-scale about the macroscopic state variables as the system evolves. Only then can the upscaled properties be fed to the macro-scale that can advance the simulation. The two scales are now coupled.

```{figure} ./figures/figure2_7_Kouznetsova_2001.png
---
height: 200px
name: coupled_scales
---
Contour plots of the effective plastic strain in the deformed macrostructure and in three deformed RVEs, corresponding to different points of the macrostructure. Figure from https://doi.org/10.1007/s004660000212
```

The coupling can also be shortcutted for complex systems where the macroscopic constitutive law cannot be directly defined. Instead of upscaling the effective property, the upscaled macroscopic variables are directly transferred. This allows to not make any constitutive assumption about the material behaviour.
When both scales are solved with finite element, these multiscale methods are called FE$^2$.

```{figure} ./figures/1-s2.0-S0045782523000579-gr1_lrg.jpg
---
height: 200px
name: FE2
---
Schematic of FE$^2$ couplings. Figure from https://doi.org/10.1016/j.cma.2023.115934
```

Information about the macroscopic state variables is downscaled under the form of a boundary condition. Voigt assumption of isostrain translates to imposing a constant deformation gradient on the boundary of the microstructure while Reuss assumption is to impose a constant stress. Periodic boundary conditions can also be adopted. Each setup satisfies Hill-Mandel condition given adequate microscopic field averaging.

As the two simulations are hierarchical and therefore run sequentially, FE$^2$ is not tightly coupled. Therefore, if the micromodel is nonlinear, we need to loop iteratively one timestep of the multiscaling, similarly to solving a nonlinear FEM problem, to reach convergence of the solution.

Typical set up for FE$^2$ is to run that multiscale loop at every Gauss point of the mesh, so that the full field is determined through upscaling. Each multiscale loop can be run in parralel which allows to accelerate the multiscale simulation which is otherwise computationally very heavy.

```{figure} ./figures/figure1_Geers2017.png
---
height: 200px
name: FE2_Gauss
---
Schematic of FE$^2$ for every Gauss point. Figure from https://doi.org/10.1002/9781119176817.ecm2107
```

It is also possible to run a multiscale loop only in certain regions of the domain to enrich certain parts with micro-scale information. Commonly this is done on shear bands/fractures/faults, i.e. flat interfaces captured as lower dimensional elements and commonly implementing a cohesive zone model. The microscale loop can return the displacement jump for example or oppositely receive the displacement jump and return the traction.

```{figure} ./figures/A-two-dimensional-solid-with-a-heterogeneous-layer_W640.jpg
---
height: 200px
name: FE2_fracture
---
Lower dimenional fracture resolved with FE$^2$. Figure from https://doi.org/10.1142/S1756973711000509
```
