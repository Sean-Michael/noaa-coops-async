from pydantic import BaseModel, model_validator
from datetime import date
from noaa_coops_async.enums import Product, Datum, Units, TimeZone


class BaseRequest(BaseModel):
    station: str
    begin_date: date
    end_date: date
    units: Units = Units.METRIC
    time_zone: TimeZone = TimeZone.GMT


class WaterLevelRequest(BaseRequest):
    product: Product = Product.WATER_LEVEL
    datum: Datum


class MeteorlogicalRequest(BaseRequest):
    product: Product = Product.AIR_TEMPERATURE


class CurrentsRequest(BaseRequest):
    product: Product = Product.CURRENTS
