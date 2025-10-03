# Control Systems

Basic idea of wave energy converter (WEC) control:

1. Measure wave excitation forces.
2. Optimize PTO damping to maximize power extraction.
3. Apply control input in real time.

Python example for a simple proportional controller:

```python
def ptodamping_control(force, k=0.5):
    """
    Simple proportional control for PTO damping
    """
    return k * force
```

See {cite}`smith2020` for control strategies.
