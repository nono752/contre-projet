import pytest
from MapSystem.MapValidator import MapValidator
from MapSystem.MapLoader import MapLoader, MapData

def test_validate() -> None:
    loader = MapLoader()
    validator = MapValidator()

    # test cas valides
    valid1 = loader.load_from_file("tests/test_map_system/maps/valid1.yaml")
    valid2 = loader.load_from_file("tests/test_map_system/maps/valid2.yaml")
    validator.validate(valid1)
    validator.validate(valid2)

    # test les clés obligatoires
    missing_key = loader.load_from_file("tests/test_map_system/maps/missing_key.yaml")
    with pytest.raises(Exception):
        validator.validate(missing_key) # ok si exception levée
    
    # test les types des clés
    wrong_type1 = loader.load_from_file("tests/test_map_system/maps/wrong_type1.yaml")
    wrong_type2 = loader.load_from_file("tests/test_map_system/maps/wrong_type2.yaml")
    with pytest.raises(Exception):
        validator.validate(wrong_type1)
    with pytest.raises(Exception):
        validator.validate(wrong_type2)

    # test les dimensions
    # on suppose que les type et clés obligatoires sont déjà vérifiés
    grid_line_too_long = loader.load_from_file("tests/test_map_system/maps/grid_line_too_long.yaml")
    grid_height_too_long = loader.load_from_file("tests/test_map_system/maps/grid_height_too_long.yaml")
    with pytest.raises(Exception):
        validator.validate(grid_line_too_long)
    with pytest.raises(Exception):
        validator.validate(grid_height_too_long)
    
    # test starts et exits
    too_much_start = loader.load_from_file("tests/test_map_system/maps/too_much_start.yaml")
    exit_but_no_next = loader.load_from_file("tests/test_map_system/maps/exit_but_no_next.yaml")
    with pytest.raises(Exception):
        validator.validate(too_much_start)
    with pytest.raises(Exception):
        validator.validate(exit_but_no_next)
    
