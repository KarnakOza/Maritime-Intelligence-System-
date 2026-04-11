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
