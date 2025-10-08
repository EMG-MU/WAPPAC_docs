# Competition Overview

This section provides a general overview of the competition. Quick-access links at the end direct readers to dedicated sections that describe each aspect of the competition in greater detail.

```{important}
The **WAPPAC competition** provides a unique opportunity for the wave energy community to push the boundaries of **passive control design**. By addressing this open and practically relevant challenge, participants will contribute to advancing the field and refining the overall community understanding of the trade-offs between energy capture, reliability, and simplicity in real-world wave energy systems.
```

## Motivation

For decades, wave energy research has primarily focused on **maximizing power absorption**, often through **reactive control strategies** {cite:p}`ringwoodBacelliFusco2014`. These controllers not only extract energy from wave-induced motion (active power) but also inject energy back into the system through the power take-off (PTO), supplying **reactive power** to enhance energy capture.  

When the PTO is limited to absorbing power only — i.e., operating under a **passivity constraint** — the control strategy is considered **passive**. While reactive control can theoretically achieve higher energy absorption, it typically does so by amplifying device motion and applying larger control forces {cite:p}`ringwoodBacelliFusco2014,windt2021`. In practice, such demands may increase mechanical wear and maintenance requirements. Moreover, the need for bidirectional power flow often entails more complex hardware architectures {cite:p}`hals2011` (e.g., energy storage systems or grid connections, bidirectional actuators), thereby increasing cost and potentially reducing overall reliability. Collectively, these factors can negatively affect the **levelized cost of energy (LCoE)** {cite:p}`said2024`.  

Conversely, **passive control** is theoretically suboptimal in terms of absorbed power but offers tangible practical advantages: it removes the need for energy storage for providing reactive power, simplifies PTO design, and generally yields milder motions and smaller control forces {cite:p}`hals2011`. These properties of passive control contribute to lower operational stress and cost, which may ultimately improve the LCoE despite lower theoretical power absorption.  

However, **all that glitters is not gold**: while passive control may appear conceptually simpler, the **nonlinear passivity constraint** poses a significant challenge for both control design and real-time implementation. Enforcing passivity typically increases the computational burden, complicating the development of efficient controllers suitable for practical deployment. Achieving high performance within these bounds, while maintaining reasonable computational cost for real-time implementation, remains an open challenge that needs innovative solutions from the community.

---

## Competition Flow

The workflow for participants is straightforward:


1. **Develop** your controller locally using the WAPPAC simulation platform.  

2. **Test locally** with provided wave scenarios and tools.  

3. **Generate evaluation files**.  

4. **Submit** your controller, evaluation files and a report for official evaluation by the organizers.


This ensures a **fair, repeatable, and secure evaluation** of all participants’ controllers.

---

## Quick Access Links

Follow the links below for further details regarding:

- Modeling and control framework, its numerical implementation and system parametrization: [WavePiston Model & Control Problem](model_control/index.md).

- Practical use and considerations of the provided simulation platform: [Using WAPPAC Simulation Platform](simulation_platform/index.md).

- [Evaluation Criteria & Competition Rules](rules_eval_criteria.md).

- [Submission Guidelines](submission.md).
