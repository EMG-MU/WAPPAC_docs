# Getting Started with WAPPAC Simulator

The **WAPPAC simulation platform** is distributed as a **precompiled package** containing ready-to-run executables, template files, and model data for both Linux and Windows systems.
No manual installation or dependency setup is required.

You can obtain the platform via **GitHub**:

## Download ZIP via GitHub Release

WAPPAC executables are distributed as a **self-contained release**. The ZIP file **includes both binaries and source code**.
Download the latest release from the [WAPPAC GitHub Releases](https://github.com/EMG-MU/WAPPAC_comp_pub/releases).

## Clone Repository (Recommended)

```bash
git clone https://github.com/EMG-MU/WAPPAC_comp_pub.git
```

```{note}
The cloned repository will **not include the WAPPAC executables**, as these are distributed separately via GitHub releases due to their file size.
```

> **Tip:** Cloning is recommended if you plan to pull updates or bug fixes from the repository during the competition.

---

## File & Folder Structure

After cloning or extracting the downloaded ZIP, your working directory should look like this:

```
WAPPAC_distribution/
├── WAPPAC                     # Linux simulation executable
├── WAPPAC.exe                 # Windows simulation executable
├── my_controller.py           # Template for your control algorithm
├── my_sim_input_file.json     # Template for simulation configuration
├── external_packages/         # Empty folder for custom Python packages
└── model_data/
    ├── exc_force_kernel.csv   # Excitation force kernel in frequency domain
    └── rad_ss_mat.json        # Radiation state-space system matrices
```

> **Notes:**
>
> * The `external_packages/` folder is **empty by default**. Participants can add custom Python packages here to use in their controllers (for details, see [Writing Your Controller](./writing_controller.md)).
>
>   * If you use additional packages, you will be requested to submit a `requirements.txt` file listing all dependencies (refer to [Submission Guidelines](./submission.md)).
> * The `model_data/` folder contains **public model information** provided to participants, including the excitation force kernel (`exc_force_kernel.csv`) and radiation system state-space matrces (`rad_ss_mat.json`).
>
>   * For additional model parametrization details, refer to [Model & Simulation Parametrization](./model_parametrization.md).

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

* `my_controller.py` → implement your control algorithm
* `my_sim_input_file.json` → define your simulation configuration
* `external_packages/` → add optional Python packages for your controller
* `model_data/` → contains public model files

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
