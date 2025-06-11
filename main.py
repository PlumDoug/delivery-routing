from src.data_loader import load_package_data, load_distance_table, load_trucks
from src.HashTable import HashTable 
from datetime import datetime, timedelta
from src.route_planner import route_planner

def main():
    print("Running Program...")
    
    package_data_raw = load_package_data("data/package_data.csv")
    package_data = []
    for row in package_data_raw:
        if row[5] == "EOD":
            deadline = datetime.strptime("11:59 PM", "%I:%M %p")
        else:
            deadline =  datetime.strptime(row[5], "%I:%M %p")
        if "Delayed" in row[7]:
            earliest_start = datetime.strptime("9:05 AM", "%I:%M %p")
        elif "Wrong" in row[7]:
            earliest_start = datetime.strptime("10:20 AM", "%I:%M %p")
        else:
            earliest_start = datetime.strptime("8:00 AM", "%I:%M %p")
        package_data.append((row[0], row[1], row[2], row[4], row[5], row[6], None, earliest_start, deadline, ))
    
    package_data_key = ["id", "address", "city", "zip", "deadline string", "weight", "delivery time", "earliest_start", "deadline"]
    print("Package data keys:")
    for i in range(len(package_data_key)):
        print(f"{i}: {package_data_key[i]}")
    print(f"Loaded {len(package_data)} package records from the CSV file.")
    print(f"Package data: {package_data[:5]}")  
    
    package_table = HashTable()
    for record in package_data:
        package_table.insert(record)
    print("Package data inserted into hash table.")

    distance_table, address_list, location_list = load_distance_table("data/distance_table.csv")
    print (f"Loaded {len(distance_table)} distance records from the CSV file.")
    # print (f"Address list: {address_list}")
    # print (f"Location list: {location_list}")
    # print (f"Distance table: {distance_table}")

    # count = 0
    # for row in package_data:
    #     found = False
        
    #     for address in address_list:
    #         if row[1] == address:
    #             print(address)
    #             found = True
    #             count += 1
    #     if found == False:
    #         print(f"Address {row[1]} not found in address list.")
    # print(count)

    #Load trucks
    truck1, truck2, truck3 = load_trucks("data/truck_list.csv")
    print("Loaded truck data from the CSV file.")
    print(f"Truck 1: {truck1}")
    print(f"Truck 2: {truck2}")
    print(f"Truck 3: {truck3}")
    start_time_truck1 = datetime.strptime("8:00 AM", "%I:%M %p")
    start_time_truck3 = datetime.strptime("9:05 AM", "%I:%M %p")
    route1 = route_planner(package_table, distance_table, address_list, truck1, start_time_truck1)
    print(f"Route 1: {route1}")
    route3 = route_planner(package_table, distance_table, address_list, truck3, start_time_truck3)
    print(f"Route 3: {route3}")
    if route1[-1][2] < route3[-1][2]:
        start_time_truck2 = route1[-1][2]
    else:
        start_time_truck2 = route3[-1][2]
    route2 = route_planner(package_table, distance_table, address_list, truck2, start_time_truck2)
    print(f"Route 2: {route2}")
    total_distance = route1[-1][3] + route2[-1][3] + route3[-1][3]
    print(f"Total distance traveled: {total_distance} miles")
    print("All routes planned successfully.")

    

if __name__ == "__main__":
    main()