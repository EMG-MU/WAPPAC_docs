# Writing Your Controller

Your control algorithm is implemented in `my_controller.py` Python file.  

*   The **required function** signature is:
```python
def my_controller(x, v, t, eta10):
    # Your code here
    return F_{pto}
```
```{note}
You can name Python file as you wish, however the function name inside **must** be `my_controller`.
```


*   **Inputs:**
    *   `x` (float): WP sail position [m]
    *   `v` (float): WP sail velocity [m/s]
    *   `t` (float): Current simulation time [s]
    *   `eta10` (float): 10-meter up-wave elevation measurement [m] (measured at $x=-10$ m).

*   **Output:**
    *   `F_{pto}` (float): Your calculated control force [N].

### Important Controller Design Considerations

#### **Evaluation criteria:**

```{important}
- **Performance Index** is evaluated along the so-called **scoring interval**: from $\mathbf{t \geq 30}$ **s** until the end of each simulation run.
- **Passivity constraint** ($p_{pto} \geq 0$) must be satisfied for the **full simulation perdiod** ($t\geq0$).
```

####   **Startup Ramp:** 
The **wave excitation force** is smoothly introduced using a raised cosine window:
```{math}
ramp(t) = 0.5 \left[ 1.0 - \cos\!\left(\frac{\pi t}{t_{ramp}}\right) \right]
```
where $ramp(t_{ramp}=20)=1$.

```{important}
**Ramp duration** (influence on excitation force) is of $\mathbf{20}$ **s** for all simulations runs.
```

####   **Zero-Order Hold (ZOH):** 
Control force is updated at the simulation time step $(\Delta t=0.5 \; \text{s})$. However, internally the solver takes sub-steps in which control force is held constant.
```{important}
**Your control** implementation (`my_controller` function) **must** be defined for the **full simulation time span** ($t\geq0$), regardless performance index is only evaluated along the scoring interval.
```

####   **Handling Up-Wave Measurement (`eta10`) NaN values:**
For $\mathbf{t < 30}$ **s** (outside the scoring interval), the signal `eta10` is NaN.
    Your controller must handle this gracefully when using `eta10` in `my_controller` function. 

Example:
```python
def my_controller(x, v, t, eta10):
if not np.isnan(eta10):
    # Optional wave preview logic
    pass
# Main control logic
F_{pto} = 1e6 * v  # Example of control force proportional to velocity
return F_{pto}
```   
 
