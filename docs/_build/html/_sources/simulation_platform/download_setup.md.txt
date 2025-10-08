# Getting Started with WAPPAC Simulator

The **WAPPAC simulation platform** is distributed as a **precompiled package** containing ready-to-run executables and template files for both Linux and Windows systems.
No manual installation or dependency setup is required.

You can get the platform via **GitHub**:

* **Clone repository (recommended):**

```bash
git clone https://github.com/EMG-MU/WAPPAC_comp_pub.git
```

* **Download ZIP via GitHub interface:**
  GitHub automatically packages the repository as a ZIP file if you choose **Download ZIP** from the repository page: [https://github.com/WAPPAC/WAPPAC-simulation](https://github.com/WAPPAC/WAPPAC-simulation)

> **Tip:** Cloning is recommended if you plan to pull updates or bug fixes from the repository during the competition.

---

## File Structure

After cloning or extracting the downloaded ZIP, the directory will contain:

```
WAPPAC_distribution/
├── WAPPAC                  # Linux simulation executable
├── WAPPAC.exe              # Windows simulation executable
├── my_controller.py        # Template for your control algorithm
├── my_sim_input_file.json  # Template for simulation configuration
└── exc_force_kernel.npz    # Excitation force kernel data
```

> **Note:**
> The `exc_force_kernel.npz` file contains the frequency-domain excitation force kernel.
> This dataset is **public** and **identical** for all participants to ensure consistency.

---

## System Requirements

### Operating Systems

* **Linux:** Ubuntu 20.04+ (recommended: Ubuntu 22.04 LTS or newer)
* **Windows:** Windows 10 or later (64-bit only)

### Hardware

* **CPU:** x86-64 architecture, minimum 2 cores @ 1.6 GHz (recommended: 4 cores @ 2.5 GHz+)
* **RAM:** ≥ 4 GB
* **Disk Space:** ≥ 200 MB free

### Software

* **Python:** Version ≥ 3.8 (required only for controller development)
* **Linux users:** Ensure the following system libraries are installed (default on Ubuntu 20.04+):

  ```bash
  sudo apt update && sudo apt install -y \
      libstdc++6 libgcc-s1 libfreetype6 libpng16-16 libjpeg8 zlib1g
  ```

---

## Setup & Verification

1. **Download and extract** the WAPPAC package to your preferred working directory.
2. On **Linux**, ensure execution permissions are set:

   ```bash
   chmod +x WAPPAC
   ```
3. **Verify Python installation** (needed for your custom controller):

   ```bash
   python --version
   ```
4. Review the provided templates:

   * `my_controller.py` → implement your control algorithm.
   * `my_sim_input_file.json` → define your simulation configuration.

---

## Test Run

To confirm your setup is correct, execute a test simulation using the provided templates.

**Linux:**

```bash
./WAPPAC my_controller.py my_sim_input_file.json
```

**Windows:**

```bash
WAPPAC.exe my_controller.py my_sim_input_file.json
```

This will:

* Run a default simulation using the provided controller and configuration.
* Create an output directory inside `sim_out/`.
* Display a brief summary of results in the console.

---

## Notes

* The platform operates entirely **offline**; no internet connection is required.
* Results are **deterministic** and **reproducible** across Windows and Linux systems.
* For more details, see:

  * [Simulation Input File](./sim_input.md)
  * [Writing Your Controller](./writing_controller.md)
  * [Running Simulations & Understanding Outputs](./running_outputs.md)
