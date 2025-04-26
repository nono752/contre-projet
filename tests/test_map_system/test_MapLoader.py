from MapSystem.MapLoader import MapLoader, MapData

loader = MapLoader()

def test_load_from_file() -> None:
    valid1 = "tests/test_map_system/maps/valid1.txt"
    separator_in_map = "tests/test_map_system/maps/separator_in_map.txt"
    valid2 = "tests/test_map_system/maps/valid2.txt"

    data = loader.load_from_file(valid1)
    assert len(data.grid) == 6
    assert data.grid[0] == "*    -  -"
    assert data.grid[3] == "    ---        -"
    assert data.grid[-1] == "======£££££========="
    assert data.keys["height"] == "6"
    assert data.keys["width"] == "20"

    data2 = loader.load_from_file(separator_in_map)
    assert len(data2.grid) == 6
    assert data2.grid[1] == "---" # ok mais dans la carte le separateur doit être suivi d'au moins un espace

    data3 = loader.load_from_file(valid2)
    assert len(data3.grid) == 8

def test_find_keys() -> None:
    section = '''\
        key1: 123
        key_2: stringvalue
             key3      :      0

        a random line

        key 4: not_valid
        key_5:
    '''
    
    res = loader.find_keys(section)
    assert len(res) == 3
    assert res["key1"] == "123"
    assert res["key3"] == "0"
    assert res.get("key_5") == None
     




    
