from datetime import datetime, timedelta

def route_planner(package_data, distance_table, address_list, loaded_packages, time_start):
    current_location_index = 0
    current_time = time_start
    route = []
    total_distance = 0
    loaded_packages = loaded_packages.copy()

    while len(loaded_packages) > 0:
        next_closest_distance = float('inf')
        next_closest_index = None
        for id in loaded_packages:
            index = address_list.index(package_data.search(id)[1])
            distance = distance_table[current_location_index][index]
            if distance < next_closest_distance and distance > 0:
                next_closest_distance = distance
                next_closest_index = index

        next_address = address_list[next_closest_index]
        current_location_index = next_closest_index
        total_distance += next_closest_distance
        delivery_time = timedelta(hours=next_closest_distance / 18)
        current_time += delivery_time

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
        
    # Return to hub
    distance_to_hub = distance_table[current_location_index][0]
    total_distance += distance_to_hub
    delivery_time = timedelta(hours=distance_to_hub / 18)
    current_time += delivery_time
    route.append((0, address_list[0], current_time, total_distance))

    return route 


