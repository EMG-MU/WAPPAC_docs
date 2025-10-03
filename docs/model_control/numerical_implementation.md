# Numerical Implementation

The [model](./modelling_framework.md) and [control](./control_problem.md) framework is implemented with a consistent numerical setup to ensure comparability across different control strategies proposed by particpants. 
When developing your control strategy, please keep the following implementation details in mind.

---

## Time Integration

- The system dynamics, given by {eq}`eq_WP_hydrodyn`, are solved using a **4th-order Runge–Kutta (RK4)** method.  
- The solver runs with a **fixed time step** of $\Delta t = 0.05$ s.  
- Within each main step, the RK4 method evaluates four internal sub-steps.  

---

## Control Update

- The control force $F_{pto}(t)$ is implemented using a **zero-order hold (ZOH)**.  
   - The controller is updated at the beginning of every simulation time-step (every $\Delta t$ s of simulation time).  
   - Practically, this means your controller function `my_controller` is called once per time-step.  
   - During the intermediate RK4 sub-steps, the control force is held constant.  

---

## Ramp Interval

To mitigate large transients at the beginning of the simulation, which could cause sail position drifting leading to premature constraint violations, the wave excitation force is **gradually introduced** during the so-called **ramp interval**, schematically represented in {numref}`fig_ramp_interval`.


```{figure} ../_static/figures/schematics/ramp_interval.png
:name: fig_ramp_interval
:width: 100%
:align: center
Ramp interval vs. scoring interval.
```

The ramp function is defined as a raised cosine:

```{math}
ramp(t) = 0.5 \left[1 - \cos\!\left(\frac{\pi t}{T_{\text{ramp}}}\right)\right], \qquad \text{defined for} \; t \in [t_{init}, T_{ramp}]
```
This function multiplies the excitation force from zero to its full value over the interval $0 \le t \le T_{\text{ramp}}$. Thus, the attenuated excitation force is given by:
```{math}
\tilde{F}_{exc} = ramp(t) F_{exc} 
```
Note that the raised cosine time derivative is zero at both the start ($t=0$) and end $(t=T_{\text{ramp}})$ of the ramp, ensuring a smooth transition. 
Also, $ramp(T_{\text{ramp}}) = 1$, so the excitation force reaches its full magnitude exactly at the end of the ramp interval.

```{note}
- The **ramp interval duration** is **fixed** for every simulation at $T_{\text{ramp}} = 20$ s.
- for $t \geq T_{ramp}$, the attenuated excitation force ($\tilde{F}_{exc}$) is equal to the full excitation force ($F_{exc}$).
- The ramp interval **finishes before** the scoring interval begins.
    - This is to mitigate the transient effects caused by the artificial ramp-up before performance evaluation starts.
```