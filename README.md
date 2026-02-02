# The Living Sky: Stellar Motion Simulation
An investigation into the shifting patterns of the night sky over geological timescales.

## 🌌 The Problem
To the human eye, constellations appear static. In reality, every star is moving at incredible speeds. Over thousands of years, the "Big Dipper" will distort, and Orion will lose its shape. This project simulates that drift using real astronomical data.

## 🔭 The Science (Phase 2)
This simulation utilizes **Proper Motion** vectors:
* **pmRA ($\mu_{\alpha}$):** Right Ascension velocity (east-west drift).
* **pmDec ($\mu_{\delta}$):** Declination velocity (north-south drift).

By applying these vectors to the current coordinates of ~100,000 stars from the **HYG Database**, we can "fast-forward" the universe.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Handling:** Pandas
* **Astronomy Calculations:** Astropy
* **Visualization:** Matplotlib / Jupyter Notebooks

## 📂 Structure
* `/data`: Raw HYG Database CSV files.
* `/notebooks`: Exploratory Data Analysis and Simulation logic.
* `/src`: Reusable Python scripts for coordinate transformation.
* `/notes`: Research journal and project logs.