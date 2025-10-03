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
  - The sail is positioned at $\mathcal{X}=0$, with incoming waves traveling along the positive $\mathcal{X}$-axis ($\beta=0$).
  - The maximum allowable displacement of the sail is denoted by $x_{\max}$.

- **Upwave Measurement:**  
  - A probe provides the upwave surface elevation measurement at $x=-10$ m.

---

## WavePiston Dynamics

The hydrodynamics of the device are described by **Cummins’ equation** and a viscous drag term {eq}`eq:WP_hydrodyn`:

```{math}
:label: eq:WP_hydrodyn

\begin{equation}
M \ddot{x}(t) + F_r(t) + S_h x(t) + \frac{1}{2} \rho A C_D \dot{x} |\dot{x}|
= F_{ex}(t) - F_{pto}(t)
\end{equation}
```


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

- **Constraints (conceptual):**  
  - Sail displacement: $|x(t)| \leq x_{\max}$  
  - PTO force: $|F_{pto}(t)| \leq F_{pto,\max}$  
  - Passivity: the PTO can only absorb power, not inject reactive power.
