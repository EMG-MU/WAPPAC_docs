## Control Problem Formulation

Participants are tasked with designing a control strategy that maximizes a defined performance index over the **scoring interval** for **three predefined sea state scenarios**. The following details clarify the control problem formulation.

### Key Time Intervals for Performance Index Evaluation

To clearly define the control problem, it is important to distinguish the key time intervals, illustrated in {numref}`fig_startup_int_vs_scoring_int`. These intervals are consistent across all three sea state scenarios:

```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

```{important}
- **Full simulation time span:** $t \in [t_{init}, t_{end}]$  
  The participant’s controller must be defined and operational for the entire simulation duration in all sea state scenarios.

- **Startup interval:** $t \in [t_{init}, T_0]$  
  Initial period during which the performance index is **not evaluated**.

- **Scoring interval:** $t \in [T_0, t_{end}]$  
  Period during which the performance index is computed for **each sea state scenario**.

- **Scoring interval start time $T_0$:**  
  The scoring interval start time is identical across all three sea states.
  
- **Sea-state-dependent simulation horizon:**  
  Note that the end time of the simulation, $t_{end}$, varies depending on the sea state scenario ($t_{init}=0$ s awlays).
```

For additional details on the startup interval, see [Numerical Implementation](./numerical_implementation.md).

---

### WAPPAC Competition Performance Index

The **performance index** $\mathcal{G}$ is designed to balance energy capture, physical constraint compliance, and capacity factor, and can be interpreted as a **surrogate for the Levelized Cost of Energy (LCoE)**.

The objective is to maximize $\mathcal{G}$ over the **scoring interval** $t \in [T_0, t_{end}]$ by defining the control force $F_{pto}(t)$ appropriately for **all three predefined sea state scenarios**:

```{math}
\max_{F_{pto}(t)} \; \mathcal{G}\!\left(F_{pto}(t); t \in [T_0,t_{end}] \right) 
= \frac{\bar{P}_{pto}}
{2 + \frac{\left[|x(t)|\right]_{98}}{x_{\max}} 
  + \frac{\left[|F_{pto}(t)|\right]_{98}}{F_{u,\max}} 
  - \frac{\bar{P}_{pto}}{\left[p_{pto}(t)\right]_{98}}}
```
```{math}
\text{s.t.}& \quad \text{WavePiston dynamics,} \quad \\
& \quad p_{pto}(t) = F_{pto}(t) \dot{x}(t) \ge 0 \quad \forall t \in [t_{init},t_{end}]
```

where:

* $\bar{P}_{pto} = \frac{1}{t_{end}-T_0}\int_{T_0}^{t_{end}} p_{pto}(t) \, dt$ — average PTO power during the **scoring interval**.
* $\left[|x(t)|\right]_{98}$ — 98th percentile of absolute sail displacement during the **scoring interval**.
* $\left[|F_{pto}(t)|\right]_{98}$ — 98th percentile of absolute PTO force during the **scoring interval**.
* $[p_{pto}(t)]_{98}$ — 98th percentile of instantaneous PTO power during the **scoring interval**.
* The constant `2` is a scaling factor.

**Constraints:**

* $x_\mathrm{max}$ — maximum allowable sail displacement (see {numref}`fig_wavepiston_sch`).
* $F_{pto,\max}$ — maximum allowable PTO control force.
* $p_{pto}(t) \ge 0 \; \forall t \in [t_{init},t_{end}]$ — PTO is passive; power cannot be negative at any time during the **full simulation time span**.

---

### WavePiston Constraints Handling Considerations

The participant’s **controller must** be defined for the **full simulation duration** $t \in [t_{init}, t_{end}]$. When designing the control strategy, the following aspects must be carefully considered:

```{important}
- **Position and PTO force constraints**  
  - Treated as *soft limits*: occasional exceedances may be tolerated but should be minimized to achieve higher performance index values.  
  - Evaluated using the 98th percentile over the **scoring interval**.

- **Passivity constraint**  
  - A **hard physical constraint**: the PTO can only absorb power and cannot supply it.  
  - Must be satisfied for the **full simulation time span**: $p_{pto}(t) \ge 0 \; \forall t \in [t_{init},t_{end}]$.
```