## Control Problem Formulation
**Objective:** Design a control system to maximize the performance metric ($\mathcal{G}$), which can be considered a surrogate for the Levelized Cost of Energy (LCoE), balancing power generation against physical constraints and capacity factor:


$$
\max:  \mathcal{G}\left(F_u(t)\right) = \frac{\bar{P}_u}{2 + \frac{|x(t)|_{98}}{x_{\max}} + \frac{|F_u(t)|_{98}}{F_{u,\max}} - \frac{\bar{P}_u}{|p_u(t)|_{98}} }
$$

$$ s.t. \quad \text{WavePiston dynamics} $$
$$ \qquad\quad p_u(t) = F_u(t) \dot{x}(t) \ge 0  $$


*   $\bar{P}_u$: Average captured power.
*   $|x(t)|_{98}$: The **98th percentile** of the absolute WP displacement.
*   $|F_u(t)|_{98}$: The **98th percentile** of the absolute control force.
*   $|p_u(t)|_{98}$: The **98th percentile** of the instantaneous control power.
*   The constant 2 is a scaling factor.

**Constraints:**
* $x_\mathrm{max}$ → maximum allowable displacement (sail position)
* $F_{u,\max}$ → maximum allowable control force magnitude
* $p_u(t) \ge 0$ → PTO is passive , meaning that control power cannot be negative
