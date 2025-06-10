from src.data_loader import load_package_data
from src.HashTable import HashTable 

def main():
    print("Running Program...")
    
    package_data = load_package_data("data/package_data.csv")
    package_table = HashTable()
    print(f"Loaded {len(package_data)} package records from the CSV file.")
    #print(type(package_data[0][0]))

    for record in package_data:
        package_table.insert(record)
    print("Package data inserted into hash table.")
   
    
if __name__ == "__main__":
    main()