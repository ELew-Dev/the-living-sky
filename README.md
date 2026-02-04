# The Living Sky: Kinematic Stellar Simulation
An investigation into the 2D projection of 3D stellar velocities over secular timescales.

## 🌌 Project Objective
This project serves as a computational tool to visualize the breakdown of "constellation stability." By utilizing high-precision astrometric data, we simulate how stellar proper motion alters the celestial sphere, transforming the night sky from a static map into a dynamic system.

## 🔭 Technical Framework
The simulation relies on the **Linear Transformation of Spherical Coordinates**. By extracting velocity vectors from the HYG Stellar Database, the model calculates future positions $(\alpha, \delta)$ based on current Epoch data:

* **RA Displacement ($\Delta\alpha$):** Derived from `pmRA` ($\mu_{\alpha} \cos \delta$).
* **Dec Displacement ($\Delta\delta$):** Derived from `pmDec` ($\mu_{\delta}$).

## ⚖️ Data Integrity & Preprocessing
To ensure simulation accuracy and visual clarity, the raw HYG dataset undergoes the following transformations:
* **Magnitude Filtering:** Exclusion of all stellar objects with an apparent magnitude $> 6.5$.
* **Null-Value Handling:** Vectorized removal of records lacking proper motion coordinates.
* **Coordinate Validation:** Normalization of Right Ascension to the $[0, 24)$ hour range.

## 🛠️ Engineering Stack
* **Data Processing:** `Pandas` for vectorized operations on 100,000+ records.
* **Astrometry:** `Astropy` for handling J2000 epoch transformations.
* **Visualization:** `Matplotlib` for generating time-series projections.

## 📂 System Architecture
* `/data`: Source astrometric catalogs (CSV).
* `/notebooks`: Algorithmic development and coordinate validation.
* `/src`: Modularized Python functions for displacement calculations.
* `/notes`: Mathematical proofs and research logs.