# Evaluation Criteria & Competition Rules 

---

## Evaluation Criteria

The **WavePiston Passive Control (WAPPAC) Competition** challenges participants to design a **passive control strategy** for the WavePiston device that maximizes a performance index balancing the capture power against the device physical constraints as well as the achieved capacity factor.

The control proposal must seek to maximize the **Performance Index** $\mathcal{G}$ across **three predefined sea state scenarios** under the same modeling framework and simulation setup provided by WAPPAC simulation platform:

$$
\max_{F_u(t)} \; \mathcal{G}\!\left(F_{pto}(t)\right) = \frac{\bar{P}_{pto}}{2 + \frac{|x(t)|_{98}}{x_{\max}} + \frac{|F_{pto}(t)|_{98}}{F_{u,\max}} - \frac{\bar{P}_{pto}}{|p_{pto}(t)|_{98}} }
$$

$$ s.t. \quad \text{WavePiston dynamics} $$
$$ \qquad\quad p_{pto}(t) = F_{pto}(t) \dot{x}(t) \ge 0  $$

For more details on the performance index $\mathcal{G}$ formulation refer to [**Performance Index & Metrics**](./performance_index.md).

### Key Time Intervals for Evaluation Criteria
[Here a sentence should be added saying something like: note the following key intervals for evaluating the particpants control propsoal must be considered when deifning the control strategy]

```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

```{important}
- **Scoring Interval (t ≥ 30s):**
    - The performance index $\mathcal{G}$ across the three predefined sea state scenarios is calculated **only** for the time window starting at **$T_0 = 30$ seconds** until the end of each simulation run. 
    
- **Full Simulation Time Span (t ≥ 0s):**
    - The controller proposed by the participants must be defined from the start of the siulation ($t_{init}=0$). 
    - The passivity constraint, $_{pto}(t) \ge 0$ W, must be satisfied for the **entire simulation duration** (t ≥ 0s). Any violation of this **fundamental rule** will result in **disqualification from the scoring** for that sea state.
```

### Participants Competition Score
The performance score for the three predefined sea state scnearios relizations ($\mathcal{G}_{1}$, $\mathcal{G}_{2}$, $\mathcal{G}_{3}$) is summed to compute the **total competition score**:

$$
\mathcal{G}_{\text{total}} = \mathcal{G}_{1} + \mathcal{G}_{2} + \mathcal{G}_{3}
\label{eq_perf_index_total}
$$

The participant achieving the highest $\mathcal{G}_{\text{total}}$ will be the **WAPPAC Competition Winner**.

All submitted controllers will be **re-run by the COER team** to verify consistency, compliance with constraints, and reproduction of the submitted results.

---

## Competition Rules

1. **Common Model and Framework**  
   - All submissions must be generated using the official **WAPPAC Simulation Platform** provided under [**Model & Simulation Parametrization**](./model_simulation_parametrization.md).  
   - Modifications to the hydrodynamic model, numerical setup, or sea state data are **strictly prohibited**.  

2. **Passivity Enforcement**  
   - The PTO power must remain non-negative at all times:  
     $p_{\text{PTO}}(t) = F_u(t)\dot{x}(t) \ge 0$.  
   - Any violation immediately disqualifies that simulation run.

3. **Constraint Handling**  
   - Position and PTO force limits are considered soft limits (affecting performance index), meaning that occasional exceedances may be tolerated but should be minimized to obtain higher performance index values. :  
     - $|x(t)| \le x_{\max}$  
     - $|F_u(t)| \le F_{u,\max}$  
   - **Passivity constraint:** The PTO power must remain non-negative at all times:  
     $p_{\text{pto}}(t) = F_u(t)\dot{x}(t) \ge 0$.  
     - Any violation immediately disqualifies that simulation run meaning the corresponding performance index $\mathcal{G}_i ($i=1,2,3$) will not be considered for the overal competition score $\mathcal{G}_{total}$ defined in {eq}`eq_perf_index_total`.

4. **Simulation Environment**  
   - Simulations use the fixed reference setup detailed in [**Numerical Implementation**](./numerical_implementation.md).
---

## Submission Guidelines

Participants must submit the following items via the official competition portal:  
**[Submission Portal Link — Coming Soon]**

1. **Encrypted Evaluation Files**  
   - The three `.enc` files automatically generated using `"eval_flag": true`.  
   - These correspond to the results for **mild**, **mid**, and **high** sea states.

2. **Controller Script**  
   - The Python (or MATLAB) file used to generate the evaluation results, named `my_controller.py`.  
   - Include any additional required helper files in the same directory.

3. **Controller Report**  
   - A short document summarizing your control approach, including:  
     - Conceptual overview  
     - Key design or tuning choices  
     - Discussion of constraint handling  

All submissions must be **self-contained and reproducible**.  
Controllers will be re-run on the **official COER environment** for verification.

---

## Disqualification Conditions

A submission will be **disqualified** if any of the following occur:

- Violation of the **passivity constraint** ($p_{\text{PTO}}(t) < 0$).  
- Modification of model parameters, sea state data, or solver settings.  
- Missing, incomplete, or non-functional controller code.  
- Non-causal control implementation (use of future information).  
- Numerical instability or divergent simulation results.

---

## Summary of Key Points

| Category | Rule / Requirement |
|:---------------------------|:--------------------------------------------------------------|
| **Objective** | Maximize the performance index $\mathcal{G}$ across three sea states |
| **Evaluation** | Sum of $\text{PI}_{\text{mild}}$, $\text{PI}_{\text{mid}}$, and $\text{PI}_{\text{high}}$ |
| **Ranking** | Higher $\text{PI}_{\text{total}}$ → higher ranking |
| **Sea States** | Mild, Mid, and High energy scenarios |
| **Model & Parameters** | Fixed and public (see *Model & Simulation Parametrization*) |
| **Control Constraints** | $|x|\!\le\!x_{\max}$, $|F_u|\!\le\!F_{u,\max}$, $p_{\text{PTO}}\!\ge\!0$ |
| **Disqualification** | Passivity violation, model modification, or instability |
| **Deliverables** | Controller code, encrypted results, and short report |
| **Fairness** | Identical simulation environment for all participants |

---

## References to Related Tabs

For further details, refer to:
- [**Model & Simulation Parametrization**](./model_simulation_parametrization.md)  
- [**Control Problem Definition**](./control_problem.md)  
- [**Performance Index & Metrics**](./performance_index.md)  
- [**Numerical Implementation**](./numerical_implementation.md)  
- [**Submission Guidelines**](./submission_guidelines.md)

---

*End of "Competition Rules & Evaluation Criteria"*


# Competition Rules & Evaluation Criteria

---
## Competition Rules

1. **Common Model and Framework**  
   - All submission must be generated or compliant with the **official WAPPAC simulation platform** provided in [Reference](...).  
   - No modifications to the hydrodynamic model, parameters, or simulation environment are permitted.
   - **Passivity constraint** must be enforced at all times:  
       $p_{\text{PTO}}(t) = F_u(t)\dot{x}(t) \ge 0$.  
       Controllers violating this condition are disqualified for that run.

---

## Objective
The **WavePiston Passive Control (WAPPAC)** Competition challenges participants to design a **passive control strategy** for the WavePiston device under three different sea state scenarios. 
Participants must design a control strategy that **maximizes the performance index** $\mathcal{G}$ across three different sea state scenarios:

$$
\max:  \mathcal{G}\left(F_u(t)\right)
$$

This objective function, along with all of its constituent terms, is fully defined in **[Reference](../)**.

The maximization of $\mathcal{G}$ is subject to the **WavePiston dynamic model** {eq}`eq_WP_hydrodyn`, and **passivity constraint**:

$$
p_u(t) = F_u(t) \dot{x}(t) \ge 0
$$


Perf index is evaluated in the scoring interval starting at $T_0=30$ s for every sea state scenario, see figure below and refer to [ref](...) for further details
Importantly, which must be satisfied throughout the entire simulation period.



## Evaluation Criteria
The three encrypted files generated using eval_flag=true in my_sim_out ....[complete], will be used for the evaluation of the particpant results.

The performance index obtain for the three sea state scenarios will be summed 

$$ \text{PI} = \left( \text{PI}\text{mild} + \text{PI}\text{mid} + \text{PI}\text{high} \right) $$

A ranking will be generated using the overal perf index PI {eq}`eq_sum_perf_index`. The particpant with the higest overall perf index will be the winer of WAPPAC competiton.

Controllers will be re-run by COER team to ensure  [] complete.





# Submission Guidelines

Participants must submit the following items via the official competition webpage: **[Link to Submission Portal Here]**

1.  **Encrypted Evaluation Files**: All three `.enc` files generated in your `evaluation_outputs/` folder when running the simulation with `"eval_flag": true`.
    Must 
2. **Controller Script**: The final version of your `my_controller.py` file that was used to generate these results.
   If any additional files were used, please include them in the same folder.
3. **Controller Report**: A **document** providing a clear and concise description of your control strategy. The description should include the methodology used, key tuning parameters, and a brief justification for your design choices.

Ensure your submission is self-contained and that the provided controller and supporting additional files (if any) can reproduce the results in the encrypted files.


- The submission portal link will be provided in the near future HERE.  

---


## Disqualification Conditions

A submission will be disqualified if any of the following occur:
- Violation of the **PTO passivity constraint** ($p_{\text{PTO}}(t) < 0$ at any time).  
- Modification of the model parameters or simulation setup.  
- Missing or non-functional controller code.

---


## Summary of Key Points

| Category | Rule / Requirement                                                |
|:---------------------------|:------------------------------------------------------------------|
| **Objective** | Maximize performance index on three different sea state scenarios |
| **Evaluation** | Based on Performance Index summ over three sea states             |
| **Ranking** | Higher $\text{PI}$ --> better ranking                             |
| **Sea States** | Mild, Mid, and High energy scenarios                              |
| **Model & Parameters** | Fixed and public (see *Model & Simulation Parametrization*)       |
| **Disqualification** | Passivity violation, model modification, or instability           |
| **Deliverables** | Controller code + short documentation                             |
| **Fairness** | Identical setup for all participants                              |

---

## References to Related Tabs

For more details, refer to:
- [**Model & Simulation Parametrization**](./model_simulation_parametrization.md)  
- [**Control Problem Definition**](./control_problem.md)  
- [**Performance Index & Metrics**](./performance_index.md)  
- [**Numerical Implementation**](./numerical_implementation.md)  
- [**Submission Guidelines**](./submission_guidelines.md)

---