# Multiscale Methods

## Relationship between macro- and micro-scale

The lack of pure homogeneity at a lower scale has a huge influence on the behaviour at the large scale. Small defects are known to often be the cause of catastrophic macroscopic failure. Macro-scale properties often depend on micro-scale features encapsulated in what is named structure-property relationship. Even further, some macro-scale behaviour can emerge exclusively from the micro-scale (example).

It is computationally impossible however to model those microscopic features when solving a macroscopic simulation as it requires a mesh resolution way too large to bridge the length scale separation (think about a TV needing to resolve every strand of hair to display a character’s face!).

Separation of scales occurs when the macroscopic length scale is larger than microscopic length scale by 3 orders of magnitude. Otherwise, concurrent/embedded multiscale method also exist (explain in further details) but we will focus on the first kind, hierarchical. Because the scales are separated, the models are appropriately solved according to the scale considered. For example, while the microstructure is discretised at the micro-scale, the macro-scale is solved as a continuum.

```{figure} ./figures/44296_2024_21_Fig3_HTML.jpg
---
height: 200px
name: sequential_vs_concurrent
---
Sequential vs concurrent multiscale modeling, applied to the fracturing problem of fiber-reinforced concrete. Figure from https://doi.org/10.1038/s44296-024-00021-z
```

```{figure} ./figures/Continuum-macrostructure-and-heterogeneous-microstructure-associated-with-point-P-Fig-2_W640.jpg
---
height: 200px
name: macro_vs_micro
---
Continuum macrostructure and heterogeneous microstructure associated with point P. Figure from https://doi.org/10.1007/s004660000212
```

To percolate information of the micro-scale to the macro-scale, we perform an upscaling using a homogenization method. The upscaled macroscopic response is called effective. Those multiscale methods are meant to couple the micro-scale and macro-scale models. In this first part we focus on the upscaling, which is a one-way coupling, upwards.

## Categories of multiscale methods

Different types of methods can be used to upscale. We can resort for example to simple empirical relationships which are the laws of mixtures. The first one from Voigt (1884) assumes that the effective medium is under a constant strain. For a two-phase medium, the effective value of the property is equivalent to setting two springs in parallel, and is expressed as:

$$
X_{eff}=\phi_1X_1+\left(1-\phi_1\right)X_2
$$

Where $\phi_1$ is the volume fraction of phase 1.
For Reuss law, the assumption is constant force and similarly the effective value of the property for a two-phase medium is equivalent to two springs in series and is expressed as

$$
\frac{1}{X_{eff}}=\frac{\phi_1}{X_1}+\frac{1-\phi_1}{X_2}
$$

Those two formulas correspond respectively to kinematic or traction condition. Kinematic condition pushes the system to its maximal entropy and corresponds therefore to an upper bound of the effective property estimation, while the traction condition is oppositely the minimum.

make a plot of the rule of mixtures like in wikipedia (https://en.wikipedia.org/wiki/Rule_of_mixtures)

When only interested in predicting failure, we can employ limit analysis which can consider more details of the microstructure. It also finds either the upper or lower bound of the solution. When trying to consider the exact microstructure, we need to resort instead to the computational methods. In this computational modelling book, we focus on that last option.

## Representative Elementary Volume

While the micro-scale is heterogeneous whether in structure or in property distribution, the application of multiscale methods can only be valid when the large scale is statistically homogeneous. We define as such a Representative Elementary Volume (REV) above which size the effective property of interest does not fluctuate. The REV is defined for the property to upscale and the length scale considered. When focusing on upscaling the microstructure, the length scale is the characteristic length of voids, inclusions, fibers or crystals depending on the material. For porous rocks, it is the average grain size. And studies show that the REV size for hydraulic conductivity of a rock is often smaller than for the mechanical stiffness.

A sample stops being statistically homogeneous when encountering a high length scale like fractures for example. Only unfractured samples can be homogenized. But a fracture network can yield an effective response considering the fracture as the length scale of interest.

When the structure is periodic such as for artificial materials like 3D printed metamaterials, the REV is directly the unit cell and the upscaling is done using periodic conditions. In the case of natural non-periodic REV, the REV size needs to be sufficiently large enough to eliminate boundary effects.

```{figure} ./figures/Continuum-macrostructure-and-heterogeneous-microstructure-associated-with-point-P-Fig-2_W640.jpg
---
height: 200px
name: REV_vs_unit_cell
---
Representative Elementary Volume for a periodic composite material (left) and for a random material (right). Figure from https://doi.org/10.1142/S1756973711000509
```

## Averaging theorem
Effective quantities are obtained by averaging the microscopic fields. The average of the quantity $X$ over the domain omega is defined as:

$$
\left\langle X\right\rangle=\overline{X}=\frac{1}{V_\mathrm{\Omega}}\int_{\mathrm{\Omega}} X dV
$$

For the relationship macro to micro, we obtain:

$$
X_M=\overline{X_m}
$$

This relation is derived from the Hill-Mandel condition which expresses an irrefutable principle of thermodynamics. Hill’s lemma states that the energy has to be conserved across scales. As a translation, the macroscopic work is equal to the average of the microscopic work. From this condition, the averaging of other quantities can be derived similarly.

At the microscopic scale, any quantity can be expressed as a fluctuating field around the averaged value:

$$
X_m=\overline{X_m}+\widetilde{X_m}
$$

Where $\widetilde{X}$ is the fluctuation. Therefore we have:

$$
X_M=\overline{\overline{X_m}+\widetilde{X_m}}=\overline{X_m}+\overline{\widetilde{X_m}}
$$

This expression implies that the fluctuations need to average out on the domain for the averaging relation to be valid. This is indeed the case when considering the domain size above REV, as per its definition. It showcases once more the need to consider a domain above the REV size for upscaling.

## Upscaling
To obtain an effective property, we use the macroscopic constitutive law. The law is inverted  to compute the property using the macroscopic fields values obtained from our simulation. The simulation often considers boundary conditions of deformation or force. Those boundary conditions corresponds to imposing the macroscopic value of the variable. The secondary variable is obtained by homogenizing the microscopic field heterogeneously distributed in the simulation result.

Let us run through the example of upscaling the Young’s modulus of a porous material:

Set up a numerical experiment of uniaxial mechanical test with displacement-control of a sample of the porous material above the REV size. The simulation solves for elasticity at the micro-scale. The macroscopic constitutive law for elasticity -- Hooke’s law -- reads as:

$$
\sigma=E\cdot\epsilon
$$

The macroscopic axial strain can be directly calculated from the prescribed displacement boundary and the macroscopic axial stress is averaged from the microscopic axial stress over the full sample.
The effective Young’s modulus is calculated from the equation above.

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

Information about the macroscopic state variables is downscaled under the form of a boundary condition. Voigt assumption is to impose a constant deformation gradient on the boundary of the microstructure while Reuss assumption is to impose a constant stress. Periodic boundary conditions can also be adopted. Each setup satisfies Hill-Mandel condition given correct microscopic field averaging.

As the two simulations are hierarchical and therefore run sequentially, FE$^2$ is not tightly coupled. Therefore, if the micromodel is nonlinear, we need to loop iteratively one timestep of the multiscaling, similarly to solving a nonlinear FEM problem, to reach convergence of the solution.

Typical set up for FE$^2$ is to run that multiscale loop at every Gauss point of the mesh, so that the full field is determined through upscaling.

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

## Surrogate model
When FE$^2$ is run at every Gauss point, the multiscale simulation becomes computationally heavy. It becomes important in an effort of optimization to replace the microscale model by a surrogate using machine learning (to be written with Joep)
