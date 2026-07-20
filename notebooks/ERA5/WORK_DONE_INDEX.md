# Ozone Work Done Index

This file organizes the ozone analysis files we have worked on so far.

## 1. Original / Existing Local Datasets

These were already present and are the base local datasets.

| File / Folder | Purpose | Notes |
|---|---|---|
| `OZONE/tco/TOMS_N7/` | NASA TOMS Nimbus-7 daily NetCDF files | Total column ozone, local coverage includes 1978-1993. |
| `OZONE/tco/TOMS1/` | NASA TOMS Earth Probe daily NetCDF files | Total column ozone, local coverage includes 1996-2003. |
| `OZONE/tco/TOMS1_/` | NASA TOMS Earth Probe daily NetCDF files | Total column ozone, local coverage includes 2004-2005. |
| `OZONE/tco/OMI/` | NASA OMI daily NetCDF files | Total column ozone, local coverage includes 2004-2020. |
| `OZONE/TOMS_N7_data.csv` | Extracted spatial table | No date column; useful for spatial snapshots only. |
| `OZONE/TOMS1_data.csv` | Extracted spatial table | No date column; useful for spatial snapshots only. |
| `OZONE/TOMS1__data.csv` | Extracted spatial table | No date column; useful for spatial snapshots only. |
| `OZONE/OMI_data.csv` | Extracted spatial table | No date column; useful for spatial snapshots only. |

## 2. Period Trend Analysis

Question handled:

- Period 1: 1979-1987
- Period 2: 1988-2000
- Period 3: 2001-2010
- Period 4: 2011-2020
- Period 5: 2021-present
- Was depletion faster before 1987?
- Is recovery visible afterward?

| File | Purpose |
|---|---|
| `OZONE/period_trend_analysis.py` | Script that creates annual gridded means and trend maps by period. |
| `OZONE/period_trend_outputs/summary_answers.md` | Main written answer for the period trend question. |
| `OZONE/period_trend_outputs/period_trend_summary.csv` | Numeric trend summary for all periods. |
| `OZONE/period_trend_outputs/period_1_trend_map.png` | Trend map for 1979-1987. |
| `OZONE/period_trend_outputs/period_2_trend_map.png` | Trend map for 1988-2000. |
| `OZONE/period_trend_outputs/period_3_trend_map.png` | Trend map for 2001-2010. |
| `OZONE/period_trend_outputs/period_4_trend_map.png` | Trend map for 2011-2020. |
| `OZONE/period_trend_outputs/period_5_trend_map.png` | Placeholder map noting 2021-present data is not local. |
| `OZONE/period_trend_outputs/period_1_trend_report.txt` to `period_5_trend_report.txt` | Separate trend reports for each period. |
| `OZONE/period_trend_outputs/selected_input_files.csv` | Log of the files used for the trend analysis. |

Key result:

- Depletion was faster before 1987: Period 1 slope was about `-2.0372 DU/year`.
- Recovery becomes visible in 2011-2020: Period 4 slope was about `+0.6892 DU/year`.
- Local files do not include 2021-present gridded ozone data.

## 3. Global Ozone Map / 1979-Present Setup

Question handled:

- Download/load global ozone data.
- Plot global ozone maps.
- Verify dates.
- Use local TOMS/OMI where present.

| File | Purpose |
|---|---|
| `OZONE/global_ozone_map.py` | Script that builds the global long-record mean map from local TOMS/OMI files and checks NASA OMI availability metadata. |
| `OZONE/global_ozone_outputs/global_ozone_map_1979_present.png` | Global ozone mean map from local files. Actual local numeric coverage is through 2020. |
| `OZONE/global_ozone_outputs/global_ozone_map_report.md` | Report explaining local coverage and latest NASA OMI metadata. |
| `OZONE/global_ozone_outputs/annual_global_ozone_means.csv` | Annual global mean ozone values from local data. |
| `OZONE/global_ozone_outputs/local_files_used.csv` | List of local files used. |
| `OZONE/global_ozone_outputs/omi_2021_present_monthly_sample_manifest.csv` | Manifest for monthly-sample OMI 2021-present downloads. |
| `OZONE/global_ozone_outputs/download_omi_2021_present_monthly_sample.sh` | Download helper script for OMI 2021-present monthly samples. |

Important status:

- Local data used in the map: `1979-01-01` to `2020-07-31`.
- NASA CMR showed OMI available through `2026-06-14` during verification.
- 2021-present files are not downloaded locally yet.

## 4. Ozone Transport, Resolution, And Validation

Question handled:

- Explain ozone transport using Brewer-Dobson Circulation.
- Document spatial and temporal resolution.
- Validate results using local datasets.

| File | Purpose |
|---|---|
| `OZONE/global_ozone_requirements.md` | Broad global methodology note: transport, resolution, validation, and date status. |
| `OZONE/local_three_requirements.py` | Local-only script using existing `TOMS_N7`, `TOMS1`, `TOMS1_`, and `OMI`. |
| `OZONE/local_three_requirements_outputs/three_requirements_existing_ozone_datasets.md` | Main local-only write-up for the three requirements. |
| `OZONE/local_three_requirements_outputs/local_dataset_resolution_coverage.csv` | Resolution and date coverage table computed from local files. |
| `OZONE/local_three_requirements_outputs/brewer_dobson_transport_diagram.png` | Brewer-Dobson Circulation diagram. |
| `OZONE/global_ozone_outputs/ozone_transport_brewer_dobson_diagram.png` | Earlier copy of Brewer-Dobson diagram. |

Local resolution summary:

| Dataset | Spatial Resolution | Temporal Resolution | Local Date Coverage |
|---|---|---|---|
| TOMS_N7 | 1.00 deg lat x 1.25 deg lon | Daily | 1978-11-01 to 1993-05-06 |
| TOMS1 | 1.00 deg lat x 1.25 deg lon | Daily | 1996-07-22 to 2003-12-31 |
| TOMS1_ | 1.00 deg lat x 1.25 deg lon | Daily | 2004-01-01 to 2005-12-14 |
| OMI | 0.25 deg lat x 0.25 deg lon | Daily | 2004-10-01 to 2020-07-31 |

## 5. Validation

Validation done:

- Same-day overlap between local EP-TOMS and OMI.
- This checks continuity across satellite sensors.

| File | Purpose |
|---|---|
| `OZONE/validate_ozone_overlap.py` | Script that compares EP-TOMS vs OMI during overlap. |
| `OZONE/global_ozone_outputs/validation_report.md` | Main validation report. |
| `OZONE/global_ozone_outputs/validation_omi_toms_overlap.csv` | Same-day comparison values. |
| `OZONE/global_ozone_outputs/validation_omi_toms_overlap.png` | Scatter plot validation figure. |

Validation result:

- Overlap days: `431`
- Date range: `2004-10-01` to `2005-12-14`
- Correlation: `0.933`
- Mean bias, OMI minus TOMS: `-2.516 DU`
- Mean absolute difference: `3.336 DU`
- RMSE: `5.252 DU`

## 6. Stratosphere vs Troposphere Layer Trend Setup

Question handled:

- Sir wants region averages for:
  - Antarctic
  - Arctic
  - Tropics
  - Mid-Latitudes
  - Global
- Separately for:
  - Stratosphere
  - Troposphere
- Using:
  - ERA5
  - Aura MLS
  - MERRA-2

Current status:

- No local ERA5, Aura MLS, or MERRA-2 pressure-level/profile files were found.
- Existing local TOMS/OMI files are total-column ozone only.
- Therefore, TOMS/OMI cannot honestly separate stratospheric and tropospheric ozone.

| File / Folder | Purpose |
|---|---|
| `OZONE/layer_ozone_trends.py` | Ready-to-run script for ERA5 / Aura MLS / MERRA-2 layer averages and trend plots. |
| `OZONE/layer_ozone_data/ERA5/` | Put ERA5 ozone pressure-level files here. |
| `OZONE/layer_ozone_data/Aura_MLS/` | Put Aura MLS ozone profile or gridded files here. |
| `OZONE/layer_ozone_data/MERRA2/` | Put MERRA-2 ozone files here. |
| `OZONE/layer_ozone_outputs/layer_ozone_trend_report.md` | Current report saying layer data are missing. |
| `OZONE/layer_ozone_outputs/dataset_scan_status.csv` | Scan showing no files found for ERA5 / MLS / MERRA-2. |
| `OZONE/layer_ozone_outputs/requested_region_layer_average_template.csv` | Requested table template with regions and layers. |

Layer definitions prepared in the script:

- Troposphere: `300-1000 hPa`
- Stratosphere: `1-100 hPa`

Regions prepared in the script:

- Antarctic: `90S-60S`
- Arctic: `60N-90N`
- Tropics: `23.5S-23.5N`
- Mid-Latitudes: `23.5-60 degrees` in both hemispheres
- Global: `90S-90N`

## 7. Older / Existing Code We Inspected

These were already in the project and helped us understand the earlier workflow.

| File | Notes |
|---|---|
| `OZONE/ozone.py` | Earlier Excel/monthly ozone time-series script. |
| `OZONE/ozone_explanation.md` | Existing explanatory note. |
| `OZONE/tco/read_nc.py` | Earlier NetCDF reader. |
| `OZONE/tco/read_nc2.py` | Earlier extraction script that created CSV spatial snapshots. |
| `OZONE/tco/read_nc3.py` | Earlier yearly/monthly/seasonal graph script. |
| `OZONE/tco/tco/O3_execute.py` | Older TCO execution script with India/Global options, hardcoded Windows paths. |
| `OZONE/tco/tco/O3_execute2.py` | Similar older TCO script. |
| `OZONE/tco/tco/O3_TCO_functions.py` | Older helper functions for TCO processing. |

## 8. How To Rerun Current Work

From project root:

```bash
.venv/bin/python OZONE/period_trend_analysis.py
.venv/bin/python OZONE/global_ozone_map.py
.venv/bin/python OZONE/validate_ozone_overlap.py
.venv/bin/python OZONE/local_three_requirements.py
.venv/bin/python OZONE/layer_ozone_trends.py
```

Expected note:

- `layer_ozone_trends.py` will only compute real stratosphere/troposphere values after ERA5, Aura MLS, or MERRA-2 files are added under `OZONE/layer_ozone_data/`.

