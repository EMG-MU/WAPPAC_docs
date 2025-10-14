# Submission Guidelines

Participants must submit the following items via the official competition portal:  
**[🔗 Link to Submission Portal will be provided here soon...]()**

---

## ✅ **Submission Checklist**

| Item | Description                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------------------|
| 🔒 **Encrypted output files** | The three `.enc` files from `evaluation_outputs/`, obtained after running your controller in **Evaluation Mode** (`eval_flag=true`). |
| 🧠 **Controller script** | `my_controller.py` (and any additional helper modules placed under `control_helpers/`).                                             |
| 📄 **Controller report** | A concise document describing your control strategy and main design choices.                                                        |
| 📋 **requirements.txt** | List of **any additional pure-Python packages** used by your controller (see details below).                                        |
| 🔁 **Self-contained submission** | All items necessary for reproducibility must be included — except large package folders.                                            |

## 📁 Recommended Submission Structure
Please see the following example structure for submission:  
```
submission_package/
├── my_controller.py
├── control_helpers/
│   ├── my_filters.py
│   ├── my_optimizer.py
│   └── helper_functions.py
├── requirements.txt
├── controller_report.pdf
└── evaluation_outputs/
    ├── waveID_1_2026_02_10_12_48_compressed.enc.enc
    ├── waveID_2_2026_02_10_12_48_compressed.enc.enc
    └── waveID_3_2026_02_10_12_48_compressed.enc.enc
```

| File/Folder             | Description                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `my_controller.py`      | Main controller script — entry point used by WAPPAC to run your control algorithm.                                                 |
| `control_helpers/`      | (Optional, recommended) Folder containing auxiliary control-related modules such as filters, optimizers, and utility functions.    |
| `requirements.txt`      | List of additional **pure-Python** dependencies (not bundled with WAPPAC). Enables COER team to recreate your environment.         |
| `controller_report.pdf` | Short report (max ~3 pages) explaining control concept, methodology, and main design decisions.                                    |
| `evaluation_outputs/`   | Folder automatically generated after Evaluation Mode runs. Must contain three encrypted `.enc` files (one per sea-state scenario). |
| `waveID_*.enc`          | Encrypted output files containing your evaluated performance data. Generated automatically — do not edit manually.                 |


Below you will find detailed descriptions of each item.

---

## 1. 🔒 Encrypted Evaluation Files

Submit the three encrypted files (`.enc`) found in your `evaluation_outputs/` directory.  
These files are automatically produced after running the WAPPAC simulator with:

```json
"eval_flag": true
````

Each file corresponds to one of the **three official sea-state scenarios** used in evaluation.

```{important}
All three `.enc` files are required for a valid submission. Incomplete or mismatched outputs when re-running participans' controllers may be deemed invalid.
```

---

## 2. 🧠 Controller Script

Include the final version of your controller script used to generate the encrypted outputs, typically named:

```
my_controller.py
```

If your implementation uses additional local modules (other Python scripts), include them alongside `my_controller.py`.

```{important}
A dedicated folder named `control_helpers/` (or similar) is optional but **strongly encouraged** to organize all auxiliary controller-related files (e.g., parameter definitions, sub-functions, or model abstractions).
```

All import paths should refer **only** to this folder, e.g.:

```python
from control_helpers.my_filters import moving_average
```

All file paths and imports should be **relative** and **self-contained** — **no absolute or OS-specific paths** or **online resources**.

> **Note:** Controllers will be re-run on the official WAPPAC simulation platform to verify results under identical conditions.

---

## 3. 📋 Requirements File for External Packages

If your controller uses **additional Python packages** beyond those bundled with WAPPAC simulation platform,
you must specify them in a `requirements.txt` file.

```{important}
Do **not upload** the `external_packages/` folder or the actual package source files —
these can be large and are unnecessary for evaluation.
```

The `requirements.txt` allows the COER evaluation team to reproduce your software environment.

### ✅ Example

If your controller relies on additional packages, such as `control`, `cvxpy`, or `sympy`,
your `requirements.txt` should look like:

```
control==0.10.1
cvxpy==1.5.2
sympy==1.13.0
```

Place this file in the same directory as your controller:

> **Important:**
>
> * Only include **pure-Python packages** compatible with CPU execution.
> * All packages must be installable from **PyPI** via standard `pip install -r requirements.txt`.
> * Custom binary libraries or GPU-dependent code are **not permitted**.
> * Internet access is **disabled** during official evaluation runs — the COER team will recreate your environment offline using the provided `requirements.txt`.

### Core Packages Already Included in WAPPAC

Do **not** list or re-install the following packages — they are pre-bundled with the official simulator:

```
torch==2.8.0+cpu  
torchdiffeq==0.2.5  
numpy==2.3.3  
scipy==1.16.2  
matplotlib==3.10.6
```

---

## 4. 📄 Controller Report

Provide a concise **Controller Report** describing your control strategy and methodology.

Recommended structure (max 3 pages):

* Overview of your control concept
* Description of tuning parameters and overall control design
* Outline of controller structure and algorithmic flow
* Discussion of key assumptions or limitations
* Notes on computational complexity (if applicable)

This document should be clear enough for the organizers to understand and verify the conceptual basis of your design.

---

## 5. 🔁 Reproducibility and Verification

Your submission must be **self-contained and reproducible**.

* Controllers will be re-executed by the COER team on the official WAPPAC platform.
* Execution will occur in a **CPU-only**, **offline** environment with fixed seeds and solver settings.
* The reproduced encrypted results must match the ones you submitted.
* If your controller fails to reproduce its own `.enc` files or cannot execute correctly, the submission may be **excluded from final evaluation**.
* Ensure your code runs without requiring user input or manual file browsing dialogs.
> 💡 **Tip:** Before submitting, test your controller locally in Evaluation Mode to confirm that all three `.enc` files are produced correctly under the provided simulator version.

---



---

### Related Sections

* [**Writing Your Controller**](./simulation_platform/writing_controller.md)
* [**Simulation Input File**](./simulation_platform/sim_input.md)
* [**Evaluation Criteria & Competition Rules**](./rules_eval_criteria.md)
* [**Control Problem Definition**](./model_control/control_problem.md)