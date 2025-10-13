# Writing Your Controller

Each participant must implement their control algorithm in a Python file (by default, `my_controller.py`).
This file defines the control strategy executed by the WAPPAC simulator.

The controller goal is to **maximize** the performance index $\mathcal{G}$ over the **scoring interval** $t \in [T_0, t_{end}]$ by defining the control force $F_{pto}(t)$ appropriately for **all three sea state scenarios**:

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
For more details, refer to [Control Problem Definition](../model_control/control_problem.md).

---

## Controller Function Interface

Your controller must define the following function:

```python
def my_controller(x, v, t, eta10):
    # Your control logic here
    return F_pto
```

```{note}
You may rename the Python file, but the function name **must** be `my_controller`.
```

### Function Arguments

| Variable | Type  | Description                                                |
| -------- | ----- | ---------------------------------------------------------- |
| `x`      | float | Sail position [m]                                          |
| `v`      | float | Sail velocity [m/s]                                        |
| `t`      | float | Current simulation time [s]                                |
| `eta10`  | float | 10 m up-wave surface elevation [m] (measured at $x=-10$ m) |

### Function Output

| Variable | Type  | Description                                 |
| -------- | ----- | ------------------------------------------- |
| `F_pto`  | float | Control force [N] applied by the PTO system |

---

## Using External Packages

Participants may include **custom or third-party Python packages** by placing them in the dedicated folder:

```
WAPPAC_distribution/
├── my_controller.py
├── external_packages/
│   └── [your custom packages here]
```

> **Important:**
> The folder name **must remain exactly** `external_packages/`.
> WAPPAC automatically searches this directory at runtime to make its packages available to your controller.

### Installing a Custom Package Locally

You can install a package directly into the `external_packages` folder using:

```bash
python -m pip install --target ./external_packages control
```

This command installs the package (e.g. `control`) locally, without requiring system-wide installation.

Then, in your controller, simply import it as usual:

```python
import control  # Loaded from external_packages

def my_controller(x, v, t, eta10):
    # Your control logic relying on control external package here
    return F_pto
```

If your controller depends on external packages, include a `requirements.txt` file in your submission listing them.
Refer to [Submission Guidelines](../submission.md) for details.

---

## Allowed and Restricted Features

The controller file (e.g. `my_controller.py`) is executed in a **restricted environment** to ensure safety, fairness, and reproducibility across participants.

✅ **Allowed**

* Standard Python syntax, arithmetic, and logical operations.
* Imports from:

  * Standard Python libraries (e.g., `math`, `json`, `random`, `os`, etc.)
  * Common scientific libraries, including:

    * `numpy`, `scipy`, `torch`, and `matplotlib` (with exact versions) are already bundled inside the WAPPAC binaries, so there is **no need** to install them in `external_packages/` folder:

      ```text
      torch==2.8.0+cpu  
      torchdiffeq==0.2.5  
      numpy==2.3.3  
      scipy==1.16.2  
      matplotlib==3.10.6
      ```
* Any lightweight, **pure-Python** module that does not require network access, system-level privileges, or GPU computation.
* Internal helper functions, persistent variables (within the same run), and lightweight data structures.
* Optional initialization or pre-computed constants at file start.

🚫 **Restricted**

| Restriction                                                                   | Rationale (based on current platform)                                                                                                                                                  |
| ----------------------------------------------------------------------------- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **No external I/O operations** (file read/write beyond provided interfaces) | To ensure reproducibility and sandbox integrity — all data exchange must occur through defined input/output channels (`my_sim_input_file.json`, `sim_out/`, or evaluation outputs).    |
| **No GPU or CUDA calls**                                                    | All evaluations are performed on the CPU for reproducibility and cross-platform consistency. The packaged `torch` build is CPU-only (`torch==2.8.0+cpu`).                              |
| **No external network or API calls**                                        | To maintain fairness and isolation — controllers must run fully offline with no external data access.                                                                                  |
| **No dynamic package installation (`pip install`, `importlib`, etc.)**      | The simulation environment is frozen at runtime. All dependencies are already provided in the binary.                                                                                  |
| **No modification of internal WAPPAC modules**                              | Internal physics models, numerical solvers, and evaluation logic are locked to guarantee identical simulation conditions across participants.                                          |

---

## Key Controller Design Considerations

Participants should consider the following aspects when developing their control law.
See related documentation for detailed explanations.

```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int_writing_controller
:width: 100%
:align: center
Key time intervals for performance evaluation.
```

### Controller Definition

```{important}
Your control law (`my_controller`) must be valid and numerically stable for the **entire simulation duration** ($t \geq 0$), even though the performance index is only computed during the scoring interval.
```

### Evaluation Criteria

```{important}
- **Performance Index ($\mathcal{G}$):** evaluated during the **scoring interval** ($t \geq T_0 = 30$ s).  
- **Passivity constraint:** $p_{pto} \ge 0$ must hold for the **entire simulation** ($t \geq 0$).
```
For a complete self-contained description of the performance index, refer to [Evaluation Criteria & Competition Rules](../rules_eval_criteria.md).

### Evaluation Mode Control Requirement

During **Evaluation Mode** (`eval_flag = true`), WAPPAC platform runs the **three official sea state scenarios (wave IDs 1–3)** in **aleatory order**.
Controllers **do not receive any prior information** about which sea state is being simulated so they should be able to adapt accordingly to maximize the performance index.
Participants can check their controller robustness to varying sea states scenarios withour prior information of the sea state, by reproducing similar simulations in **development mode** (`eval_flag = false`).


### Startup Ramp

The **wave excitation force** is gradually introduced (attenuated) via a smooth raised-cosine ramp (refer to [Numerical Implementation](../model_control/numerical_implementation.md) for further details):

```{math}
ramp(t) = 0.5 \left[ 1 - \cos\!\left(\frac{\pi t}{T_{ramp}}\right) \right]
```

where $ramp(T_{ramp}=20) = 1$.

```{important}
Ramp duration is fixed to $\mathbf{T_{ramp}} = 20$ seconds for all simulations.
```

### Control Update Scheme (ZOH)

The control force is updated at every simulation time step of $\Delta t = 0.05\ \text{s}$.
Within each time-step, the solver internally performs Runge–Kutta (RK4) intermediate evaluations at which the control force remains constant (Zero-Order Hold).
See [Numerical Implementation](../model_control/numerical_implementation.md) for details.

### Handling Up-Wave Data (`eta10`)

The signal `eta10` (10 m up-wave surface elevation) is **available only during the scoring interval**.
For $t < 30$ s, `eta10` is set to `NaN`. Your controller must handle this robustly.

Example:

```python
def my_controller(x, v, t, eta10):
    if not np.isnan(eta10):
        # Optional preview or estimation logic
        pass
    # Example: proportional velocity control
    F_pto = 1e6 * v
    return F_pto
```

---

### ✅ Summary

* Implement your control in a Python function named `my_controller`.
* Ensure the controller is **numerically stable** and satisfies the **passivity constraint** ($p_{pto} \ge 0$) for the full simulation time span.
* Use the provided inputs (`x`, `v`, `t`, `eta10`).
* You may use external Python packages located in `external_packages/`. (submit corresponding `requirements.txt`).
* The controller should be able to adapt accordingly across all sea states evaluated in aleatory order during evaluation mode.
