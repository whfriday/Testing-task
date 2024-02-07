import pytest

from src.enums.global_enums import GlobalErrorMessages
from unittest.mock import patch, Mock
from cloud import get_data, local_profile

# Mocking secrets and EE initialization
@pytest.fixture
def mock_st_secrets():
    with patch("streamlit.secrets") as secrets:
        secrets.__getitem__.side_effect = lambda key: {
            "ee_email": "service_account",
            "ee_key": "service_key"
        }[key]
        yield secrets


def test_get_data():
    # Test for sand parameter
    sand_data = get_data("sand")
    assert sand_data.getInfo() == "Your Expected Sand Data", GlobalErrorMessages.WRONG_SAND_PARAMETER.value

    # Test for clay parameter
    clay_data = get_data("clay")
    assert clay_data.getInfo() == "Your Expected Clay Data", GlobalErrorMessages.WRONG_CLAY_PARAMETER.value

    # Test for orgc parameter
    orgc_data = get_data("orgc")
    assert orgc_data.getInfo() == "Your Expected Organic Carbon Data", GlobalErrorMessages.WRONG_ORGC_PARAMETER.value

    # Test for elev parameter
    elev_data = get_data("elev")
    assert elev_data.getInfo() == "Your Expected Organic Carbon Data", GlobalErrorMessages.WRONG_ELEV_PARAMETER.value

    # Test for diurnal parameter
    diurnal_data = get_data("diurnal")
    assert diurnal_data.getInfo() == "Your Expected Organic Carbon Data", GlobalErrorMessages.WRONG_DIURNAL_PARAMETER.value

    # Test for invalid parameter
    with pytest.raises(Exception):
        get_data("invalid_param")


def test_local_profile():
    # Mock the dataset for local_profile function
    mock_dataset = Mock()
    mock_dataset.sample.return_value = {
        "features": [{
            "properties": {"b0": 1, "b10": 2, "b30": 3, "b60": 4, "b100": 5, "b200": 6}
        }]
    }

    with patch("__main__.ee.Image", return_value=mock_dataset):
        profile = local_profile(mock_dataset, [0, 0], 10)
        assert profile == {"b0": 1, "b10": 2, "b30": 3, "b60": 4, "b100": 5, "b200": 6}

    # Test case where no data is available
    mock_dataset.sample.return_value = {"features": []}
    profile = local_profile(mock_dataset, [0, 0], 10)
    assert profile == 'No data :(', GlobalErrorMessages.WRONG_DATA_OUT.value
