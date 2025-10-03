# Model & Simulation Parametrization
This section provides the numerical and physical parameters of the competition model.

---

## WavePiston Device Values

- Maximum displacement: $x_{\max} = 2.0$ m  
- Maximum PTO force: $F_{u,\max} = 1.0$ MN   
- Time step: $\Delta t = 0.05$ s  
- Scoring start time: $t_{\text{score}} = 30$ s  

**Note:** These values are public and identical for all participants. Internally, additional parameters are used for model fidelity but remain undisclosed.

---

## Numerical Implementation
- Ramp duration: $t_{ramp} = 20$ s 
- Performance evaluation Time Span: $[30,t_{end}]$ s, where $t_{end}$ is the end of simulation varying for the different sea states scenarios (`wave_id= {1,2,3}`).
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