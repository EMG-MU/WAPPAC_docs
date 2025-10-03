# Running Simulations & Understanding Outputs

The WAPPAC platform can operate in two modes: **Development Mode** and **Evaluation Mode**. These modes differ in how the simulation is executed and what outputs are generated.

---

## Development Mode (`"eval_flag": false`)

Use this mode for **testing and tuning** your controller.  

### How to Run

**Linux:**
```bash
./WAPPAC my_controller.py my_sim_input_file.json
```

**Windows:**
```bash
WAPPAC.exe my_controller.py my_sim_input_file.json
```

### Outputs

A new folder `sim_out/` is created containing:

- **results.npz** → Time series arrays:
  - `t` → Time [s]  
  - `pos` → Sail displacement [m]  
  - `vel` → Sail velocity [m/s]  
  - `Fu` → Control force [N]  
  - `p_{pto}` → Absorbed power [W]  

- **results_metadata.json** → Performance metrics and metadata:
  - `Participant's name` → Name of the participant  
  - `Wave ID` → Wave scenario ID  
  - `Wave realization seed` → Seed used for reproducibility  
  - `Time Stamp` → Timestamp of the simulation  
  - `Performance Index` → Calculated $\mathcal{G}$ value  
  - `Performance Index Evaluation time span` → `[start, end]` seconds of scoring interval  
  - `Mean Generated Power` → Average absorbed power over scoring window  
  - `Power constraint satisfaction` → Boolean flag for passivity compliance  

- **results_visual.pdf** → Plots of sail position, velocity, control force, and power.

```{important}
All simulation outputs are **stored** in `sim_out/waveID_[ID]_[timestamp]/`. 
```

```{tip} 
Retain some simulation run folders `sim_out/waveID_X_YY_MM_DD_HH_mm_SS` for reproducibility, especially if you need to revisit results or debug unexpected behaviors.
```

---

## Evaluation Mode (`"eval_flag": true`)

Use this mode **only when ready to generate official submission files**.  

### What Happens

- All **three sea states (Wave IDs 1–3)** are simulated automatically.  
- Fixed deterministic seeds are used (your `wave_realiz_seed` is ignored).  
- Simulation outputs are hidden: **no `.npz` or `.pdf` files are generated**.  
- Passivity constraint **compliance** is printed to the terminal for your info.  

### Outputs
A new folder `evaluation_outputs/` is created containing:

```{important}
- Three **encrypted** files (one per sea state): `evaluation_outputs/waveID_[ID]_[timestamp]_compressed.enc`.  
```

Take into consideration that:
```{important}
 - These are your **official submission results**. 
   
   ⚠️ Without these files, your submission is incomplete.  
```

---
## Summary Workflow

1. **Development Mode (`"eval_flag": false`)**
   - Test and refine your controller.  
   - Inspect `.npz`, `.json`, and `.pdf` files in `sim_out/[timestamp]/` to debug and optimize.

2. **Evaluation Mode (`"eval_flag": true`)**
   - Generate encrypted output files in `evaluation_outputs/`.  
   - Submit `.enc` files, `my_controller.py` (and any extra scripts), and your controller report.



