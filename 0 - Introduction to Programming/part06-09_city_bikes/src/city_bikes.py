# Write your solution here
import math
from itertools import combinations
def get_station_data(filename):
    stations = {}
    with open(f"src/{filename}") as station:
    #with open(filename) as station:
        #document = [line.strip().split(";") for line in station]
        for line in station:
            line = line.strip().split(";")
            if line[0] == "Longitude":
                continue
            stations[line[3]] = (float(line[0]),float(line[1]))
    return stations

def distance(stations: dict, station1: str, station2: str):
    for name_station, values in stations.items():
        if name_station == station1:
            longitude1 = float(values[0])
            latitude1 = float(values[1])
        if name_station == station2:
            longitude2 = float(values[0])
            latitude2 = float(values[1])

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station1, station2 = "", ""

    for s1, s2 in combinations(stations.keys(), 2):
        dist = distance(stations, s1, s2)
        if dist > max_distance:
            max_distance = dist
            station1, station2 = s1, s2

    return station1, station2, max_distance

if __name__ == "__main__":
    #(longitud y latitud)
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
        