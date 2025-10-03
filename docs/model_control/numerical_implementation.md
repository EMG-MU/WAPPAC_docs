# Numerical Implementation

The simulation environment is implemented with a consistent numerical setup to ensure comparability across controllers.

---

## Time Integration

- **Fixed-step solver** with $\Delta t = 0.05$ s.  
- The solver integrates Cummins’ equation with the radiation state-space model and nonlinear drag.

---

## Control Update

- Control inputs $F_{pto}(t)$ are applied using a **zero-order hold (ZOH)** behavior.  
- Controller updates occur at the simulation time step $\Delta t$.

---

## Startup Ramp

The wave excitation force is introduced gradually using a **raised cosine window**:

```{math}
ramp(t) = 0.5 \left[1.0 - \cos\!\left(\frac{\pi t}{t_{ramp}}\right)\right]