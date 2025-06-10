import src.data_loader

print("Available in data_loader:", dir(src.data_loader))

def test_load_package_data():
    # Load the package data from the CSV file
    package_data = src.data_loader.load_package_data('data/package_data.csv')
    
    # Check if the data is loaded correctly
    assert len(package_data) > 0, "Package data should not be empty"
    
    # Check if the first row has the expected number of columns
    assert len(package_data[0]) == 8, "Each package should have 8 attributes"

    # Check if the first row is a tuple
    assert isinstance(package_data[0], tuple), "Each package should be represented as a tuple"