from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    WRONG_SAND_PARAMETER = "Sand parameter not equal to expected"
    WRONG_CLAY_PARAMETER = "Clay parameter not equal to expected"
    WRONG_ORGC_PARAMETER = "Orgc parameter not equal to expected"
    WRONG_ELEV_PARAMETER = "Elev parameter not equal to expected"
    WRONG_DIURNAL_PARAMETER = "Diurnal parameter not equal to expected"
    WRONG_DATA_OUT = "Fault to have data"
    WRONG_JSON_RESULT = "Received JSON result is not equal to expected"
    WRONG_COMPARISON_RESULT = "Received comparison result is not equal to expected"
    WRONG_SOIL_RESULT = "Received soil result is not equal to expected"
    WRONG_QUARIFED_RESULT = "Received quarifed in df result is not equal to expected"
    WRONG_ELEVATION = "Received elevation is not equal to expected"
    WRONG_SOIL = "Received soil is not equal to expected"
