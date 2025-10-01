# Competition Overview
General information o the competiton is provided next. For further details on the rules, performanc eevaluation index, please refer to [].

## Motivation

For many years, wave energy research has focused on **maximizing power capture**, often through **reactive control strategies**. These approaches not only absorb energy from wave-induced motion (active power) but also inject energy back into the system via the PTO (reactive power). 

When the PTO is restricted to absorbing power only — a **passive PTO** — it is inherently subject to the **passivity constraint**. While reactive control can, in theory, achieve higher energy capture than passive strategies, it often does so by amplifying device motion and applying larger control forces. The larger motion and control force operational spaces can lead to more wear on the PTO and mechanical components, implying higher maintenance demands. In addition, the need for bidirectional power capability is usually associated with more complex system (e.g., energy storage, grid connection, or bidirectional actuators), further increasing system  costs. As a result, these factors can collectively negatively impact on the **levelized cost of energy (LCoE)**.  

By contrast, passive control is theoretically associated with lower energy capture due to its inherent suboptimality. Yet it offers practical advantages: elimination of energy storage requirements, potentially simpler PTO configurations, and milder device motions with smaller control forces, leading to reduced operational regimes. Together, these characteristics can positively influence the LCoE, even if theoretical energy capture is lower.  

**Not all that glitters is gold:** while passive control can appear simpler and less demanding, the nonlinear passivity constraint inherent in these strategies introduces significant challenges for control design. This is precisely where the **real challenge of the competition** lies.  

```{important} 
In this context, the WAPPAC competition offers an attractive opportunity for the wave energy community to advance the state of the art in **passive control strategies**. By focusing on this active debate topic with still open challenges to overcome, participants’ proposals will help scrutinize practical trade-offs and contribute to progress in wave energy control design field.  
```

---


## WavePiston Device


[WavePiston](https://wavepiston.dk/) is a Danish wave energy technology developer, harnessing the power of ocean waves. Its system captures wave energy using a series of **sails and PTO units** mounted on a submerged string, converting wave motion into usable energy.  


📌 *Schematic/illustration placeholder — insert device diagram here.*



---


## Objective


The objective of the competition is to design **passive control strategies** that achieve the best trade-off between energy production and reliability.  

Controllers will be evaluated on their ability to:


- **Maximize a performance index** that balances energy capture, physical constraint handling of the WavePiston device, and capacity factor — serving as a surrogate for the LCoE,  

- **Maintain robust performance across different sea states**,  

- Operate strictly under the **passivity constraint**, without access to reactive power.


The overall aim is to identify control approaches that, while limited by passivity, still have meaningful performance

indexes and demonstrate practical value for real-world deployment.


For more details please refer (refer to [/docs/model_Control/control_problem] for details) 


---


## Competition Flow


The workflow for participants is straightforward:


1. **Develop** your controller locally using the simulation platform.  

2. **Test locally** with provided wave scenarios and tools.  

3. **Generate evaluation files**.  

4. **Submit** your controller, evaluation files and a report for official evaluation by the organizers. For further details refer to [docs/submission]


This ensures a **fair, repeatable, and secure evaluation** of all participants’ controllers.
