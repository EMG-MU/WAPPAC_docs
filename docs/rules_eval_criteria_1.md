# Competition Rules & Evaluation Criteria

## Objective

The **Wave Energy Control Competition (WECC)** challenges participants to design an **optimal control strategy** for the WavePiston device that **maximizes energy extraction** while ensuring **safe and compliant operation** under a range of sea states.  
All participants are provided with the same numerical model, parameters, and environmental data to ensure **fair and reproducible comparison**.

The competition aims to:
- Encourage innovation in **control-oriented wave energy conversion**.  
- Benchmark control strategies in a **consistent and transparent** simulation environment.  
- Promote **energy efficiency, robustness, and constraint compliance** across realistic operating conditions.

Three representative **sea states** are used for evaluation:
- **Mild energy** scenario  
- **Mid energy** scenario  
- **High energy** scenario  

Participants’ controllers must handle all three conditions effectively.

---

## Competition Rules

1. **Common Model and Framework**  
   - All simulations must use the **official model** and **numerical setup** provided under the tabs  
     [*Model & Simulation Parametrization*](./model_simulation_parametrization.md) and  
     [*Control Problem Definition*](./control_problem.md).  
   - No modifications to the hydrodynamic model, parameters, or simulation environment are permitted.

2. **Controller Implementation**
   - The controller shall compute the **PTO (control) force** at each control step based on available measurements and states.
   - The control signal must respect the limits:  
     - Position constraint: $|x(t)| \le x_{\max}$  
     - PTO force constraint: $|F_u(t)| \le F_{u,\max}$
   - **Passivity constraint** must be enforced at all times:  
     $p_{\text{PTO}}(t) = F_u(t)\dot{x}(t) \ge 0$.  
     Controllers violating this condition are disqualified for that run.

3. **Simulation Setup**
   - The time integration, update rate, and ramp-up period follow the **standard numerical configuration** (see *Numerical Implementation* tab).  
   - The **control update** occurs at every simulation step $\Delta t$.  
   - Excitation forces ramp up smoothly during the first $T_{\text{ramp}} = 20$ s to avoid transient shocks.  
   - Performance scoring begins only after $T_0 = 30$ s.

4. **Submission Format**
   - Participants must submit:
     - The **controller code** (Python or MATLAB, according to the provided API).  
     - A **short description document** summarizing the control principle and relevant tuning parameters.  
     - Optional: plots illustrating control behavior or performance analysis.  
   - The submission must conform to the official folder structure and interface provided with the competition package.

5. **Fair Play and Transparency**
   - External data or additional model identification is **not allowed**.  
   - Controllers must operate **causally**, using only information available up to the current time.  
   - Any post-processing of simulation outputs for improving performance indices is **strictly prohibited**.

---

## Evaluation Criteria

Each participant’s submission is evaluated using a **Performance Index (PI)** defined in  
[*Evaluation Metrics*](./performance_index.md).  
The PI consolidates energy performance and constraint compliance into a single numerical score for ranking.

The overall ranking is based on the **average PI** across the three sea states:

\[
\text{PI}_{\text{avg}} = \frac{1}{3}\left( \text{PI}_\text{mild} + \text{PI}_\text{mid} + \text{PI}_\text{high} \right)
\]

Higher $\text{PI}_{\text{avg}}$ indicates better performance.

### Scoring Components

The **Performance Index (PI)** aggregates several sub-indices (see dedicated tab for full definitions):
- **Energy Absorption Index ($\eta_E$):** quantifies the extracted energy relative to the incoming wave power.  
- **Constraint Compliance Index ($\eta_C$):** penalizes violations of position, PTO force, and passivity constraints.  
- **Smoothness / Control Effort Index ($\eta_U$):** rewards well-conditioned control signals that reduce mechanical wear.  

Each term is normalized and weighted according to the official formulation provided in the  
[*Performance Index*](./performance_index.md) tab.

---

## Ranking Procedure

1. Simulations are run using the official environment for all three sea states.  
2. For each run, the corresponding **PI** is computed.  
3. The average $\text{PI}_{\text{avg}}$ across sea states determines the final ranking.  
4. In case of a tie, preference is given to the controller with:  
   - Better compliance (higher $\eta_C$), then  
   - Higher efficiency under the **high-energy** condition.

---

## Disqualification Conditions

A submission will be disqualified if any of the following occur:
- Violation of the **PTO passivity constraint** ($p_{\text{PTO}}(t) < 0$ at any time).  
- Modification of the model parameters or simulation setup.  
- Non-causal or predictive use of future wave data.  
- Numerical instability or unbounded response leading to simulation failure.  
- Missing or non-functional controller code.

---

## Deliverables and Deadlines

- The submission portal, deadlines, and template structure are provided under the  
  [*Submission Guidelines*](./submission_guidelines.md) tab.  
- Participants are strongly encouraged to validate their controller locally using the **reference simulation environment** before submission.

---

## Summary of Key Points

| Category | Rule / Requirement |
|:---------------------------|:--------------------------------------------------------------|
| **Objective** | Maximize extracted energy while satisfying constraints |
| **Sea States** | Mild, Mid, and High energy scenarios |
| **Model & Parameters** | Fixed and public (see *Model & Simulation Parametrization*) |
| **Control Constraints** | $|x|\!\le\!x_{\max}$, $|F_u|\!\le\!F_{u,\max}$, $p_{\text{PTO}}\!\ge\!0$ |
| **Evaluation** | Based on Performance Index averaged over three sea states |
| **Ranking** | Higher $\text{PI}_{\text{avg}}$ = better ranking |
| **Disqualification** | Passivity violation, model modification, or instability |
| **Deliverables** | Controller code + short documentation |
| **Fairness** | Identical setup for all participants |

---

## References to Related Tabs

For more details, refer to:
- [**Model & Simulation Parametrization**](./model_simulation_parametrization.md)  
- [**Control Problem Definition**](./control_problem.md)  
- [**Performance Index & Metrics**](./performance_index.md)  
- [**Numerical Implementation**](./numerical_implementation.md)  
- [**Submission Guidelines**](./submission_guidelines.md)

---

*End of "Competition Rules & Evaluation Criteria"*






# Competition Rules & xEvaluation Criteria

To ensure a clear evaluation of the results, a crucial distinction between the full simulation time span and the scoring interval must be made.

```{important}
**Scoring Period (t ≥ 30s):**
The performance index $\mathcal{G}$ {eq}`eq-performance-index` is calculated **only** for the time window starting at **t = 30 seconds** until the end of the simulation run. This is done to mitigate the influence of initial system transients on the final score.
```

```{important}
**Full Simulation Period (t ≥ 0s):**
The controller proposed by the participants must be defined from the start of the siulation (t=0). 
The passivity constraint, $_{pto}(t) \ge 0$ W, must be satisfied for the **entire simulation duration** (t ≥ 0s). Any violation of this **fundamental rule** will result in **disqualification from the scoring** for that sea state.
```

```{important}
The performance index for the three sea states will be summed to compute the overall performance of the controller.
A list of merit will be made.
```

The performance index, also presented in the control problem formulation {doc}`model_control/control_problem`, is as follows:
```{math}
:label: eq-performance-index
\mathcal{G}\left(F_u(t)\right) = \frac{\bar{P}_u}{2 + \frac{|x(t)|_{98}}{x_{\max}} + \frac{|F_u(t)|_{98}}{F_{u,\max}} - \frac{\bar{P}_u}{|p_u(t)|_{98}} }
```

$$ s.t. \quad \text{WavePiston dynamics} $$
$$ \qquad\quad p_u(t) = F_u(t) \dot{x}(t) \ge 0  $$

where $\bar{P}_u$ is the average captured power **during the scoring period**, $|x(t)|_{98}$, $|F_u(t)|_{98}$, and $|p_u(t)|_{98}$ are the **98th percentiles** of the absolute sail displacement,  absolute control force, and instantaneous control power, respectively, **evaluated during the scoring period**. The simulated device motion obeys the Wavepiston dynamics and is subject to maximum allowable displacement $x_\mathrm{max}$ and force $F_{u,\max}$ constraints, in addition to the passivity constraint $p_u(t) \ge 0$, meaning that power extracted from the system cannot be negative
