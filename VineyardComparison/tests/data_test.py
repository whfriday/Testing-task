
import pandas
from src.enums.global_enums import GlobalErrorMessages
from data_analysis import queried_df, calculate_soil_mean, comparison, make_queried_json


def test_queried_df():
    sand_profile = {"b0": 1, "b10": 2, "b30": 3, "b60": 4, "b100": 5, "b200": 6}
    clay_profile = {"b0": 7, "b10": 8, "b30": 9, "b60": 10, "b100": 11, "b200": 12}
    orgc_profile = {"b0": 13, "b10": 14, "b30": 15, "b60": 16, "b100": 17, "b200": 18}

    result = queried_df(sand_profile, clay_profile, orgc_profile)
    expected_result = pandas.DataFrame(
        data={"Sand": [1, 2, 3, 4, 5, 6], "Clay": [7, 8, 9, 10, 11, 12], "Organic Matter": [13, 14, 15, 16, 17, 18]},
        index=["Surface", "10cm", "20cm", "60cm", "100cm", "200cm"])

    pandas.testing.assert_frame_equal(result, expected_result), GlobalErrorMessages.WRONG_QUARIFED_RESULT.value


def test_calculate_soil_mean():
    dataframe = pandas.DataFrame(data={"Sand": [10, 20, 30], "Clay": [40, 50, 60], "Organic Matter": [70, 80, 90]},
                                 index=["Surface", "10cm", "20cm"])
    result = calculate_soil_mean(dataframe)
    expected_result = pandas.DataFrame(data={"Mean": [20.0, 50.0, 80.0, -50.0]},
                                       index=["Sand", "Clay", "Organic Matter", "Other"])

    pandas.testing.assert_frame_equal(result, expected_result), GlobalErrorMessages.WRONG_SOIL_RESULT.value


def test_comparison():
    queried_profile = {
        "mean_elevation": 100,
        "mean_temp": 20,
        "mean_soil_content_%": {"Clay": 30, "Sand": 40, "Organic Matter": 10, "Other": 20},
        "avg_diurnal_range": 5
    }

    profiles = [
        {"mean_elevation": 110, "mean_temp": 21,
         "mean_soil_content_%": {"Clay": 32, "Sand": 42, "Organic Matter": 12, "Other": 18}, "avg_diurnal_range": 6},
        {"mean_elevation": 90, "mean_temp": 19,
         "mean_soil_content_%": {"Clay": 28, "Sand": 38, "Organic Matter": 8, "Other": 26}, "avg_diurnal_range": 4}
    ]

    closest_profile, list_of_dicts = comparison(queried_profile, profiles)

    assert closest_profile == profiles[0]["region"]
    assert list_of_dicts == [
        {"region": profiles[0]["region"], "score": 7.2},
        {"region": profiles[1]["region"], "score": 14.4}
    ], GlobalErrorMessages.WRONG_COMPARISON_RESULT.value


def test_make_queried_json():
    soil_df = pandas.DataFrame(data={"Sand": [10], "Clay": [20], "Organic Matter": [30], "Other": [40]}, index=["Mean"])
    elevation = 100
    lat = 40.0
    long = -75.0

    result = make_queried_json(soil_df, elevation, lat, long)

    expected_result = {
        "mean_elevation": 100,
        "mean_temp": 20.0,  # You need to mock the get_location_temp function for accurate testing
        "mean_soil_content_%": {"Clay": 20.0, "Organic Matter": 30.0, "Other": 40.0, "Sand": 10.0},
        "avg_diurnal_range": 5
    }

    assert result == expected_result, GlobalErrorMessages.WRONG_JSON_RESULT.value
