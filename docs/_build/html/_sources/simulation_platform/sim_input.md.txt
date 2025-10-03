# Simulation Input File

All simulation settings are configured through a **JSON file** named `my_sim_input_file.json`. In this file the wave conditions, simulation mode, and reproducibility settings are defined.

### Example

```json
{
  "participant_name": "Team_COER",
  "wave_id": 1,
  "wave_realiz_seed": "random",
  "eval_flag": false
}
```

Key parameters:

*   `wave_id` (1, 2, or 3): Selects the sea state for the simulation.

*   `wave_realiz_seed`:
    *   `"random"`: Generates a new, random wave surface realization each time you run.
    *   An integer (e.g., `123`): Generates a specific, reproducible wave realization. This is useful for repeated testing under identical conditions.
    *   **This setting is ignored if `eval_flag=true`**.

*   `eval_flag` (true/false):
    *   `false` → **Development Mode**: Runs a single simulation with your chosen `wave_id` and `seed`. It generates full time-series data and visualization plots in the `sim_out/` folder for debugging and tuning.
    *   `true` → **Evaluation Mode**: Runs the official evaluation sequence. It automatically simulates all three sea states (Wave IDs 1–3) using fixed, deterministic seeds and produces encrypted evaluation files in the `evaluation_outputs/` folder for submission.
