# Submission Guidelines

Participants must submit the following items via the official competition portal:
**[Link to Submission Portal will be provided HERE soon...]()**

### ✅ Submission Checklist

| Item                        | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| 🔒 **Encrypted files**      | Three `.enc` files from `evaluation_outputs/`                |
| 🧠 **Controller script**    | `my_controller.py` (plus any auxiliary scripts, if needed)   |
| 📄 **Controller report**    | Summary document describing your control strategy            |
| 📦 **Self-contained**       | All files necessary for reproducibility are included         |

---

### 1. Encrypted Evaluation Files

Submit the three encrypted files (`.enc`) generated in your `evaluation_outputs/` directory after running the simulation in **Evaluation Mode** (`"eval_flag": true`).
Each file corresponds to one of the three official sea-state evaluations.

```{important}
All three `.enc` files are required for a valid submission.
Incomplete submissions may be deemed invalid at the organizers’ discretion.
```

---

### 2. Controller Script

Include the final version of your **controller implementation** (e.g., `my_controller.py`) used to produce the encrypted results.

If your controller depends on additional scripts, configuration files, or helper modules, include **all supporting files** within the same submission package **to ensure full reproducibility**.

Your submission must be **self-contained** — all files required to reproduce your results must be included.
The controllers will be **re-executed by the organizers** using the official WAPPAC simulation platform.

Submissions that cannot reproduce the results encoded in the `.enc` files, or that fail to execute correctly, may be **excluded from evaluation**.

---

### 3. Controller Report

Provide a concise **Controller Report** describing your control strategy.
The report should include:

* A brief overview of your control approach and methodology
* Key assumptions or simplifications
* Description of tuning parameters and their rationale
* Summary of controller structure and computational requirements (if applicable)

This document should be clear enough for the organizers to understand and verify the conceptual basis of your design.

---

[//]: # (### 4. Reproducibility and Self-Containment)

[//]: # ()
[//]: # (Your submission must be **self-contained** — all files required to reproduce your results must be included.)

[//]: # (The controllers will be **re-executed by the organizers** using the official WAPPAC simulation platform.)

[//]: # ()
[//]: # (Submissions that cannot reproduce the results encoded in the `.enc` files, or that fail to execute correctly, may be **excluded from evaluation**.)

[//]: # ()
[//]: # (---)
