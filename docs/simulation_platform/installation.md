# Installation & Setup

The WAPPAC simulation platform is distributed as **precompiled executables** with supporting template files. No compilation is required.  

## File Structure

The package contains:

```
distribution/
├── WAPPAC                  # Linux simulation executable
├── WAPPAC.exe              # Windows simulation executable
├── my_controller.py        # Template for your control algorithm
└── my_sim_input_file.json  # Template for simulation configuration
```

### System Requirements

- **Operating systems**: Linux (x86-64) or Windows 10+  
- **Python**: Version ≥ 3.8 (for controller implementation only)  
- **Memory**: ≥ 4 GB RAM  
- **Disk space**: ~200 MB  

### Setup Instructions

1. Download and extract the package to a working directory.  
2. Ensure the executable (`WAPPAC` or `WAPPAC.exe`) has run permissions:
   ```bash
   chmod +x WAPPAC
   ```
3. Verify Python is installed and available on your system path:
   ```python
   python --version
   ```

   
### Test Run
**Linux:**
   ```bash
   ./WAPPAC my_controller.py my_sim_input_file.json
   ```

**Windows:**
   ```bash
   WAPPAC.exe my_controller.py my_sim_input_file.json
   ```
This executes the simulation with the provided controller and configuration.
The results are stored in a new folder inside sim_out/ and a summary is printed to the console.
