import pandas as pd
import os

print("--- DEBUG START ---")

# Checkpoint 1: Does the file actually exist?
file_path = 'data/hygdata_v3.csv'
if os.path.exists(file_path):
    print(f"SUCCESS: Found {file_path}")
else:
    print(f"ERROR: Cannot find {file_path}. Did you rename it?")

# Checkpoint 2: Try to load the file
try:
    df = pd.read_csv(file_path, low_memory=False)
    print(f"SUCCESS: Loaded {len(df)} rows of data.")
except Exception as e:
    print(f"FAILED to read CSV: {e}")

# Checkpoint 3: Look for the stars
big_dipper_names = ["Dubhe", "Merak", "Phecda", "Megrez", "Alioth", "Mizar", "Alkaid"]
# .str.strip() just in case there are hidden spaces in the names
dipper_df = df[df['proper'].fillna('').str.strip().isin(big_dipper_names)]

print(f"SUCCESS: Found {len(dipper_df)} Big Dipper stars.")

if not dipper_df.empty:
    print("\n--- RESULTS ---")
    print(dipper_df[['proper', 'ra', 'dec', 'pmra', 'pmdec']])

print("--- DEBUG END ---")