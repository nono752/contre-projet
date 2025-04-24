import pytest
from MapSystem.MapValidator import MapValidator
from MapSystem.MapLoader import MapLoader, MapData

loader = MapLoader()
validator = MapValidator()
valid_data = loader.load_from_file("tests/test_map_system/maps/valid.txt")

def test_check_required_keys() -> None: 
    invalid_data = loader.load_from_file("tests/test_map_system/maps/missing_key.txt")

    validator.validate(valid_data) # erreur si exception levée
    with pytest.raises(Exception):
        validator.validate(invalid_data) # ok si exception levée

def test_check_keys_type() -> None:
    invalid_data1 = loader.load_from_file("tests/test_map_system/maps/wrong_type1.txt")
    invalid_data2 = loader.load_from_file("tests/test_map_system/maps/wrong_type2.txt")

    validator.validate(valid_data)
    with pytest.raises(Exception):
        validator.validate(invalid_data1)

    with pytest.raises(Exception):
        validator.validate(invalid_data2)

def test_check_grid_dimension() -> None:
    # on suppose que les type et clés obligatoires sont déjà vérifiés
    invalid_data = loader.load_from_file("tests/test_map_system/maps/grid_line_too_long.txt")
    validator.validate(valid_data)
    with pytest.raises(Exception):
        validator.validate(invalid_data)