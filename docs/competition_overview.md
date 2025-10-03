# Competition Overview
General information about the competition is provided in this section. At the end, quick acess links are provided directing readers to sections that describe each aspect of the competition in more detail.

## Motivation

For many years, wave energy research has focused on **maximizing power capture**, often through **reactive control strategies**. These approaches not only absorb energy from wave-induced motion (active power) but also inject energy back into the system via the PTO (reactive power). 

When the PTO is restricted to absorbing power only — a **passive PTO** — it is inherently subject to the **passivity constraint**. While reactive control can, in theory, achieve higher energy capture than passive strategies, it often does so by amplifying device motion and applying larger control forces {cite:p}`ringwoodBacelliFusco2014,windt2021`. The larger motion and control force operational spaces can lead to more wear on the PTO and mechanical components, implying higher maintenance demands. In addition, the need for bidirectional power capability is usually associated with more complex system {cite:p}`hals2011` (e.g., energy storage, grid connection, or bidirectional actuators), further increasing system  costs. As a result, these factors can collectively negatively impact on the **levelized cost of energy (LCoE)** {cite:p}`said2024`.  

By contrast, passive control is theoretically associated with lower energy capture due to its inherent suboptimality. Yet it offers practical advantages: elimination of energy storage requirements, potentially simpler PTO configurations, and milder device motions with smaller control forces, leading to reduced operational regimes, e.g. {cite:p}`hals2011`. Together, these characteristics can positively influence the LCoE, even if theoretical energy capture is lower.  

**Not all that glitters is gold:** while passive control can appear simpler and less demanding, the nonlinear passivity constraint inherent in these strategies introduces significant challenges for control design. This is precisely where the **real challenge of the competition** lies.  

```{important} 
In this context, the WAPPAC competition offers an attractive opportunity for the wave energy community to advance the state of the art in **passive control strategies**. By focusing on this active debate topic with still open challenges to overcome, participants’ proposals will help scrutinize practical trade-offs and contribute to progress in wave energy control design field.  
```

---

## WavePiston Device

[WavePiston](https://wavepiston.dk/) is a Danish wave energy technology developer, working to harness the vast potential of ocean waves.
Its system captures wave energy using a series of **sails and power take-off (PTO) units** mounted on a submerged string, as illustrated in {numref}`fig-wavepiston-3`, converting the surge motion of waves into usable energy.

```{figure} _static/figures/WavePiston_device/Wavepiston_system_illustration_1.jpg
:name: fig-wavepiston-3
:alt: Illustration of an elevation view of Wavepiston WEC system.
:width: 600px
Illustration of Wavepiston WEC system, comprising a string of energy collectors. Image courtesy of Wavepiston.
```
---

## Objective

The objective of the competition is to design **passive control strategies** that achieve the best trade-off between energy production and reliability.  

Controllers will be evaluated on their ability to:


- **Maximize a performance index** that balances energy capture, physical constraint handling of the WavePiston device, and capacity factor — serving as a surrogate for the LCoE,  

- **Maintain robust performance across different sea states**,  

- Operate strictly under the **passivity constraint**, without access to reactive power.


The overall aim is to identify control approaches that, while limited by passivity, still have meaningful performance indexes and demonstrate practical value for real-world deployment.

---

## Competition Flow

The workflow for participants is straightforward:


1. **Develop** your controller locally using the simulation platform.  

2. **Test locally** with provided wave scenarios and tools.  

3. **Generate evaluation files**.  

4. **Submit** your controller, evaluation files and a report for official evaluation by the organizers. For further details refer to {doc}`submission`


This ensures a **fair, repeatable, and secure evaluation** of all participants’ controllers.

---

## Quick Access Links

Follow the links below for further details regarding:

- Modeling and control framework, its numerical implementation and system parametrization: [WavePiston Model & Control Problem](model_control/index.md).

- [Using WAPPAC Simulation Platform](...).

- [Evaluation Criteria & Competition Rules](...).

- [Submission Guidelines](submission.md).

```{bibliography}
:filter: docname in docname
:style: plain