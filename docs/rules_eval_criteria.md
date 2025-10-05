# Evaluation Criteria & Competition Rules

---

## Evaluation Criteria

The **WavePiston Passive Control (WAPPAC) Competition** challenge participants to design a **passive control strategy** that maximizes a performance index balancing captured power against device constraints and capacity factor.  
All controllers are evaluated under the same modeling framework and numerical setup provided by the official WAPPAC simulation platform.

The **performance index** to be maximized is:

```{math}
:label: eq_perf_G
\max_{F_{pto}(t)} \; \mathcal{G}\!\left(F_{pto}(t)\right) \;=&\; 
\frac{\overline{P}_{pto}}
{\,2 \;+\; \dfrac{|x(t)|_{98}}{x_{\max}} \;+\; \dfrac{|F_{pto}(t)|_{98}}{F_{u,\max}} \;-\; \dfrac{\overline{P}_{pto}}{|p_{pto}(t)|_{98}}\,} \\
&s.t. \quad \text{WavePiston dynamics} \qquad \\[2pt]
&p_{pto}(t) = F_{pto}(t) \dot{x}(t) \ge 0
```
For more details on the performance index $\mathcal{G}$ defintion refer to [**Performance Index & Metrics**](./performance_index.md).

### Key Time Intervals


The following key time intervals aspects must be considered when defining, testing, and evaluating your control strategy:

```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int_eval
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

```{important}
- **Scoring interval (t ≥ 30 s):**  
  The performance index $\mathcal{G}$ is computed only over the **scoring interval** $t \in [T_0, t_{end}]$, starting at **$T_0 = 30$ s** until the end of the simulation (for every sea state).  

- **Full simulation span (t ≥ 0 s):**  
  Your controller must be defined for the entire simulation time span $t \in [t_{init}, t_{end}]$, see {numref}`fig_startup_int_vs_scoring_int_eval`.  
  The passivity constraint $p_u(t) \ge 0$ must hold for the **entire** simulation duration.  
  Any **violation** of this **hard constraint** for a given run will **disqualify** that run (see *Disqualification Conditions*).
```

### Participant's Total Competition Score
Each of the three predefined sea states is evaluated independently, producing scores $\mathcal{G}_1, \mathcal{G}_2, \mathcal{G}_3$.
The total competition score is the sum:

```{math}
:label: eq_perf_index_total
\mathcal{G}_{\text{total}} \;=\; \mathcal{G}_1 \;+\; \mathcal{G}_2 \;+\; \mathcal{G}_3
```
The participant with the highest $\mathcal{G}_{\text{total}}$ will be the **winner of WAPPAC Competition**.


## Competition Rules

1. **Evaluation Mode & Reproducibility**

   * Final evaluation is performed with `eval_flag=true`, generating three encrypted `.enc` files, one per sea state.
   * These encrypted outputs are the **official evaluation files** that participants are requested to submit.
   * The COER team will **re-run participants controller** on WAPPAC simulation platform to verify the results.
   * For more details on submission guidelines please refer to []().

2. **Passivity (Hard) Constraint**
   * The PTO power must remain non-negative for the full simulation time span:
     $p_{pto}(t) = F_u(t)\dot{x}(t) \ge 0$. 
   * If any violation of passivity constraint is occurs at any of the three sea states evaluations, the corresponding $\mathcal{G}_i$ ($i=1,2,3$) will be excluded from the total score.

3. **Position and Force Handling (Soft Constraints)**

   * Position and PTO force limits are considered *soft constraints*:
     occasional exceedances are tolerated but may results in lower performance index.

4. **Integrity**
   * **No modifications** to the hydrodynamic model, numerical solver, sea-state data, or official executables are permitted. 
   * Any tampering with the platform, sea state data, or encrypted outputs is **strictly forbidden**. If any inappropriate use of WAPPAC platform is detected, the participant will be reported and immediately disqualified. and results in immediate disqualification.


---

## Disqualification Conditions

A run or submission will be **disqualified** if any of the following occur:

* A **passivity violation** (`\(p_u(t) < 0\)`) at any time during the simulation.
* Unauthorized modification of the model, numerical setup, or evaluation artifacts.
* Missing, non-functional, or non-reproducible controller code.
* Use of **non-causal** or future information in control computation.
* Numerical instability leading to divergent or meaningless results.

If a single sea-state run is disqualified, that run’s `\(\mathcal{G}_i\)` is **excluded** from the total score.
If multiple runs are disqualified, the full submission may be removed from the ranking (see [Submission Guidelines](./submission_guidelines.md)).

---

## Quick Reference

| **Topic**            | **Summary**                                                                                                                                                                                 |   |          |     |                                   |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | - | -------- | --- | --------------------------------- |
| **Objective**        | Maximize `\(\mathcal{G}\)` (performance index) across three sea states                                                                                                                      |   |          |     |                                   |
| **Scoring**          | `\(\mathcal{G}_{\text{total}} = \mathcal{G}_1 + \mathcal{G}_2 + \mathcal{G}_3\)`                                                                                                            |   |          |     |                                   |
| **Hard Constraint**  | `\(p_u(t) = F_u(t)\dot{x}(t) \ge 0\)` — violations disqualify runs                                                                                                                          |   |          |     |                                   |
| **Soft Constraints** | Position and force limits (`(                                                                                                                                                               | x | _{\max}, | F_u | _{\max})`) affect `(\mathcal{G})` |
| **Reproducibility**  | Organizers re-run submitted controllers on the official platform                                                                                                                            |   |          |     |                                   |
| **More Details**     | [Model & Simulation Parametrization](./model_simulation_parametrization.md), [Numerical Implementation](./numerical_implementation.md), [Submission Guidelines](./submission_guidelines.md) |   |          |     |                                   |







