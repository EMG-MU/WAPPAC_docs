# Running Simulations & Understanding Outputs

The WAPPAC simulation platform operates in **two modes**: **Development Mode** and **Evaluation Mode**. These modes differ in execution behavior, output generation, and intended use.

---

## How to Run

**Linux:**

```bash
./WAPPAC my_controller.py my_sim_input_file.json
```

**Windows:**

```bash
WAPPAC.exe my_controller.py my_sim_input_file.json
```

---

## Development Mode (`"eval_flag": false`)

Use this mode for **iterative testing, tuning, and debugging** of your controller.

### Outputs

A new folder `sim_out/` is generated for each simulation run, containing:

* **results.npz** → Time series arrays:

  * `t` → Time [s]
  * `pos` → Sail displacement [m]
  * `vel` → Sail velocity [m/s]
  * `Fu` → Control force [N]
  * `p_pto` → Absorbed power [W]

* **results_metadata.json** → Summary metadata and performance metrics:

  * Participant name
  * Wave ID
  * Wave realization seed
  * Simulation timestamp
  * Performance Index $\mathcal{G}$
  * Scoring interval `[start, end]`
  * Mean absorbed power over scoring window
  * Passivity constraint compliance (Boolean)

* **results_visual.pdf** → Plots of sail position, velocity, control force, and power.

```{important}
All simulation outputs are stored in `sim_out/waveID_[ID]_[timestamp]/`.
```

```{tip}
Keep previous simulation folders for reproducibility and to revisit results during controller development.
```

---

## Evaluation Mode (`"eval_flag": true`)

Use this mode **only when ready to generate official submission files**.

### Behavior

* All **three sea states (Wave IDs 1–3)** are simulated sequentially.
* Fixed deterministic seeds are used; your `wave_realiz_seed` is ignored.
* No detailed outputs (`.npz` or `.pdf`) are generated.
* Compliance with the **passivity constraint** is printed in the console.

### Outputs

A new folder `evaluation_outputs/` is created containing:

```{important}
- Three encrypted files (one per sea state): 
    `evaluation_outputs/waveID_[ID]_[timestamp]_compressed.enc`.
- These are your **official submission results**. 
    ⚠️ Submissions without these files are considered incomplete.
```

---

## Summary Workflow

1. **Development Mode (`"eval_flag": false`)**

   * Test, debug, and optimize your controller.
   * Inspect `.npz`, `.json`, and `.pdf` outputs in `sim_out/`.

2. **Evaluation Mode (`"eval_flag": true`)**

   * Generate encrypted `.enc` files for all three sea states.
   * Submit `.enc` files, your `my_controller.py`, and any supplementary scripts or reports.
