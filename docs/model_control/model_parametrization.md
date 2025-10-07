# Model & Simulation Parametrization

This section presents the **WavePiston model parametrization** and **simulation setup** used throughout the competition.
All quantities, conventions, and numerical configurations are identical for all participants to ensure a **fair and consistent comparison** of submitted control strategies.

---

## WavePiston Device Parametrization

The WavePiston device dynamics are represented as a **single-degree-of-freedom (heave) oscillator**, governed by equation {eq}`eq_WP_hydrodyn`.
The following parameters fully characterize the model accessible to participants.


| Variable             | Description                           | Value / Units                                                |
| :------------------- | :------------------------------------ | :----------------------------------------------------------- |
| $m_w$                | Sail module mass                      | 3.47 × 10³ kg                                                |
| $m_\infty$           | Added mass at infinite frequency      | 7.06 × 10⁴ kg                                                |
| $M = m_w + m_\infty$ | Total effective mass                  | 7.41 × 10⁴ kg                                                |
| $\mathbf{A_r}$       | Radiation state matrix                | $\begin{bmatrix} -1.40 & -5.80 \\ 1.00 & 0.00 \end{bmatrix}$ |
| $\mathbf{B_r}$       | Radiation input matrix                | $\begin{bmatrix} 0.32 & 0.00 \end{bmatrix}^T$                |
| $\mathbf{C_r}$       | Radiation output matrix               | $\begin{bmatrix} 1.45 & 0.25 \end{bmatrix}$                  |
| $S_h$                | Hydrostatic stiffness coefficient     | 0 N/m                                                        |
| $\rho$               | Water density                         | 1025 kg/m³                                                   |
| $A_{\text{sail}}$    | Effective sail area                   | 32.0 m²                                                      |
| $C_D$                | Quadratic viscous drag coefficient    | 1.5                                                          |
| $x_{\max}$           | Maximum allowed displacement          | 2.0 m                                                        |
| $F_{pto,\max}$       | Maximum allowed PTO (control) force magnitude | 1.0 MN                                                       |
| Up-wave measurement location | Surface elevation probe position              | $x = -10$ m                                            |

**Note:** These values are public and identical for all participants. Additional internal parameters may be used to ensure model fidelity but remain undisclosed.

---

## Excitation Force Characterization

The **excitation force** acting on the WavePiston sail is defined by the interaction between the **incident wave surface elevation** and the **excitation force kernel** of the WavePiston device.
Three **predefined sea states** — representing realistic conditions at a potential WavePiston deployment site — are used in the competition. These remain **undisclosed** to participants.

Although the excitation force time series $F_{ex}(t)$ is **not directly provided**, participants may **estimate or reconstruct** it if needed, using the following available information and resources:

* **Real-time sail motion data:** The instantaneous sail position and velocity available within the controller function (see [Writing Your Controller](../simulation_platform/writing_controller.md) for details).
* **Excitation force kernel:** The frequency-domain excitation kernel distributed with the WAPPAC simulation platform (see [Installation & Setup](../simulation_platform/download_setup.md) for details).
* **Up-wave surface elevation measurement:** The surface elevation probe located 10 m up-wave of the device ($x = -10$ m), available to participants during the **scoring interval** via the simulation interface (see [Numerical Implementation](./numerical_implementation.md) and [Writing Your Controller](../simulation_platform/writing_controller.md) for details).
* **Public WavePiston model parametrization:** The shared model parameters provided above.

In summary, while direct excitation force data remain undisclosed, participants are equipped with sufficient information to implement **observer-based** or **model-driven estimators** as part of their control strategy.



---
## Excitation Force Characterization

The **excitation force** acting on the WavePiston sail is characterized using the incident wave surface elevation and the excitation force kernel of the WavePiston device.
**Three predefined sea states**, representing realistic conditions at a potential WavePiston deployment site, are used which remain undisclosed to participants.

Although the excitation force time series $F_{ex}(t)$ is **not provided directly**, participants may **estimate or forecast** it if needed, using the following available information and resources:

* **Real-time sail motion data:** The current sail position and velocity, available within the controller function (see [Writing Your Controller](../simulation_platform/writing_controller.md) for details).
* **Excitation force kernel:** The frequency-domain excitation kernel distributed with the WAPPAC simulation platform (see [Installation & Setup](../simulation_platform/download_setup.md) for details).
* **Up-wave surface elevation measurement:** The wave surface elevation located 10 m up-wave of the device ($x = -10$ m) is accessible by participants through the simulation interface for the **scoring interval** (see [Numerical Implementation](./numerical_implementation.md) and [Writing Your Controller](../simulation_platform/writing_controller.md) for details).
* **Public WavePiston model parametrization** shared above.
* 
In summary, while direct excitation force data remain undisclosed, participants are equipped with sufficient information to develop **observer-based** or **model-driven estimators** if required by their control strategy.



## Excitation Force Characterization

* The excitation force corresponds to **three predefined sea states** which remain undisclosed for participants.
* These sea states are representative of conditions at a **potential WavePiston deployment site**.
* Excitation forces are derived from **frequency-domain hydrodynamic characterizations** of the radiation kernel.
* Participants **do not have direct access** to:

  * The local surface elevation at the device position ($x = 0$)
  * The excitation force time series $F_{ex}(t)$
* Participants **do have access** to:

  * The **10 m up-wave** surface elevation measurement ($x = -10$ m)
  * Frequency domain excitation force kernel included with WPPAC simulation platform distirbution (see [Installation & Setup](../simulation_platform/download_setup.md) for more details)

---

## Simulation Parametrization

The simulation environment defines the **time integration**, **control update**, and **transient handling** procedures.
All control strategies are evaluated under the same deterministic numerical setup.

| Variable                    | Description                                   | Value / Units                                          |
| :-------------------------- | :-------------------------------------------- |:-------------------------------------------------------|
| Integrator                  | Time integration method                       | 4th-order Runge–Kutta (RK4)                            |
| $\Delta t$                  | Fixed integration time step                   | 0.05 s                                                 |
| –                           | Controller update interval (ZOH)              | $\Delta t$                                             |
| $t_{\text{init}}$           | Simulation initial time                       | 0 s                                                    |
| $t_{\text{end}}$            | Simulation end time                           | Sea-state dependent                                    |
| $T_{\text{ramp}}$           | Excitation force ramp-up duration             | 20 s                                                   |
| $T_0$                       | Scoring interval start time                   | 30 s                                                   |
| Initial conditions          | Sail position, velocity, and radiation states | $x(0)=0$, $\dot{x}(0)=0$, $\mathbf{\xi}(0)=\mathbf{0}$ |
