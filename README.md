# The Living Sky: Kinematic Stellar Simulation
An investigation into the 2D projection of 3D stellar velocities over secular timescales.

## 🌌 Project Objective
This project serves as a computational tool to visualize the breakdown of "constellation stability." By utilizing high-precision astrometric data, we simulate how stellar proper motion and radial velocity alter the celestial sphere, transforming the night sky from a static map into a dynamic, evolving system.

## 🔭 Technical Framework
The simulation models the **3D Kinematics** of the solar neighborhood. By extracting velocity vectors from the HYG Stellar Database, the model calculates 4D state changes (position + brightness) over time $t$:

* **Transverse Displacement:** Derived from Proper Motion vectors `pmRA` ($\mu_{\alpha}$) and `pmDec` ($\mu_{\delta}$).
* **Radial Flux Evolution:** Modeling changes in Apparent Magnitude as stars alter their distance from Earth via Radial Velocity ($v_r$).
* **Geometric Distortion:** Quantifying the "shear" of familiar asterisms (e.g., the Big Dipper) as individual stellar components diverge.



## ⚖️ Data Integrity & Preprocessing
To ensure simulation accuracy and visual clarity, the raw HYG dataset undergoes the following transformations:
* **Magnitude Filtering:** Exclusion of all stellar objects with an apparent magnitude $> 6.5$ to simulate the human visual limit.
* **Feature Engineering:** Mapping star IDs to specific constellation asterisms for targeted tracking.
* **Vectorized Cleaning:** Removal of records lacking critical kinematic data ($v_r$ or $\mu$).

## 🛠️ Engineering Stack
* **Data Processing:** `Pandas` for high-performance vectorized operations.
* **Astrometry:** `Astropy` for J2000 epoch transformations and coordinate handling.
* **Visualization:** `Matplotlib` for generating time-series projections and luminosity shifts.

## 📂 System Architecture
* `/data`: Source astrometric catalogs (CSV).
* `/notebooks`: Algorithmic development and coordinate validation.
* `/src`: Modularized Python functions for 3D-to-2D projection.
* `/notes`: Research journal covering stellar evolution and mathematical proofs.