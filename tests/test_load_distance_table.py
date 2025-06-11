from src.data_loader import load_distance_table

def test_load_distance_table():
    # Test loading a distance table from a CSV file
    distance_table, address_list, location_name = load_distance_table('data/distance_table.csv')
    
    # Check the structure of the distance table
    assert isinstance(distance_table, list)
    assert all(isinstance(row, list) for row in distance_table)
    
    # Check the length of the address list and location names
    assert len(address_list) == len(location_name) == len(distance_table)
    
    # Check that distances are correctly loaded
    for i in range(len(distance_table)):
        for j in range(len(distance_table[i])):
            if i != j:
                assert distance_table[i][j] == distance_table[j][i]  # Ensure symmetry