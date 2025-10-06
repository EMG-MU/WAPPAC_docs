# Installation & Setup

The **WAPPAC simulation platform** is distributed as a **precompiled package** that includes ready-to-run executables and template files for both Linux and Windows systems.
No manual compilation or installation of dependencies is required to execute simulations.

---

## File Structure

The distributed package includes the following files:

```
distribution/
├── WAPPAC                  # Linux simulation executable
├── WAPPAC.exe              # Windows simulation executable
├── my_controller.py        # Template for your control algorithm
├── my_sim_input_file.json  # Template for simulation configuration
└── exc_force_kernel.npz    # Excitation force kernel data
```

> **Note:**
> The `exc_force_kernel.npz` file provides the frequency domain excitation force kernel.
> This data is **public** and identical for all participants.

---

## System Requirements

### Operating Systems

* **Linux:** Ubuntu 20.04+ (recommended: Ubuntu 22.04 LTS or newer)
* **Windows:** Windows 10 or later (64-bit only)

### Hardware

* **CPU:** x86-64 architecture, minimum 2 cores @ 1.6 GHz (recommended 4 cores @ 2.5 GHz+)
* **RAM:** ≥ 4 GB
* **Disk space:** ≥ 200 MB free

### Software

* **Python:** Version ≥ 3.8 (required only for controller development)
* **Linux users:** Ensure the following system libraries are installed (default on Ubuntu 20.04+):

  ```bash
  sudo apt update && sudo apt install -y \
      libstdc++6 libgcc-s1 libfreetype6 libpng16-16 libjpeg8 zlib1g
  ```

---

## Setup Instructions

1. **Download and extract** the package to your working directory.
2. On **Linux**, ensure the executable has run permissions:

   ```bash
   chmod +x WAPPAC
   ```
3. **Verify Python installation** (for controller implementation):

   ```bash
   python --version
   ```
4. Review the distributed templates:

   * `my_controller.py` → implement your control algorithm.
   * `my_sim_input_file.json` → define the simulation setup.

---

## Test Run

Once extracted, you can test the setup using the provided templates.

**Linux:**

```bash
./WAPPAC my_controller.py my_sim_input_file.json
```

**Windows:**

```bash
WAPPAC.exe my_controller.py my_sim_input_file.json
```

The simulation will:

* Run using the selected controller and input configuration.
* Automatically create an output directory inside `sim_out/`.
* Display a summary of results in the console.

---

## Notes

* The package operates entirely **offline**; no internet connection is required.
* Results are deterministic and reproducible across all systems meeting the above requirements.
* For details on input files, controller design, and output interpretation, see:

  * [Simulation Input File](./sim_input.md)
  * [Writing Your Controller](./writing_controller.md)
  * [Running Simulations & Understanding Outputs](./running_outputs.md)