# Modelling Framework

The WavePiston competition model represents a simplified one-sail, one-collector device. The system has **one degree of freedom (DoF)** in the surge direction.

- **Geometry & Coordinates:**  
  The sail is positioned at $x=0$, with incoming waves traveling along the positive $x$-axis ($\beta=0$).  
  An up-wave wave probe provides a reference elevation signal at $x=-10$ m.

- **Constraints (conceptual):**  
  - Sail displacement: $|x(t)| \leq x_{\max}$  
  - PTO force: $|F_{pto}(t)| \leq F_{pto,\max}$  
  - Passivity: the PTO can only absorb power, not inject reactive power.

---

## Hydrodynamic Equation

The hydrodynamics of the device are described by **Cummins’ integro-differential equation**:

[//]: # ($$)

[//]: # (M \ddot{x}&#40;t&#41; + \int_{-\infty}^t K&#40;t-\tau&#41; v&#40;\tau&#41;\, d\tau + S_h x&#40;t&#41; + \frac{1}{2} \rho A C_D \dot{x} |\dot{x}|)

[//]: # (= F_{ex}&#40;t&#41; - F_{pto}&#40;t&#41;)

[//]: # ($$)

$$
M \ddot{x}(t) + F_r(t) + S_h x(t) + \frac{1}{2} \rho A C_D \dot{x} |\dot{x}|
= F_{ex}(t) - F_{pto}(t)
$$


*   $x(t)$: sail position,

*   $\dot{x}(t)$: velocity,

*   $M = m_w + m_\infty$: total mass (device mass + added mass asymptote),

*   $f_r(t)$: radiation impulse kernel,

*   $F_{ex}(t)$: wave excitation force,

*   $F_{pto}(t)$: control force applied by the PTO.

*   $\rho$: sea water density.

*   $A$: sail area.

*   $C_D$: viscous drag coefficient.

Additionally, $F_r(t)$ is the radiation force term, typically approximated by a finite-order state-space system as follows:
```{math}
\dot{\mathbf{\xi}}(t) &= \mathbf{A_r}\,\mathbf{\xi}(t) + \mathbf{B_r}\,\dot{x}(t) \\
F_r(t) &= \mathbf{C_r}\,\mathbf{\xi}(t)
```
where $\mathbf{\xi}(t)$ is the radiation state vector.

Note that no hydrodynamic restoring force acts on the WEC, since the sails are constrained to move horizontally and are assumed rigid. Therefore, this term does not appear in the hydrodynamical equation.