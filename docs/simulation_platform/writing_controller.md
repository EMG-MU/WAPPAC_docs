# Writing Your Controller

Each participant must implement their control algorithm in a Python file (by default, `my_controller.py`).
This file defines the control strategy implemented by the simulation.

Recall that the objective of your controller is to maximize $\mathcal{G}$ over the **scoring interval** $t \in [T_0, t_{end}]$ by defining the control force $F_{pto}(t)$ appropriately for **all three predefined sea state scenarios**:

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

## Key Controller Design Considerations
Some important considerations for participants when defining their controller are summarized below, however, participants are encouraged to explore the full details in the corresponding sections in this documentation.
For convenience, the key time intervals are also illustrated again in {numref}`fig_startup_int_vs_scoring_int_writing_controller`:

```{figure} ../_static/figures/schematics/startup_int_vs_scoring_int.png
:name: fig_startup_int_vs_scoring_int_writing_controller
:width: 100%
:align: center
Key time intervals for the performance index evaluation.
```

### Controller Definition
```{important}
**Your control** implementation (`my_controller` function) **must** be defined for the **full simulation time span** ($t\geq0$), regardless of whether the performance index is only evaluated along the scoring interval.
```
For more details, refer to [Control Problem Definition](../model_control/control_problem.md).

### Evaluation Criteria

```{important}
- **Performance Index ($\mathcal{G}$):** evaluated during the **scoring interval** ($t \geq T_0 = 30$ s).  
- **Passivity constraint:** $p_{pto} \geq 0$ must hold at all times over the **full simulation duration** ($t \geq 0$).
```
For a complete self-contained description of the performance index, refer to [Evaluation Criteria & Competition Rules](../rules_eval_criteria.md).
### Startup Ramp

The **wave excitation force** is gradually introduced via a smooth raised-cosine ramp:

```{math}
ramp(t) = 0.5 \left[ 1 - \cos\!\left(\frac{\pi t}{T_{ramp}}\right) \right]
```

where $ramp(T_{ramp}=20) = 1$.

```{important}
Ramp duration is $\mathbf{T_{ramp}} = 20$ seconds for all simulation runs.
```
For further details on the ramp implementation refer to [Numerical Implementation](../model_control/numerical_implementation.md).

### Control Update Scheme (Zero-Order Hold, ZOH)
Control force is updated at the simulation time step $(\Delta t=0.5 \; \text{s})$. However, internally the solver takes sub-steps in which control force is held constant (see [Numerical Implementation](../model_control/numerical_implementation.md) for details).

### Handling Up-Wave Data (`eta10`)

Up-wave measurement is only available during the **scoring interval**. For times **before the scoring interval** ($t < 30$ s), the up-wave signal `eta10` is set to **NaN**.
Your controller must handle these values robustly, e.g., bypassing up-wave measurement when the measurement is unavailable.

Example:

```python
import numpy as np

def my_controller(x, v, t, eta10):
    if not np.isnan(eta10):
        # Optional preview or estimation logic
        pass
    # Example: simple proportional velocity control
    F_pto = 1e6 * v
    return F_pto
```

---

### ✅ Summary

* Implement your control law in a Python function named `my_controller`.
* Ensure the controller is **operational and numerically stable** for the full simulation duration.
* Respect the **passivity constraint** ($p_{pto} \geq 0$) at all times.
* Use the provided inputs (`x`, `v`, `t`, `eta10`) appropriately.


[//]: # (# Writing Your Controller)

[//]: # ()
[//]: # (Your control algorithm is implemented in `my_controller.py` Python file.  )

[//]: # ()
[//]: # (*   The **required function** signature is:)

[//]: # (```python)

[//]: # (def my_controller&#40;x, v, t, eta10&#41;:)

[//]: # (    # Your code here)

[//]: # (    return F_{pto})

[//]: # (```)

[//]: # (```{note})

[//]: # (You can name Python file as you wish, however the function name inside **must** be `my_controller`.)

[//]: # (```)

[//]: # ()
[//]: # ()
[//]: # (*   **Inputs:**)

[//]: # (    *   `x` &#40;float&#41;: WP sail position [m])

[//]: # (    *   `v` &#40;float&#41;: WP sail velocity [m/s])

[//]: # (    *   `t` &#40;float&#41;: Current simulation time [s])

[//]: # (    *   `eta10` &#40;float&#41;: 10-meter up-wave elevation measurement [m] &#40;measured at $x=-10$ m&#41;.)

[//]: # ()
[//]: # (*   **Output:**)

[//]: # (    *   `F_{pto}` &#40;float&#41;: Your calculated control force [N].)

[//]: # ()
[//]: # (### Important Controller Design Considerations)

[//]: # ()
[//]: # (#### **Evaluation criteria:**)

[//]: # ()
[//]: # (```{important})

[//]: # (- **Performance Index** is evaluated along the so-called **scoring interval**: from $\mathbf{t \geq 30}$ **s** until the end of each simulation run.)

[//]: # (- **Passivity constraint** &#40;$p_{pto} \geq 0$&#41; must be satisfied for the **full simulation perdiod** &#40;$t\geq0$&#41;.)

[//]: # (```)

[//]: # ()
[//]: # (####   **Startup Ramp:** )

[//]: # (The **wave excitation force** is smoothly introduced using a raised cosine window:)

[//]: # (```{math})

[//]: # (ramp&#40;t&#41; = 0.5 \left[ 1.0 - \cos\!\left&#40;\frac{\pi t}{t_{ramp}}\right&#41; \right])

[//]: # (```)

[//]: # (where $ramp&#40;t_{ramp}=20&#41;=1$.)

[//]: # ()
[//]: # (```{important})

[//]: # (**Ramp duration** &#40;influence on excitation force&#41; is of $\mathbf{20}$ **s** for all simulations runs.)

[//]: # (```)

[//]: # ()
[//]: # (####   **Zero-Order Hold &#40;ZOH&#41;:** )

[//]: # (Control force is updated at the simulation time step $&#40;\Delta t=0.5 \; \text{s}&#41;$. However, internally the solver takes sub-steps in which control force is held constant.)

[//]: # (```{important})

[//]: # (**Your control** implementation &#40;`my_controller` function&#41; **must** be defined for the **full simulation time span** &#40;$t\geq0$&#41;, regardless performance index is only evaluated along the scoring interval.)

[//]: # (```)

[//]: # ()
[//]: # (####   **Handling Up-Wave Measurement &#40;`eta10`&#41; NaN values:**)

[//]: # (For $\mathbf{t < 30}$ **s** &#40;outside the scoring interval&#41;, the signal `eta10` is NaN.)

[//]: # (    Your controller must handle this gracefully when using `eta10` in `my_controller` function. )

[//]: # ()
[//]: # (Example:)

[//]: # (```python)

[//]: # (def my_controller&#40;x, v, t, eta10&#41;:)

[//]: # (if not np.isnan&#40;eta10&#41;:)

[//]: # (    # Optional wave preview logic)

[//]: # (    pass)

[//]: # (# Main control logic)

[//]: # (F_{pto} = 1e6 * v  # Example of control force proportional to velocity)

[//]: # (return F_{pto})

[//]: # (```   )

[//]: # ( )
