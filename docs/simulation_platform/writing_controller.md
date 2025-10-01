# Writing Your Controller

Your control algorithm is implemented in `my_controller.py`.  

*   The **required function** signature is:
```python
def my_controller(x, v, t, eta10):
    # Your code here
    return F_{pto}
```

*   **Inputs:**
    *   `x` (float): WP sail position [m]
    *   `v` (float): WP sail velocity [m/s]
    *   `t` (float): Current simulation time [s]
    *   `eta10` (float): 10-meter up-wave elevation measurement [m].

*   **Output:**
    *   `F_{pto}` (float): Your calculated control force [N].

### Important Controller Design Considerations

*   **Zero-Order Hold (ZOH):** Control force is updated at the simulation time step ($\Delta t=0.5$ s). However, internally the solver takes sub-steps in which control force is held constant.


*   **Startup Ramp:** The wave excitation force is smoothly introduced using a raised cosine window:
    ```{math}
    ramp(t) = 0.5 \left[ 1.0 - \cos\!\left(\frac{\pi t}{t_{ramp}}\right) \right]
    ```
    where $ramp(t_{ramp}=20)=1$. therefore, the **ramp duration** is of $\mathbf{20}$ **s** for all simulations runs.


*   **Performance Index** is evaluated from $\mathbf{t \geq 30}$ **s** until the end of simulation. 


*   **Handling Up-Wave Measurement (`eta10`) NaN values:** For $\mathbf{t < 30}$ **s**, the signal `eta10` is NaN.
    Your controller must handle this gracefully when using `eta10` in `my_controller.py`. Example:
    ```python
    def my_controller(x, v, t, eta10):
    if not np.isnan(eta10):
        # Optional wave preview logic
        pass
    # Main control logic
    F_{pto} = 1e6 * v  # Example of control force proportional to velocity
    return F_{pto}
    ```   
 
