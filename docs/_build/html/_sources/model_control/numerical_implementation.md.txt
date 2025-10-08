# Numerical Implementation

The [model](./modelling_framework.md) and [control](./control_problem.md) frameworks are implemented with a consistent numerical setup to ensure comparability across all control strategies submitted by participants. When developing your controller, the following implementation details should be carefully considered.

---

## Time Integration

* The WavePiston dynamics, given by {eq}`eq_WP_hydrodyn`, are integrated using a **4th-order Runge–Kutta (RK4)** scheme.
* The solver operates with a **fixed time step** of $\Delta t = 0.05$ s.
* Within each time step, RK4 performs **four intermediate evaluations (stages)** of the WavePiston dynamics function, modeled by {eq}`eq_WP_hydrodyn`, to estimate the state at the next time step:  
  * Evaluates WavePiston dynamics once at the beginning of the time step, twice at the midpoint, and once at the end of the time step.

## Control Update

* The control force $F_{pto}(t)$ is implemented using a **zero-order hold (ZOH)**:

  * The controller is **evaluated once** at the start of each simulation time step ($\Delta t$).
  * During RK4 internal evaluations or stages, the control force is **held constant**.
  * Practically, this means your controller **function** `my_controller` is **called once** per time step of duration $\Delta t$.

---

## Ramp Interval

To reduce large transients at the start of the simulation—which could induce sail position drift and premature constraint violations—the **wave excitation force is gradually applied** during the **ramp interval**, illustrated in {numref}`fig_ramp_interval`.

```{figure} ../_static/figures/schematics/ramp_interval.png
:name: fig_ramp_interval
:width: 100%
:align: center
Ramp interval versus scoring interval.
```

The ramp function is defined as a raised cosine:

```{math}
ramp(t) = 0.5 \left[1 - \cos\!\left(\frac{\pi t}{T_{\text{ramp}}}\right)\right], \quad t \in [t_{init}, T_{\text{ramp}}]
```
This function multiplies the excitation force from zero to its full value over the interval $0 \le t \le T_{\text{ramp}}$. Thus, the attenuated excitation force is given by:
```{math}
\tilde{F}_{exc} = ramp(t) F_{exc} 
```
Note that the raised cosine time derivative is zero at both the start ($t=0$) and end $(t=T_{\text{ramp}})$ of the ramp, ensuring a smooth transition. 
Also, $ramp(T_{\text{ramp}}) = 1$, so the excitation force reaches its full magnitude exactly at the end of the ramp interval. 

```{note}
- The **ramp interval duration** is **fixed** for every simulation at $T_{\text{ramp}} = 20$ s across all three predefined sea state scenarios.
- For $t \ge T_{\text{ramp}}$ → $\tilde{F}_{exc} = F_{exc}$.
- The ramp interval ends **before the scoring interval begins** ($T_{ramp}=20 < T_0 = 30$ s), mitigating transient effects of the artifical ramp-up function before start evaluating the performance index.
```
---

## Up-wave Measurement

Participants have access to the **up-wave surface elevation measurement** located at $x=-10$ m (see {numref}`fig_wavepiston_sch_sensor`):

```{figure} ../_static/figures/schematics/WavePiston_sch.png
:name: fig_wavepiston_sch_sensor
:width: 100%
:align: center
Schematic of the one-sail WavePiston device and up-wave surface elevation measurement.
```

### Handling Up-wave Measurement

```{important}
- Up-wave measurement is available **only during the scoring interval** ($t \ge T_0$).  
- For $t < T_0$, the measurement value is `NaN`. Refer to [Writing Your Controller](/simulation_platform/writing_controller.md) for instructions on handling `NaN` inputs safely in your control strategy.
```