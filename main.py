# Author: Douglas Faehndrich, Student ID: 012315568

from src.data_loader import load_package_data, load_distance_table, load_trucks
from src.HashTable import HashTable 
from datetime import datetime, timedelta
from src.route_planner import route_planner, return_to_hub
from src.status_checkers import package_status, time_status

def main():
    print("Running Program...")
    # Load package data
    package_data_raw = load_package_data("data/package_data.csv")
    print(f"Loaded {len(package_data_raw)} package records from the CSV file.")

    package_data = []
    # Convert raw package data to a list of tuples with appropriate types
    # Each tuple contains: (id, address, city, zip, deadline string, weight, delivery time, 
    # earliest start time, deadline, delivery status, truck number, start time)
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
        package_data.append((row[0], row[1], row[2], row[4], row[5], row[6], None, earliest_start, deadline, "at hub", None, None))
   
    #region - debugging code
    #package_data_key = ["id", "address", "city", "zip", "deadline string", "weight", "delivery time", 
    # "earliest_start", "deadline", "delivery status", "truck number", "start time"]
    # print("Package data keys:")
    # for i in range(len(package_data_key)):
    #     print(f"{i}: {package_data_key[i]}")
    
    # print(f"Package data: {package_data[:5]}")  
    #endregion
    
    # Create a hash table and insert package data
    package_table = HashTable()
    for record in package_data:
        package_table.insert(record)
    print("Package data inserted into hash table.")

    # Load distance table from CSV - this will return a 2D list matrix of distances, a list of addresses, and a list of locations
    distance_table, address_list, location_list = load_distance_table("data/distance_table.csv")
    print (f"Loaded {len(distance_table)} distance records from the CSV file.")
    
    # region - debugging code
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
    # endregion
    
    # Load trucks manually from CSV file
    truck1, truck2, truck3 = load_trucks("data/truck_list.csv")
    print("Loaded truck data from the CSV file.")
    # print(f"Truck 1: {truck1}")
    # print(f"Truck 2: {truck2}")
    # print(f"Truck 3: {truck3}")

    # Set the start times for trucks 1 and 3
    start_time_truck1 = datetime.strptime("8:00 AM", "%I:%M %p")
    start_time_truck3 = datetime.strptime("9:05 AM", "%I:%M %p")
    end_of_day = datetime.strptime("5:00 PM", "%I:%M %p")

    # Run route planning algroithm for trucks 1 and 3
    route1 = route_planner(package_table, distance_table, address_list, truck1, start_time_truck1, end_of_day)
    route3 = route_planner(package_table, distance_table, address_list, truck3, start_time_truck3, end_of_day)

    # Determine the start time for truck 2 based on the last delivery time of trucks 1 and 3
    if route1[-1][2] < route3[-1][2]:
        route1 = return_to_hub(route1, distance_table, address_list, end_of_day)
        start_time_truck2 = route1[-1][2]
    else:
        route3 = return_to_hub(route3, distance_table, address_list, end_of_day)
        start_time_truck2 = route3[-1][2]
    
    # Run route planning algorithm for truck 2
    route2 = route_planner(package_table, distance_table, address_list, truck2, start_time_truck2, end_of_day)
    print("All routes planned successfully.")

    # Assign truck numbers and start times to packages
    for package_id in truck1:
        package = list(package_table.search(package_id))
        package[10] = 1
        package[11] = start_time_truck1
        package_table.insert(tuple(package))
    for package_id in truck2:
        package = list(package_table.search(package_id))
        package[10] = 2
        package[11] = start_time_truck2
        package_table.insert(tuple(package))
    for package_id in truck3:
        package = list(package_table.search(package_id))
        package[10] = 3
        package[11] = start_time_truck3
        package_table.insert(tuple(package))

    # Calculate and print total distance traveled by all trucks
    total_distance = route1[-1][3] + route2[-1][3] + route3[-1][3]
    print(f"Total distance traveled: {total_distance:.2f} miles")

    # Double check for late deliveries and early deliveries
    for i in range(1, 41):
        package = package_table.search(i)
        delivery_time = package[6]
        earliest_start = package[7]
        deadline = package[8]
        if deadline < delivery_time:
            print(f"Package {package[0]} was delivered late. Expected delivery time: {deadline.strftime('%I:%M %p')}, Actual delivery time: {delivery_time.strftime('%I:%M %p')}")
        if earliest_start > delivery_time:
            print(f"Package {package[0]} was delivered before the earliest start time. Expected delivery time: {earliest_start.strftime('%I:%M %p')}, Actual delivery time: {delivery_time.strftime('%I:%M %p')}")   

    # Give the user the option to check on a package or print the status of all packages
    while True:
        user_input = input("\nEnter 1 to check the status of a package by ID, 2 to print the status of all packages, or 0 to exit: ")
        if user_input == "1":
            package_status(package_table)
        elif user_input == "2":
            time_status(route1, route2, route3, start_time_truck1, start_time_truck2, start_time_truck3)
        elif user_input == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 0.")




if __name__ == "__main__":
    main()