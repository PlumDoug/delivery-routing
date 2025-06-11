import csv

def load_package_data(file_path):
    package_data = []
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            row[0] = int(row[0])  # Convert the first element (ID) to an integer
            package_data.append(tuple(row))
    return package_data

def load_distance_table(file_path):
    distance_table = [] #2D list to store distances
    address_list = [] #List to store addresses. The index of the address in this list will be used to access the distance table.
    location_name = [] #List to store the names of the locations. 
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        for row in reader:
            location_name.append(row[0].strip()) # Add the first column (location name) to the location name list
            address_list.append(row[1].strip())  # Add the second column (address) to the address list
            distance_row = [] # Create a new list for the distances
            for column in row[2:]:  # Start from the third column to get the distances
                if column == '':
                    distance_row.append(0.0)
                else:
                    distance_row.append(float(column))
            distance_table.append(distance_row)
        for i in range(len(distance_table)):
            for j in range(len(distance_table[i])):
                if distance_table[i][j] == 0.0 and i != j:
                    distance_table[i][j] = float(distance_table[j][i])  # Ensure symmetry in the distance table
    return distance_table, address_list, location_name

def load_trucks(file_path):
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        truck1 = next(reader)[1:]
        truck2 = next(reader)[1:]
        truck3 = next(reader)[1:]
        # Convert the truck data to integers
        for i in range(len(truck1)):
            truck1[i] = int(truck1[i])
        for i in range(len(truck2)):
            truck2[i] = int(truck2[i])
        for i in range(len(truck3)):
            truck3[i] = int(truck3[i])
    return truck1, truck2, truck3