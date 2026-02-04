# 🌌 The Living Sky: Kinematic Stellar Simulation

An investigation into the 2D projection of 3D stellar velocities over secular timescales.

## 🌌 Project Objective
This project serves as a computational tool to visualize the breakdown of "constellation stability" as observed from Earth. By utilizing high-precision astrometric data, the simulation models how stellar proper motion and radial velocity alter the celestial sphere. It transforms the night sky from a static map into a dynamic, evolving system, localized to the **Solar Neighborhood** within the **Orion Arm of the Milky Way**.

## 🔭 Technical Framework & Perspective
The simulation models the **3D Kinematics** of the local galactic environment. While stars move through 3D galactic space, this project specifically adopts a **Geocentric (Earth-centered) perspective**. This allows us to track how human-defined asterisms change as our specific "vantage point" in the galaxy remains the origin.



By extracting velocity vectors from the HYG Stellar Database, the system propagates stellar positions through 3D space over time $t$:

* **Transverse Displacement:** Derived from Proper Motion vectors `pmRA` ($\mu_{\alpha}$) and `pmDec` ($\mu_{\delta}$).
* **Radial Displacement & Photometric Adjustment:** Updating stellar distance via integrated radial velocity ($v_r$), with apparent magnitude recomputed using the inverse-square law.
* **Geometric Distortion:** Quantifying the "shear" of familiar asterisms specifically focusing on **The Big Dipper (Ursa Major)**—as individual stellar components diverge.



## 🕒 Temporal Scope
The simulation generates three distinct celestial snapshots to validate kinematic drift:
1. **Paleolithic Reconstruction (-50,000 Years):** Modeling the celestial sphere during the Upper Paleolithic to identify prehistoric asterism variance.
2. **Modern Epoch (Year 2000.0):** Establishing the J2000 baseline coordinates as defined by the HYG database.
3. **Deep Future Projection (+50,000 Years):** Visualizing the divergence of modern constellations and the emergence of new stellar patterns.

## ⚖️ Data Integrity & Preprocessing
To ensure simulation accuracy and visual clarity, the raw HYG dataset undergoes the following transformations:
* **Magnitude Filtering:** Exclusion of stellar objects with an apparent magnitude $> 6.5$ to simulate the human visual limit.
* **Feature Engineering:** Mapping star IDs to specific constellation asterisms for targeted tracking.
* **Vectorized Cleaning:** Removal of records lacking critical kinematic data ($v_r$ or $\mu$).

## 🛠️ Engineering Stack
* **Data Processing:** `Pandas` for high-performance vectorized operations.
* **Astrometry:** `Astropy` for J2000 epoch transformations and coordinate handling.
* **Visualization:** `Matplotlib` for generating time-series projections and luminosity shifts.

## 📂 System Architecture
* `/data`: Source astrometric catalogs (CSV - **Ignored by Git**).
* `/notebooks`: Algorithmic development and coordinate validation.
* `/src`: Modularized Python functions for 3D-to-2D projection.
* `/notes`: Research journal covering stellar evolution and mathematical proofs.