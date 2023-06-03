import os
import time
import json
import math
from string import Template
from shapely.geometry import shape
import pyautogui

FOV = 55 # Approximation based on Google Earth Pro altitude figures
ratio = 16 / 9 # Most common display aspect ratio


def read_geojson(file_path: str):
    with open(file_path) as f:
        geojson_data = json.load(f)
    return geojson_data

def get_polygon(geojson):
    # TODO: validate data and throw error if invalid
    polygon_points = geojson['features'][0]['geometry']['coordinates'][0]
    return polygon_points

def get_polygon_stats(polygon):
    min_lng = min(point[0] for point in polygon)
    max_lng = max(point[0] for point in polygon)
    min_lat = min(point[1] for point in polygon)
    max_lat = max(point[1] for point in polygon)
    center_lng = (min_lng + max_lng) / 2
    center_lat = (min_lat + max_lat) / 2
    corners = [(min_lat, min_lng), (min_lat, max_lng), (max_lat, min_lng), (max_lat, max_lng)]
    return corners, (center_lat, center_lng)

# distance between two points in spherical coordinates
# TODO: test in multiple locations around the globe
def haversine(lat1, lon1, lat2, lon2):
    r = 6371  # radius of Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
    return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def estimate_altitude(corner_coords, center_coords):
    # get the maximum distance from the center to the corners of the bounding box
    distances = [
        haversine(center_coords[0], center_coords[1], lat, lng)
        for lat, lng in corner_coords
    ]
    max_distance = max(distances)

    altitude_km = max_distance / math.tan(math.radians(FOV / 2)) * ((1 + ratio ** 2) ** 0.5) / 2
    return altitude_km * 1000

def convert_geojson(geojson):
    return
    with open(output_file, "w") as f:
        f.write("Your GEPrint data")

def take_screenshot(geojson, name: str):
    pass

def run(geojson_path: str, run_name: str):
    os.makedirs("screenshots", exist_ok=True)

def write_geprint(center, altitude):
    with open('template.geprint') as template_file:
        values = {
            'latitude': center[0],
            'longitude': center[1],
            'altitude': altitude
        }
        geprint_template = Template(template_file.read())
        result_geprint = geprint_template.substitute(values)
        print(result_geprint)


if __name__ == '__main__':
    geojson = read_geojson('./paris.geojson')
    polygon_coords = get_polygon(geojson)
    polygon_corners, polygon_center = get_polygon_stats(polygon_coords)
    altitude = estimate_altitude(polygon_corners, polygon_center)
    write_geprint(polygon_center, altitude)
