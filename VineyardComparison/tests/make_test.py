from make_profile import get_mean_elevation, profile_mean_soil_content
from src.enums.global_enums import GlobalErrorMessages


def test_get_mean_elevation():
    bounding_geometry = [[-180, -90], [180, -90], [180, 90], [-180, 90], [-180, -90]]
    result = get_mean_elevation(bounding_geometry)
    # Replace expected_value на ожидаемое значение
    expected_value = 0
    assert result == expected_value, GlobalErrorMessages.WRONG_ELEVATION.value


def test_profile_mean_soil_content():
    queried_polygon = [[-180, -90], [180, -90], [180, 90], [-180, 90], [-180, -90]]
    result = profile_mean_soil_content(queried_polygon)
    # Replace expected_value на ожидаемое значение
    expected_value = {"Sand": 0, "Clay": 0, "Organic Matter": 0, "Other": 0}
    assert result == expected_value, GlobalErrorMessages.WRONG_SOIL.value
