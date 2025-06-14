from datetime import datetime, timedelta

def route_planner(package_data, distance_table, address_list, loaded_packages, time_start, time_end):
    current_location_index = 0
    current_time = time_start
    route = []
    total_distance = 0
    loaded_packages = loaded_packages.copy()

    while len(loaded_packages) > 0:
        next_closest_distance = float('inf')
        next_closest_index = None
        
        # Find the next closest package to deliver
        for id in loaded_packages:
            index = address_list.index(package_data.search(id)[1])
            distance = distance_table[current_location_index][index]
            if distance < next_closest_distance and distance > 0:
                next_closest_distance = distance
                next_closest_index = index

        # Exit without updating if the next delivery would be past the end time
        delivery_time = timedelta(hours=next_closest_distance / 18)
        current_time += delivery_time
        if current_time > time_end:
            break
        
        # Update the address, and total distance travelled
        next_address = address_list[next_closest_index]
        current_location_index = next_closest_index
        total_distance += next_closest_distance
        
        
        # Update the route with the next delivery and remove the package from the truck
        to_remove = []
        for id in loaded_packages:
            package = list(package_data.search(id))
            if package[1] == next_address:
                route.append((id, next_address, current_time, total_distance))
                package[6] = current_time 
                package_data.insert(tuple(package))
                to_remove.append(id)
        for id in to_remove:
            loaded_packages.remove(id)

    return route 

def return_to_hub(route, distance_table, address_list, end_time):
    # Add the return to hub logic to the end of the route
    last_location_index = address_list.index(route[-1][1])
    distance_to_hub = distance_table[last_location_index][0]
    total_distance = route[-1][3] + distance_to_hub
    delivery_time = timedelta(hours=distance_to_hub / 18)
    current_time = route[-1][2] + delivery_time
    if current_time > end_time:
        return route  # Do not return to hub if it exceeds the end time 
    route.append((0, address_list[0], current_time, total_distance))
    
    return route
