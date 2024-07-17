# Crack models

The main cause of the nonlinearity of concrete is cracking, which is primarily due to the limited capacity of concrete to sustain tensile stresses (or perhaps better, tensile strains). Numerical modelling of cracking concrete started in the late 1960s with the landmark papers of Ngo and Scordelis (1967) and Rashid (1968), in which the discrete and smeared crack models were introduced. Especially the latter approach gained much popularity, and in the 1970s comprehensive efforts were invested in developing constitutive models in a smeared setting which could reproduce the experimentally observed stress-strain characteristics of concrete.

```{figure} Images/single_notched_shear.png 
---
---
Single-notched shear beam
```

```{figure} Images/discrete_approach.png
---
---
Discrete approach (interface elements/predefined crack)
```

```{figure} Images/smeared_approach.png 
---
---
Smeared approach (fixed crack model)
```

## Discrete cracking

### Interface elements

```{figure} Images/experiment_interface.png
---
---
Experimental results - masonry wall subjected to a static vertical compression load
```

```{figure} Images/computational_interface.png 
---
---
Computational results - masonry wall subjected to a static vertical compression load. Cracking takes place along a predefined path with 3D interface elements
```

```{figure} Images/biomechanic_interface.png
---
---
Discrete cracking in biomechanics applications (Mota et al., JCM (2003))
```

### Embedded elements

```{figure} Images/strain_field.png
---
---
Standard strain field and strain field with embedded crack band
```

```{figure} Images/2d_spec.png
---
---
2D single-notched specimen
```

```{figure} Images/3d_spec.png
---
---
3D specimens with asymmetric nodes
```

### XFEM

```{figure} Images/xfem_disc_medium.png
---
---
eXtended Finite Element Method (XFEM) - discontinuity in medium
```

```{figure} Images/xfem_disc_discretized.png
---
---
eXtended Finite Element Method (XFEM) - discontinuity in discretized medium
```

```{figure} Images/discontinuity_tip.png
---
---
Propagating discontinuity in discretized medium
```

```{figure} Images/propagation.png
---
---
Propagation direction
```

```{figure} Images/fracture_SEN_beam.png
---
---
Fracture in a SEN-beam - experiment
```

```{figure} Images/SEN_analysis_prop_disc.png
---
---
Fracture in a SEN-beam - analysis with propagating cohesive discontinuities
```

```{figure} Images/open_hole_laminate.png
---
---
 Open hole laminate [+45/-45] - matrix cracking (ply splitting) modelled with XFEM and delamination modelled with interface elements
```

## Smeared Cracking

```{figure} Images/tension_cut_off_experiments.png 
---
---
Tension cut-off criteria - experimental results
```

```{figure} Images/tension_cut_off_models.png 
---
---
Tension cut-off criteria - models
```