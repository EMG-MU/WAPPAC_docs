# Getting Started

This page explains how to set up and run the project.

## Installation (project runtime)

Open a terminal and run:

```bash
# clone the repository (replace with your username/repo)
git clone https://github.com/YOURUSER/YOURREPO.git
cd YOURREPO

# install project runtime dependencies
pip install -r requirements.txt
```

> Note: the file `requirements.txt` referenced above is the **root** `requirements.txt` (project runtime deps).  
> To build the documentation locally, see the *Build docs locally* section below.

## Example usage (python snippet)

```python
# a tiny example showing how a hypothetical function might be used
from wave_energy import simulate

results = simulate(Hs=2.0, Tp=8.0)
print(results)
```
