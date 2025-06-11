from src.data_loader import load_package_data, load_distance_table
from src.HashTable import HashTable 

def main():
    print("Running Program...")
    
    package_data = load_package_data("data/package_data.csv")
    package_table = HashTable()
    print(f"Loaded {len(package_data)} package records from the CSV file.")
    # print(type(package_data[0][0]))
    # print(f"Package data: {package_data[:5]}")  # Display first 5 records for verification

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


if __name__ == "__main__":
    main()