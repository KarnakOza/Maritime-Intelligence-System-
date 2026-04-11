## Methodology

1. SAR Preprocessing

-Sentinel-1 GRD data 
-calibration,
-orbit files, 
-thermal noise removal, 
-speckle filter, 
-Adaptive thresolding, 
-ocean object detection, 
-terrain correction.

2. Ship Detection 

-Bright target extraction 
-thresoldhing + filtering 
-False positive reduction

3. Shipping Lane Extraction 

-Spatial clustering (DBSCAN) 
-Density mapping
-Lane dominance analysis

4. Land Masking

-Geopandas + Natural Earth Dataset
-Eliminates coastal false detections

6. Economic Analysis

-Lagged correlation with oil prices
-Z-score anomaly detection

7. Maritime Risk Index

-Traffic congestion
-Lane density imbalance 
-Economic indicators

---
