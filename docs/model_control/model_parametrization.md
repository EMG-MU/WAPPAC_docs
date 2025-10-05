# Model & Simulation Parametrization

This section provides the WavePiston model parametrization and simulation setup. All quantities and conventions are identical for all participants to ensure fair comparison across submitted control strategies.

---

## WavePiston Device Parametrization
The WavePiston device dynamics are modeled as a **single degree-of-freedom (heave) oscillator** according to equation {eq}`eq_WP_hydrodyn`. Below are all the parameters needed to characetrize the model.

- Maximum displacement: $x_{\max} = 2.0$ m  
- Maximum PTO force: $F_{u,\max} = 1.0$ MN   
- Time step: $\Delta t = 0.05$ s  
- Scoring start time: $t_{\text{score}} = 30$ s  

**Note:** These values are public and identical for all participants. Internally, additional parameters are used for model fidelity but remain undisclosed.

| Variable             | Description                           | Value / Units                                                  |
|:---------------------|:--------------------------------------|:---------------------------------------------------------------|
| $m_w$                | Mass of the WavePiston sail module    | 3.47 × 10³ kg                                                  |
| $m_\infty$           | Added mass at infinite frequency      | 7.06 × 10⁴ kg                                                  |
| $M = m_w + m_\infty$ | Total mass                            | 7.41 × 10⁴ kg                                                  |
| $\mathbf{A_r}$       | Radiation state matrix                | $\begin{bmatrix} -1.40 & -5.80 \\\\ 1.00 & 0.00 \end{bmatrix}$ |
| $\mathbf{B_r}$       | Radiation input matrix                | $\begin{bmatrix} 0.32 & 0.00 \end{bmatrix}^T$                  |
| $\mathbf{C_r}$       | Radiation output matrix               | $\begin{bmatrix} 1.45 & 0.25 \end{bmatrix}$                    |
| $S_h$                | Hydrostatic stiffness coefficient     | 0 N/m                                                          |
| $\rho$               | Water density                         | 1025 kg/m³                                                     |
| $A_{\text{sail}}$    | Effective sail area                   | 32.0 m²                                                        |
| $C_D$                | Quadratic viscous drag coefficient    | 1.5                                                            |
| $x_{\max}$           | Maximum allowed displacement          | 2.0 m                                                          |
| $F_{pto,\max}$       | Maximum PTO (control) force magnitude | 1.0 MN                                                         |
---

## Simulation Parametrization

The simulation setup defines the time integration scheme, control update rate, and transient handling procedures.
All controllers are executed using the same deterministic numerical environment.

| Variable                    | Description                                   | Value / Units                                              |
|:----------------------------|:----------------------------------------------| :--------------------------------------------------------- |
| Integrator                  | Time integration method                       | 4th-order Runge–Kutta (RK4)                                |
| $\Delta t$                  | Fixed integration time step                   | 0.05 s                                                     |
| -                           | Controller update interval (ZOH)              | $\Delta t$                                                 |
| $t_{\text{init}}$           | Simulation initial time                       | 0 s                                                        |
| $t_{\text{end}}$            | Simulation end time                           | sea state dependent                                        |
| $T_{\text{ramp}}$           | Duration of excitation force ramp-up          | 20 s                                                       |
| $T_0$                       | Scoring interval (evaluation) start time      | 30 s                                                       |
| Upwave measurement location | Surface elevation probe position              | $x = -10$ m                                                |
| Initial conditions          | Sail position, velocity, and radiation states | $x(0)=0$, $\dot{x}(0)=0$, $\boldsymbol{\xi}(0)=\mathbf{0}$ |

---

## Excitation Force Characterization

- Based on **three representative sea states**: mild, moderate, and energetic.  
- Sea states are inspired by WavePiston potential deployment site.  
- Excitation forces are derived from frequency-domain characterizations of the radiation kernel.  
- No direct access is provided to:
  - Surface elevation at $x=0$,  
  - Excitation force $F_{ex}(t)$.  
- Direct access is provided to:
  - 10 m up-wave surface elevation measurment ($x = -10$ m).