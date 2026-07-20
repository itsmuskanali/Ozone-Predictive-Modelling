import os
import glob
import xarray as xr
import pandas as pd

# 1. Define your base path and the specific folders
base_path = '/Users/muskanali/Desktop/ISRO/OZONE/tco/'
instrument_folders = ['OMI', 'TOMS1', 'TOMS1_', 'TOMS_N7']

datasets = {}

# -------------------------------------------------------------
# STEP 2: Iterative Loading (Stays exactly the same)
# -------------------------------------------------------------
print("Starting to load datasets...")
for instrument in instrument_folders:
    pattern = os.path.join(base_path, instrument, '*.nc')
    files = sorted(glob.glob(pattern)) 
    
    if len(files) == 0:
        continue
        
    print(f"⏳ Loading {instrument} ({len(files)} files)...")
    
    try:
        ds = xr.open_mfdataset(files, combine='by_coords')
    except ValueError:
        ds = xr.open_mfdataset(files, combine='nested', concat_dim='time')
        
    datasets[instrument] = ds

print("\n✅ All available datasets loaded into memory!")
print("="*60)

# -------------------------------------------------------------
# STEP 3: Displaying the Raw Data
# -------------------------------------------------------------
for instrument, ds in datasets.items():
    if 'OMI' in instrument:
        ozone_var = 'OMDOAO3e_003_ColumnAmountO3'
        lat_coord = 'lat'
        lon_coord = 'lon'
    else:
        ozone_var = 'Ozone' 
        lat_coord = 'Latitude'
        lon_coord = 'Longitude'
        
    if ozone_var in ds.variables:
        print(f"\n📊 --- {instrument} SENSOR DATA ---")
        
        # 1. Isolate just the Ozone variable
        ozone_data = ds[ozone_var]
        
        # 2. Extract a single "slice" of time to display
        # Because the dataset is massive, we select the very first time index (time=0)
        # to view a snapshot of the Latitude/Longitude grid.
        single_day_data = ozone_data.isel(time=0)
        
        # 3. Convert that slice into a Pandas DataFrame for clean tabular viewing
        # We use .dropna() to remove coordinates where the satellite didn't collect data (e.g., over the poles)
        df = single_day_data.to_dataframe().dropna()
        
        # 4. Display the first 10 rows of the data table
        print(f"Total valid data points for this time step: {len(df)}")
        print("First 10 rows:")
        print(df.head(10))
        
        print("-" * 40)
    else:
        print(f"❌ Variable '{ozone_var}' not found in {instrument}.")