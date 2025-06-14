from datetime import datetime

# Prints the status of a specific package at a given time
def package_status(package_table):
    while True:
        try:
            # Prompt the user for a package ID
            package_id = int(input("Enter a package ID to check its status (1-40) or 0 to exit: "))
            if package_id == 0:
                print("Exiting program.")
                break
            if 1 <= package_id <= 40:
                package = package_table.search(package_id) # Pulls package data from the hash table
                try:
                    # Prompt the user for a time to check the package status
                    input_time = input("Enter a time to check the package status (format: HH:MM AM/PM, e.g., 10:00 AM): ")
                    input_time = datetime.strptime(input_time, "%I:%M %p")
                except ValueError:
                    print("Invalid time format. Please enter the time in the format HH:MM AM/PM.")
                    continue
                if input_time < package[11]: #if the input time is before the start time of the truck
                    status = "at hub"
                    print(f"Package {package[0]} is at the hub and will be delivered at {package[6].strftime('%I:%M %p')}.")
                elif input_time < package[6]: #if the input time is before the delivery time
                    status = "en route"
                    print(f"Package {package[0]} is en route and will be delivered at {package[6].strftime('%I:%M %p')}.")
                else:
                    status = "delivered"
                    print(f"Package {package[0]} was delivered at {package[6].strftime('%I:%M %p')}.")
                
            else:
                print("Invalid package ID. Please enter a number between 1 and 40.")
        except ValueError:
            print("Invalid input. Please enter a valid package ID.")

#print the status of all packages at a given time
def time_status(route1, route2, route3, start_time_truck1, start_time_truck2, start_time_truck3):
    # Prompt the user for a time to check the status of all packages
    package_time = input("Enter a time to check the status of all packages (format: HH:MM AM/PM, e.g., 10:00 AM): ")
    try:
        input_time = datetime.strptime(package_time, "%I:%M %p")
    except ValueError:
        print("Invalid time format. Please enter the time in the format HH:MM AM/PM.")
        return
    truck1_distance = 0
    truck2_distance = 0
    truck3_distance = 0
    # Print each package's status based on the input time
    print(f"\nTruck 1:")
    for delivery in route1:
        if delivery[0] == 0: #if the package is at the hub
            truck1_distance = delivery[3] #add the distance travelled to the hub to the total distance
            print(f"Truck 1 returned to hub at {delivery[2].strftime('%I:%M %p')}")
        elif input_time <= start_time_truck1: #if the input time is before the start time of truck 1
            print(f"{delivery[0]}: at hub)")
        elif delivery[2] <= input_time: #if the input time is after the delivery time
            truck1_distance = delivery[3] #add the distance travelled to the total distance
            print(f"{delivery[0]}: delivered at {delivery[2].strftime('%I:%M %p')}")
        else: #if the input time is between the start time and delivery time
            print(f"{delivery[0]}: en route")
    print(f"\nTruck 2:")
    for delivery in route2:
        if input_time <= start_time_truck2:
            print(f"{delivery[0]}: at hub")
        elif delivery[2] <= input_time:
            truck2_distance = delivery[3]
            print(f"{delivery[0]}: delivered at {delivery[2].strftime('%I:%M %p')}")
        else:
            print(f"{delivery[0]}: en route")
    print(f"\nTruck 3:")
    for delivery in route3:
        if input_time <= start_time_truck3:
            print(f"{delivery[0]}: at hub")
        elif delivery[2] <= input_time:
            truck3_distance = delivery[3]
            print(f"{delivery[0]}: delivered at {delivery[2].strftime('%I:%M %p')}")
        else:
            print(f"{delivery[0]}: en route")
    # Calculate and print the total distance traveled by all trucks at the input time
    total_distance = truck1_distance + truck2_distance + truck3_distance
    print(f"\nTotal distance traveled by all trucks at {input_time.strftime('%I:%M %p')}: {total_distance:.2f} miles\n")