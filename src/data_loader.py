import csv

def load_package_data(file_path):
    package_data = []
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            package_data.append(tuple(row))
    return package_data

