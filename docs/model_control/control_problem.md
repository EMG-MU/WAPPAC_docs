## Control Problem Formulation
The **performance index** $\mathcal{G}$, which participants aim to maximize, is designed to balance power generation against physical constraints and capacity factor.
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
* $x_\mathrm{max}$ → maximum allowable displacement (sail position).
* $F_{pto,\max}$ → maximum allowable control force magnitude.
* $p_{pto}(t) \ge 0$ → PTO is passive, meaning that control power cannot be negative by design.



### Performance Index Scoring Interval
To ensure a clear evaluation of the results, a crucial **distinction** between the **full simulation time span** and the **scoring interval** must be made.

- **Full simulation time span:** defined from $t_{init}=0$ until the end of each simulation run denoted as $t_{end}$.
- **Scoring interval:** defined from $T_0 = 30$  until the end of each simulation run ($t_{end}$).

For the computation of the performance index, the initial part of the simulation, specifically for $t < T_0$, is disregarded therefore:
```{important}
**Performance index** is evaluated during the **scoring interval** defined in time interval $t = [T_0, t_{end}]$.
```

### WavePiston Constraints Handling
```{important}
The **position** and **PTO force** constraints represent *soft limits*: they define maximum allowable values, but occasional exceedances may be tolerated in practice.   
  - They are evaluated using percentile values.
In contrast, the **passivity constraint** is a *hard limit*: by design, the PTO can **only absorb power**, it cannot supply power back into the system.  
  - PTO power must be non-negative $p_{pto}(t) \geq 0$ for the **full simulation time span**.
```

### WAPPAC Competition Control Objective

```{important}
Design a control system to maximize the performance metric ($\mathcal{G}$), which can be considered a surrogate for the Levelized Cost of Energy (LCoE), balancing power generation against physical constraints and capacity factor:
```

**Objective:** 




$$
\max:  \mathcal{G}\left(F_{pto}(t)\right) = \frac{\bar{P}_{pto}}{2 + \frac{|x(t)|_{98}}{x_{\max}} + \frac{|F_{pto}(t)|_{98}}{F_{u,\max}} - \frac{\bar{P}_{pto}}{|p_{pto}(t)|_{98}} }
$$

$$ s.t. \quad \text{WavePiston dynamics} $$
$$ \qquad\quad p_{pto}(t) = F_{pto}(t) \dot{x}(t) \ge 0  $$



