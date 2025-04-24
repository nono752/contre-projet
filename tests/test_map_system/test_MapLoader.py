from MapSystem.MapLoader import MapLoader, MapData

loader = MapLoader()

def test_load_from_file() -> None:
    valid_path1 = "tests/test_map_system/maps/valid.txt"
    valid_path2 = "tests/test_map_system/maps/separator_in_map.txt"

    data = loader.load_from_file(valid_path1)
    assert len(data.grid) == 6
    assert data.grid[0] == "*    -  -"
    assert data.grid[3] == "    ---        -"
    assert data.grid[-1] == "======£££££========="
    assert data.keys["height"] == "6"
    assert data.keys["width"] == "20"

    data2 = loader.load_from_file(valid_path2)
    assert len(data2.grid) == 6
    assert data2.grid[1] == "---"

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
     




    
