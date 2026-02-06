import pandas as pd
import os

def project_stellar_motion(df, years):
    """
    Simulates 3D and 2D stellar drift over a given timeframe.
    """
    mas_to_deg = 3600000 
    km_s_to_pc_yr = 1.0227e-6 
    
    result = df.copy()
    
    # Update Coordinates (2D)
    result['new_ra'] = result['ra'] + (result['pmra'] * years / mas_to_deg)
    result['new_dec'] = result['dec'] + (result['pmdec'] * years / mas_to_deg)
    
    # Update Distance (3D)
    result['new_dist'] = result['dist'] + (result['rv'] * km_s_to_pc_yr * years)
    
    return result

# --- EXECUTION ---
file_path = 'data/hygdata_v3.csv'

# Still need to load and filter, but skipping the debug checkpoints for brevity. Assuming the file is correct and the data is loaded successfully.
df = pd.read_csv(file_path, low_memory=False)
names = ["Dubhe", "Merak", "Phecda", "Megrez", "Alioth", "Mizar", "Alkaid"]
dipper_df = df[df['proper'].fillna('').str.strip().isin(names)].copy()

if not dipper_df.empty:
    # Generate snapshots (The "Temporal Scope" from README)
    past_sky   = project_stellar_motion(dipper_df, -50000)
    future_sky = project_stellar_motion(dipper_df, 50000)

    print("--- SIMULATION ENGINE ONLINE ---")
    print(f"Projecting {len(dipper_df)} stars across +/- 50,000 years.\n")
    
    # Verification Table
    print("Star    | Modern Dist | Future Dist (+50k)")
    print("-" * 40)
    for i in range(len(dipper_df)):
        name = dipper_df.iloc[i]['proper']
        curr = dipper_df.iloc[i]['dist']
        fut  = future_sky.iloc[i]['new_dist']
        print(f"{name:8} | {curr:11.2f} | {fut:11.2f}")