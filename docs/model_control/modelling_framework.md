# Modeling Framework

WAPPAC competition uses a simplified one-sail, one PTO device, schematically represented in {numref}`fig_wavepiston_sch`. 



```{figure} ../_static/figures/schematics/WavePiston_sch.png
:name: fig_wavepiston_sch
:width: 100%
:align: center
Schematic of the one-sail WavePiston device and upwave surface elevation measurement.
```

- **WavePiston characteristics:**  
  - The system has **one degree of freedom (DoF)** in the surge direction.
  - The sail **excursion midpoint** is at $x=0$, with incoming waves traveling along the positive $x$-axis ($\beta=0$).
  - The sail **maximum allowable displacement** of the sail is denoted by $x_{\max}$.

- **Upwave Measurement:**  
  - A probe provides the **upwave** surface elevation **measurement** at $x=-10$ m.

---

## WavePiston Dynamics

The hydrodynamics of the WavePiston device can be described using Cummins’ equation together with a viscous drag term {eq}`eq_WP_hydrodyn`:

```{math}
:label: eq_WP_hydrodyn
M \ddot{x}(t) + F_r(t) + \frac{1}{2} \rho A C_D \, \dot{x} |\dot{x}|
= F_{ex}(t) - F_{pto}(t) ,
```

where
*   $x(t)$: sail position,

*   $\dot{x}(t)$: sail velocity,

*   $M = m_w + m_\infty$: total mass (device mass + added mass asymptote),

[//]: # (*   $f_r&#40;t&#41;$: radiation impulse kernel,)
*   $F_{ex}(t)$: wave excitation force,

*   $F_{pto}(t)$: control force applied by the PTO.

*   $\rho$: seawater density.

*   $A$: sail area.

*   $C_D$: viscous drag coefficient.

Additionally, $F_r(t)$ is the radiation force term, typically approximated by a finite-order state-space system as follows:
```{math}
\dot{\mathbf{\xi}}(t) &= \mathbf{A_r}\,\mathbf{\xi}(t) + \mathbf{B_r}\,\dot{x}(t) \\
F_r(t) &= \mathbf{C_r}\,\mathbf{\xi}(t)
```
where $\mathbf{\xi}(t)$ is the radiation state vector.

[//]: # (```{note})
**No hydrodynamic restoring force** acts on the WEC, since the sails are constrained to move horizontally and are assumed rigid. Therefore, this term does not appear in the hydrodynamical equation.

[//]: # (```)

[//]: # (## WavePiston Constraint)

[//]: # ()
[//]: # ()
[//]: # (### PTO Passivity constraint)

[//]: # (Because of the WavePiston’s design, the PTO can only extract power from the waves.)

[//]: # (This means that the PTO cannot inject reactive power back into the system, and therefore:)

[//]: # ()
[//]: # (```{important})

[//]: # (PTO power is constrained to be non-negative: )

[//]: # (```{math})

[//]: # (    p_{pto}&#40;t&#41; = F_{pto}&#40;t&#41; \dot{x}&#40;t&#41; \geq 0)

[//]: # (```)