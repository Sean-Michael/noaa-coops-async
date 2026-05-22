from enum import StrEnum


class Product(StrEnum):
    WATER_LEVEL = "water_level"
    HOURLY_HEIGHT = "hourly_height"
    HIGH_LOW = "high_low"
    DAILY_MEAN = "daily_mean"
    DAILY_MAX_MIN = "daily_max_min"
    MONTHLY_MEAN = "monthly_mean"
    ONE_MINUTE_WATER_LEVEL = "one_minute_water_level"
    PREDICTIONS = "predictions"
    AIR_GAP = "air_gap"
    AIR_TEMPERATURE = "air_temperature"
    WATER_TEMPERATURE = "water_temperature"
    WIND = "wind"
    AIR_PRESSURE = "air_pressure"
    CONDUCTIVITY = "conductivity"
    VISIBILITY = "visibility"
    HUMIDITY = "humidity"
    SALINITY = "salinity"
    CURRENTS = "currents"
    CURRENTS_PREDICTIONS = "currents_predictions"
    CURRENTS_HEADER = "currents_header"
    OFS_WATER_LEVEL = "ofs_water_level"


class Datum(StrEnum):
    CRD = "CRD"    # Columbia River Datum
    IGLD = "IGLD"  # International Great Lakes Datum
    LWD = "LWD"    # Great Lakes Low Water Datum
    MHHW = "MHHW"  # Mean Higher High Water
    MHW = "MHW"    # Mean High Water
    MTL = "MTL"    # Mean Tide Level
    MSL = "MSL"    # Mean Sea Level
    MLW = "MLW"    # Mean Low Water
    MLLW = "MLLW"  # Mean Lower Low Water
    NAVD = "NAVD"  # North American Vertical Datum
    STND = "STND"  # Station Datum


class Units(StrEnum):
    METRIC = "metric"
    ENGLISH = "english"


class TimeZone(StrEnum):
    GMT = "gmt"
    LST = "lst"
    LST_LDT = "lst_ldt"


class Interval(StrEnum):
    ONE_MINUTE = "1"
    FIVE_MINUTES = "5"
    SIX_MINUTES = "6"
    TEN_MINUTES = "10"
    FIFTEEN_MINUTES = "15"
    THIRTY_MINUTES = "30"
    HOURLY = "h"
    SIXTY_MINUTES = "60"
    HILO = "hilo"
    MAX_SLACK = "max_slack"


class VelocityType(StrEnum):
    DEFAULT = "default"
    SPEED_DIR = "speed_dir"


class Format(StrEnum):
    JSON = "json"
    XML = "xml"
    CSV = "csv"


class Date(StrEnum):
    TODAY = "today"
    LATEST = "latest"
    RECENT = "recent"


class Expand(StrEnum):
    DETAILED = "detailed"
