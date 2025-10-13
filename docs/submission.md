# Submission Guidelines

Participants must submit the following items via the official competition portal:  
**[🔗 Link to Submission Portal will be provided here soon...]()**

---

## ✅ **Submission Checklist**

| Item | Description                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------|
| 🔒 **Encrypted output files** | The three `.enc` files from `evaluation_outputs/`, obtained after running your controller in **Evaluation Mode** (`eval_flag=ture`). |
| 🧠 **Controller script** | `my_controller.py` (and any additional `.py` helper modules if needed).                                                            |
| 📄 **Controller report** | A concise document describing your control strategy and main design choices.                                                       |
| 📋 **requirements.txt** | List of **any additional pure-Python packages** used by your controller (see details below).                                       |
| 🔁 **Self-contained submission** | All items necessary for reproducibility must be included — except large package folders.                                           |

---

## 1. 🔒 Encrypted Evaluation Files

Submit the three encrypted files (`.enc`) found in your `evaluation_outputs/` directory. These files are automatically produced after running the WAPPAC simulator with:

```json
"eval_flag": true
````

Each file corresponds to one of the **three official sea-state scenarios** used in evaluation.

```{important}
All three `.enc` files are required for a valid submission. Incomplete or mismatched outputs when recomputing may be deemed invalid.
```

---

## 2. 🧠 Controller Script

Include the final version of your controller script used to generate the encrypted outputs, typically named:

```
my_controller.py
```

If your implementation uses additional local modules (other Python scripts), include them alongside `my_controller.py`.
All file paths and imports must be **relative** and **self-contained** — no absolute paths or online resources.

> **Note:** Controllers will be re-run on the official WAPPAC simulation platform to verify results under identical conditions.

---

## 3. 📋 Requirements File for External Packages

If your controller uses **additional Python packages** beyond those bundled with WAPPAC,
you must specify them in a `requirements.txt` file.

Do **not upload** the `external_packages/` folder or the actual package source files —
these can be large and are unnecessary for evaluation.

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

```
submission_package/
├── my_controller.py
├── requirements.txt
├── controller_report.pdf
└── evaluation_outputs/
    ├── sea_state_1.enc
    ├── sea_state_2.enc
    └── sea_state_3.enc
```

> **Important:**
>
> * Only include **pure-Python packages** compatible with CPU execution.
> * All packages must be installable from **PyPI** via standard `pip install -r requirements.txt`.
> * Custom binary libraries or GPU-dependent code are **not permitted**.
> * Internet access is **disabled** during official evaluation runs — the COER team will recreate your environment offline using the provided requirements.

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
* Description of tuning parameters and rationale
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

> 💡 **Tip:** Before submitting, test your controller locally in Evaluation Mode to confirm that all three `.enc` files are produced correctly under the provided simulator version.

---

## 📁 Recommended Submission Structure

```
submission_package/
├── my_controller.py
├── requirements.txt
├── controller_report.pdf
└── evaluation_outputs/
    ├── sea_state_1.enc
    ├── sea_state_2.enc
    └── sea_state_3.enc
```

---

### Related Sections

* [**Simulation Input File**](./simulation_platform/sim_input.md)
* [**Evaluation Criteria & Competition Rules**](./evaluation_criteria.md)
* [**Control Problem Definition**](./model_control/control_problem.md)

```