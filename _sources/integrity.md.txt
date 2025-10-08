# Integrity & Fairness

To ensure a transparent and fair competition, the WAPPAC platform has been designed around principles of **standardization**, **security**, and **verifiable evaluation**.

* **Standardized Evaluation:**
  The WAPPAC application uses protected executables that enforce consistent conditions across all participants. When running in Evaluation Mode (`"eval_flag": true`), every controller is assessed using the **same hydrodynamic model** and **deterministic sea states**. The process produces **encrypted output files**, ensuring all evaluation data remain consistent, authentic, and tamper-proof.

* **Secure Execution:**
  Participant controllers are executed within a **restricted environment**, with file system and network access disabled. This guarantees identical runtime conditions for all participants and ensures that each controller operates **solely based on its internal logic** defined in `my_controller.py`.

* **Independent Verification:**
  To validate the integrity of the competition results, the organizers will **re-run all submitted controllers** using the official WAPPAC platform. This verification step confirms that the reported performance metrics are **legitimate, reproducible, and compliant** with the competition rules.

```{important}
These measures collectively ensure that the WAPPAC Competition is conducted in a fair, secure, and fully reproducible manner for all participants.

While no system is entirely impervious to misuse, we rely on the **honesty** and **fair play** of all **participants** to uphold the integrity of the competition and to contribute positively to the wave energy community.
```