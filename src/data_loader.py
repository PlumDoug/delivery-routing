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

