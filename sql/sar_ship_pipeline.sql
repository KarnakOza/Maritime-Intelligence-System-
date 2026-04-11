-- Create table
CREATE TABLE ship_detection (
  id serial PRIMARY KEY,
  scene TEXT,
  lat DOUBLE PRECISION,
  lon DOUBLE PRECISION
);

-- ADD GEOMETRY COLUMN
ALTER TABLE ship_detections
ADD COLUMN geom GEOMETRY(POINT, 4326);

-- Convert lat/lon to geometry
UPDATE ship_detections
SET geom = ST_SetSRID(ST_MakePoint(lon, lat), 4326);

-- Count ships
SELECT COUNT(*) FROM ship_detections;

-- ships per scene
-- Ships per scene
SELECT scene, COUNT(*) 
FROM ship_detections
GROUP BY scene
ORDER BY COUNT(*) DESC;

-- Spatial query example
SELECT COUNT(*)
FROM ship_detections
WHERE ST_Intersects(
    geom,
    ST_MakeEnvelope(56.2, 27.1, 56.5, 27.3, 4326)
);

-- Density analysis
SELECT ST_SnapToGrid(geom, 0.02), COUNT(*) 
FROM ship_detections 
GROUP BY 1
ORDER BY COUNT(*) DESC;
