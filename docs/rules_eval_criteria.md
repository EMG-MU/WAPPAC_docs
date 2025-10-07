# Evaluation Criteria & Competition Rules

This section presents the **evaluation framework** and **official competition rules** for the **WavePiston Passive Control (WAPPAC) Competition**.

It is self-contained for participants’ convenience, while details on formulations and implementations are provided in the relevant sections of the **WAPPAC Competition Documentation**.

---

## Evaluation Criteria

The WAPPAC Competition challenges participants to design a **passive control strategy** that maximizes a **performance index** balancing absorbed power, physical constraints, and capacity factor.

All controllers are evaluated using the **official WAPPAC simulation platform**, under **identical numerical setups, model configurations, and sea-state data** to ensure fairness and reproducibility.

The **performance index** $\mathcal{G}$ to be maximized across three predefined sea states is:

```{math}
:label: eq_perf_G
\max_{F_{pto}(t)} \; \mathcal{G}\!\left(F_{pto}(t)\right) \;=&\; 
\frac{\overline{P}_{pto}}
{\,2 \;+\; \dfrac{|x(t)|_{98}}{x_{\max}} \;+\; \dfrac{|F_{pto}(t)|_{98}}{F_{u,\max}} \;-\; \dfrac{\overline{P}_{pto}}{|p_{pto}(t)|_{98}}\,} \\[4pt]
s.t.& \qquad \text{WavePiston dynamics,} \\ 
& \qquad p_{pto}(t) = F_{pto}(t)\dot{x}(t) \ge 0
```

A full derivation and explanation of $\mathcal{G}$ and its terms are provided in [**Control Problem Definition**](./model_control/control_problem.md).

---

### Key Time Intervals

When defining and testing their controllers, participants must account for two key time intervals:

```{figure} ./_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int_eval
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

```{important}
- **Scoring interval ($t \ge 30$ s):**  
  - The performance index $\mathcal{G}$ is computed only during the **scoring interval** $t \in [T_0, t_{end}]$, where $T_0 = 30$ s.  

- **Full simulation time span ($t \ge 0$ s):**  
  - The controller must remain defined and stable for the **entire** simulation duration $t \in [t_{init}, t_{end}]$.  
  - The passivity constraint $p_{pto}(t) \ge 0$ must hold for the **entire time span**.  
  - Any violation of the passivity (hard) constraint results in **disqualification of the corresponding sea state evaluation** (see *Competition Rules* below).
```

---

### Participant’s Final Competition Score

Each of the three predefined sea states is evaluated independently, producing scores $\mathcal{G}_1$, $\mathcal{G}_2$, and $\mathcal{G}_3$. The **final competition score** is computed as:

```{math}
:label: eq_perf_index_total
\mathcal{G}_{\text{total}} \;=\; \mathcal{G}_1 \;+\; \mathcal{G}_2 \;+\; \mathcal{G}_3
```

The participant achieving the highest $\mathcal{G}_{\text{total}}$ will be declared the **winner of the WAPPAC Competition**.
In case of a **tie**, the organizers may apply secondary criteria such as lowest computational cost or earliest valid submission.

---

## Competition Rules

1. **Evaluation Mode & Reproducibility**

   * Final evaluation is performed by setting `eval_flag = true` in `my_sim_input_file.json` (refer to [Simulation Input File](./simulation_platform/sim_input.md)).
     This sequentially generates three **encrypted** `.enc` files (one per sea state) corresponding to the official evaluation runs.
     Performance indices are computed according to {eq}`eq_perf_index_total` and the rules in this section.
   * The three encrypted outputs produced in Evaluation Mode are the **official submission files**.
     Participants must submit these files along with all items listed in [**Submission Guidelines**](./submission.md).
   * The **COER team will re-run** each participant’s controller on the **official WAPPAC simulation platform**, using identical numerical solvers, hydrodynamic models, and fixed seeds.
     This ensures **reproducibility and fairness** across all submissions.
   * Any missing, non-functional, or non-reproducible controller for a given sea state will result in exclusion of that sea state’s score $\mathcal{G}_i$ from the total $\mathcal{G}_{\text{total}}$.
     If fewer than three valid evaluations are obtained, only valid ones are counted — however, **incomplete submissions may be deemed invalid** at the organizers’ discretion.

2. **Passivity (Hard) Constraint Handling**

   * The PTO power must remain **non-negative** throughout the entire simulation:
     $p_{pto}(t) = F_{pto}(t)\dot{x}(t) \ge 0 \, \forall t$.
   * Any violation of this constraint leads to **exclusion** of the affected sea state score $\mathcal{G}_i$ from the total $\mathcal{G}_{\text{total}}$.

3. **Position and Force (Soft) Constraints Handling**

   * Position and PTO force limits are treated as **soft constraints**.
     Occasional exceedances are permitted but penalized through reduced $\mathcal{G}$ values (see [**Control Problem Definition**](./model_control/control_problem.md)).

4. **Integrity and Evaluation Environment**

   * All evaluations are performed on the **official WAPPAC simulation platform** provided in this documentation.
     These ensure identical simulation conditions for all participants.
   * **No modifications** to the simulation binaries, hydrodynamic model, solver settings, or wave data are permitted.
   * Any attempt to alter or tamper with the simulation platform, inputs, or encrypted outputs constitutes a violation of competition integrity and results in **immediate disqualification and reporting the participant**.

5. **Unit System and Conventions**

   * All physical quantities are expressed in **SI units**.
   * Participants must ensure that their controller implementation adheres to the **variable naming and normalization conventions** defined in the documentation to maintain compatibility and correctness.

---

## Quick Reference

| **Topic**            | **Summary**                                                                                       |
| :------------------- | :------------------------------------------------------------------------------------------------ |
| **Objective**        | Maximize the performance index $\mathcal{G}$ across three predefined sea-state scenarios          |
| **Scoring**          | $\mathcal{G}_{\text{total}} = \mathcal{G}_1 + \mathcal{G}_2 + \mathcal{G}_3$                      |
| **Hard Constraint**  | $p_{pto}(t) = F_{pto}(t)\dot{x}(t) \ge 0$ — violations **disqualify** corresponding sea state run |
| **Soft Constraints** | Position and force limits are penalized within $\mathcal{G}$ (occasional violations permitted)    |
| **Reproducibility**  | Organizers re-run controllers under identical conditions using the official WAPPAC platform       |
| **Fairness**         | All evaluations executed on uniform software, and sea-state datasets                    |
| **Units**            | All variables and parameters expressed in **SI units**                                            |

---

### Related Sections for Further Details

* [**Modeling Framework**](./model_control/modelling_framework.md)
* [**Control Problem Definition**](./model_control/control_problem.md)
* [**Performance Index & Metrics**](./performance_index.md)
* [**Simulation Framework**](./simulation_platform/index.md)
* [**Submission Guidelines**](./submission.md)
