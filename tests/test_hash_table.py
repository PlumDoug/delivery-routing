from src.HashTable import HashTable

def test_hash_table_initialization():
    ht = HashTable(10)
    assert ht.size == 10
    assert len(ht.buckets) == 10
    for bucket in ht.buckets:
        assert isinstance(bucket, list)

def test_hash_table_insert_and_search():
    ht = HashTable(10)
    ht.insert((1, 'one'))
    ht.insert((2, 'two'))
    ht.insert((12, 'twelve'))  
    assert ht.search(1) == (1, 'one')
    assert ht.search(2) == (2, 'two')
    assert ht.search(12) == (12, 'twelve')
    assert ht.search(3) is None  
