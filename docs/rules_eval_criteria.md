# Evaluation Criteria & Competition Rules

This section provides a concise overview of the evaluation criteria and competition rules for the WAPPAC Competition.  

It is designed to be self-contained for participants’ convenience, while detailed explanations and technical specifications can be found in the corresponding sections of the **WAPPAC Competition documentation**.

---

## Evaluation Criteria

The **WavePiston Passive Control (WAPPAC) Competition** challenges participants to design a **passive control strategy** that maximizes a performance index balancing captured power,device constraints, and capacity factor.  

All controllers are evaluated under the same **modeling framework** and **numerical setup** provided by the official WAPPAC simulation platform.

The **performance index** to be maximized across **three predefined sea states** is:

```{math}
:label: eq_perf_G
\max_{F_{pto}(t)} \; \mathcal{G}\!\left(F_{pto}(t)\right) \;=&\; 
\frac{\overline{P}_{pto}}
{\,2 \;+\; \dfrac{|x(t)|_{98}}{x_{\max}} \;+\; \dfrac{|F_{pto}(t)|_{98}}{F_{u,\max}} \;-\; \dfrac{\overline{P}_{pto}}{|p_{pto}(t)|_{98}}\,} \\[4pt]
&s.t. \quad \text{WavePiston dynamics,} \\
& \qquad p_{pto}(t) = F_{pto}(t)\dot{x}(t) \ge 0
````

For a complete definition and interpretation of the performance index $\mathcal{G}$ and its terms, refer to [**Performance Index & Metrics**](./performance_index.md).

---

### Key Time Intervals

The participants must consider the following time intervals when defining, testing, and evaluating their control strategies:

```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int_eval
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

```{important}
- **Scoring interval (t ≥ 30 s):**  
  The performance index $\mathcal{G}$ is computed only over the **scoring interval** $t \in [T_0, t_{end}]$, starting at **$T_0 = 30$ s** for every sea state, until the end of the simulation ($t_{end}$).  

- **Full simulation span (t ≥ 0 s):**  
  The participant's controller must be defined for the **full** simulation time span $t \in [t_{init}, t_{end}]$.  
  The passivity constraint $p_{pto}(t) \ge 0$ must be satisfied for the **full** simulation time span.  
  Any **violation** of the **passivity** (hard) constraint will result in disqualifing the corresponding sea state evaluation (see *Competition Rules* below).
```

---

### Participant’s Final Competition Score

Each of the three predefined sea states is evaluated independently, producing scores $\mathcal{G}_1$, $\mathcal{G}_2$, and $\mathcal{G}_3$, correspondingly.

The final competition score is computed as:

```{math}
:label: eq_perf_index_total
\mathcal{G}_{\text{total}} \;=\; \mathcal{G}_1 \;+\; \mathcal{G}_2 \;+\; \mathcal{G}_3
```

The participant achieving the highest $\mathcal{G}_{\text{total}}$ will be declared the **winner of the WAPPAC Competition**.

---

## Competition Rules

1. **Evaluation Mode & Reproducibility**

   * Final evaluation is performed by setting `eval_flag=true` in `my_sim_input_file.json` ([Simulation Input File](...)) , which results in generating three encrypted `.enc` files, one per sea state.
     The performance indexes of the three evaluation sea states realizations will be computed according to {eq}`eq_perf_index_total` and the rules stated in this section.
     (See [**Using WAPPAC Simulation Platform**](./simulation_framework.md) for details on the evaluation mode associated with `eval_flag=true`.)
   * The three encrypted outputs generated when `eval_flag=true` are the **official evaluation files** participants must submit.
     All files specified in [**Submission Guidelines**](./submission_guidelines.md) must be provided by the participants.
   * The COER team will **re-run each participant’s controller** on the WAPPAC simulation platform to verify results.
     Any missing, non-functional, or non-reproducible controller for a sea state will result in excluding that sea state’s $\mathcal{G}_i$ from the total score.

2. **Passivity (Hard) Constraint Handling**

   * The PTO power must remain non-negative for the entire simulation time span:
     $p_{pto}(t) = F_{pto}(t)\dot{x}(t) \ge 0 \; \forall t$.
   * Violation of the passivity constraint in any sea state evaluation leads to exclusion of that sea state score $\mathcal{G}_i$ from $\mathcal{G}_{\text{total}}$.

3. **Position and Force (Soft) Constraints Handling**

   * Position and PTO force limits are considered **soft constraints**.
     Occasional exceedances are tolerated but may result in reduced performance index values (see $\mathcal{G}$ definition).

4. **Integrity**

    * **No modifications** to the hydrodynamic model, numerical solver, sea-state data, or official executables are permitted.
    * Any tampering with the platform, input data, or encrypted outputs is strictly prohibited.
      Detection of such actions will result in **reporting** the **participant** and **immediate disqualification**.

---

## Quick Reference

| **Topic**            | **Summary**                                                                                          |
| :------------------- |:-----------------------------------------------------------------------------------------------------|
| **Objective**        | Maximize the performance index $\mathcal{G}$ across three predefined sea states scenarios            |
| **Scoring**          | $\mathcal{G}_{\text{total}} = \mathcal{G}_1 + \mathcal{G}_2 + \mathcal{G}_3$                         |
| **Hard Constraint**  | $p_{pto}(t) = F_{pto}(t)\dot{x}(t) \ge 0$ — violations **disqualify** corresponding sea state run    |
| **Soft Constraints** | Position and force limits are penalized within the performance index (occasional violations allowed) |
| **Reproducibility**  | Organizers re-run all submitted controllers on the official WAPPAC platform                          |

---

### Related Sections for Further Details

* [**Modeling Framework**](./modelling_framework.md)
* [**Control Problem Definition**](./control_problem.md)
* [**Performance Index & Metrics**](./performance_index.md)
* [**Simulation Framework**](./simulation_framework.md)
* [**Submission Guidelines**](./submission_guidelines.md)

```

[//]: # ()
[//]: # (# Evaluation Criteria & Competition Rules)

[//]: # ()
[//]: # (This is a summary of the evaluation criteria and competition rules for ht eparticpants convenience. Please refer to the corresponding sections of WAPPAC comeptition documentation for further details. )

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Evaluation Criteria)

[//]: # ()
[//]: # (The **WavePiston Passive Control &#40;WAPPAC&#41; Competition** challenge participants to design a **passive control strategy** that maximizes a performance index balancing captured power against device constraints and capacity factor.  )

[//]: # (All controllers are evaluated under the same modeling framework and numerical setup provided by the official WAPPAC simulation platform.)

[//]: # ()
[//]: # (The **performance index** to be maximized is:)

[//]: # ()
[//]: # (```{math})

[//]: # (:label: eq_perf_G)

[//]: # (\max_{F_{pto}&#40;t&#41;} \; \mathcal{G}\!\left&#40;F_{pto}&#40;t&#41;\right&#41; \;=&\; )

[//]: # (\frac{\overline{P}_{pto}})

[//]: # ({\,2 \;+\; \dfrac{|x&#40;t&#41;|_{98}}{x_{\max}} \;+\; \dfrac{|F_{pto}&#40;t&#41;|_{98}}{F_{u,\max}} \;-\; \dfrac{\overline{P}_{pto}}{|p_{pto}&#40;t&#41;|_{98}}\,} \\)

[//]: # (&s.t. \quad \text{WavePiston dynamics} \qquad \\\\)

[//]: # (&p_{pto}&#40;t&#41; = F_{pto}&#40;t&#41; \dot{x}&#40;t&#41; \ge 0)

[//]: # (```)

[//]: # (For more details on the performance index $\mathcal{G}$ definition refer to [**Performance Index & Metrics**]&#40;./performance_index.md&#41;.)

[//]: # ()
[//]: # (### Key Time Intervals)

[//]: # ()
[//]: # ()
[//]: # (The following key time intervals aspects must be considered when defining, testing, and evaluating your control strategy:)

[//]: # ()
[//]: # (```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png)

[//]: # (:name: fig_startup_int_vs_scoring_int_eval)

[//]: # (:width: 100%)

[//]: # (:align: center)

[//]: # (Key time intervals for the performance index evaluation.)

[//]: # (```)

[//]: # ()
[//]: # (```{important})

[//]: # (- **Scoring interval &#40;t ≥ 30 s&#41;:**  )

[//]: # (  The performance index $\mathcal{G}$ is computed only over the **scoring interval** $t \in [T_0, t_{end}]$, starting at **$T_0 = 30$ s** until the end of the simulation &#40;for every sea state&#41;.  )

[//]: # ()
[//]: # (- **Full simulation span &#40;t ≥ 0 s&#41;:**  )

[//]: # (  Your controller must be defined for the entire simulation time span $t \in [t_{init}, t_{end}]$, see {numref}`fig_startup_int_vs_scoring_int_eval`.  )

[//]: # (  The passivity constraint $p_{pto}&#40;t&#41; \ge 0$ must hold for the **entire** simulation duration.  )

[//]: # (  Any **violation** of this **hard constraint** for a given run will **disqualify** that run &#40;see *Competition Rules* below&#41;.)

[//]: # (```)

[//]: # ()
[//]: # (### Participant's Final Competition Score)

[//]: # (Each of the three predefined sea states is evaluated independently, producing scores $\mathcal{G}_1, \mathcal{G}_2, \mathcal{G}_3$.)

[//]: # (The final competition score is the sum:)

[//]: # ()
[//]: # (```{math})

[//]: # (:label: eq_perf_index_total)

[//]: # (\mathcal{G}_{\text{total}} \;=\; \mathcal{G}_1 \;+\; \mathcal{G}_2 \;+\; \mathcal{G}_3)

[//]: # (```)

[//]: # (The participant with the highest $\mathcal{G}_{\text{total}}$ will be the **winner of WAPPAC Competition**.)

[//]: # ()
[//]: # ()
[//]: # (## Competition Rules)

[//]: # ()
[//]: # (1. **Evaluation Mode & Reproducibility**)

[//]: # ()
[//]: # (   * Final evaluation is performed with `eval_flag=true`, generating three encrypted `.enc` files, one per sea state. The performance indexes for those sea states will be computed according to {eq}`eq_perf_index_total` and following the rules established in this section to evaluate the particpants final score. &#40;refer to []&#40;&#41; for further details&#41;.)

[//]: # (   * These encrypted outputs are the **official evaluation files** that participants are requested to submit. For more details on submission guidelines please refer to []&#40;&#41;.)

[//]: # (   * The COER team will **re-run participants controller** on WAPPAC simulation platform to verify the results. Missing, non-functional, or non-reproducible controller for any of the three sea states, will result in excluding the corresponding sea state performance index $\mathcal{G}_i$ &#40;$i=1,2,3$&#41; from the total score.)

[//]: # ()
[//]: # (2. **Passivity &#40;Hard&#41; Constraint Handling**)

[//]: # (   * The PTO power must remain non-negative for the full simulation time span:)

[//]: # (     $p_{pto}&#40;t&#41; = F_{pto}&#40;t&#41;\dot{x}&#40;t&#41; \ge 0 \;\; \forall t$. )

[//]: # (   * If any violation of the passivity constraint occurs at any of the three sea states evaluations, the corresponding $\mathcal{G}_i$ &#40;$i=1,2,3$&#41; will be excluded from the total score.)

[//]: # ()
[//]: # (3. **Position and Force &#40;Soft&#41; Constraints Handling**)

[//]: # ()
[//]: # (   * Position and PTO force limits are considered *soft constraints*:)

[//]: # (     occasional exceedances are tolerated but may results in lower performance index.)

[//]: # ()
[//]: # (4. **Integrity**)

[//]: # (   * **No modifications** to the hydrodynamic model, numerical solver, sea-state data, or official executables are permitted. )

[//]: # (   * Any tampering with the platform, sea state data, or encrypted outputs is **strictly forbidden**. If any inappropriate use of WAPPAC platform is detected, the participant will be reported and immediately disqualified.)

[//]: # ()
[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## Quick Reference)

[//]: # ()
[//]: # (| **Topic**            | **Summary**                                                                                                                                                                                 |   |          |     |                                   |)

[//]: # (| :------------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| - | -------- | --- | --------------------------------- |)

[//]: # (| **Objective**        | Maximize `\&#40;\mathcal{G}\&#41;` &#40;performance index&#41; across three sea states                                                                                                                      |   |          |     |                                   |)

[//]: # (| **Scoring**          | `\&#40;\mathcal{G}_{\text{total}} = \mathcal{G}_1 + \mathcal{G}_2 + \mathcal{G}_3\&#41;`                                                                                                            |   |          |     |                                   |)

[//]: # (| **Hard Constraint**  | `\&#40;p_{pto}&#40;t&#41; = F_{pto}&#40;t&#41;\dot{x}&#40;t&#41; \ge 0\&#41;` — violations disqualify runs                                                                                                                          |   |          |     |                                   |)

[//]: # (| **Reproducibility**  | Organizers re-run submitted controllers on the official platform                                                                                                                            |   |          |     |                                   |)






