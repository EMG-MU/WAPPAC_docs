# Simulation Input File

All simulation parameters are specified in a **JSON configuration file**, typically named `my_sim_input_file.json` (you can change the file name but the variables must remain the same).
This file defines the **wave conditions**, **simulation mode**, and **reproducibility settings** used by the WAPPAC platform.

### Example

```json
{
  "participant_name": "Team_COER",
  "wave_id": 1,
  "wave_realiz_seed": "random",
  "eval_flag": false
}
```

### Parameter Overview

| Parameter          | Description                                                                                                                                                                                                                                                                     |
| ------------------ |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `participant_name` | Identifier of the participant or team. Used to label simulation outputs.                                                                                                                                                                                                        |
| `wave_id`          | Selects the sea state scenario (1, 2, or 3). Each corresponds to a distinct, undisclosed sea condition as described in the competition documentation.                                                                                                                           |
| `wave_realiz_seed` | Controls the generation of the wave surface realization:<br>• `"random"` → A new stochastic realization is generated at each run.<br>• *Integer value* (e.g., `123`) → A fixed seed for reproducible simulations.<br>**Note:** This setting is ignored when `eval_flag = true`. |
| `eval_flag`        | Determines the **simulation mode** (see below).                                                                                                                                                                                                                                 |

---

### Simulation Modes

The `eval_flag` parameter defines the operational mode of the WAPPAC simulator. Two distinct modes are available:

#### 1. Development Mode (`eval_flag = false`)

This mode is intended for **testing and tuning** of your control strategy.

* Runs a **single simulation** for the chosen `wave_id` and `wave_realiz_seed`.
* Produces full **time-series data**, diagnostic logs, and **visualization plots** in the `sim_out/` directory.
* Use during controller design and validation, as it allows iteration and debugging results.

#### 2. Evaluation Mode (`eval_flag = true`)

This mode is reserved for **official performance evaluation** and **submission files generation**.

* Automatically executes **all three sea state scenarios** (`wave_id = 1–3`) using **fixed, deterministic seeds**.
* Produces **encrypted evaluation output files** in the `evaluation_outputs/` directory for submission.
* The internal configuration is locked to ensure consistency and fairness across participants.
* No visualizations or detailed diagnostic outputs are generated. Only a console message is provided to inform the participant whether the **passivity constraint** is satisfied in each sea state scenario.

### Summary

* Use **Development Mode** (`eval_flag = false`) for iterative testing your controller across the three different sea state scenarios, and performance index evaluation.
* Switch to **Evaluation Mode** (`eval_flag = true`) only when ready to generate submission files for official evaluation of the results.
