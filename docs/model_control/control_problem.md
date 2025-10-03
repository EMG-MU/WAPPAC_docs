## Control Problem Formulation
The **performance index** $\mathcal{G}$, which participants aim to maximize across different sea state scenarios, is designed to balance power generation against physical constraints and capacity factor.
In this way, $\mathcal{G}$ can be interpreted as a **surrogate for the Levelized Cost of Energy (LCoE)**:

$$
\max:  \mathcal{G}\left(F_{pto}(t)\right) = \frac{\bar{P}_{pto}}{2 + \frac{|x(t)|_{98}}{x_{\max}} + \frac{|F_{pto}(t)|_{98}}{F_{u,\max}} - \frac{\bar{P}_{pto}}{|p_{pto}(t)|_{98}} }
$$

$$ s.t. \quad \text{WavePiston dynamics} $$
$$ \qquad\quad p_{pto}(t) = F_{pto}(t) \dot{x}(t) \ge 0  $$

where
*   $\bar{P}_{pto}$: Average captured power.
*   $|x(t)|_{98}$: The **98th percentile** of the absolute WP displacement.
*   $|F_{pto}(t)|_{98}$: The **98th percentile** of the absolute control force.
*   $|p_{pto}(t)|_{98}$: The **98th percentile** of the instantaneous control power.
*   The constant 2 is a scaling factor.

**Constraints:**
* $x_\mathrm{max}$ → maximum allowable displacement (refer to {numref}`fig_wavepiston_sch` for further details).
* $F_{pto,\max}$ → maximum allowable control force magnitude.
* $p_{pto}(t) \ge 0$ → PTO is passive, meaning that control power cannot be negative by design.



### Key Time Intervals for Performance Index Evaluation
To ensure a clear evaluation of the results, a crucial **distinction** between key time intervals is performed bellow, illustrated in {numref}`fig_startup_int_vs_scoring_int`

[//]: # (the **full simulation time span** and the **scoring interval** must be made.)

- **Full simulation time span:** Characterized by the time interval $t \in [t_{init}, t_{end}]$.
- **Scoring interval:** Period in which the performance index is evaluated $t \in [T_0, t_{end}]$. 
- **Startup Interval:** Initial period where performance index is not evaluated $t \in [t_{init}, T_0]$.


```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

```{important}
**Performance index** is evaluated during the **scoring interval** defined as $t = [T_0, t_{end}]$.
```
For more details on the startup interval refer to [Numerical Implementation](./numerical_implementation.md).

### WavePiston Constraints Handling
The following aspects need to be considered when designing the control strategy to adequately handle constraints:

```{important}
- **Position and PTO force constraints**  
  - Treated as *soft limits*: occasional exceedances may be tolerated but should be minimized to obtain higher performance index values. 
  - Evaluated using 98th percentile values during the **scoring period**. 

- **Passivity constraint**  
  - A **hard physical constraint**: the PTO can only absorb power, never supply it.
  - Power must be non-negative ($p_{pto}(t) \geq 0$) for the **full simulation time span**.
```

[//]: # (```{important})

[//]: # (- The **position** and **PTO force** constraints represent *soft limits*: they define maximum allowable values, but occasional exceedances may be tolerated in practice.   )

[//]: # (  - They are evaluated using 98th percentile values during the **scoring period**.)

[//]: # (- In contrast, the **passivity constraint** is a *hard limit*: by design, the PTO can **only absorb power**, it cannot supply power back into the system. As a result:)

[//]: # (  - PTO power must be non-negative $p_{pto}&#40;t&#41; \geq 0$ for the **full simulation time span**.)

[//]: # (```)



