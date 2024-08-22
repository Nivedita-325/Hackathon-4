import geopy.distance
from datetime import datetime

# Example charging station data
def get_charging_stations():
    stations = [
        {"id": 1, "name": "Station A", "location": (37.7749, -122.4194), "connector_type": "Type 2", "speed": 50, "slots": [True, True, False]},
        {"id": 2, "name": "Station B", "location": (37.8044, -122.2711), "connector_type": "Type 2", "speed": 150, "slots": [False, False, False]},
        {"id": 3, "name": "Station C", "location": (37.7749, -122.5144), "connector_type": "Type 1", "speed": 20, "slots": [True, False, True]},
    ]
    return stations

# Calculate the distance between two geographical points
def calculate_distance(point1, point2):
    return geopy.distance.distance(point1, point2).km

# Find optimal charging stations along the route
def find_optimal_stations(route, max_distance=20):
    stations = get_charging_stations()
    optimal_stations = []

    for station in stations:
        # Calculate distance of station from the route's last point
        station_distance = calculate_distance(route[-1], station["location"])
        if station_distance < max_distance:
            optimal_stations.append(station)

    return optimal_stations

# Check availability of slots in a station
def check_slot_availability(station):
    return any(slot for slot in station["slots"])

# Book a charging slot
def book_slot(station_id):
    stations = get_charging_stations()
    for station in stations:
        if station["id"] == station_id:
            for i in range(len(station["slots"])):
                if station["slots"][i]:
                    station["slots"][i] = False  # Mark slot as booked
                    print(f"Slot booked at {station['name']} at {datetime.now()}")
                    return True
    print("No available slots.")
    return False

# Example usage
current_route = [(37.7749, -122.4194), (37.8044, -122.2711)]  # Start and end points

# Step 1: Find nearby charging stations
optimal_stations = find_optimal_stations(current_route)

# Step 2: Display available stations and check for available slots
if optimal_stations:
    print("Available Charging Stations:")
    for station in optimal_stations:
        if check_slot_availability(station):
            print(f"{station['name']} - Location: {station['location']} - Speed: {station['speed']} kW - Slots available")
        else:
            print(f"{station['name']} - Location: {station['location']} - Speed: {station['speed']} kW - No slots available")

    # Step 3: Book a slot at a chosen station (e.g., Station A with id=1)
    station_id_to_book = 1  # Example of choosing Station A
    book_slot(station_id_to_book)
else:
    print("No suitable charging stations found.")
